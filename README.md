# AI Events Worldwide

> Discover and track major AI conferences, workshops, summits, and talks from around the globe

**Built with ♥ by [Responsible AI Labs](https://responsibleailabs.ai)**

[![GitHub Actions](https://github.com/SumitVermakgp/AI-Events-Track/workflows/AI%20Events%20Crawler/badge.svg)](https://github.com/SumitVermakgp/AI-Events-Track/actions)
[![Last Crawl](https://img.shields.io/badge/last%20crawl-daily-blue)](https://github.com/SumitVermakgp/AI-Events-Track/actions)
[![Events](https://img.shields.io/badge/events-30-green)](./docs/events_data.json)

## 📋 Overview

This repository contains an automated system that:
- 🔄 Crawls major AI events worldwide **daily**
- 📊 Maintains a curated list of conferences, summits, and workshops
- 🌐 Publishes a mobile-friendly website with search and filtering
- 🚫 Prevents duplicates with intelligent deduplication
- ✅ Only tracks high-quality, major AI events

## 🌟 Features

- **🔄 Daily Automated Updates**: GitHub Actions workflow runs at midnight UTC
- **🌍 Global Coverage**: Events from North America, Europe, Asia, Africa, and Latin America
- **📊 30 Major AI Events**: Curated events from November 2025 to November 2026
- **📱 Mobile-First Design**: Collapsible filters and responsive layout optimized for mobile
- **🎨 Timeline & Grid Views**: Beautiful chronological timeline or card grid layout
- **🔍 Smart Search & Filtering**: Filter by format, type, month, and search across all fields
- **📈 Real-time Stats**: Event counts, upcoming events, countdown timers, and more
- **🎯 Auto-hide Past Events**: Only shows current and upcoming events

## 📊 Event Coverage (30 Events)

### 🎓 Academic Conferences (11)
- **NeurIPS 2025** - Neural Information Processing Systems (Vancouver)
- **ICML 2025** - International Conference on Machine Learning (Vancouver)
- **CVPR 2026** - Computer Vision and Pattern Recognition (Nashville)
- **ICLR 2026** - Learning Representations (Singapore)
- **ACL 2026** - Computational Linguistics (Bangkok)
- **AAAI 2026** - Artificial Intelligence (Philadelphia)
- **EMNLP 2025** - NLP & Language Models (Miami)
- **AISTATS 2026** - AI & Statistics (Valencia)
- **KDD 2026** - Knowledge Discovery & Data Mining (Chicago)
- **IJCAI 2026** - International Joint Conference on AI (Montreal)
- **ECCV 2026** - European Computer Vision (Milan)

### 🏢 Business & Enterprise Summits (8)
- **AI Summit New York 2025** - Enterprise AI
- **AI Summit London 2026** - Business AI
- **World Summit AI 2025** - Doha, Qatar
- **RE•WORK Deep Learning Summit 2026** - San Francisco
- **Generative AI World 2026** - Las Vegas
- **AI World Government Summit 2026** - Dubai, UAE
- **AI & Big Data Expo 2026** - Amsterdam
- **EmTech Digital 2026** - MIT Technology Review

### 🎯 Specialized AI Events (5)
- **FAccT 2026** - Fairness, Accountability & Transparency (Barcelona)
- **MLOps World 2026** - ML Operations (Austin)
- **AI in Healthcare Summit 2026** - Medical AI (Boston)
- **AI for Good Global Summit 2026** - UN Platform (Geneva)
- **AI Hardware Summit 2026** - AI Chips & Accelerators (Santa Clara)

### 💻 Developer Events (2)
- **PyTorch Conference 2026** - Deep Learning Frameworks
- **TensorFlow Dev Summit 2026** - Google ML Platform (Virtual)

### 🌍 Regional Events (4)
- **IndiaAI Summit 2026** - New Delhi (Government of India flagship event)
- **AI China Conference 2026** - Beijing
- **AI Africa Summit 2026** - Cape Town
- **AI LATAM 2026** - São Paulo

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

## 📧 Contact & Support

- **Report Issues**: [GitHub Issues](https://github.com/SumitVermakgp/AI-Events-Track/issues)
- **Responsible AI Labs**: [responsibleailabs.ai](https://responsibleailabs.ai)

---

<div align="center">

**Built with ♥ by [Responsible AI Labs](https://responsibleailabs.ai)**

🤖 Automated by GitHub Actions | 📅 Updated Daily | 🌍 Global Coverage

</div>
