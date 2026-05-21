# AURA India — Group Analytics Dashboard (Enhanced)

> A comprehensive data-driven feasibility study for the **AURA Art Experience Pod** business concept.
> Built for the Group PBL submission · SP Jain School of Global Management · 2026

## 🚀 Live Deployment

Deploy on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo → set `app.py` as main file → Deploy

---

## 📊 Dashboard Tabs (9 Tabs)

| Tab | Type | What's New vs Individual |
|---|---|---|
| 🏠 Executive Summary | Overview | NEW — KPI cards, pipeline overview, business context |
| 📊 Overview | Descriptive | + Word cloud, treemap, stress vs interest, download |
| 🔍 Diagnostic | Diagnostic | + Funnel, correlation heatmap, WTP by barrier |
| 🧩 Clustering | Predictive | + **Pure silhouette K** (no hardcode), radar overlay, per-cluster silhouette |
| 🤖 Classification | Predictive | + **5-fold CV**, ROC curves (all 3 models), confusion matrix with business cost |
| 🔗 Association Rules | Predictive | + Lift chart, scatter, business interpretation cards |
| 📈 Regression | Predictive | + CV R², residuals, **live WTP predictor widget** |
| 🚀 Predict New | Prescriptive | + Template download, priority action list, WTP histogram |
| 💡 Prescriptive | Prescriptive | NEW — **A/B pricing simulator**, geographic heatmap, launch sequence, channel mix |

---

## 🔑 Key Algorithm Enhancements

### K-Means Clustering — Fixed
```python
# BEFORE (hardcoded override — defeats the algorithm):
best_k = max(4, min(best_k, 6))

# AFTER (pure silhouette-driven):
best_k = K_range[int(np.argmax(silhouettes))]
# No override. Data decides.
```

### 5-Fold Cross-Validation — Added to All Models
```python
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
# Mean ± Std shown in dashboard
```

### ROC Curves — Multi-class (One-vs-Rest)
- Random Forest, XGBoost, Logistic Regression side by side
- Per-class AUC for Not Interested / Maybe / Interested

### ARM — Proper Display
- Support · Confidence · Lift table
- Scatter: Support vs Confidence coloured by Lift
- Business interpretation per rule category

---

## 📁 File Structure

```
app.py                  # Main entry point (9 tabs)
aura_theme.py           # Brand colours, CSS, UI helpers
aura_data.py            # Data loading, encoding, model training (enhanced)
tab_summary.py          # NEW — Executive summary landing
tab_overview.py         # Descriptive + word cloud + treemap
tab_diagnostic.py       # Diagnostic + funnel + correlation heatmap
tab_clustering.py       # K-Means + radar charts + silhouette per cluster
tab_classification.py   # RF + XGB + LR + ROC + CV + confusion matrix
tab_arm.py              # Apriori + rules table + lift chart
tab_regression.py       # Regression + residuals + LIVE WTP predictor
tab_predict.py          # Upload CSV → score new customers
tab_prescriptive.py     # NEW — A/B simulator + geo heatmap + launch strategy
requirements.txt        # Dependencies
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/aura-group-dashboard.git
cd aura-group-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 Dependencies

```
streamlit==1.35.0
scikit-learn==1.5.0
xgboost==2.0.3
plotly==5.22.0
mlxtend==0.23.1
imbalanced-learn==0.12.3
pandas==2.2.2
numpy==1.26.4
scipy==1.13.0
```

---

## 🎨 AURA Brand Palette

| Colour | Hex | Use |
|---|---|---|
| Gold | `#e8c547` | Primary accent, KPIs |
| Teal | `#5ec4a1` | Positive signals, clusters |
| Orange | `#e07c3a` | Warnings, secondary |
| Rose | `#e06b8b` | Negative, alerts |
| Indigo | `#7b8cde` | ROC curves, correlation |
| Dark BG | `#0e0c0a` | Background |

---

*AURA India · Group PBL · SP Jain School of Global Management · 2026*
