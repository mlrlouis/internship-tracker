# Internship Application Tracker

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

## About The Project

Searching for an internship involves managing dozens of applications, portals, and deadlines. This **Internship Application Tracker** replaces chaotic Excel sheets with a streamlined, automated dashboard.

It helps you organize the entire application lifecycle—from "Saved" to "Offer"—and uses the **Yahoo Finance API** to automatically fetch and display company data (Industry, Employee Count, Description) simply by entering a stock ticker.

## Key Features

* **Live Dashboard:** Real-time statistics showing your progress (Total Applications, Interviews, Rejections, etc.).
* **Auto-Enrichment:** Enter a ticker (e.g., `AAPL` or `BMW.DE`), and the app automatically pulls the company's description, industry, and size via `yfinance`.
* **Location Tracking:** Track the country/location for every position.
* **Smart Notes:** Rich text notes to keep track of interview details or specific application requirements.
* **Full Control:** Edit statuses (e.g., move from "Applied" to "Interview") or delete old entries easily.
* **Clean UI:** Built with **PicoCSS** for a minimalist, dark-mode-friendly look that focuses on the data.

## Screenshots

<img width="588" height="870" alt="grafik" src="https://github.com/user-attachments/assets/f0647b35-f542-4c75-9174-d1ddbc6d4d8a" />

## Tech Stack

* **Backend:** [Django](https://www.djangoproject.com/) (Python)
* **Frontend:** HTML5, CSS3 ([PicoCSS](https://picocss.com/))
* **API:** [yfinance](https://pypi.org/project/yfinance/)
* **Database:** SQLite (Standard)

## Getting Started

If you want to run this project locally on your machine:

### 1. Clone the repository
```bash
git clone [https://github.com/mlrlouis/internship-tracker.git](https://github.com/mlrlouis/internship-tracker.git)
cd internship-tracker
```

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the Server
```bash
python manage.py runserver
```
Open your browser and visit http://127.0.0.1:8000/.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for new features (e.g., email reminders, file uploads)

<p align="right">(<a href="#top">back to top</a>)</p>
