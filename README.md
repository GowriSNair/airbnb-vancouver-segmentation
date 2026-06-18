# 🏠 Airbnb Vancouver — Market Segmentation & BI Dashboard

![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Models-F7931E?style=flat-square&logo=scikit-learn)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?style=flat-square&logo=tableau)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat-square&logo=powerbi)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 🎯 Project Overview

This project uncovers hidden market segments within Vancouver's Airbnb listings using **unsupervised machine learning and NLP sentiment analysis**. By applying K-Means clustering and PCA on listing features, and VADER sentiment on guest reviews, this analysis identifies which segments drive satisfaction — and why.

**Key Highlights:**

- **Market Segments:** X distinct listing clusters identified across Vancouver neighbourhoods *(replace X)*
- **Top Sentiment Drivers:** Cleanliness and host communication drove the most positive reviews
- **Churn Signal:** Listings rated low on value-for-money showed the highest negative sentiment concentration
- **Dashboard:** Interactive Power BI & Tableau dashboard for business decision-makers

---

## 📊 Dashboard Preview

> 🔗 [View Live Tableau Dashboard](#) *(paste your Tableau Public link here)*

![Dashboard Preview](dashboard/preview.png) *(replace with a screenshot of your dashboard)*

---

## 🔍 Business Problem

Vancouver's short-term rental market is highly competitive. Hosts and property managers lack visibility into:
- Which listing types command premium pricing
- What guest experience factors drive 5-star reviews
- How neighbourhood and room type affect sentiment and occupancy

**This project answers all three.**

---

## 🧠 Methodology

### 1. Exploratory Data Analysis
- Cleaned and processed X,XXX listings with XX features
- Analysed price distributions, availability patterns, and review scores by neighbourhood

### 2. Dimensionality Reduction (PCA)
- Reduced feature space from XX dimensions to 2 principal components
- Retained ~80% of variance for interpretable clustering

### 3. Market Segmentation (K-Means Clustering)
- Applied elbow method and silhouette scores to determine optimal K
- Identified X clusters ranging from budget private rooms to premium entire-unit listings

### 4. Sentiment Analysis (VADER)
- Processed X,XXX guest reviews using VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Mapped sentiment scores back to each cluster to surface experience patterns

---

## 💡 Key Findings

| Cluster | Segment Type | Avg Price | Avg Sentiment | Key Insight |
|---|---|---|---|---|
| 0 | Budget Private Room | $XX/night | 0.XX | Price-sensitive guests, value focus |
| 1 | Mid-range Entire Unit | $XX/night | 0.XX | Highest volume segment |
| 2 | Premium Entire Unit | $XX/night | 0.XX | Best sentiment scores |
| 3 | Luxury/Unique Stay | $XX/night | 0.XX | Niche but high-loyalty guests |

*(Fill in with your actual cluster results)*

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| Language | Python 3.9 |
| Data Manipulation | Pandas, NumPy |
| Machine Learning | Scikit-learn (K-Means, PCA) |
| NLP | VADER Sentiment Analysis (NLTK) |
| Visualisation | Matplotlib, Seaborn, Power BI, Tableau |
| Dataset | Inside Airbnb — Vancouver |

---

## 📁 Project Structure

```
airbnb-vancouver-segmentation/
│
├── data/
│   └── listings.csv                  # Source dataset
│
├── notebooks/
│   ├── 01_eda.ipynb                  # Exploratory data analysis
│   ├── 02_clustering.ipynb           # K-Means & PCA
│   └── 03_sentiment_analysis.ipynb   # VADER sentiment
│
├── dashboard/
│   ├── airbnb_vancouver.pbix         # Power BI file
│   └── preview.png                   # Dashboard screenshot
│
└── README.md
```

---

## ⚙️ How to Run

```bash
# Clone the repo
git clone https://github.com/GowriSNair/airbnb-vancouver-segmentation.git
cd airbnb-vancouver-segmentation

# Install dependencies
pip install -r requirements.txt

# Launch notebooks in order
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
jupyter
```

---

## 📈 Skills Demonstrated

- ✅ Unsupervised machine learning (K-Means, PCA)
- ✅ Natural language processing (VADER sentiment analysis)
- ✅ Exploratory data analysis & feature engineering
- ✅ Business intelligence dashboard design (Power BI & Tableau)
- ✅ Translating analytical findings into business recommendations

---

## 👩‍💻 About Me

**Gowri S Nair** — Aspiring Data Analyst with hands-on experience in Python, machine learning, and BI tools.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](#)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-brightgreen?style=flat-square)](#)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](#)
