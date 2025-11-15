# AI Events Worldwide 🤖

A comprehensive, automatically-updated directory of AI-related conferences, workshops, summits, and talks from around the world.

## 🌟 Features

- **Daily Updates**: Automatically crawls and updates event information every day at midnight UTC
- **Global Coverage**: Events from all continents and major tech hubs
- **Multiple Event Types**: Conferences, workshops, summits, and developer events
- **Rich Information**: Dates, venues, themes, submission deadlines, ticket information, and more
- **Mobile-Friendly**: Responsive design works perfectly on all devices
- **Smart Filtering**: Search, filter by format (in-person/online/hybrid), month, and event type
- **No Duplicates**: Intelligent deduplication ensures each event appears only once

## 📊 Event Information

Each event includes:

- **#**: Event number in chronological order
- **Name**: Official event name
- **Format**: In-person, Online, or Hybrid
- **Venue**: Location (city, country) or Virtual
- **Date**: Event date
- **Theme**: Main focus area or tagline
- **Type**: Conference, Summit, Workshop, or Expo
- **Submission Deadline**: For academic conferences accepting papers
- **Ticket Dates**: When tickets go on sale and event closes
- **URL**: Official event website
- **Description**: Brief overview of the event
- **Expected Attendees**: Estimated attendance

## 🎯 Event Types Covered

### Academic Conferences
- NeurIPS, ICML, CVPR, ICLR, ACL, AAAI
- Top-tier research venues with peer-reviewed papers

### Business Summits
- AI Summit series (New York, London, etc.)
- Regional business-focused events

### Developer Events
- PyTorch Conference
- TensorFlow Dev Summit
- Framework-specific gatherings

### Specialized Events
- MLOps World (ML Engineering)
- Generative AI World (LLMs & GenAI)
- AI in Healthcare Summit
- AI for Good Global Summit

### Regional Events
- AI India Summit
- AI China Conference
- AI Africa Summit
- AI LATAM

## 🌍 Geographic Coverage

Events from:
- **North America**: USA, Canada
- **Europe**: UK, Switzerland
- **Asia**: Singapore, India, China, Thailand
- **Africa**: South Africa
- **Latin America**: Brazil

## 📅 Timeline

Currently tracking events from:
- **Start**: July 2025
- **End**: November 2026

The system automatically updates daily and adds newly announced events.

## 🔄 How It Works

1. **Daily Crawl**: GitHub Actions workflow runs at 00:00 UTC every day
2. **Smart Detection**: Crawler identifies new AI events from curated sources
3. **Deduplication**: System prevents duplicate entries using intelligent hashing
4. **Auto-Commit**: Only commits when new events are found
5. **Live Update**: GitHub Pages deploys automatically with updated data

## 🚀 Technology Stack

- **Backend**: Python 3.11
- **Data Storage**: JSON
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Automation**: GitHub Actions
- **Hosting**: GitHub Pages

## 📱 Mobile-First Design

The interface is optimized for:
- ✅ Smartphones (iOS & Android)
- ✅ Tablets
- ✅ Desktop browsers
- ✅ High-DPI displays

## 🎨 Features

### Search & Filter
- Real-time text search across all event fields
- Filter by format (In-person, Online, Hybrid)
- Filter by month/year
- Filter by event type (Conference, Summit, Workshop)

### Statistics Dashboard
- Total events count
- Upcoming events count
- Number of countries represented

### Event Cards
- Color-coded by format
- Visual badges for event type
- Direct links to official websites
- Ticket availability windows
- Submission deadlines (for conferences)

## 🔗 Live Site

Visit the live site at: `https://<username>.github.io/AI-Events-Track/`

## 📝 License

This is a public data aggregation project. Event information is sourced from official event websites and public announcements.

## 🤝 Contributing

This project uses automated crawling. Events are curated for quality to include only major, reputable AI events.

## 📧 Contact

For event submissions or corrections, please open an issue in this repository.

---

**Last Updated**: Automatically updated daily by GitHub Actions

**Next Update**: Tomorrow at 00:00 UTC
