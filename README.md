# global-energy-emissions-analysis
> Analyzing 23 years of energy data across 15 major countries to understand what drives greenhouse gas emissions — and whether the world is transitioning to clean energy fast enough.

##  Project Overview

Every country in the world consumes energy. But **how** that energy is generated determines how much the planet warms.

This project digs into real-world energy data from **2000 to 2023** across 15 major economies to answer four core questions:

- Which countries are driving global energy demand growth?
- Does higher energy demand always lead to higher emissions?
- Are countries actually getting cleaner over time?
- What factors predict greenhouse gas emissions most accurately?

## Key Findings

| # | Finding |
|---|---------|
| 1 | **China's electricity demand grew ~7x** from 2000 to 2023 — no other country comes close |
| 2 | **USA reduced emissions** despite flat energy demand — proof that energy transition works |
| 3 | **Brazil and France** have high energy use but near-zero emissions — clean energy mix is the answer |
| 4 | **Most of the world is still 80%+ fossil fuel dependent** despite 25 years of climate policy |
| 5 | **Fossil fuel consumption** is the single strongest predictor of emissions — not energy volume alone |



##  Project Structure

```
global-energy-emissions-analysis/
│
├── energy_project.ipynb       # Full analysis notebook (EDA + ML)
├── app.py                     # Interactive Streamlit dashboard
├── clean_energy_data.csv      # Cleaned dataset (15 countries, 2000–2023)
├── requirements.txt           # Required Python libraries
└── README.md                  # You are here
```

---

## Notebook Walkthrough

The notebook is divided into two major sections:

### Part 1 — Data Cleaning
| Step | What it does |
|------|-------------|
| Step 1 | Load raw dataset (23,377 rows, 130 columns) |
| Step 2 | Select 18 relevant columns, remove regions, filter from year 2000 |
| Step 3 | Check data quality and missing values per country |
| Step 4 | Select 15 geographically and economically diverse countries |
| Step 5 | Fill missing values using forward fill within each country group |

### Part 2 — Exploratory Data Analysis (EDA)
| Chart | Question answered |
|-------|------------------|
| Chart 1 | Who consumes the most electricity over time? |
| Chart 2 | Does higher demand always mean higher emissions? |
| Chart 3 | Does higher renewable share mean lower emissions? |
| Chart 4 | Which countries are getting cleaner? (Heatmap) |
| Chart 5 | How have emissions changed: 2000 vs 2023? |

### Part 3 — Machine Learning
| Step | What it does |
|------|-------------|
| Step 6 | Prepare features and target, split into train/test (80/20) |
| Step 7 | Train and evaluate Linear Regression, Random Forest, XGBoost |
| Step 8 | Extract feature importance to identify emission drivers |

---

## 🤖 Model Performance

| Model | MAE | RMSE | R² |
|-------|-----|------|----|
| Linear Regression | 41.58 | 68.51 | 0.9973 |
| Random Forest | 35.74 | 77.89 | 0.9965 |
| XGBoost | 49.63 | 121.82 | 0.9913 |

✅ All three models explain **99%+ of variation** in greenhouse gas emissions.  
🏆 **Best model: Linear Regression** (lowest RMSE, highest R²)

---

## 🌱 Top Emission Drivers (Feature Importance)

Based on Random Forest feature importance:

1. 🥇 **Fossil fuel consumption** — by far the strongest driver
2. 🥈 **Oil consumption** — second strongest
3. 🥉 **Electricity demand** — third strongest
4. Coal consumption, GDP, Population — moderate contributors
5. Renewable share — surprisingly weak predictor on its own

> **Insight:** Reducing total fossil fuel consumption matters more than simply increasing renewable share.

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3 |
| Data manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Dashboard | Streamlit |

---

## 🚀 How to Run This Project

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/global-energy-emissions-analysis.git
cd global-energy-emissions-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Jupyter notebook**
```bash
jupyter notebook energy_project.ipynb
```

**4. Launch the interactive dashboard**
```bash
streamlit run app.py
```

---

## 📦 Dataset

- **Source:** [Our World in Data — Energy Dataset](https://github.com/owid/energy-data)
- **Coverage:** All countries, 1900–2023
- **Key variables:** Energy consumption by source, renewable share, CO₂ emissions, GDP, population

---

## 💼 Business Applications

This analysis is directly useful for:

- **Energy policy teams** — identify which countries need the most urgent emission reduction intervention
- **Climate consultancies** — estimate emission impact of switching from fossil fuels to renewables
- **ESG investment firms** — assess climate risk in country-level portfolios
- **NGOs and researchers** — communicate the pace (and slowness) of the global energy transition

---



## 📄 License

This project is open source and available under the [MIT License](LICENSE).
