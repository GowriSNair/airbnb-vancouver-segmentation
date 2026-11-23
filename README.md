# 🏠 Airbnb Vancouver — Market Segmentation & BI Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-K--Means%20%7C%20PCA-F7931E?style=flat-square&logo=scikit-learn)
![NLTK](https://img.shields.io/badge/NLTK-Sentiment%20Analysis-3776AB?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 🎯 Project Overview

This project examines **6,131 Vancouver Airbnb listings** and **346,589 guest reviews** (Inside Airbnb snapshot of 17 September 2026) to uncover pricing patterns, market segments, and customer sentiment. Using K-Means clustering, PCA, and VADER sentiment analysis, it segments the market into four distinct listing types and identifies what separates positive reviews from complaints. Results are explored in an interactive Streamlit dashboard.

**Key Highlights:**

- **Dataset:** 6,131 listings × 90 features + 346,589 guest reviews
- **Segments identified:** Short-Stay Homes, Monthly Rentals, Private Rooms, Multi-Listing Operators
- **Long-stay shift:** 30% of listings now require a stay of 30 nights or more
- **Sentiment:** 91% of reviews positive, 6% neutral, 3% negative — but the positive share has slipped from 96% (2021) to 88% (2026)
- **Complaint signals:** dirtiness, smell and noise are mentioned far more often in negative reviews

---

## 🔍 Business Problem

Vancouver's short-term rental market is highly competitive and tightly regulated. Hosts and property managers lack visibility into:
- Which listing types command premium pricing
- What guest experience factors drive positive versus negative reviews
- How room type, minimum stay and host scale separate the market into segments

**This project answers all three.**

---

## 🧠 Methodology

### 1. Exploratory Data Analysis
- Analysed price distributions, room types, neighbourhood concentrations, review frequency and correlations
- Converted price from text, capped prices at the 99th percentile ($1,539) and minimum stay at 30 nights
- Found price only weakly related to most numeric features; its strongest link is with minimum stay (r = −0.37)

### 2. Market Segmentation (K-Means Clustering)
- Clustered on price, minimum nights, review volume and rate, availability, host listing count, room type and neighbourhood (standardised)
- Elbow method → **K = 4**; clusters are named automatically from their profiles

### 3. Dimensionality Reduction (PCA)
- Projected the clustering features to 2 components (41% of variance) to visualise segment separation

### 4. Sentiment Analysis (VADER)
- Cleaned and scored **346,553 reviews** with comment text using VADER (NLTK)
- Mapped sentiment to each segment and over time; compared theme mentions in positive vs negative reviews; built word clouds

---

## 💡 Key Findings

### Market Segments

| Segment | Listings | Median price | Profile | Positive reviews |
|---|---|---|---|---|
| 🔵 Short-Stay Homes | 3,595 | $353 | Entire homes, ~2-night minimum, most reviews | 91.1% |
| 🟡 Monthly Rentals | 1,300 | $151 | Entire homes, 30-night minimum, fewer reviews | 92.6% |
| 🟢 Private Rooms | 1,013 | $150 | Rooms in shared homes, ~12-night average minimum | 86.0% |
| 🟣 Multi-Listing Operators | 223 | $87 | Hosts with ~125 listings each, near-monthly minimums, high availability | 90.0% |

### What Guests Talk About

| Theme | % of positive reviews | % of negative reviews |
|---|---|---|
| Location | 49.9% | 12.2% |
| Cleanliness | 32.5% | 8.5% |
| Host communication | 25.3% | 7.5% |
| Comfort / bed | 22.0% | 6.8% |
| Noise | 3.2% | 6.3% |
| Dirty | 0.5% | 4.6% |
| Smell | 0.5% | 2.5% |

### Market & Neighbourhood Insights
- **Entire homes** make up 82% of listings; median nightly price is **$273**
- **Downtown** has the most listings (1,434) and the highest median price ($345), followed by Downtown Eastside ($331)
- Listings with 30-night minimums charge less per night and collect fewer reviews

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python |
| Data Manipulation | Pandas, NumPy |
| Machine Learning | Scikit-learn (K-Means, PCA) |
| NLP / Sentiment | VADER (NLTK), WordCloud |
| Visualisation | Matplotlib, Seaborn, Plotly, Streamlit |
| Dataset | [Inside Airbnb](https://insideairbnb.com/get-the-data/) — Vancouver, 17 Sep 2026 (CC BY 4.0) |

---

## 📁 Project Structure

```
airbnb-vancouver-segmentation/
├── EDA_Airbnb_Vancouver.ipynb   # Full analysis: EDA, PCA, K-Means, VADER sentiment; exports dashboard data
├── app.py                       # Streamlit dashboard
├── listings_processed.csv       # Dashboard input: listings with segment labels
├── reviews_processed.csv        # Dashboard input: review dates, sentiment and segment
├── .streamlit/config.toml       # Dark theme for the dashboard
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run

```bash
git clone https://github.com/GowriSNair/airbnb-vancouver-segmentation.git
cd airbnb-vancouver-segmentation
pip install -r requirements.txt
```

**Dashboard:** `streamlit run app.py` (uses the processed CSVs already in the repo)

**Notebook:** from [Inside Airbnb](https://insideairbnb.com/get-the-data/), download the Vancouver **detailed** `listings.csv.gz` and `reviews.csv.gz`, place them in the project folder, and run `EDA_Airbnb_Vancouver.ipynb`. The last cell regenerates the dashboard CSVs. Newer snapshots will give slightly different numbers.

---

## 📈 Key Recommendations

- **Short-stay hosts** compete hardest on reviews: location, cleanliness and communication dominate positive feedback
- **Private-room hosts** have the weakest sentiment (86% positive) and should prioritise cleanliness and noise control
- **Monthly rentals** keep guests happiest (92.6% positive) at a lower nightly price — a viable alternative to short stays
- **Falling positive share since 2021** is worth monitoring: complaints about dirtiness, smell and noise are the clearest signals to act on

---

## ✅ Skills Demonstrated

- ✅ Unsupervised machine learning (K-Means clustering, PCA)
- ✅ Natural language processing (VADER sentiment analysis, theme analysis, word clouds)
- ✅ Large-scale data processing (346K+ records)
- ✅ Exploratory data analysis & data cleaning
- ✅ Interactive BI dashboard (Streamlit, Plotly)
- ✅ Translating analytical findings into business recommendations

---

## 👩‍💻 Author

**Gowri S Nair** — Data Analyst · [LinkedIn](https://www.linkedin.com/in/gowri-s-nair-9ba795354) · [GitHub](https://github.com/GowriSNair)
