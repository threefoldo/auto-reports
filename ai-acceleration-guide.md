# AI Acceleration Guide for PhD-Assist User Acquisition

## Purpose

This guide shows you how to use AI to 10x your user acquisition efforts while maintaining authenticity and quality. The goal: reach more people, faster, without sacrificing the genuine engagement that builds trust.

---

## Table of Contents

1. [AI Strategy Overview](#overview)
2. [AI-Powered Reddit Monitoring](#reddit-monitoring)
3. [AI-Assisted Response Writing](#response-writing)
4. [Content Repurposing Automation](#content-repurposing)
5. [Email Personalization at Scale](#email-scale)
6. [Multi-Platform Content Distribution](#multi-platform)
7. [Analytics & Optimization](#analytics)
8. [Research & Insight Synthesis](#research)
9. [Workflow Automation](#workflows)
10. [AI Tools Stack](#tools-stack)
11. [Prompts Library](#prompts)
12. [What NOT to Automate](#boundaries)

---

<a name="overview"></a>
## 1. AI Strategy Overview

### The Core Principle: AI Augments, Human Approves

**AI's Role**:
- Find relevant conversations (monitoring)
- Draft responses (writing assistant)
- Repurpose content (efficiency)
- Personalize at scale (outreach)
- Analyze data (optimization)

**Your Role**:
- Review and approve all outputs
- Add personal touches
- Make strategic decisions
- Build genuine relationships
- Handle sensitive conversations

### Time Savings Breakdown

| Task | Manual Time | With AI | Time Saved |
|------|-------------|---------|------------|
| Finding relevant Reddit threads | 60 min/day | 10 min/day | 50 min |
| Drafting comments | 45 min/day | 15 min/day | 30 min |
| Writing personalized emails | 2 hours/week | 30 min/week | 90 min |
| Content repurposing | 3 hours/week | 30 min/week | 150 min |
| Analytics review | 60 min/week | 15 min/week | 45 min |
| **TOTAL WEEKLY SAVINGS** | | | **~8 hours** |

**Result**: You can do in 10 hours/week what would take 18 hours manually, OR you can engage with 2x more people in the same time.

---

<a name="reddit-monitoring"></a>
## 2. AI-Powered Reddit Monitoring

### Problem: Finding Relevant Threads Takes Hours

**Manual Approach**: Browse r/PhD, r/GradSchool, r/AskAcademia daily, scroll through hundreds of posts

**AI Approach**: Automated monitoring alerts you to only relevant threads

### Solution 1: Reddit API + AI Filtering

**Tools Needed**:
- Reddit API access (free)
- Python script (provided below)
- Claude API or GPT-4 API
- Email notifications

**How It Works**:
1. Script monitors target subreddits every 2 hours
2. AI filters posts by relevance to your pain points
3. You get email digest with top 10 relevant threads
4. Click to engage immediately

**Python Script** (Save as `reddit_monitor.py`):

```python
import praw
import anthropic
import os
from datetime import datetime, timedelta

# Initialize Reddit API
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="PhD_Feedback_Monitor"
)

# Initialize Claude API
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Target subreddits
SUBREDDITS = ['PhD', 'GradSchool', 'AskAcademia', 'dissertation']

# Pain point keywords (from your research)
PAIN_POINTS = [
    'advisor feedback', 'no feedback', 'vague feedback',
    'slow feedback', 'dissertation feedback', 'committee feedback',
    'advisor not responding', 'waiting for advisor', 'harsh feedback'
]

def is_relevant_post(post_title, post_text):
    """Use Claude to determine if post is relevant"""

    prompt = f"""Analyze if this Reddit post is about dissertation/thesis feedback challenges:

Title: {post_title}
Content: {post_text[:500]}

Pain points we care about:
1. No/insufficient advisor feedback
2. Vague, unactionable feedback
3. Slow turnaround times (weeks/months)
4. Inconsistent/contradictory feedback
5. Harsh or demotivating feedback
6. Unavailable/overextended advisors

Respond with:
- RELEVANT: [brief reason] if it matches our pain points
- NOT_RELEVANT: [brief reason] if it doesn't

Be strict - only mark as relevant if genuinely about feedback challenges."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )

    response = message.content[0].text
    return response.startswith("RELEVANT"), response

def monitor_subreddits():
    """Monitor subreddits and find relevant posts"""

    relevant_posts = []

    for subreddit_name in SUBREDDITS:
        subreddit = reddit.subreddit(subreddit_name)

        # Get new posts from last 6 hours
        for post in subreddit.new(limit=50):
            # Skip if older than 6 hours
            post_time = datetime.fromtimestamp(post.created_utc)
            if datetime.now() - post_time > timedelta(hours=6):
                continue

            # Check relevance with AI
            is_relevant, reason = is_relevant_post(post.title, post.selftext)

            if is_relevant:
                relevant_posts.append({
                    'subreddit': subreddit_name,
                    'title': post.title,
                    'url': f"https://reddit.com{post.permalink}",
                    'author': str(post.author),
                    'score': post.score,
                    'num_comments': post.num_comments,
                    'reason': reason,
                    'preview': post.selftext[:200]
                })

    return relevant_posts

def generate_email_digest(posts):
    """Generate HTML email digest"""

    if not posts:
        return None

    html = f"""
    <h2>📊 Reddit Monitoring Digest - {datetime.now().strftime('%Y-%m-%d %H:%M')}</h2>
    <p>Found {len(posts)} relevant threads in the last 6 hours:</p>
    """

    for i, post in enumerate(posts, 1):
        html += f"""
        <div style="border: 1px solid #ddd; padding: 15px; margin: 10px 0;">
            <h3>{i}. r/{post['subreddit']}: {post['title']}</h3>
            <p><strong>Author:</strong> u/{post['author']} |
               <strong>Score:</strong> {post['score']} |
               <strong>Comments:</strong> {post['num_comments']}</p>
            <p><strong>Why relevant:</strong> {post['reason']}</p>
            <p><strong>Preview:</strong> {post['preview']}...</p>
            <p><a href="{post['url']}" style="background: #0066cc; color: white;
                  padding: 8px 15px; text-decoration: none; border-radius: 4px;">
                  View & Respond →
               </a></p>
        </div>
        """

    return html

if __name__ == "__main__":
    posts = monitor_subreddits()

    if posts:
        email_html = generate_email_digest(posts)
        # Send email (integrate with your email service)
        print(f"Found {len(posts)} relevant posts")
        print(email_html)
    else:
        print("No relevant posts found")
```

**Setup**:
```bash
# Install dependencies
pip install praw anthropic

# Set environment variables
export ANTHROPIC_API_KEY="your_api_key"

# Run every 6 hours with cron
crontab -e
# Add: 0 */6 * * * /usr/bin/python3 /path/to/reddit_monitor.py
```

**Cost**: ~$0.10-0.20/day in API calls (very cheap)

---

### Solution 2: No-Code Alternative (F5Bot + Claude)

**Tools**: F5Bot (free) + Claude Desktop

**Setup**:
1. Go to f5bot.com
2. Add keywords: "dissertation feedback", "advisor feedback", "vague feedback", etc.
3. Get email alerts for new Reddit posts
4. When alert arrives, paste post into Claude with this prompt:

**Claude Prompt**:
```
I received this Reddit post alert about dissertation feedback. Help me:

1. Assess if it's truly relevant to my 6 pain points (no feedback, vague feedback, slow turnaround, inconsistent, harsh, unavailable advisor)
2. If relevant, identify which specific pain point(s) it relates to
3. Draft a helpful, non-promotional response based on my research

Reddit post:
[paste post here]

My research insights:
[paste relevant pain point research]

Return:
- RELEVANCE: Yes/No + reason
- PAIN POINT(s): [which ones]
- SUGGESTED RESPONSE: [draft comment]
```

---

<a name="response-writing"></a>
## 3. AI-Assisted Response Writing

### The Workflow: AI Drafts, You Refine

**Step 1: Feed Claude Context**

Create a Claude Project with these documents:
- All 6 pain point research files
- Reddit engagement guide
- Your positioning statement
- Example comments that performed well

**Step 2: Use This Prompt Template**

```
I found a Reddit post where a PhD student is struggling with [PAIN POINT].

Post context:
Title: [title]
Content: [paste content]
Subreddit: r/[subreddit]

Help me write a helpful, authentic response that:
1. Shows empathy and validates their experience
2. Shares relevant data from my research (pain point #X affects Y% of students)
3. Provides 2-3 specific, actionable strategies
4. Uses peer-to-peer tone, not expert-to-novice
5. Only mentions my tool if conversation naturally develops (not in first response)
6. Asks a follow-up question to continue discussion

Keep it 200-300 words, conversational, specific to their situation.
```

**Step 3: Review & Personalize**

AI gives you 80% there. You add:
- Specific detail from their post AI might have missed
- Personal touch ("I went through this too")
- Adjust tone to match subreddit culture
- Remove anything that sounds too polished/corporate

**Time Saved**: 30 seconds to draft vs 5 minutes from scratch

---

### Batch Response Generation

**For Daily Engagement (3-5 comments)**:

**Prompt**:
```
I'm going to share 5 Reddit posts I want to respond to today. For each, generate:
1. Quick relevance assessment
2. Which pain point it relates to
3. Draft response (200-250 words)
4. Suggested follow-up question

Format as:
POST 1: [title]
- Relevance: [score 1-10]
- Pain Point: #[number]
- Response: [draft]
- Follow-up: [question]

Here are the posts:

[Post 1]
---
[Post 2]
---
[Post 3]
---
etc.
```

**Result**: Get 5 draft responses in 2 minutes instead of 25 minutes writing from scratch

---

<a name="content-repurposing"></a>
## 4. Content Repurposing Automation

### The Strategy: Write Once, Publish Everywhere

You have great research content. Don't manually rewrite it for each platform.

### Use Case 1: Reddit Post → Twitter Thread

**Tool**: Claude or ChatGPT

**Prompt**:
```
Transform this Reddit post into a Twitter thread (10-15 tweets):

[Paste your Reddit post]

Requirements:
- Tweet 1: Hook that makes people want to read more
- Tweets 2-14: Break down the content into digestible insights
- Tweet 15: CTA to full research or beta signup
- Each tweet: 280 chars max
- Use line breaks for readability
- Include relevant emojis (minimal, academic tone)
- Hashtags: #PhDChat #AcademicTwitter #GradSchool (end of thread)

Maintain academic credibility while being engaging.
```

**Time Saved**: 45 minutes → 5 minutes

---

### Use Case 2: Reddit Post → LinkedIn Article

**Prompt**:
```
Transform this Reddit research post into a professional LinkedIn article:

[Paste Reddit post]

Requirements:
- Professional tone (less casual than Reddit)
- 800-1200 words
- Add section: "Implications for Graduate Programs/Advisors"
- More formal structure with clear sections
- Include data visualizations suggestions
- Professional headline that works for LinkedIn algorithm
- Maintain core insights but reframe for mixed audience (students, faculty, administrators)

Target audience: PhD students, graduate program directors, academic administrators
```

---

### Use Case 3: Email Research Report → Blog Post Series

**Prompt**:
```
I have a comprehensive research report on dissertation feedback challenges (attached).

Break this into a 6-part blog post series where each post focuses on one pain point:

For each post, create:
1. SEO-optimized title
2. Meta description (155 chars)
3. Outline with H2/H3 structure
4. Suggested word count
5. Internal linking opportunities
6. CTA for that specific post

Focus on making each post rankable for Google searches like:
- "why doesn't my advisor give feedback"
- "how to get better dissertation feedback"
- "advisor feedback taking too long"
```

---

### Automation Tool: Make.com or Zapier Workflow

**Workflow**:
1. You publish Reddit post
2. Webhook triggers when post goes live
3. Post content sent to Claude API with repurposing prompts
4. AI generates Twitter thread, LinkedIn version, blog outline
5. Drafts sent to your email or project management tool
6. You review and schedule

**Setup** (Make.com example):
```
Trigger: RSS feed from Reddit post
↓
OpenAI/Claude Module: "Transform to Twitter thread"
↓
OpenAI/Claude Module: "Transform to LinkedIn article"
↓
Google Docs: Create drafts
↓
Email: Send you notification with links
```

**Time Saved**: 3 hours/week → 30 minutes/week

---

<a name="email-scale"></a>
## 5. Email Personalization at Scale

### The Challenge: 50 University Outreach Emails

**Manual Approach**: Research each university, customize template, takes 15 min each = 12.5 hours

**AI Approach**: 3 hours total

### Workflow: AI-Powered Personalization

**Step 1: Gather University Data**

Create spreadsheet with:
- University name
- Contact name
- Contact title
- Department/center
- URL to their program/website

**Step 2: Use Claude with This Workflow**

**Prompt** (paste for each university):
```
I'm reaching out to [Name], [Title] at [University] about my PhD-Assist beta program.

Their program info: [paste from website]

Using this email template, personalize it specifically for them:

[Paste Template 1A from outreach-templates.md]

Personalization requirements:
1. Reference specific programs they run (dissertation boot camps, writing groups, etc.)
2. Mention recent news/achievements if found on their site
3. Tie my research to their existing work
4. Adjust tone to match their institutional culture (formal vs casual)
5. Use their preferred terminology (check their site)

Keep core message but make it feel genuinely personal, not template.

Also suggest:
- Best subject line for this specific contact
- Optimal send time based on institutional culture
```

**Step 3: Batch Processing**

For 10+ emails, use this approach:

```
I'm doing outreach to 10 writing center directors. Help me personalize emails efficiently.

Here's my template: [template]

Here's my research on each person:
1. [Name] at [University] - [context from website]
2. [Name] at [University] - [context from website]
...

For each, generate:
- Personalized subject line
- 2-3 specific personalizations to add to template
- Optimal send day/time
- Follow-up timing

Format as table for easy copy-paste.
```

**Time Saved**: 15 min per email → 3 min per email

---

### Email Sequence Automation

**Tool**: Mailchimp, ConvertKit, or custom with Claude API

**Use Case**: Beta Waitlist Email Sequence

**Setup**:
1. Someone signs up for beta
2. Their info (name, field, pain point selection) stored
3. Claude API generates personalized email sequence based on their pain point
4. Emails scheduled automatically

**Claude API Integration** (Python example):

```python
def generate_personalized_email_sequence(user_data):
    """Generate personalized 5-email sequence based on user's pain point"""

    prompt = f"""
    Generate personalized email sequence for beta waitlist member:

    Name: {user_data['name']}
    Field: {user_data['field']}
    Pain Point: {user_data['pain_point']}
    Signup Date: {user_data['signup_date']}

    Using these base templates: [paste email sequence from beta-signup-page-content.md]

    Personalize each email by:
    1. Referencing their specific pain point throughout
    2. Sharing research insights most relevant to their field
    3. Including discipline-specific examples
    4. Adjusting tone for their career stage

    Generate all 5 emails with:
    - Subject lines
    - Personalized body copy
    - Optimal send timing

    Keep the structure but make it feel personally written for them.
    """

    # Call Claude API
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text
```

---

<a name="multi-platform"></a>
## 6. Multi-Platform Content Distribution

### The Vision: Post Once, Reach Everywhere

**Platforms to Cover**:
- Reddit (5 subreddits)
- Twitter/X
- LinkedIn
- PhD Facebook groups
- Discord communities
- Your blog

**Manual**: Post individually to each = 2 hours
**With AI**: 20 minutes

### Solution: AI Content Adapter + Scheduler

**Step 1: Master Content Creation**

Write one comprehensive piece (e.g., Reddit post on Pain Point #1)

**Step 2: AI Adaptation**

**Prompt**:
```
I wrote this master content piece about dissertation feedback challenges:

[Paste content]

Adapt it for these platforms while maintaining core message:

1. REDDIT (r/PhD):
   - Keep current version, minimal changes
   - Suggest optimal post time

2. TWITTER:
   - 12-tweet thread
   - Hook tweet that drives engagement
   - Academic but accessible tone

3. LINKEDIN:
   - Professional article format
   - Add "For Graduate Programs" section
   - More formal tone

4. FACEBOOK (PhD groups):
   - More conversational, supportive tone
   - Shorter than Reddit version
   - Encourage discussion

5. DISCORD (#dissertation-help channel):
   - Very casual, peer-to-peer
   - Bullet points preferred
   - Offer to discuss in thread

6. BLOG POST:
   - SEO-optimized version
   - Add sections, FAQs
   - 1500-2000 words
   - Include meta description, title tag

For each, provide:
- Optimized headline/title
- Full adapted content
- Suggested posting time
- Platform-specific CTA
```

**Result**: All versions ready to post in 10 minutes

**Step 3: Schedule with Buffer or Hootsuite**

- Load AI-generated content into scheduler
- Set optimal times per platform
- Monitor and respond to engagement

---

<a name="analytics"></a>
## 7. Analytics & Optimization

### AI-Powered Performance Analysis

**Weekly Review Automation**

**Data to Collect**:
- Reddit post upvotes, comments, engagement rate
- Email open rates, click rates
- Landing page conversion rate
- Beta signup sources
- Comment karma growth

**AI Analysis Prompt**:

```
Here's my user acquisition performance data from this week:

REDDIT:
- Post 1 (Pain Point #1): 234 upvotes, 45 comments, 12 DMs
- Post 2 (Survey): 89 upvotes, 23 comments, 34 survey responses
- Comments: 47 total, avg 8 upvotes each
- Total karma gain: +312

EMAIL:
- Waitlist email 1: 42% open, 12% click
- Waitlist email 2: 38% open, 8% click

LANDING PAGE:
- Visits: 450
- Signups: 67
- Conversion: 14.9%

BETA SIGNUPS:
- Total: 67
- Sources: Reddit (41), Twitter (12), LinkedIn (8), Direct (6)

Analyze this data and provide:

1. What's working well? (Be specific about why)
2. What's underperforming? (Identify root causes)
3. Week-over-week trends (if I provide last week's data)
4. Specific recommendations for next week
5. Which content/platform to prioritize
6. A/B test suggestions
7. Red flags or concerns

Format as actionable weekly report with priority actions at top.
```

**Result**: Comprehensive weekly analysis in 2 minutes vs 1 hour of manual review

---

### Predictive Insights

**Prompt**:
```
Based on this 4-week trend data:

Week 1: [data]
Week 2: [data]
Week 3: [data]
Week 4: [data]

Predict:
1. When will I hit 100 beta signups at current growth rate?
2. Which acquisition channel is accelerating/declining?
3. What's my CAC (cost per acquisition) trend?
4. Should I adjust strategy? If so, how?
5. What's the projected beta signup total by launch date (Week 12)?

Provide data-driven forecasts with confidence levels.
```

---

<a name="research"></a>
## 8. Research & Insight Synthesis

### AI-Powered Reddit Research at Scale

**Use Case**: You want to analyze 1000+ more Reddit posts to expand your research

**Manual**: Weeks of reading and note-taking
**With AI**: 2-3 hours

### Workflow: Mass Content Analysis

**Step 1: Data Collection**

Use Reddit API to pull 1000 posts matching your keywords:

```python
def collect_reddit_posts(subreddit_name, keyword, limit=1000):
    """Collect posts containing keywords"""

    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.search(keyword, limit=limit):
        posts.append({
            'title': post.title,
            'content': post.selftext,
            'score': post.score,
            'num_comments': post.num_comments,
            'created': datetime.fromtimestamp(post.created_utc),
            'url': post.permalink
        })

    return posts

# Collect data
all_posts = []
for keyword in ['dissertation feedback', 'advisor feedback', 'thesis feedback']:
    posts = collect_reddit_posts('PhD', keyword, 500)
    all_posts.extend(posts)
```

**Step 2: AI Analysis**

**Prompt** (for batches of 50 posts):
```
Analyze these 50 Reddit posts about dissertation feedback challenges:

[Paste post summaries]

Extract:
1. Common themes (categorize by our 6 pain points)
2. New pain points not in our original research
3. Emotional sentiment (frustrated/defeated/angry/hopeful)
4. Specific quotes that illustrate pain points powerfully
5. Solutions students mention trying (success rate if mentioned)
6. Discipline-specific patterns
7. Career stage patterns (early vs ABD)

Provide:
- Frequency count for each pain point
- Most impactful quotes (for use in marketing)
- Emerging trends not yet in our data
- Segmentation insights (by field, stage, etc.)
```

**Step 3: Synthesis Report**

**Prompt**:
```
I've analyzed 1000 Reddit posts in batches. Here are the summaries from each batch:

[Paste 20 batch summaries]

Synthesize this into:
1. Updated pain point frequency distribution
2. New pain points discovered
3. Most compelling student quotes (top 20)
4. Discipline-specific insights
5. Changes from my original 500-post analysis
6. Implications for PhD-Assist features
7. New content ideas for next posts

Create comprehensive research update report.
```

**Time Saved**: 40 hours → 3 hours

---

<a name="workflows"></a>
## 9. Workflow Automation

### Complete Daily Workflow (AI-Accelerated)

**Morning Routine (15 minutes)**:

```
8:00 AM - Check Reddit Monitor Email (AI-generated digest)
         → Click top 3 relevant threads

8:05 AM - Paste threads into Claude with batch response prompt
         → Get 3 draft responses

8:10 AM - Review, personalize, post responses

8:15 AM - Check analytics dashboard (AI summary)
```

**Weekly Content Creation (1 hour)**:

```
Monday 9:00 AM - Write one master content piece (Reddit post)
                → Use Claude to expand research into full post

Monday 9:30 AM - Run through multi-platform adaptation prompt
                → Get Twitter thread, LinkedIn article, blog outline

Monday 9:45 AM - Review and schedule all adaptations

Monday 10:00 AM - Week complete! Content scheduled for all platforms
```

**Monthly Outreach (2 hours)**:

```
First Monday of Month:
- Export 20 new university contacts from research
- Batch personalization prompt for all 20
- Review and send emails
- Schedule follow-ups automatically
```

---

### Automation Stack Setup

**Tools**:
1. **Make.com** (workflow automation) - $9/month
2. **Claude API** or **OpenAI API** - ~$20/month usage
3. **Buffer** (social scheduling) - $6/month
4. **Airtable** (database tracking) - Free tier
5. **Zapier** (backup automation) - $20/month

**Total Cost**: ~$55/month to save 8+ hours/week

**ROI**: Your time is worth more than $55/month!

---

<a name="tools-stack"></a>
## 10. AI Tools Stack

### Recommended Setup

**Tier 1: Core AI (Required)**

| Tool | Use Case | Cost | Why This One |
|------|----------|------|--------------|
| **Claude Pro** | Response drafting, content creation, analysis | $20/mo | Best for nuanced academic writing, large context window |
| **ChatGPT Plus** | Quick drafts, brainstorming, backups | $20/mo | Faster for simple tasks, different voice |
| **Perplexity Pro** | Research, finding contact info, fact-checking | $20/mo | Real-time web search, citations |

**Tier 2: Automation (Highly Recommended)**

| Tool | Use Case | Cost |
|------|----------|------|
| **Make.com** | Workflow automation, API integration | $9/mo |
| **Zapier** | Simpler automations, email workflows | $20/mo |
| **Buffer** | Social media scheduling | $6/mo |

**Tier 3: Specialized (Optional)**

| Tool | Use Case | Cost |
|------|----------|------|
| **Jasper.ai** | Marketing copy optimization | $49/mo |
| **Lex** | Long-form writing assistant | $8/mo |
| **Notion AI** | Note organization, summaries | $10/mo |

**Recommended Starting Stack**:
- Claude Pro ($20/mo)
- Make.com ($9/mo)
- Buffer ($6/mo)
- **Total: $35/month**

---

<a name="prompts"></a>
## 11. Prompts Library

### Master Prompts (Copy-Paste Ready)

#### Prompt 1: Reddit Comment Generator

```
CONTEXT:
I'm a PhD student who researched dissertation feedback challenges. I engage authentically on Reddit to help students, occasionally mentioning my beta tool.

RESEARCH SUMMARY:
- Pain Point #1: No feedback (38%)
- Pain Point #2: Vague feedback (24%)
- Pain Point #3: Inconsistent feedback (19%)
- Pain Point #4: Slow turnaround (17%)
- Pain Point #5: Harsh feedback (12%)
- Pain Point #6: Unavailable advisor (14%)

MY TONE:
- Peer-to-peer, not expert-to-novice
- Empathetic and validating
- Data-driven but conversational
- Helpful first, promotional never (unless asked)

REDDIT POST I WANT TO RESPOND TO:
[paste post]

GENERATE:
1. Relevance score (1-10)
2. Which pain point(s) this relates to
3. Draft response (200-250 words) that:
   - Validates their experience with relevant data
   - Provides 2-3 specific, actionable strategies
   - Asks follow-up question
   - Does NOT mention my tool (first response)
4. Suggested follow-up approach if they reply
```

---

#### Prompt 2: Content Repurposer

```
MASTER CONTENT:
[paste your content]

TARGET PLATFORM: [Reddit/Twitter/LinkedIn/Blog]

TRANSFORM this content for [platform] while:
1. Maintaining core insights and data
2. Adapting tone for platform culture
3. Optimizing format for platform (thread/article/post)
4. Including platform-specific CTA
5. Suggesting optimal posting time

PLATFORM GUIDELINES:
- Reddit: Conversational, detailed, peer support
- Twitter: Punchy, thread format, hashtags minimal
- LinkedIn: Professional, implications for institutions
- Blog: SEO-optimized, comprehensive, sections

OUTPUT:
- Adapted content
- Headline/title optimized for platform
- Posting time suggestion
- Engagement prediction
```

---

#### Prompt 3: Email Personalizer

```
EMAIL TEMPLATE:
[paste template from outreach-templates.md]

TARGET CONTACT:
- Name: [name]
- Title: [title]
- Institution: [university]
- Program: [what they run]

RESEARCH ON THEIR WORK:
[paste from their website/LinkedIn]

PERSONALIZE this email by:
1. Referencing specific programs they run
2. Connecting my research to their existing work
3. Using their terminology/language
4. Adjusting formality to institutional culture
5. Adding genuine compliment/observation about their work

OUTPUT:
- Personalized subject line (3 options)
- Customized email body
- Optimal send day/time
- Follow-up strategy
```

---

#### Prompt 4: Analytics Analyzer

```
USER ACQUISITION DATA (This Week):

REDDIT:
- Posts: [data]
- Comments: [data]
- Engagement: [data]

EMAIL:
- Open rates: [data]
- Click rates: [data]

LANDING PAGE:
- Traffic: [data]
- Conversions: [data]

BETA SIGNUPS:
- Total: [number]
- By source: [breakdown]

ANALYZE:
1. What's working? (specific reasons why)
2. What's underperforming? (root causes)
3. Week-over-week trends (if previous data provided)
4. Top 3 priority actions for next week
5. A/B test recommendations
6. Risks or red flags

FORMAT:
- Executive summary (3 bullets)
- Detailed analysis by channel
- Actionable recommendations
- Predicted Week+1 outcomes
```

---

#### Prompt 5: Research Synthesizer

```
I collected [number] Reddit posts about dissertation feedback. Here are summaries:

BATCH 1 (Posts 1-50):
[summary]

BATCH 2 (Posts 51-100):
[summary]

[etc.]

SYNTHESIZE into comprehensive research update:

1. PAIN POINT FREQUENCY:
   - Updated percentages
   - Distribution by discipline
   - Distribution by career stage

2. NEW INSIGHTS:
   - Themes not in original research
   - Emerging pain points
   - Surprising patterns

3. BEST QUOTES:
   - Top 20 most powerful student quotes
   - Categorized by pain point
   - Usage recommendations (marketing copy)

4. IMPLICATIONS:
   - For PhD-Assist features
   - For content strategy
   - For positioning/messaging

5. CONTENT IDEAS:
   - 10 new post topics based on findings

FORMAT: Comprehensive report suitable for strategic planning
```

---

<a name="boundaries"></a>
## 12. What NOT to Automate

### The Human-Only Zone

**❌ Never Fully Automate**:

1. **Final Approval of Public Posts**
   - AI drafts, you must review
   - Why: Brand consistency, avoiding tone-deaf responses

2. **Personal DM Conversations**
   - AI can suggest responses, you must personalize
   - Why: These are relationships, not transactions

3. **Crisis Management**
   - If someone criticizes you publicly
   - If a post backfires
   - Why: Requires human judgment and empathy

4. **Beta Tester Onboarding Calls**
   - Must be genuinely you
   - Why: Building trust, gathering nuanced feedback

5. **Strategic Decisions**
   - Which features to prioritize
   - Major positioning changes
   - Partnership negotiations
   - Why: Context and intuition matter

6. **Sensitive Topics**
   - Mental health crises
   - Abusive advisor situations
   - Ethical dilemmas
   - Why: Requires human empathy and judgment

---

### The 80/20 Rule

**AI Does 80%**: Drafting, researching, analyzing, scheduling, monitoring

**You Do 20%**: Reviewing, personalizing, approving, relationship-building, strategic thinking

**This 20% is what makes you authentic and trustworthy.**

---

## 13. Weekly AI-Accelerated Schedule

### Example Week Using AI Tools

**Monday (2 hours)**:
```
9:00-9:30   - Review weekend Reddit digest (AI-monitored)
            - Respond to top 5 threads (AI-drafted, you personalize)

9:30-10:30  - Create master content piece for week
            - Use Claude to expand research into full post
            - Run multi-platform adaptation
            - Schedule all versions

10:30-11:00 - University outreach (5 emails)
            - AI personalizes template for 5 contacts
            - You review and send
```

**Tuesday-Thursday (30 min/day)**:
```
Morning     - Check Reddit digest
            - Post 3-5 AI-drafted comments (personalized)

Evening     - Respond to DMs and replies (human-only)
```

**Friday (1 hour)**:
```
9:00-9:30   - Review weekly analytics (AI summary)
            - Identify what worked/didn't

9:30-10:00  - Plan next week content based on AI insights
            - Adjust strategy as needed
```

**Total Time**: 5.5 hours/week (vs 18 hours without AI)
**Reach**: 2-3x more people due to efficiency
**Quality**: Maintained or improved (more time for personalization)

---

## 14. Implementation Roadmap

### Week 1: AI Setup

- [ ] Subscribe to Claude Pro
- [ ] Set up Reddit API access
- [ ] Create Reddit monitoring script (or F5Bot)
- [ ] Set up Claude Projects with your content
- [ ] Test response generation workflow
- [ ] Create prompts library in doc

### Week 2: Automation Setup

- [ ] Subscribe to Make.com or Zapier
- [ ] Create first automation (Reddit digest)
- [ ] Set up Buffer for social scheduling
- [ ] Test email personalization workflow
- [ ] Create analytics tracking sheet

### Week 3: Content Automation

- [ ] Test multi-platform repurposing
- [ ] Schedule first week of automated content
- [ ] Set up email sequence automation
- [ ] Test end-to-end workflow

### Week 4: Optimization

- [ ] Review what's working
- [ ] Refine prompts based on results
- [ ] Add more automations for bottlenecks
- [ ] Scale up volume

---

## 15. ROI Calculation

### Monthly Investment

**AI Tools**: $35/month
**Your Time Saved**: 32 hours/month (8 hours/week)
**Your Time Value**: $50/hour (conservative for PhD-level work)

**ROI**:
- Cost: $35
- Time Value Saved: $1,600
- **Net Benefit: $1,565/month**

### Reach Amplification

**Without AI**:
- 10 hours/week → 50-75 meaningful engagements/week
- Estimated: 30-50 beta signups in 12 weeks

**With AI**:
- 10 hours/week → 150-200 meaningful engagements/week
- Estimated: 100-150 beta signups in 12 weeks

**Result**: 3x reach with same time investment

---

## Final Thoughts

### The AI Advantage

You're a PhD student researching this topic. You have:
- ✅ Genuine expertise (500+ posts analyzed)
- ✅ Authentic pain points research
- ✅ Real solution being built
- ✅ Academic credibility

**AI helps you scale what's already authentic.**

You're not using AI to fake expertise. You're using it to:
- Reach more people who need your insights
- Respond faster to people asking for help
- Spend more time on high-value activities (relationship building)
- Less time on repetitive tasks (drafting, scheduling, formatting)

**This is the right use of AI.**

### Remember

The goal isn't to automate away the human connection. The goal is to **amplify your ability to help more PhD students** while maintaining the authenticity that makes your approach valuable.

AI writes the draft. You add the humanity.

Good luck! 🚀

---

**Next Steps**:
1. Start with Reddit monitoring (biggest time saver)
2. Add response drafting (quality maintained, speed increased)
3. Layer in content repurposing (reach multiplied)
4. Optimize based on what works for you

You don't need to implement everything at once. Start with one automation, master it, add the next.
