# Goodreads Book Scraper

A Python application that scrapes book information from Goodreads.com based on user-specified categories. The application provides both a command-line interface and a graphical user interface (GUI).

## Features

- Search books by category
- Scrapes following book details:
  - Title
  - Author
  - Publication Year
  - Rating
  - Edition
  - Book Link
- Export results to CSV file
- User-friendly GUI interface
- Command-line interface option

## Requirements


selenium
webdriver-manager
tkinter (usually comes with Python)


## Installation

1. Clone or download this repository
2. Install required packages:
bash
pip install selenium webdriver-manager


## Usage

### GUI Version
Run the graphical interface:
bash
python gui.py


### Command Line Version
Run the command line version:
bash
python Books.py


## Project Structure

- Books.py - Core scraping functionality
- gui.py - Graphical user interface
- Books_details.csv - Output file for scraped data

## How It Works

1. Enter a book category in the search field
2. Click "Search Books" to start scraping
3. Results will be displayed in the status area
4. Click "Save to CSV" to export the results
5. Find the exported data in Books_details.csv

## Limitations

- Maximum of 10 pages of results per search
- Requires stable internet connection
- May be affected by Goodreads website changes

## Error Handling

- Handles network connectivity issues
- Validates user input
- Graceful error reporting through GUI/console
- Safe browser closure on exit

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT
