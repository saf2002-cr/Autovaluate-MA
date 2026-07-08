<div align="center">

# AutoValuate MA
### AI-Powered Used Car Price Prediction for the Moroccan Market

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4+-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)]()

*An end-to-end Machine Learning pipeline that predicts the market value of second-hand vehicles in Morocco — from raw web-scraped data to an interactive Streamlit application.*

</div>

---

##  Project Overview

**AutoValuate MA** is a complete data science project built to address a real-world problem: **the lack of transparent, data-driven pricing in the Moroccan used car market**.

Starting from raw listings scraped from **moteur.ma**, the project covers the entire ML lifecycle — data collection, cleaning, exploratory analysis, feature engineering, model training, evaluation, and deployment — resulting in a **production-ready web application** that delivers instant vehicle valuations.

> Built as a practical academic project for the *AI Algorithms and Predictions* course — Group 10, SDBDIA2A.

---

##  Features

| Feature | Description |
|---|---|
|  **Price Prediction** | Instant estimated market value for any used car |
|  **Vehicle Form** | Interactive input for brand, year, mileage, fuel, city & transmission |
|  **Analytics Dashboard** | Model performance metrics and dataset visualizations |
|  **Architecture Page** | Full ML pipeline breakdown for technical transparency |
|  **Modern UI** | Dark-themed, responsive Streamlit interface |

---

##  Machine Learning Workflow

The project follows a structured, production-grade ML pipeline:

```
Raw Data (moteur.ma)
        │
        ▼
┌───────────────────┐
│   Data Cleaning   │  Remove nulls, fix parsing errors, IQR outlier filtering
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│       EDA         │  Univariate, bivariate analysis · Distribution plots
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│Feature Engineering│  Usage Intensity ratio · Cardinality reduction · log1p(Price)
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Train/Test Split │  80/20 · random_state=42 · Anti-leakage strategy
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  One-Hot Encoding │  Brand · City · Fuel · Transmission
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Model Training   │  Linear Regression · Random Forest · Gradient Boosting
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Model Evaluation  │  R² · RMSE · MAE · 5-Fold Cross-Validation
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   Model Saving    │  Persisted with Joblib
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│Streamlit Deployment│ Interactive web application
└───────────────────┘
```

### Key Pipeline Decisions

- **Anti-leakage strategy** — Train/Test split performed *before* any imputation or scaling
- **Group-based imputation** — Missing values filled using (Brand, Model) group medians/modes computed on train set only
- **Log transformation** — `log1p(Price)` applied to the target to correct right-skewed distribution
- **Cardinality reduction** — Rare brands and cities (< 1% frequency) grouped into `Autre / Autres`

---

##  Dataset Description

Data was collected via a custom **multi-threaded web scraper** targeting [moteur.ma](https://www.moteur.ma) — Morocco's leading used car marketplace.

| Property | Value |
|---|---|
| **Source** | moteur.ma |
| **Raw listings** | 2 010 |
| **After cleaning** | 1 496 |
| **Features (final)** | 39 |
| **Target variable** | Price (MAD) |
| **Scraping method** | `requests` + `BeautifulSoup4` + `ThreadPoolExecutor` |

### Features Used

| Feature | Type | Description |
|---|---|---|
| `Marque` | Categorical | Car brand (23 after grouping) |
| `Ville` | Categorical | City (top 5 + Autres) |
| `Transmission` | Categorical | Automatique / Manuelle |
| `Carburant` | Categorical | Diesel / Essence / Electrifié |
| `Annee` | Numerical | Year of registration |
| `Kilometrage` | Numerical | Mileage in km |
| `Usage_Intensity` | Engineered | `Km / (2026 − Year + 1)` |

---

## 📈 Model Performance

Three regression models were trained and evaluated using **5-Fold Cross-Validation**:

| Model | CV R² | CV RMSE |
|---|---|---|
| Linear Regression | 0.602 | 0.320 |
| **Random Forest** ✅ | **0.647** | **0.318** |
| Gradient Boosting | 0.598 | 0.322 |

###  Best Model — Random Forest Regressor

Hyperparameter tuning via `RandomizedSearchCV` (20 iterations):

```
n_estimators     = 300
min_samples_split = 5
max_features     = 'sqrt'
max_depth        = None
```

| Metric | Score |
|---|---|
| **R² (test set)** | **0.66** |
| **RMSE** | **59 600 MAD** |
| **MAE** | **41 200 MAD** |

> The model explains **66% of price variance** on unseen data — a strong baseline given the heterogeneity of the Moroccan used car market.

---

## 📁 Project Structure

```
AutoValuate-MA/
│
├── app/                        # Streamlit application
│   ├── app.py                  # Entry point · global CSS · routing
│   ├── views/
│   │   ├── Home.py             # Prediction form & result display
│   │   ├── Dashboard.py        # Analytics & model performance
│   │   └── About.py            # ML pipeline documentation
│   └── utils/
│       ├── prediction.py       # Model inference logic
│       └── charts.py           # Plotly chart generators
│
├── models/                     # Saved model artifacts
│   └── random_forest_model.joblib
│
├── notebooks/                  # Jupyter notebooks
│   └── Group_10_Practical_project_second_hand_car_price.ipynb
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

##  Technologies Used

| Category | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **Web App** | Streamlit |
| **ML / Modeling** | scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly |
| **Web Scraping** | Requests, BeautifulSoup4 |
| **Model Persistence** | Joblib |

---

##  Installation

**1 — Clone the repository**
```bash
git clone https://github.com/your-username/AutoValuate-MA.git
cd AutoValuate-MA
```

**2 — Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3 — Install dependencies**
```bash
pip install -r requirements.txt
```

---

##  Usage

```bash
cd app
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

**How to get a prediction:**
1. Select the vehicle brand, year, fuel type and city
2. Enter the mileage and transmission type
3. Click **Estimate Price** → instant market valuation

---

##  Screenshots

> *Replace the placeholders below with actual screenshots of your app.*

| Home — Prediction Form | Dashboard — Analytics |
|---|---|
| `screenshots/home.png` | `screenshots/dashboard.png` |

| Architecture — Pipeline |
|---|
| `screenshots/about.png` |

---

##  Future Improvements

- [ ] Integrate **XGBoost / LightGBM** for higher accuracy
- [ ] Add a **daily cron-scheduled scraper** to keep the dataset fresh
- [ ] Expand geographic coverage beyond the top 5 Moroccan cities
- [ ] Incorporate **computer vision** to detect vehicle damage from photos
- [ ] Add **confidence intervals** to price predictions
- [ ] Deploy to **Streamlit Cloud** or **Hugging Face Spaces**

---

##  Author

**SAFAA OUSSALEM**
*juin 2026*

Supervised by **Abdellah TAHIRI, Ph.D.**

---

<div align="center">

*If you found this project useful, consider giving it a ⭐ on GitHub!*

</div>
