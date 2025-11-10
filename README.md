# Solar Data Discovery

This project analyzes solar farm data from Benin, Sierra Leone, and Togo. It provides insights into solar irradiance, temperature, and other environmental factors.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kidus-Yoseph1/solar-challenge-week0.git
    cd solar-challenge-week0
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the Streamlit dashboard, use the following command:

```bash
streamlit run src/app/main.py
```

## Folder Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── data/
│   ├── cleaned/
│   └── raw/
├── notebooks/
├── README.md
├── requirements.txt
└── src/
    └── app/
        ├── main.py
        └── utils.py
```
