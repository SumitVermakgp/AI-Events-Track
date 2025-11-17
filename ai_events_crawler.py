#!/usr/bin/env python3
"""
AI Events Crawler - Real-time web scraping for AI conferences and events
Crawls WikiCFP, AI Conference Deadlines, and other sources for AI/ML events worldwide.
"""

import json
import os
import hashlib
import re
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from dateutil import parser as date_parser
    SCRAPING_ENABLED = True
except ImportError:
    SCRAPING_ENABLED = False
    print("⚠️  Warning: requests/beautifulsoup4 not installed. Install with: pip install -r requirements.txt")


class AIEventsCrawler:
    """Real-time crawler for AI-related events worldwide."""

    # Keywords to search for AI/ML related events
    AI_KEYWORDS = [
        "artificial intelligence", "machine learning", "deep learning",
        "neural networks", "natural language processing", "NLP",
        "computer vision", "reinforcement learning", "AI",
        "data science", "big data", "MLOps", "generative AI",
        "large language models", "LLM", "responsible AI", "AI safety",
        "AI ethics", "fairness", "accountability", "transparency"
    ]

    def __init__(self, data_file: str = "docs/events_data.json"):
        self.data_file = data_file
        self.events = []
        self.session = requests.Session() if SCRAPING_ENABLED else None
        if self.session:
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
        self.load_existing_data()

    def load_existing_data(self):
        """Load existing events data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.events = json.load(f)
                print(f"📥 Loaded {len(self.events)} existing events")
            except json.JSONDecodeError:
                print("⚠️  Error reading existing data, starting fresh")
                self.events = []
        else:
            print("📝 No existing data found, starting fresh")
            self.events = []

    def save_data(self):
        """Save events data to JSON file."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.events, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved {len(self.events)} total events to {self.data_file}")

    def generate_event_id(self, event: Dict) -> str:
        """Generate unique ID for event based on name, date, and location."""
        name = event.get('name', '').strip()
        date = event.get('date', '').strip()
        venue = event.get('venue', '').strip()
        key = f"{name}_{date}_{venue}".lower()
        return hashlib.md5(key.encode()).hexdigest()

    def event_exists(self, event: Dict) -> bool:
        """Check if event already exists in our data."""
        event_id = self.generate_event_id(event)
        existing_ids = [self.generate_event_id(e) for e in self.events]
        return event_id in existing_ids

    def add_event(self, event: Dict) -> bool:
        """Add event if it doesn't already exist."""
        if not self.event_exists(event):
            self.events.append(event)
            return True
        return False

    def normalize_date(self, date_str: str) -> Optional[str]:
        """Normalize various date formats to YYYY-MM-DD."""
        if not date_str or date_str == "N/A":
            return None

        try:
            # Try parsing the date
            parsed_date = date_parser.parse(date_str, fuzzy=True)
            return parsed_date.strftime("%Y-%m-%d")
        except:
            return None

    def extract_venue(self, location_str: str) -> str:
        """Extract clean venue from location string."""
        if not location_str:
            return "TBD"

        # Clean up common patterns
        location_str = location_str.strip()
        location_str = re.sub(r'\s+', ' ', location_str)

        # Remove "Location:" prefix if present
        location_str = re.sub(r'^Location:\s*', '', location_str, flags=re.IGNORECASE)

        return location_str if location_str else "TBD"

    def scrape_wikicfp(self) -> List[Dict]:
        """Scrape AI/ML conferences from WikiCFP."""
        if not SCRAPING_ENABLED:
            return []

        print("\n🔍 Scraping WikiCFP for AI conferences...")
        events = []

        # WikiCFP categories for AI/ML
        categories = ["artificial intelligence", "machine learning", "data mining"]

        for category in categories:
            try:
                url = f"http://www.wikicfp.com/cfp/call?conference={category.replace(' ', '%20')}"
                response = self.session.get(url, timeout=15)

                if response.status_code != 200:
                    print(f"  ⚠️  Failed to fetch WikiCFP category: {category}")
                    continue

                soup = BeautifulSoup(response.content, 'lxml')
                rows = soup.find_all('tr')

                for row in rows:
                    try:
                        cells = row.find_all('td')
                        if len(cells) < 3:
                            continue

                        # Extract event name and link
                        event_link = cells[0].find('a')
                        if not event_link:
                            continue

                        event_name = event_link.get_text(strip=True)
                        event_url = urljoin("http://www.wikicfp.com", event_link.get('href', ''))

                        # Extract location
                        location = cells[1].get_text(strip=True) if len(cells) > 1 else "TBD"

                        # Extract date
                        date_str = cells[2].get_text(strip=True) if len(cells) > 2 else None
                        event_date = self.normalize_date(date_str)

                        if not event_date:
                            continue

                        # Only include future events
                        if datetime.strptime(event_date, "%Y-%m-%d") < datetime.now():
                            continue

                        # Create event object
                        event = {
                            "name": event_name,
                            "format": "Hybrid",  # Default, can be refined
                            "venue": self.extract_venue(location),
                            "date": event_date,
                            "theme": category.title(),
                            "type": "Conference",
                            "submission_deadline": "N/A",
                            "ticket_start_date": "N/A",
                            "ticket_end_date": "N/A",
                            "url": event_url,
                            "description": f"{event_name} - {category.title()} conference",
                            "estimated_attendees": 1000  # Default estimate
                        }

                        events.append(event)

                    except Exception as e:
                        continue

                print(f"  ✓ Found {len([e for e in events if category.lower() in e.get('theme', '').lower()])} events in {category}")
                time.sleep(1)  # Be polite to the server

            except Exception as e:
                print(f"  ⚠️  Error scraping WikiCFP {category}: {str(e)}")

        return events

    def scrape_ai_deadlines(self) -> List[Dict]:
        """Scrape AI conference deadlines from aideadlin.es."""
        if not SCRAPING_ENABLED:
            return []

        print("\n🔍 Scraping AI Conference Deadlines...")
        events = []

        try:
            url = "https://aideadlin.es/?sub=ML,CV,NLP,RO,SP,DM"
            response = self.session.get(url, timeout=15)

            if response.status_code != 200:
                print("  ⚠️  Failed to fetch aideadlin.es")
                return events

            soup = BeautifulSoup(response.content, 'lxml')

            # Find conference entries
            conf_items = soup.find_all('div', class_='conf-instance')

            for item in conf_items[:30]:  # Limit to top 30 conferences
                try:
                    # Extract conference name
                    title_elem = item.find('h4')
                    if not title_elem:
                        continue

                    conf_name = title_elem.get_text(strip=True)

                    # Extract link
                    link_elem = title_elem.find('a')
                    conf_url = link_elem.get('href', 'N/A') if link_elem else 'N/A'

                    # Extract date
                    date_elem = item.find('span', class_='date')
                    date_str = date_elem.get_text(strip=True) if date_elem else None
                    conf_date = self.normalize_date(date_str)

                    if not conf_date:
                        continue

                    # Only include future events
                    if datetime.strptime(conf_date, "%Y-%m-%d") < datetime.now():
                        continue

                    # Extract location
                    location_elem = item.find('span', class_='location')
                    location = location_elem.get_text(strip=True) if location_elem else "TBD"

                    # Extract deadline
                    deadline_elem = item.find('span', class_='deadline')
                    deadline = self.normalize_date(deadline_elem.get_text(strip=True)) if deadline_elem else "N/A"

                    # Determine category
                    category = "Machine Learning"
                    if "NLP" in conf_name.upper() or "ACL" in conf_name.upper():
                        category = "Natural Language Processing"
                    elif "CV" in conf_name.upper() or "CVPR" in conf_name.upper() or "ICCV" in conf_name.upper():
                        category = "Computer Vision"

                    event = {
                        "name": conf_name,
                        "format": "Hybrid",
                        "venue": self.extract_venue(location),
                        "date": conf_date,
                        "theme": category,
                        "type": "Conference",
                        "submission_deadline": deadline if deadline else "N/A",
                        "ticket_start_date": "N/A",
                        "ticket_end_date": "N/A",
                        "url": conf_url,
                        "description": f"{conf_name} - Top-tier {category} conference",
                        "estimated_attendees": 3000
                    }

                    events.append(event)

                except Exception as e:
                    continue

            print(f"  ✓ Found {len(events)} conferences from AI Deadlines")

        except Exception as e:
            print(f"  ⚠️  Error scraping AI Deadlines: {str(e)}")

        return events

    def get_curated_baseline_events(self) -> List[Dict]:
        """
        Curated baseline of major AI events (fallback if scraping fails).
        These are high-quality, well-known events that should always be included.
        """
        return [
            {
                "name": "NeurIPS 2025",
                "format": "Hybrid",
                "venue": "Vancouver, Canada",
                "date": "2025-12-08",
                "theme": "Neural Information Processing Systems",
                "type": "Conference",
                "submission_deadline": "2025-05-15",
                "ticket_start_date": "2025-08-01",
                "ticket_end_date": "2025-12-07",
                "url": "https://neurips.cc",
                "description": "The leading conference in machine learning and computational neuroscience",
                "estimated_attendees": 15000
            },
            {
                "name": "ICML 2025",
                "format": "Hybrid",
                "venue": "Vancouver, Canada",
                "date": "2025-07-15",
                "theme": "International Conference on Machine Learning",
                "type": "Conference",
                "submission_deadline": "2025-01-30",
                "ticket_start_date": "2025-04-01",
                "ticket_end_date": "2025-07-14",
                "url": "https://icml.cc",
                "description": "Premier gathering of researchers in machine learning",
                "estimated_attendees": 10000
            },
            {
                "name": "CVPR 2026",
                "format": "Hybrid",
                "venue": "Nashville, USA",
                "date": "2026-06-19",
                "theme": "Computer Vision and Pattern Recognition",
                "type": "Conference",
                "submission_deadline": "2025-11-15",
                "ticket_start_date": "2026-03-01",
                "ticket_end_date": "2026-06-18",
                "url": "https://cvpr.cc",
                "description": "Leading conference in computer vision research",
                "estimated_attendees": 12000
            },
            {
                "name": "ICLR 2026",
                "format": "Hybrid",
                "venue": "Singapore",
                "date": "2026-04-24",
                "theme": "International Conference on Learning Representations",
                "type": "Conference",
                "submission_deadline": "2025-10-01",
                "ticket_start_date": "2026-02-01",
                "ticket_end_date": "2026-04-23",
                "url": "https://iclr.cc",
                "description": "Top-tier deep learning research conference",
                "estimated_attendees": 8000
            },
            {
                "name": "ACL 2026",
                "format": "Hybrid",
                "venue": "Bangkok, Thailand",
                "date": "2026-08-03",
                "theme": "Association for Computational Linguistics",
                "type": "Conference",
                "submission_deadline": "2026-02-15",
                "ticket_start_date": "2026-05-01",
                "ticket_end_date": "2026-08-02",
                "url": "https://www.aclweb.org",
                "description": "Premier conference for natural language processing",
                "estimated_attendees": 6000
            }
        ]

    def run(self):
        """Main crawler execution."""
        print("=" * 60)
        print("🤖 AI Events Crawler - Real-time Data Collection")
        print("=" * 60)
        print(f"📅 Searching for AI/ML events worldwide\n")

        new_events_count = 0

        # Add curated baseline events first
        print("📚 Adding curated baseline events...")
        baseline_events = self.get_curated_baseline_events()
        for event in baseline_events:
            if self.add_event(event):
                new_events_count += 1
        print(f"  ✓ Added {new_events_count} baseline events\n")

        if SCRAPING_ENABLED:
            # Scrape WikiCFP
            wikicfp_events = self.scrape_wikicfp()
            wikicfp_new = 0
            for event in wikicfp_events:
                if self.add_event(event):
                    wikicfp_new += 1
                    new_events_count += 1
            print(f"  ✓ Added {wikicfp_new} new events from WikiCFP\n")

            # Scrape AI Deadlines
            ai_deadline_events = self.scrape_ai_deadlines()
            ai_deadlines_new = 0
            for event in ai_deadline_events:
                if self.add_event(event):
                    ai_deadlines_new += 1
                    new_events_count += 1
            print(f"  ✓ Added {ai_deadlines_new} new events from AI Deadlines\n")
        else:
            print("⚠️  Scraping disabled - using baseline events only")
            print("   Install dependencies: pip install -r requirements.txt\n")

        # Sort events by date
        self.events.sort(key=lambda x: x.get('date', '9999-99-99'))

        # Add numbering
        for idx, event in enumerate(self.events, 1):
            event['#'] = idx

        # Save data
        self.save_data()

        # Summary
        print("=" * 60)
        if new_events_count > 0:
            print(f"✨ Successfully added {new_events_count} new AI events!")
        else:
            print(f"💫 No new events found. All {len(self.events)} events are up to date!")

        print(f"📊 Total events tracked: {len(self.events)}")

        if self.events:
            print(f"🌍 Geographic coverage: Global")
            print(f"📅 Date range: {self.events[0].get('date', 'N/A')} to {self.events[-1].get('date', 'N/A')}")

        print("=" * 60)


if __name__ == "__main__":
    crawler = AIEventsCrawler()
    crawler.run()
