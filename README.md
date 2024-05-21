# Currency-Exchange-Rates-Scraper
### Currency Exchange Rates Scraper

This repository contains a Python script that scrapes currency exchange rates from [bonbast.com](https://www.bonbast.com) and provides the data in a structured format.

#### How It Works

The script sends a GET request to bonbast.com to retrieve the initial HTML page, extracts a specific parameter from the JavaScript code embedded in the page, and then sends a POST request to the JSON endpoint with the extracted parameter. Finally, it parses the JSON response to extract currency exchange rates.

#### Requirements

- Python 3.x
- requests library
- BeautifulSoup library

#### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/currency-exchange-rates-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd currency-exchange-rates-scraper
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python scrape.py
   ```

5. The script will output the currency exchange rates in a structured format.

#### Note

This script is intended for educational purposes only and should not be used for any commercial or production purposes.

#### Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request if you have any suggestions or improvements.

#### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.