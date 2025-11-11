# Solar Data Discovery Challenge: West Africa

This project is a comprehensive analysis of solar farm data from three West African countries: **Benin, Sierra Leone, and Togo**. The goal is to identify high-potential regions for solar installation to guide the investment strategy of **MoonLight Energy Solutions**, a company focused on enhancing its operational efficiency and sustainability through targeted solar investments.

This repository contains the code for data cleaning, exploratory data analysis (EDA), cross-country comparison, and a Streamlit-based interactive dashboard to visualize the findings.

## Features

*   **Data Cleaning & Preparation:** Scripts to process and clean raw solar data.
*   **Exploratory Data Analysis (EDA):** Jupyter notebooks for in-depth analysis of solar irradiance, temperature, and other meteorological data.
*   **Cross-Country Comparison:** Analysis to rank the countries by their solar potential.
*   **Interactive Dashboard:** A Streamlit application to visualize and interact with the data.

## Getting Started

### Prerequisites

*   Python 3.9 or later
*   A virtual environment manager (`venv` or `conda`)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kidus-Yoseph1/solar-challenge-week0.git
    cd solar-challenge-week0
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

The project includes an interactive dashboard built with Streamlit that allows you to visualize the solar data. To run the dashboard, use the following command:

```bash
streamlit run src/app/main.py
```

This will open a new tab in your browser with the interactive dashboard.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          
├── data/
│   ├── cleaned/            
│   └── raw/                
├── notebooks/              
├── src/
│   └── app/
│       ├── main.py         
│       └── utils.py        
├── tests/
│   └── test_utils.py       
├── .gitignore
├── README.md               
└── requirements.txt       
```

## Continuous Integration

This project uses GitHub Actions for Continuous Integration. The workflow, defined in `.github/workflows/ci.yml`, automatically runs on every push or pull request to the `main` branch. It performs the following steps:

1.  Sets up a Python 3.9 environment.
2.  Installs all the required dependencies.
3.  Runs the test suite using `pytest`.

This ensures that the codebase remains healthy and that all tests pass before any new code is merged.


