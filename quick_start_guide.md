# Quick Start Guide: Building Task Submission UI

## Recommended Stack for Approach 5 (Hybrid Dashboard)

This guide will help you get started with implementing the Hybrid Dashboard approach.

---

## Project Setup

### 1. Initialize Next.js Project

```bash
npx create-next-app@latest auto-reports-ui --typescript --tailwind --app
cd auto-reports-ui
```

### 2. Install Dependencies

```bash
# UI Components
npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu @radix-ui/react-progress @radix-ui/react-tabs
npm install class-variance-authority clsx tailwind-merge lucide-react

# State Management & Data Fetching
npm install @tanstack/react-query zustand

# File Upload
npm install react-dropzone

# PDF Handling
npm install react-pdf

# Date Formatting
npm install date-fns

# Development
npm install -D @types/react @types/node
```

### 3. Project Structure

```
auto-reports-ui/
├── app/
│   ├── layout.tsx                  # Root layout
│   ├── page.tsx                    # Home/Dashboard page
│   ├── api/
│   │   ├── tasks/
│   │   │   ├── route.ts           # GET /api/tasks, POST /api/tasks
│   │   │   ├── [id]/route.ts      # GET /api/tasks/:id
│   │   │   └── [id]/stream/route.ts # SSE endpoint
│   │   └── upload/route.ts        # File upload endpoint
│   └── globals.css
├── components/
│   ├── dashboard/
│   │   ├── TaskList.tsx           # Left panel
│   │   ├── TaskDetail.tsx         # Right panel
│   │   ├── NewTaskForm.tsx        # Submission form
│   │   └── ProgressTimeline.tsx   # Timeline component
│   ├── ui/                        # Reusable UI components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── progress.tsx
│   │   ├── tabs.tsx
│   │   └── dialog.tsx
│   └── providers/
│       └── QueryProvider.tsx      # React Query setup
├── lib/
│   ├── api.ts                     # API client functions
│   ├── store.ts                   # Zustand store
│   ├── types.ts                   # TypeScript types
│   └── utils.ts                   # Utility functions
└── public/
    └── uploads/                   # Temporary upload storage
```

---

## Core Data Models

### TypeScript Types (`lib/types.ts`)

```typescript
export type TaskType = 'data_collection' | 'questionnaire_generation' | 'literature_review' | 'custom';

export type TaskStatus = 'submitted' | 'processing' | 'in_progress' | 'review' | 'completed' | 'failed';

export type TaskStage =
  | 'task_received'
  | 'initial_processing'
  | 'data_collection'
  | 'llm_analysis'
  | 'human_review'
  | 'final_report';

export interface Task {
  id: string;
  title: string;
  type: TaskType;
  status: TaskStatus;
  progress: number; // 0-100
  currentStage: TaskStage;
  createdAt: Date;
  updatedAt: Date;
  completedAt?: Date;
  paperTitle?: string;
  paperFile?: string;
  estimatedCompletion?: Date;
  config?: Record<string, any>;
}

export interface TaskActivity {
  id: string;
  taskId: string;
  type: 'info' | 'success' | 'error' | 'warning';
  message: string;
  timestamp: Date;
  metadata?: Record<string, any>;
}

export interface IntermediateResult {
  id: string;
  taskId: string;
  stage: TaskStage;
  title: string;
  description?: string;
  fileUrl?: string;
  fileType?: string;
  fileSize?: number;
  previewData?: any; // JSON data for preview
  createdAt: Date;
}

export interface TaskTimeline {
  stage: TaskStage;
  status: 'completed' | 'in_progress' | 'pending' | 'failed';
  startedAt?: Date;
  completedAt?: Date;
  progress?: number;
  message?: string;
}
```

---

## API Implementation

### Task Creation Endpoint (`app/api/tasks/route.ts`)

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { Task, TaskType } from '@/lib/types';

