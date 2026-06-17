# BeautifulSoupRequest

Simple Python web scraper using BeautifulSoup and Requests.

## What it does
BeautifulSoupRequest is a basic scraping script that demonstrates how to fetch a webpage and extract specific HTML elements. In its current implementation, it retrieves heading tags (h1, h2, h3) from zoesquad.me and prints them to the console.

## Stack
| Component | Detail |
|---|---|
| Language | Python |
| Key libraries | BeautifulSoup4, Requests, Scrapy |
| Port / endpoint | N/A |

## Quick Start
```bash
# Install dependencies
pip install bs4 requests lxml

# Run the scraper
python main.py
```

## Environment Variables (if any)
| Variable | Default | Description |
|---|---|---|
| None | | |

## API / Usage
Run the `main.py` script to perform a live scrape of the configured URL. The script will output the tag name and text content for all found heading elements.
