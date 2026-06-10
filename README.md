# Books To Scrape Scraper

## Project Overview

A Playwright scraper for the Books To Scrape practice website.

This project collects book data from list pages, visits each book detail page, extracts detailed book information, and exports the results into a CSV file.

## Features

* User-defined page range
* Scrape book title
* Scrape book detail link
* Visit each book detail page
* Extract book price
* Extract stock availability
* Extract rating
* Extract product description
* Export results to CSV

## Technologies

* Python
* Playwright
* CSV

## Output Fields

* book_title
* book_link
* price
* stock
* rating
* description

## Learning Goals

This project focuses on:

* List page scraping
* Detail page scraping
* HTML structure analysis
* CSS selectors
* Attribute extraction
* Relative URL handling
* CSV data export
* Function-based code structure
* Basic exception handling

## Version History

### v1.0

* Added page range input
* Scraped book titles and detail links from list pages
* Visited each book detail page
* Extracted price, stock, rating and description
* Exported complete book data to CSV

### v1.1

* Refactored scraper into reusable functions
* Added `get_book_links()` for list page scraping
* Added `scrape_book_detail()` for detail page scraping
* Added basic input validation for page range
* Added error handling so one failed book does not stop the whole scraper
* Improved code readability and project structure



## Notes

This is a beginner-friendly scraping project designed to practice the common commercial scraping pattern:

List page → Detail page → Structured CSV output
