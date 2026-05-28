# AURA India — Group PBL Analytics Dashboard
### MGB QTT 206 · Data Analytics · Dr Anshul Gupta · SP Jain School of Global Management · 2026

> A comprehensive data-driven feasibility study for the **AURA Art Experience Pod** —
> India's first subscription-based art experience pod network.
> Built as the Group PBL submission covering all 9 course sessions.

---

## 🚀 Live App

[aura-art-experience-pod-group-bmsvkz6fujxlefgly8ouws.streamlit.app](https://aura-art-experience-pod-group-bmsvkz6fujxlefgly8ouws.streamlit.app/)

---

## 📊 Dashboard — 13 Tabs Covering All 9 Sessions

| Tab | Session | Analysis Type | Key Algorithms / Content |
|---|---|---|---|
| 🏠 Executive Summary | S1 | Overview | KPI cards, 4-layer pipeline, business problem statement, model comparison |
| 📊 Overview | S1–2 | Descriptive | Demographics, city treemap, art form preferences, word cloud, stress vs interest |
| 🔍 Diagnostic | S2 | Diagnostic | Conversion funnel, cross-tabs, correlation heatmap, WTP by barrier |
| 🌳 Decision Tree | S3 | Predictive | Decision Tree (Gini/Entropy), node map, depth vs accuracy, business rules extraction |
| 🔗 Association Rules | S4 | Predictive | Apriori (Support · Confidence · Lift), scatter, lift chart, bundling strategy |
| 🧩 Clustering | S5 | Predictive | K-Means (silhouette-driven K), PCA scatter, 8-dim radar, persona comparison heatmap |
| 🌿 RFM + Hierarchical | S5–6 | Predictive | RFM segmentation, dendrogram, Ward/complete/average linkage, K-Means vs Hierarchical |
| 📈 Regression | S7 | Predictive | RF + Gradient Boosting + Linear Regression, 5-fold CV R², residuals, live WTP predictor |
| 📉 Time Series + ARIMA | S7 | Predictive | Decomposition, moving average, MLR forecast, ARIMA(p,d,q), stationarity check |
| 💬 Text Mining + Ethics | S8–9 | Predictive + Prescriptive | Sentiment analysis, word frequency, topic detection, AI ethics (Fairness/Transparency/Privacy), ESG scorecard |
| 🤖 Classification Models | S3 | Predictive | RF + XGBoost + LR, 5-fold CV box plots, ROC curves (one-vs-rest), confusion matrix with business cost |
| 🚀 Predict New | Prescriptive | Prescriptive | Upload CSV → interest label + confidence + WTP + persona + recommended action |
| 💡 Prescriptive Strategy | S9 | Prescriptive | A/B pod pricing simulator, geographic city heatmap, 3-phase launch sequence, channel budget mix |

---

## 🔑 Key Enhancements vs Individual Submission

### 1. K-Means — Silhouette-Driven K (Bug Fixed)
```python
# BEFORE — hardcoded override, defeats the algorithm:
best_k = max(4, min(best_k, 6))

# AFTER — purely data-driven:
best_k = K_range[int(np.argmax(silhouettes))]
```

### 2. 5-Fold Cross-Validation on All Models
```python
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
# Mean ± Std shown as box plot in dashboard
```

### 3. ROC Curves — Multi-Class One-vs-Rest
- Random Forest, XGBoost, Logistic Regression plotted side by side
- Per-class AUC: Not Interested / Maybe / Interested

### 4. Decision Tree — Fully Implemented (Session 3)
- Interactive depth/criterion/min-samples controls
- Colour-coded text tree (like Python's `export_text`)
- Plotly node map visualisation
- Depth vs accuracy overfitting chart
- 5 plain-English business decision rules

### 5. RFM Analysis + Hierarchical Clustering (Sessions 5–6)
- RFM scores built from survey features (Recency · Frequency · Monetary)
- Segment profiles: Champions → Loyal → Potential → At Risk → Lost
- Full dendrogram with Ward/complete/average/single linkage
- Direct K-Means vs Hierarchical silhouette comparison

### 6. Time Series + ARIMA (Session 7)
- Trend decomposition: original → moving average → seasonality → residual
- Multilinear regression forecast with train/test split + 12-month projection
- ARIMA(p,d,q) with interactive parameter sliders
- Stationarity check via rolling mean/std
- Festival peak annotations (Diwali, Valentine's, New Year)

### 7. Text Mining + AI Ethics (Sessions 8–9)
- Rule-based NLP sentiment analysis on AURA customer reviews
- Word frequency chart, topic identification (5 themes)
- Sentiment score vs rating scatter
- 5 AI ethics principles applied to AURA models (Fairness, Transparency, Privacy, Accountability, Sustainability)
- ESG scorecard: current vs target scores

---

## 📁 File Structure

```
app.py                   # Main entry — 13 tabs, all sessions
aura_theme.py            # Brand system: colours, CSS, UI helpers
aura_data.py             # Data loading, feature engineering, model training
tab_summary.py           # Executive Summary — KPIs, pipeline, business context
tab_overview.py          # S1-2 Descriptive — demographics, word cloud, treemap
tab_diagnostic.py        # S2 Diagnostic — funnel, correlation heatmap
tab_decision_tree.py     # S3 Decision Tree — interactive tree, business rules
tab_arm.py               # S4 Association Rules — Apriori, lift analysis
tab_clustering.py        # S5 K-Means — radar charts, silhouette, personas
tab_hierarchical.py      # S5-6 RFM + Hierarchical — dendrogram, comparison
tab_regression.py        # S7 Regression — CV, residuals, live WTP predictor
tab_timeseries.py        # S7 Time Series — ARIMA, decomposition, forecast
tab_text_ethics.py       # S8-9 Text Mining + AI Ethics + ESG
tab_classification.py    # S3 Classification — RF + XGB + LR, ROC, CV
tab_predict.py           # Prescriptive — upload CSV, score new customers
tab_prescriptive.py      # S9 Strategy — A/B simulator, geo heatmap, launch plan
requirements.txt         # Python dependencies
runtime.txt              # Python 3.12 runtime
.python-version          # Python 3.12 pin
aura_survey1_n2000.csv   # Main survey dataset (2,000 rows)
aura_survey2_n1314.csv   # Deep profile dataset (1,314 rows)
aura_arm_transactions.csv # ARM binary basket matrix
aura_combined_wide.csv   # Merged wide dataset
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/Vaish020/Aura-art-experience-pod-group.git
cd Aura-art-experience-pod-group
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 Dependencies

```
streamlit>=1.35.0
pandas>=2.2.2
numpy>=1.26.4
plotly>=5.22.0
scikit-learn>=1.5.0
xgboost>=2.0.3
mlxtend>=0.23.1
imbalanced-learn>=0.12.3
scipy>=1.13.0
```

---

## 🎨 AURA Brand Palette

| Colour | Hex | Use |
|---|---|---|
| Gold | `#e8c547` | Primary accent, KPIs, headers |
| Teal | `#5ec4a1` | Positive signals, clusters, success |
| Orange | `#e07c3a` | Warnings, secondary accent |
| Rose | `#e06b8b` | Negative signals, alerts |
| Indigo | `#7b8cde` | ROC curves, correlation, tree nodes |
| Dark BG | `#0e0c0a` | Background |

---

## 📐 Assessment Alignment

| ULO | Description | Tabs |
|---|---|---|
| A | Understand fundamentals of data analytics | Executive Summary, Overview, Diagnostic |
| B | Design and execute comprehensive analytics report | All tabs — full 4-layer pipeline |
| C | Apply tools and techniques to solve business problems | Classification, Clustering, Regression, ARM |
| D | Formulate strategic inferences through MBA, Decision Trees, Clustering | Decision Tree, RFM + Hierarchical, Association Rules, Text Mining |
| E | Apply forecasting concepts and techniques innovatively | Time Series + ARIMA, Regression, Prescriptive Strategy |

---

*AURA India · Group PBL · MGB QTT 206 · SP Jain School of Global Management · 2026*
