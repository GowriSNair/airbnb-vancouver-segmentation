# 🏠 Airbnb Vancouver — Market Segmentation & BI Dashboard

![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-K--Means%20%7C%20PCA-F7931E?style=flat-square&logo=scikit-learn)
![NLTK](https://img.shields.io/badge/NLTK-Sentiment%20Analysis-3776AB?style=flat-square&logo=python)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?style=flat-square&logo=tableau)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 🎯 Project Overview

This project examines **4,705 Vancouver Airbnb listings** and **277,819 guest reviews** to uncover pricing patterns, market segments, and customer sentiment. Using K-Means clustering, PCA, and VADER sentiment analysis, the project segments the market into four distinct listing types and identifies the key drivers of guest satisfaction.

**Key Highlights:**

- **Dataset:** 4,705 listings × 49 features + 277,819 guest reviews × 6 columns
- **Clusters Identified:** 4 distinct market segments (budget, mid-range, premium, long-term)
- **Sentiment:** ~80–90% positive reviews across all listings
- **Top Satisfaction Drivers:** Cleanliness, comfort, location, and host communication
- **Top Complaint Areas:** Noise, cleanliness issues, inaccurate listing photos
---

## 🔍 Business Problem

Vancouver's short-term rental market is highly competitive. Hosts and property managers lack visibility into:
- Which listing types command premium pricing
- What guest experience factors drive 5-star reviews
- How neighbourhood, room type, and pricing strategy affect performance across segments

**This project answers all three.**

---

## 🧠 Methodology

### 1. Exploratory Data Analysis
- Analysed price distributions, room types, neighbourhood concentrations, and review score patterns
- Removed extreme price outliers above $1,000/night for cleaner analysis
- Found price has **weak correlation** with all numeric features — pricing is driven by qualitative factors

### 2. Dimensionality Reduction (PCA)
- Reduced 49 features to 2 principal components for visualisation
- Confirmed clear cluster separation in the PCA plot — K-Means captured natural listing groupings

### 3. Market Segmentation (K-Means Clustering)
- Applied elbow method to determine optimal K = **4 clusters**
- Merged clustering results with listing features to profile each segment

### 4. Sentiment Analysis (VADER)
- Processed **277,819 guest reviews** using VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Mapped compound sentiment scores back to each cluster to surface experience patterns
- Built word clouds for positive and negative feedback themes

---

## 💡 Key Findings

### Market Segments

| Cluster | Segment Name | Description | Sentiment |
|---|---|---|---|
| 0 | Budget Small Listings | Cheap, small, long minimum stay, lower ratings | Slightly more neutral/negative |
| 1 | High-Performing Mid-Range | Flexible, affordable, many reviews, high occupancy | Strongest positive sentiment |
| 2 | Premium Large Family Homes | Expensive, large homes, group stays, niche market | Strong positive, fewer reviews |
| 3 | Long-Term Professional Host Units | 1-month minimum stay, run by multi-listing hosts | More neutral (fewer daily interactions) |

### Sentiment Breakdown

| Sentiment | Share |
|---|---|
| ✅ Positive | ~80–90% |
| 😐 Neutral | ~5–8% |
| ❌ Negative | <5% |

### Neighbourhood Insights
- **Downtown** has the highest listing concentration
- **Kitsilano & Mount Pleasant** show strong mid-range Airbnb activity
- Some residential areas have low supply — indicating limited competition opportunity

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python 3.9 |
| Data Manipulation | Pandas, NumPy |
| Machine Learning | Scikit-learn (K-Means, PCA) |
| NLP / Sentiment | VADER (NLTK) |
| Visualisation | Matplotlib, Seaborn, Power BI, Tableau |
| Dataset | Inside Airbnb — Vancouver (public dataset) |

---

## 📁 Project Structure

```
airbnb-vancouver-segmentation/
│
├── data/
│   ├── listings.csv                  # 4,705 listings × 49 features
│   └── reviews.csv                   # 277,819 guest reviews
│
├── EDA_Airbnb_Vancouver.ipynb   # Full analysis: EDA, clustering & sentiment
│
│
└── README.md
```

---

## ⚙️ How to Run

```bash
# Clone the repo
git clone https://github.com/GowriSNair/airbnb-vancouver-segmentation.git

# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
jupyter notebook
```

**Requirements:**
```
pandas
numpy
scikit-learn
nltk
matplotlib
seaborn
wordcloud
jupyter
```

---

## 📈 Key Recommendations

- **Hosts** should prioritise cleanliness, communication, and accurate listing photos — these are the top drivers of positive sentiment
- **Mid-range and premium segments** show the highest satisfaction — ideal candidates for aggressive marketing
- **Budget and long-term clusters** should optimise pricing and improve service quality to reduce neutral/negative feedback
- **Low-supply neighbourhoods** represent opportunity for new hosts with limited competition

---

## ✅ Skills Demonstrated

- ✅ Unsupervised machine learning (K-Means clustering, PCA)
- ✅ Natural language processing (VADER sentiment analysis, word clouds)
- ✅ Large-scale data processing (277K+ records)
- ✅ Exploratory data analysis & feature engineering
- ✅ Business intelligence dashboard design (Power BI & Tableau)
- ✅ Translating analytical findings into business recommendations

---

## 👩‍💻 About Me

**Gowri Sukumaran** — Aspiring Data Analyst with hands-on experience in Python, machine learning, NLP, and BI tools.