// In production, this would use a database
const tasks: Task[] = [];

export async function GET(request: NextRequest) {
  // Get query params for filtering
  const searchParams = request.nextUrl.searchParams;
  const status = searchParams.get('status');
  const type = searchParams.get('type');

  let filteredTasks = tasks;

  if (status) {
    filteredTasks = filteredTasks.filter(t => t.status === status);
  }

  if (type) {
    filteredTasks = filteredTasks.filter(t => t.type === type);
  }

  return NextResponse.json({
    tasks: filteredTasks,
    total: filteredTasks.length
  });
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { title, type, paperFile, config } = body;

    // Validate required fields
    if (!title || !type) {
      return NextResponse.json(
        { error: 'Title and type are required' },
        { status: 400 }
      );
    }

    // Create new task
    const newTask: Task = {
      id: `task_${Date.now()}`,
      title,
      type: type as TaskType,
      status: 'submitted',
      progress: 0,
      currentStage: 'task_received',
      createdAt: new Date(),
      updatedAt: new Date(),
      paperFile,
      config,
      estimatedCompletion: new Date(Date.now() + 2 * 60 * 60 * 1000) // 2 hours from now
    };

    tasks.push(newTask);

    // Start background processing (in production, this would be a queue)
    processTask(newTask.id);

    return NextResponse.json(newTask, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to create task' },
      { status: 500 }
    );
  }
}

// Simulate task processing
async function processTask(taskId: string) {
  const task = tasks.find(t => t.id === taskId);
  if (!task) return;

  // Simulate progression through stages
  const stages: TaskStage[] = [
    'initial_processing',
    'data_collection',
    'llm_analysis',
    'human_review',
    'final_report'
  ];

  for (let i = 0; i < stages.length; i++) {
    await new Promise(resolve => setTimeout(resolve, 10000)); // 10 seconds per stage

    task.currentStage = stages[i];
    task.progress = Math.min(((i + 1) / stages.length) * 100, 100);
    task.updatedAt = new Date();

    if (i === stages.length - 1) {
      task.status = 'completed';
      task.completedAt = new Date();
    } else {
      task.status = 'in_progress';
    }
  }
}
```

### Server-Sent Events Endpoint (`app/api/tasks/[id]/stream/route.ts`)

```typescript
import { NextRequest } from 'next/server';

export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  const taskId = params.id;

  // Create a ReadableStream for SSE
  const encoder = new TextEncoder();

  const stream = new ReadableStream({
    async start(controller) {
      // Send initial connection message
      controller.enqueue(
        encoder.encode(`data: ${JSON.stringify({ type: 'connected', taskId })}\n\n`)
      );

      // Poll for updates every 2 seconds
      const interval = setInterval(async () => {
        try {
          // Fetch task from database
          const task = await fetchTask(taskId);

          if (!task) {
            controller.enqueue(
              encoder.encode(`data: ${JSON.stringify({ type: 'error', message: 'Task not found' })}\n\n`)
            );
            clearInterval(interval);
            controller.close();
            return;
          }

          // Send update
          controller.enqueue(
            encoder.encode(`data: ${JSON.stringify({ type: 'update', task })}\n\n`)
          );

          // Close stream if task is completed or failed
          if (task.status === 'completed' || task.status === 'failed') {
            clearInterval(interval);
            controller.close();
          }
        } catch (error) {
          controller.enqueue(
            encoder.encode(`data: ${JSON.stringify({ type: 'error', message: 'Update failed' })}\n\n`)
          );
        }
      }, 2000);

      // Cleanup on close
      request.signal.addEventListener('abort', () => {
        clearInterval(interval);
        controller.close();
      });
    }
  });

  return new Response(stream, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}

// Mock function - replace with actual database query
async function fetchTask(id: string) {
  // In production, query from database
  return {
    id,
    title: 'Sample Task',
    status: 'in_progress',
    progress: 45,
    currentStage: 'data_collection',
    updatedAt: new Date()
  };
}
```

---

## React Components

### Main Dashboard (`app/page.tsx`)

```typescript
'use client';

