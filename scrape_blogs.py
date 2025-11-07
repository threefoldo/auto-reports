#!/usr/bin/env python3
"""
Scrape PyMC Labs blog posts and create summaries
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
from pathlib import Path
from datetime import datetime

def clean_filename(title):
    """Create a safe filename from title"""
    # Remove special characters
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    # Replace spaces with dashes
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename[:100]  # Limit length

def fetch_blog_post(url):
    """Fetch a single blog post content"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'lxml')

        # Extract title
        title = soup.find('h1')
        title_text = title.get_text(strip=True) if title else url.split('/')[-1]

        # Extract main content
        content = ""

        # Try article tag
        article = soup.find('article')
        if article:
            # Get all text but clean it up
            paragraphs = article.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li'])
            content = '\n\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

        # Fallback: main tag
        if not content:
            main = soup.find('main')
            if main:
                paragraphs = main.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'li'])
                content = '\n\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

        # Extract metadata
        date = None
        author = None
        description = None

        # Look for date
        date_meta = soup.find('meta', property='article:published_time') or \
                    soup.find('meta', attrs={'name': 'date'}) or \
                    soup.find('time')
        if date_meta:
            date = date_meta.get('content') or date_meta.get('datetime') or date_meta.get_text(strip=True)

        # Look for author
        author_meta = soup.find('meta', attrs={'name': 'author'}) or \
                      soup.find('meta', property='article:author')
        if author_meta:
            author = author_meta.get('content')

        # Look for description
        desc_meta = soup.find('meta', attrs={'name': 'description'}) or \
                    soup.find('meta', property='og:description')
        if desc_meta:
            description = desc_meta.get('content')

        return {
            'title': title_text,
            'url': url,
            'date': date,
            'author': author,
            'description': description,
            'content': content,
            'word_count': len(content.split()) if content else 0
        }

    except Exception as e:
        print(f"  Error: {e}")
        return None

def create_summary(post_data):
    """Create a brief summary of the blog post"""
    # Create a simple extractive summary (first few paragraphs + metadata)
    content = post_data['content']
    if not content:
        return "No content available."

    # Get first 300 words as summary
    words = content.split()
    summary_words = words[:300]
    summary = ' '.join(summary_words)

    if len(words) > 300:
        summary += "..."

    return summary

def main():
    # Read URLs from file
    urls_file = Path("blog_urls.txt")
    with open(urls_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Found {len(urls)} blog post URLs")

    # Create output directory
    output_dir = Path("pymc_blog_posts")
    output_dir.mkdir(exist_ok=True)

    # Fetch each blog post
    all_posts = []
    summaries = []

    for i, url in enumerate(urls):
        print(f"\n[{i+1}/{len(urls)}] Fetching: {url}")

        post_data = fetch_blog_post(url)

        if post_data:
            all_posts.append(post_data)

            # Create filename
            slug = url.split('/blog-posts/')[-1]
            filename = f"{i+1:03d}_{clean_filename(slug)}.txt"

            # Save individual post
            filepath = output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"Title: {post_data['title']}\n")
                f.write(f"URL: {post_data['url']}\n")
                if post_data['date']:
                    f.write(f"Date: {post_data['date']}\n")
                if post_data['author']:
                    f.write(f"Author: {post_data['author']}\n")
                if post_data['description']:
                    f.write(f"Description: {post_data['description']}\n")
                f.write(f"Word Count: {post_data['word_count']}\n")
                f.write(f"\n{'='*80}\n\n")
                f.write(post_data['content'])

            print(f"  ✓ Saved to {filename}")
            print(f"  Title: {post_data['title']}")
            print(f"  Words: {post_data['word_count']}")

            # Create summary
            summary = create_summary(post_data)
            summaries.append({
                'number': i+1,
                'title': post_data['title'],
                'url': post_data['url'],
                'date': post_data['date'],
                'description': post_data['description'],
                'word_count': post_data['word_count'],
                'summary': summary,
                'filename': filename
            })
        else:
            print(f"  ✗ Failed to fetch")

        # Rate limiting - be respectful
        time.sleep(2)

    # Save all posts as JSON
    with open(output_dir / "all_posts.json", 'w', encoding='utf-8') as f:
        json.dump(all_posts, f, indent=2)

    # Save summaries as JSON
    with open(output_dir / "summaries.json", 'w', encoding='utf-8') as f:
        json.dump(summaries, f, indent=2)

    # Create an index file with summaries
    with open(output_dir / "INDEX.md", 'w', encoding='utf-8') as f:
        f.write("# PyMC Labs Blog Posts Summary\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Posts: {len(summaries)}\n\n")
        f.write("---\n\n")

        for s in summaries:
            f.write(f"## {s['number']}. {s['title']}\n\n")
            f.write(f"**URL:** {s['url']}\n\n")
            if s['date']:
                f.write(f"**Date:** {s['date']}\n\n")
            if s['description']:
                f.write(f"**Description:** {s['description']}\n\n")
            f.write(f"**Word Count:** {s['word_count']}\n\n")
            f.write(f"**File:** `{s['filename']}`\n\n")
            f.write(f"**Summary:**\n\n{s['summary']}\n\n")
            f.write("---\n\n")

    print(f"\n{'='*80}")
    print(f"✓ Successfully scraped {len(all_posts)} blog posts")
    print(f"✓ Saved to: {output_dir}/")
    print(f"✓ Index file: {output_dir}/INDEX.md")
    print(f"✓ Summaries JSON: {output_dir}/summaries.json")
    print(f"✓ All posts JSON: {output_dir}/all_posts.json")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
