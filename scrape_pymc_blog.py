#!/usr/bin/env python3
"""
Scrape blog posts from PyMC Labs website
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
from pathlib import Path
from urllib.parse import urljoin

def fetch_blog_listing(url):
    """Fetch the blog listing page and extract blog post URLs"""
    print(f"Fetching blog listing from {url}...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'lxml')

    # Look for blog post links
    blog_posts = []

    # Strategy 1: Find all links that might be blog posts
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href and '/blog-posts/' in href:
            full_url = urljoin(url, href)
            title = link.get_text(strip=True)
            if title and full_url not in [bp['url'] for bp in blog_posts]:
                blog_posts.append({
                    'title': title,
                    'url': full_url
                })

    # Strategy 2: Check for JSON-LD or other structured data
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string)
            # Process structured data if available
            print(f"Found structured data: {type(data)}")
        except:
            pass

    # Strategy 3: Look for Next.js data
    for script in soup.find_all('script', id=True):
        if 'next' in script.get('id', '').lower():
            print(f"Found Next.js script: {script.get('id')}")
            # Try to extract data
            content = script.string
            if content:
                # Look for URLs in the script content
                urls = re.findall(r'"/blog-posts/[^"]+', content)
                for url_path in urls:
                    full_url = urljoin(url, url_path.strip('"'))
                    if full_url not in [bp['url'] for bp in blog_posts]:
                        # Extract title from URL path
                        title = url_path.split('/')[-1].replace('-', ' ').title()
                        blog_posts.append({
                            'title': title,
                            'url': full_url
                        })

    print(f"Found {len(blog_posts)} blog posts")
    return blog_posts

def fetch_blog_post(url):
    """Fetch a single blog post content"""
    print(f"  Fetching {url}...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'lxml')

    # Extract title
    title = soup.find('h1')
    title_text = title.get_text(strip=True) if title else "Untitled"

    # Extract main content - try different strategies
    content = None

    # Strategy 1: Look for article tag
    article = soup.find('article')
    if article:
        content = article.get_text(separator='\n', strip=True)

    # Strategy 2: Look for main content div
    if not content:
        main = soup.find('main')
        if main:
            content = main.get_text(separator='\n', strip=True)

    # Strategy 3: Get all paragraphs
    if not content:
        paragraphs = soup.find_all('p')
        content = '\n\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

    # Extract metadata
    date = None
    author = None

    # Look for date in meta tags
    date_meta = soup.find('meta', property='article:published_time') or \
                soup.find('meta', attrs={'name': 'date'})
    if date_meta:
        date = date_meta.get('content')

    # Look for author
    author_meta = soup.find('meta', attrs={'name': 'author'}) or \
                  soup.find('meta', property='article:author')
    if author_meta:
        author = author_meta.get('content')

    return {
        'title': title_text,
        'url': url,
        'date': date,
        'author': author,
        'content': content
    }

def main():
    base_url = "https://www.pymc-labs.com/blog-posts"

    # Fetch blog listing
    blog_posts = fetch_blog_listing(base_url)

    if not blog_posts:
        print("No blog posts found. The page might be fully JavaScript-rendered.")
        print("Trying alternative approach...")

        # Try to manually construct some known blog post URLs
        # We can also just save the page source to inspect
        response = requests.get(base_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        print("\n=== Page Source Preview ===")
        print(response.text[:2000])
        print("\n=== Searching for blog post patterns ===")

        # Find all potential blog post URLs in the raw HTML/JavaScript
        urls = set(re.findall(r'"/blog-posts/([^"]+)"', response.text))
        for url_path in urls:
            if url_path and url_path != '':
                full_url = f"{base_url}/{url_path}"
                blog_posts.append({
                    'title': url_path.replace('-', ' ').title(),
                    'url': full_url
                })

        print(f"Found {len(blog_posts)} potential blog posts in source")

    # Create output directory
    output_dir = Path("pymc_blog_posts")
    output_dir.mkdir(exist_ok=True)

    # Save blog post list
    with open(output_dir / "blog_list.json", 'w') as f:
        json.dump(blog_posts, f, indent=2)

    print(f"\nSaved blog post list to {output_dir / 'blog_list.json'}")
    print(f"Found {len(blog_posts)} blog posts")

    # Fetch each blog post
    all_posts = []
    for i, post in enumerate(blog_posts[:10]):  # Limit to first 10 for now
        try:
            print(f"\n[{i+1}/{min(len(blog_posts), 10)}] {post['title']}")
            post_data = fetch_blog_post(post['url'])
            all_posts.append(post_data)

            # Save individual post
            filename = re.sub(r'[^\w\s-]', '', post['title'].lower())
            filename = re.sub(r'[-\s]+', '-', filename)
            filename = f"{i+1:03d}_{filename}.txt"

            with open(output_dir / filename, 'w') as f:
                f.write(f"Title: {post_data['title']}\n")
                f.write(f"URL: {post_data['url']}\n")
                if post_data['date']:
                    f.write(f"Date: {post_data['date']}\n")
                if post_data['author']:
                    f.write(f"Author: {post_data['author']}\n")
                f.write(f"\n{'='*80}\n\n")
                f.write(post_data['content'])

            print(f"  Saved to {filename}")

            # Be respectful with rate limiting
            time.sleep(1)

        except Exception as e:
            print(f"  Error fetching {post['url']}: {e}")

    # Save all posts as JSON
    with open(output_dir / "all_posts.json", 'w') as f:
        json.dump(all_posts, f, indent=2)

    print(f"\n✓ Scraped {len(all_posts)} blog posts to {output_dir}/")
    return output_dir, all_posts

if __name__ == "__main__":
    main()