import { useState } from 'react';
import { TaskList } from '@/components/dashboard/TaskList';
import { TaskDetail } from '@/components/dashboard/TaskDetail';
import { NewTaskForm } from '@/components/dashboard/NewTaskForm';
import { useQuery } from '@tanstack/react-query';
import { fetchTasks } from '@/lib/api';

export default function DashboardPage() {
  const [selectedTaskId, setSelectedTaskId] = useState<string | null>(null);
  const [showNewTaskForm, setShowNewTaskForm] = useState(false);

  const { data, isLoading } = useQuery({
    queryKey: ['tasks'],
    queryFn: fetchTasks,
    refetchInterval: 10000 // Poll every 10 seconds
  });

  const tasks = data?.tasks ?? [];
  const selectedTask = tasks.find(t => t.id === selectedTaskId);

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Left Panel - Task List */}
      <div className="w-80 bg-white border-r border-gray-200 flex flex-col">
        <div className="p-4 border-b border-gray-200">
          <h1 className="text-xl font-bold text-gray-900">Auto Reports</h1>
          <p className="text-sm text-gray-500 mt-1">Research Task Manager</p>
        </div>

        <div className="p-4">
          <button
            onClick={() => setShowNewTaskForm(!showNewTaskForm)}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-lg transition"
          >
            + New Task
          </button>
        </div>

        {showNewTaskForm && (
          <div className="px-4 pb-4">
            <NewTaskForm
              onSuccess={(task) => {
                setShowNewTaskForm(false);
                setSelectedTaskId(task.id);
              }}
              onCancel={() => setShowNewTaskForm(false)}
            />
          </div>
        )}

        <TaskList
          tasks={tasks}
          selectedTaskId={selectedTaskId}
          onSelectTask={setSelectedTaskId}
          isLoading={isLoading}
        />
      </div>

      {/* Right Panel - Task Details */}
      <div className="flex-1 overflow-auto">
        {selectedTask ? (
          <TaskDetail task={selectedTask} />
        ) : (
          <div className="flex items-center justify-center h-full text-gray-500">
            <div className="text-center">
              <svg className="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
              <p className="mt-4 text-sm">Select a task to view details</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
```

### Task List Component (`components/dashboard/TaskList.tsx`)

```typescript
import { Task } from '@/lib/types';
import { formatDistanceToNow } from 'date-fns';

interface TaskListProps {
  tasks: Task[];
  selectedTaskId: string | null;
  onSelectTask: (taskId: string) => void;
  isLoading: boolean;
}

const statusColors = {
  submitted: 'bg-gray-100 text-gray-800',
  processing: 'bg-blue-100 text-blue-800',
  in_progress: 'bg-yellow-100 text-yellow-800',
  review: 'bg-purple-100 text-purple-800',
  completed: 'bg-green-100 text-green-800',
  failed: 'bg-red-100 text-red-800'
};

const taskTypeIcons = {
  data_collection: '📊',
  questionnaire_generation: '📝',
  literature_review: '📚',
  custom: '⚙️'
};

export function TaskList({ tasks, selectedTaskId, onSelectTask, isLoading }: TaskListProps) {
  if (isLoading) {
    return (
      <div className="flex-1 p-4">
        <div className="animate-pulse space-y-3">
          {[1, 2, 3].map(i => (
            <div key={i} className="h-20 bg-gray-200 rounded-lg"></div>
          ))}
        </div>
      </div>
    );
  }

  if (tasks.length === 0) {
    return (
      <div className="flex-1 p-4 text-center text-gray-500">
        <p className="text-sm">No tasks yet</p>
        <p className="text-xs mt-1">Create your first task to get started</p>
      </div>
    );
  }

  return (
    <div className="flex-1 overflow-auto p-4 space-y-2">
      {tasks.map(task => (
        <button
          key={task.id}
          onClick={() => onSelectTask(task.id)}
          className={`w-full text-left p-3 rounded-lg border-2 transition ${
            selectedTaskId === task.id
              ? 'border-blue-500 bg-blue-50'
              : 'border-gray-200 bg-white hover:border-gray-300'
          }`}
        >
          <div className="flex items-start justify-between mb-2">
            <div className="flex items-center gap-2">
              <span className="text-xl">{taskTypeIcons[task.type]}</span>
              <h3 className="font-medium text-sm text-gray-900 line-clamp-1">
                {task.title}
              </h3>
            </div>
          </div>

          <div className="flex items-center justify-between">
            <span className={`text-xs px-2 py-1 rounded-full ${statusColors[task.status]}`}>
              {task.status.replace('_', ' ')}
            </span>
            <span className="text-xs text-gray-500">
              {formatDistanceToNow(new Date(task.createdAt), { addSuffix: true })}
            </span>
          </div>

          {task.status !== 'completed' && task.status !== 'failed' && (
            <div className="mt-2">
              <div className="flex items-center justify-between text-xs text-gray-600 mb-1">
                <span>Progress</span>
                <span>{task.progress}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-1.5">
                <div
                  className="bg-blue-600 h-1.5 rounded-full transition-all"
                  style={{ width: `${task.progress}%` }}
                ></div>
              </div>
            </div>
          )}
        </button>
      ))}
    </div>
  );
}
```

### New Task Form (`components/dashboard/NewTaskForm.tsx`)

```typescript
'use client';

import { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { createTask } from '@/lib/api';
import { Task, TaskType } from '@/lib/types';

interface NewTaskFormProps {
  onSuccess: (task: Task) => void;
  onCancel: () => void;
}

const taskTypes: { value: TaskType; label: string; description: string }[] = [
  { value: 'literature_review', label: 'Literature Review', description: 'Comprehensive review of academic papers' },
  { value: 'questionnaire_generation', label: 'Questionnaire', description: 'Generate survey questions' },
  { value: 'data_collection', label: 'Data Collection', description: 'Gather data from various sources' },
  { value: 'custom', label: 'Custom Task', description: 'Define a custom research task' }
];

export function NewTaskForm({ onSuccess, onCancel }: NewTaskFormProps) {
  const [taskType, setTaskType] = useState<TaskType>('literature_review');
  const [title, setTitle] = useState('');
  const [file, setFile] = useState<File | null>(null);
  const queryClient = useQueryClient();

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: { 'application/pdf': ['.pdf'] },
    maxFiles: 1,
    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        setFile(acceptedFiles[0]);
        // Auto-fill title from filename if empty
        if (!title) {
          setTitle(acceptedFiles[0].name.replace('.pdf', ''));
        }
      }
    }
  });

  const mutation = useMutation({
    mutationFn: createTask,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
      onSuccess(data);
    }
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title || !file) return;

    // In production, upload file first and get URL
    const fileUrl = `/uploads/${file.name}`;

    mutation.mutate({
      title,
      type: taskType,
      paperFile: fileUrl,
      config: {}
    });
  };

  return (
    <form onSubmit={handleSubmit} className="bg-gray-50 rounded-lg p-4 space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Task Type
        </label>
        <select
          value={taskType}
          onChange={(e) => setTaskType(e.target.value as TaskType)}
          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        >
          {taskTypes.map(type => (
            <option key={type.value} value={type.value}>
              {type.label}
            </option>
          ))}
        </select>
        <p className="text-xs text-gray-500 mt-1">
          {taskTypes.find(t => t.value === taskType)?.description}
        </p>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Task Title
        </label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter task title..."
          className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-1">
          Paper Proposal (PDF)
        </label>
        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-lg p-4 text-center cursor-pointer transition ${
            isDragActive ? 'border-blue-500 bg-blue-50' : 'border-gray-300 hover:border-gray-400'
          }`}
        >
          <input {...getInputProps()} />
          {file ? (
            <div className="text-sm">
              <p className="font-medium text-gray-900">{file.name}</p>
              <p className="text-gray-500">{(file.size / 1024).toFixed(1)} KB</p>
            </div>
          ) : (
            <div className="text-sm text-gray-600">
              <p>Drag & drop your PDF here, or click to select</p>
            </div>
          )}
        </div>
      </div>

      <div className="flex gap-2">
        <button
          type="submit"
          disabled={!title || !file || mutation.isPending}
          className="flex-1 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-300 text-white font-medium py-2 px-4 rounded-lg transition"
        >
          {mutation.isPending ? 'Creating...' : 'Create Task'}
        </button>
        <button
          type="button"
          onClick={onCancel}
          className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition"
        >
          Cancel
        </button>
      </div>

      {mutation.isError && (
        <p className="text-sm text-red-600">
          Failed to create task. Please try again.
        </p>
      )}
    </form>
  );
}
```

### Task Detail with SSE (`components/dashboard/TaskDetail.tsx`)

```typescript
'use client';

import { useEffect, useState } from 'react';
import { Task, TaskActivity, IntermediateResult } from '@/lib/types';
import { ProgressTimeline } from './ProgressTimeline';

interface TaskDetailProps {
  task: Task;
}

export function TaskDetail({ task }: TaskDetailProps) {
  const [liveTask, setLiveTask] = useState<Task>(task);
  const [activities, setActivities] = useState<TaskActivity[]>([]);
  const [results, setResults] = useState<IntermediateResult[]>([]);

  // Server-Sent Events for real-time updates
  useEffect(() => {
    const eventSource = new EventSource(`/api/tasks/${task.id}/stream`);

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);

      if (data.type === 'update') {
        setLiveTask(data.task);
      } else if (data.type === 'activity') {
        setActivities(prev => [data.activity, ...prev]);
      } else if (data.type === 'result') {
        setResults(prev => [...prev, data.result]);
      }
    };

    eventSource.onerror = () => {
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, [task.id]);

  return (
    <div className="h-full flex flex-col">
      {/* Header */}
      <div className="bg-white border-b border-gray-200 p-6">
        <h2 className="text-2xl font-bold text-gray-900">{liveTask.title}</h2>
        <div className="flex items-center gap-4 mt-3">
          <div className="flex items-center gap-2">
            <div className="w-full max-w-xs bg-gray-200 rounded-full h-2">
              <div
                className="bg-blue-600 h-2 rounded-full transition-all duration-500"
                style={{ width: `${liveTask.progress}%` }}
              ></div>
            </div>
            <span className="text-sm font-medium text-gray-700">
              {liveTask.progress}%
            </span>
          </div>
          <span className="text-sm text-gray-500">
            Current: {liveTask.currentStage.replace('_', ' ')}
          </span>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex-1 overflow-hidden">
        <div className="border-b border-gray-200 bg-white">
          <nav className="flex gap-8 px-6">
            <button className="py-4 border-b-2 border-blue-600 text-sm font-medium text-blue-600">
              Progress
            </button>
            <button className="py-4 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700">
              Results ({results.length})
            </button>
            <button className="py-4 border-b-2 border-transparent text-sm font-medium text-gray-500 hover:text-gray-700">
              Activity ({activities.length})
            </button>
          </nav>
        </div>

        {/* Content */}
        <div className="overflow-auto p-6 bg-gray-50">
          <ProgressTimeline task={liveTask} />

          {/* Intermediate Results */}
          {results.length > 0 && (
            <div className="mt-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">
                Intermediate Results
              </h3>
              <div className="space-y-3">
                {results.map(result => (
                  <div key={result.id} className="bg-white rounded-lg p-4 border border-gray-200">
                    <div className="flex items-start justify-between">
                      <div>
                        <h4 className="font-medium text-gray-900">{result.title}</h4>
                        {result.description && (
                          <p className="text-sm text-gray-600 mt-1">{result.description}</p>
                        )}
                      </div>
                      {result.fileUrl && (
                        <a
                          href={result.fileUrl}
                          download
                          className="text-sm text-blue-600 hover:text-blue-700 font-medium"
                        >
                          Download
                        </a>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
```

---

## Environment Variables

Create `.env.local`:

```bash
# Database (PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/auto_reports

# File Storage (S3 or compatible)
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
S3_BUCKET_NAME=auto-reports-uploads

# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:3000/api

# Authentication (if using)
NEXTAUTH_SECRET=your_secret_key
NEXTAUTH_URL=http://localhost:3000
```

---

## Database Schema (PostgreSQL)

```sql
-- Tasks table
CREATE TABLE tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title VARCHAR(255) NOT NULL,
  type VARCHAR(50) NOT NULL,
  status VARCHAR(50) NOT NULL,
  progress INTEGER DEFAULT 0,
  current_stage VARCHAR(50),
  paper_title VARCHAR(255),
  paper_file_url TEXT,
  config JSONB,
  estimated_completion TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP
);

-- Task activities/logs
CREATE TABLE task_activities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
  type VARCHAR(20) NOT NULL,
  message TEXT NOT NULL,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Intermediate results
CREATE TABLE intermediate_results (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
  stage VARCHAR(50) NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  file_url TEXT,
  file_type VARCHAR(50),
  file_size INTEGER,
  preview_data JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_created_at ON tasks(created_at DESC);
CREATE INDEX idx_task_activities_task_id ON task_activities(task_id);
CREATE INDEX idx_intermediate_results_task_id ON intermediate_results(task_id);
```

---

## Running the Application

### Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Open browser to http://localhost:3000
```

### Production Build

```bash
# Build for production
npm run build

# Start production server
npm start
```

---

## Testing Strategy

### Unit Tests (Jest + React Testing Library)

```bash
npm install -D jest @testing-library/react @testing-library/jest-dom
```

Test example:

```typescript
import { render, screen } from '@testing-library/react';
import { TaskList } from '@/components/dashboard/TaskList';

describe('TaskList', () => {
  it('renders empty state when no tasks', () => {
    render(
      <TaskList
        tasks={[]}
        selectedTaskId={null}
        onSelectTask={() => {}}
        isLoading={false}
      />
    );

    expect(screen.getByText('No tasks yet')).toBeInTheDocument();
  });
});
```

### E2E Tests (Playwright)

```bash
npm install -D @playwright/test
```

---

## Deployment

### Vercel (Recommended for Next.js)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Docker

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

---

## Next Steps

1. Set up database (PostgreSQL)
2. Implement authentication (NextAuth.js)
3. Add file upload to S3
4. Build actual task processing backend
5. Add email notifications
6. Implement user settings/preferences
7. Add team collaboration features
8. Set up CI/CD pipeline

---

## Performance Optimization

1. **Code Splitting**: Next.js automatic code splitting
2. **Image Optimization**: Use next/image
3. **Caching**: React Query caching + SWR
4. **Bundle Size**: Analyze with @next/bundle-analyzer
5. **Database**: Add indexes, use connection pooling
6. **CDN**: Serve static assets from CDN

---

## Security Considerations

1. **File Upload**: Validate file types and sizes
2. **Authentication**: Implement proper auth (JWT, sessions)
3. **Authorization**: Check permissions before showing tasks
4. **CSRF Protection**: Use Next.js built-in protection
5. **Rate Limiting**: Prevent API abuse
6. **Input Validation**: Sanitize all user inputs
7. **HTTPS**: Always use HTTPS in production

This should give you a solid foundation to start building!
