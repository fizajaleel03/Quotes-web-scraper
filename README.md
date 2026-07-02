# Quotes Web Scraper

## Overview

This project is a Python web scraper that extracts quotes and their authors from the **Quotes to Scrape** website. The scraped data is exported to an Excel file for further analysis.

## Features

- Scrapes quotes and authors from multiple pages.
- Handles HTTP request errors using `try-except`.
- Parses HTML using BeautifulSoup.
- Exports the scraped data to an Excel file using Pandas.

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas
- OpenPyXL

## Project Structure

```text
Quotes_Web_Scraper/
│── Quotes_Scraper.py
│── Quotes_Scraping.xlsx
│── README.md
│── requirements.txt
│── .gitignore
└── Screenshots/
    └── output.png
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/fizajaleel03/Quotes-web-scraper.git
```

### 2. Navigate to the project folder

```bash
cd Quotes-web-scraper
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the scraper

```bash
python Quotes_Scraper.py
```

## Output

The scraper generates an Excel file named:

`Quotes_Scraping.xlsx`

containing the following columns:

- Quote
- Author

## Screenshot

![Sample Output](Screenshots/output.png)

## Author

**Fiza Jaleel**