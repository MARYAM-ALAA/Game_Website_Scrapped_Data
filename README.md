# 🎮 GamesSpider

GamesSpider is a Scrapy-powered web crawler that collects game data from the Oxylabs sandbox website. It scrapes important details such as the game's name, category, price, link, and description — making it a great small project for practicing web scraping and data extraction techniques.

## 🚀 Features
- Extracts game details: name, category, price, link, and description.
- Supports pagination: continues to scrape across multiple pages.
- Built using Scrapy framework (Python).

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
   
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
  pip install scrapy
  

## 📋 Usage

  Run the spider with:
   ```bash
  scrapy runspider games.py -o games_data.json
  ```
- The data will be saved to games_data.json.

- You can also export to CSV or XML by changing the file extension (games_data.csv, games_data.xml, etc.).
   
## 📦 Scraped Fields
- name

- category

- price

- link

- description

## 📌 Notes
The project scrapes from a  **sandbox environment**   , which is safe for learning and testing.

Some fields like **rating** and **stock status** were not scraped due to complexity or missing data. They can be added in future improvements.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.











