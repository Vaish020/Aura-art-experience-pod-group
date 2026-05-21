"""
app.py — AURA India Group Analytics Dashboard
==============================================
Enhanced group submission with full ML pipeline,
cross-validation, ROC curves, radar charts, live predictors,
word clouds, geographic heatmaps, A/B pricing simulator.

Run: streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="AURA India — Group Analytics Dashboard",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "AURA India Group PBL — Data-Driven Art Experience Analytics"}
)

import pandas as pd
import numpy as np
from aura_theme import GLOBAL_CSS, GOLD, TEAL, ORANGE, ROSE, INDIGO, MUTED, SURFACE, SURFACE2, INK, BG, kpi_card
from aura_data import (
    load_data, train_classification_models,
    train_regression_models, train_clustering,
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
    <div style="padding:28px 0 12px;border-bottom:1px solid rgba(255,255,255,0.07);margin-bottom:20px;">
        <div style="font-size:32px;font-weight:900;color:{GOLD};letter-spacing:0.08em;line-height:1;">AURA</div>
        <div style="font-size:9px;letter-spacing:0.25em;text-transform:uppercase;color:{MUTED};margin-top:5px;">
        Art Experience Pod · India · Group PBL</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="color:{MUTED};font-size:11px;line-height:1.8;margin-bottom:24px;">
        Comprehensive analytics for the AURA Art Experience Pod —
        2,000 Indian consumers · 7 ML algorithms · 4-layer analysis pipeline
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<div style='color:{GOLD};font-size:10px;letter-spacing:0.15em;text-transform:uppercase;margin-bottom:10px;font-weight:700;'>Dashboard</div>", unsafe_allow_html=True)

    tabs_config = [
        ("🏠", "Executive Summary",  "KPIs · Business Context"),
        ("📊", "Overview",           "Descriptive Analysis"),
        ("🔍", "Diagnostic",         "Why Customers Convert"),
        ("🧩", "Clustering",         "Persona Segmentation"),
        ("🤖", "Classification",     "Interest Prediction + CV"),
        ("🔗", "Association Rules",  "Product Bundling"),
        ("📈", "Regression",         "WTP Prediction + Simulator"),
        ("🚀", "Predict New",        "Score New Customers"),
        ("💡", "Prescriptive",       "Strategy & Simulator"),
    ]

    selected_tab = st.radio(
        "Select analysis:",
        [f"{icon} {name}" for icon, name, _ in tabs_config],
        label_visibility="collapsed"
    )

    # Sub-label
    for icon, name, sub in tabs_config:
        if selected_tab == f"{icon} {name}":
            st.markdown(f"<div style='color:{MUTED};font-size:10px;margin-top:-8px;margin-bottom:16px;padding-left:4px;'>{sub}</div>", unsafe_allow_html=True)
            break

    st.markdown(f"""
    <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.06);">
        <div style="color:{MUTED};font-size:10px;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:10px;">Dataset</div>
        <div style="font-size:11px;color:{TEAL};line-height:2.0;">
            ● Survey 1: 2,000 respondents<br>
            ● Survey 2: 1,314 deep profiles<br>
            ● ARM Transactions: 2,000 rows<br>
            ● Features: 81 columns
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,0.06);">
        <div style="color:{MUTED};font-size:10px;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:10px;">Analysis Pipeline</div>
        <div style="font-size:11px;color:{MUTED};line-height:2.0;">
            ✓ Descriptive · Diagnostic<br>
            ✓ K-Means (Silhouette-driven)<br>
            ✓ RF · XGBoost · LR + 5-fold CV<br>
            ✓ Apriori ARM (Support/Confidence/Lift)<br>
            ✓ RF · GBM · LR Regression<br>
            ✓ Live WTP Predictor<br>
            ✓ Prescriptive A/B Simulator
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<div style='margin-top:28px;color:{MUTED};font-size:10px;'>AURA India · Group PBL · 2026</div>", unsafe_allow_html=True)

# ── LOAD DATA ─────────────────────────────────────────────────
with st.spinner("Loading AURA dataset..."):
    df1, df2, arm, wide = load_data()

# ── TRAIN MODELS ──────────────────────────────────────────────
with st.spinner("Training & cross-validating models..."):
    clf_models, clf_results, clf_feat_imp, X_test_clf, y_test_clf, X_train_clf, y_train_clf = \
        train_classification_models(df1)

    reg_models, reg_results, reg_feat_imp, X_test_reg, y_test_reg, reg_scaler = \
        train_regression_models(df1)

    km_model, df_clustered, km_scaler, best_k, k_range, inertias, silhouettes, pca = \
        train_clustering(df1)

# ── RENDER TABS ───────────────────────────────────────────────
tab_name = selected_tab.split(" ", 1)[1]

if tab_name == "Executive Summary":
    import tab_summary
    tab_summary.render(df1, df2, arm, wide, clf_results, reg_results, best_k, silhouettes)

elif tab_name == "Overview":
    import tab_overview
    tab_overview.render(df1, df2, arm, wide)

elif tab_name == "Diagnostic":
    import tab_diagnostic
    tab_diagnostic.render(df1, df2, arm, wide)

elif tab_name == "Clustering":
    import tab_clustering
    tab_clustering.render(df1, df2, arm, wide,
                          km_model, df_clustered, km_scaler,
                          best_k, k_range, inertias, silhouettes, pca)

elif tab_name == "Classification":
    import tab_classification
    tab_classification.render(df1, df2, arm, wide,
                              clf_models, clf_results, clf_feat_imp,
                              X_test_clf, y_test_clf, X_train_clf, y_train_clf)

elif tab_name == "Association Rules":
    import tab_arm
    tab_arm.render(df1, df2, arm, wide)

elif tab_name == "Regression":
    import tab_regression
    tab_regression.render(df1, df2, arm, wide,
                          reg_models, reg_results, reg_feat_imp,
                          X_test_reg, y_test_reg, reg_scaler)

elif tab_name == "Predict New":
    import tab_predict
    tab_predict.render(df1, df2, arm, wide,
                       clf_models, reg_models, km_model, km_scaler)

elif tab_name == "Prescriptive":
    import tab_prescriptive
    tab_prescriptive.render(df1, df2, arm, wide,
                            clf_models, reg_models, km_model, km_scaler,
                            df_clustered, best_k)
