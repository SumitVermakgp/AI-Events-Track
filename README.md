# 🤖 AI Events Worldwide

> Automatically-updated directory of AI conferences, workshops, summits, and talks from around the globe

[![GitHub Actions](https://github.com/SumitVermakgp/AI-Events-Track/workflows/AI%20Events%20Crawler/badge.svg)](https://github.com/SumitVermakgp/AI-Events-Track/actions)
[![Last Crawl](https://img.shields.io/badge/last%20crawl-daily-blue)](https://github.com/SumitVermakgp/AI-Events-Track/actions)
[![Events](https://img.shields.io/badge/events-20+-green)](./docs/events_data.json)

## 📋 Overview

This repository contains an automated system that:
- 🔄 Crawls major AI events worldwide **daily**
- 📊 Maintains a curated list of conferences, summits, and workshops
- 🌐 Publishes a mobile-friendly website with search and filtering
- 🚫 Prevents duplicates with intelligent deduplication
- ✅ Only tracks high-quality, major AI events

## 🌟 Features

- **Daily Automated Updates**: GitHub Actions workflow runs at midnight UTC
- **Global Coverage**: Events from North America, Europe, Asia, Africa, and Latin America
- **20+ Major Events**: From July 2025 to November 2026
- **Mobile-Friendly UI**: Responsive design for all devices
- **Smart Filtering**: Search, format, date, and type filters
- **Real-time Stats**: Event counts, upcoming events, geographic coverage

## 📊 Event Coverage

### Academic Conferences
- NeurIPS 2025, ICML 2025, CVPR 2026, ICLR 2026, ACL 2026, AAAI 2026

### Business Summits
- AI Summit (New York, London)
- RE•WORK Deep Learning Summit
- Generative AI World

### Specialized Events
- MLOps World 2026
- AI in Healthcare Summit 2026
- AI for Good Global Summit 2026

### Developer Events
- PyTorch Conference 2026
- TensorFlow Dev Summit 2026

### Regional Events
- AI India Summit, AI China Conference, AI Africa Summit, AI LATAM

## 🚀 Live Website

Visit: **[https://sumitvermakgp.github.io/AI-Events-Track/](https://sumitvermakgp.github.io/AI-Events-Track/)**

## 🛠️ How It Works

```
┌─────────────────────┐
│  GitHub Actions     │
│  (Daily at 00:00)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Python Crawler     │
│  ai_events_crawler  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  events_data.json   │
│  (Deduplicated)     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  GitHub Pages       │
│  (Auto Deploy)      │
└─────────────────────┘
```

## 📁 Repository Structure

```
AI-Events-Track/
├── ai_events_crawler.py       # Python crawler script
├── docs/
│   ├── index.html             # Mobile-friendly website
│   ├── events_data.json       # Events database
│   ├── _config.yml            # GitHub Pages config
│   ├── .nojekyll              # Disable Jekyll processing
│   └── README.md              # Documentation
├── .github/
│   └── workflows/
│       └── ai-events-crawler.yml  # Daily automation
└── README.md                  # This file
```

## 🔧 Technical Details

**Backend:**
- Python 3.11
- JSON data storage
- Smart deduplication using MD5 hashing

**Frontend:**
- Pure JavaScript (no frameworks)
- Responsive CSS Grid
- Mobile-first design

**Automation:**
- GitHub Actions (cron schedule)
- Automatic commits on new events
- GitHub Pages deployment

## 📅 Data Format

Each event includes:
```json
{
  "#": 1,
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
  "description": "...",
  "estimated_attendees": 15000
}
```

## 🚦 Workflow Schedule

- **Automated Run**: Daily at 00:00 UTC
- **Manual Trigger**: Available via GitHub Actions UI
- **Auto-Deploy**: On every data update

## 🎯 Quality Standards

✅ Only major, reputable events
✅ No duplicates
✅ Verified information
✅ Active/upcoming events (2025-2026)
✅ Significant attendance (1000+ for major conferences)

## 🤝 Contributing

This is an automated system. For event suggestions or corrections:
1. Open an issue with event details
2. Include: name, date, location, official URL
3. Ensure it's a major, reputable AI event

## 📝 License

MIT License - Data sourced from official event websites and public sources.

## 📧 Contact

- GitHub Issues: [Report a problem](https://github.com/SumitVermakgp/AI-Events-Track/issues)
- Repository: [SumitVermakgp/AI-Events-Track](https://github.com/SumitVermakgp/AI-Events-Track)

---

**🤖 Automated by GitHub Actions** | **📅 Updated Daily** | **🌍 Global Coverage**
