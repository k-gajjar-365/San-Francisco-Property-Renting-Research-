# Zillow Data Automation with Selenium and BeautifulSoup🔎

# Overview
This Python script automates the process of scraping property listings from a [Zillow](https://www.zillow.com/) website and submits the extracted data into a Google Form. It utilizes [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for web scraping, [Selenium](https://pypi.org/project/selenium/) for form automation, and includes optimizations like explicit waits to ensure a smooth workflow.

# Features
- Web Scraping with BeautifulSoup: Extracts property addresses, prices, and listing links.

- Data Submission with Selenium: Automates input into a Google Form.

- Efficient Processing: Implements delays to ensure elements load correctly before interaction.

# Dependencies
Ensure you have the following installed before running the script:

- Python 3

- selenium

- beautifulsoup4

- requests

- Google Chrome and ChromeDriver

Install dependencies using:

-> pip install selenium beautifulsoup4 requests
# Usage
- Update URLs: Modify form_url to your Google Form link and zillow_clone to your target website.

- Run the script: Execute the script in a terminal or IDE.

- Automated Submission: The bot extracts Zillow-style data and submits it sequentially to the form.

# How It Works
- Sends a request to the Zillow clone site and parses the HTML using BeautifulSoup.

- Extracts property details including addresses, prices, and listing links.

- Launches Chrome using Selenium and navigates to the Google Form.

- Automatically enters the scraped data into the form fields using XPath selectors and submits responses.

- Iterates through all listings, ensuring smooth automation.

# Future Implementation
To enhance functionality and scalability, the following improvements can be considered:

- Database Integration: Storing extracted data in a database before submission for better tracking.

- Multi-threading Support: Speeding up scraping and form submission by processing multiple entries in parallel.

- Dynamic Form Handling: Making form field selection adaptable to changes in Google Form structure.

- Logging Mechanism: Adding detailed logs to track script execution and troubleshoot errors.

- GUI Interface: Creating a simple UI for users to input parameters instead of modifying the script directly.