"""tab_summary.py — Executive Summary Landing Page"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from aura_theme import (GOLD, TEAL, ORANGE, ROSE, INDIGO, MUTED,
                        SURFACE, SURFACE2, INK, PALETTE, kpi_card,
                        page_header, section_header, info_card)


def render(df1, df2, arm, wide, clf_results, reg_results, best_k, silhouettes):
    # Hero header
    st.markdown(f"""
    <div style="padding:40px 0 8px;">
        <div style="font-size:11px;letter-spacing:0.25em;text-transform:uppercase;
        color:{TEAL};font-weight:700;margin-bottom:12px;">AURA INDIA · GROUP PBL · 2026</div>
        <div style="font-size:42px;font-weight:900;color:{INK};line-height:1.1;margin-bottom:12px;">
            Art Experience Pod<br>
            <span style="background:linear-gradient(90deg,{GOLD},{TEAL});
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            Analytics Dashboard</span>
        </div>
        <div style="font-size:15px;color:{MUTED};max-width:680px;line-height:1.7;margin-bottom:20px;">
            A data-driven feasibility study for launching AURA — India's first subscription-based
            art experience pod network. 2,000 respondents · 4-layer ML pipeline · Full prescriptive output.
        </div>
        <div style="width:60px;height:3px;background:linear-gradient(90deg,{GOLD},{TEAL});border-radius:2px;"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── KPI CARDS ────────────────────────────────────────────
    section_header("Key Findings at a Glance", GOLD)

    interested_pct = (df1["aura_interest_label"] == "Interested").mean() * 100
    maybe_pct      = (df1["aura_interest_label"] == "Maybe").mean() * 100
    total_n        = len(df1)

    wtp_col = "session_wtp_numeric"
    avg_wtp = df1[wtp_col].median() if wtp_col in df1.columns else 550

    best_clf = max(clf_results, key=lambda k: clf_results[k]["accuracy"])
    best_acc = clf_results[best_clf]["accuracy"]
    best_cv  = clf_results[best_clf].get("cv_mean", best_acc)

    best_reg = max(reg_results, key=lambda k: reg_results[k]["r2"])
    best_r2  = reg_results[best_reg]["r2"]

    sil_score = max(silhouettes)

    cols = st.columns(6)
    kpis = [
        ("Respondents",    f"{total_n:,}",       "Survey 1 sample",    GOLD),
        ("Interested",     f"{interested_pct:.1f}%", f"+ {maybe_pct:.1f}% Maybe", TEAL),
        ("Median WTP",     f"₹{int(avg_wtp):,}",  "Per session",        ORANGE),
        ("Best Model CV",  f"{best_cv*100:.1f}%",  f"{best_clf}",        INDIGO),
        ("Reg R²",         f"{best_r2:.3f}",       f"{best_reg}",        ROSE),
        ("Clusters (K)",   f"{best_k}",            f"Silhouette {sil_score:.3f}", TEAL),
    ]
    for col, (label, value, delta, color) in zip(cols, kpis):
        with col:
            st.markdown(kpi_card(label, value, delta, color), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── INTEREST DISTRIBUTION ────────────────────────────────
    c1, c2, c3 = st.columns([1, 1, 1])

    with c1:
        section_header("Interest Distribution", GOLD)
        interest_counts = df1["aura_interest_label"].value_counts()
        colors_map = {"Interested": TEAL, "Maybe": GOLD, "Not_Interested": ROSE}
        fig_pie = go.Figure(go.Pie(
            labels=interest_counts.index,
            values=interest_counts.values,
            hole=0.6,
            marker_colors=[colors_map.get(l, ORANGE) for l in interest_counts.index],
            textinfo="percent+label",
            textfont=dict(size=11, color=INK),
            hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Share: %{percent}<extra></extra>"
        ))
        fig_pie.update_layout(
            height=300, showlegend=False,
            annotations=[dict(text=f"<b>{total_n:,}</b><br>Total", x=0.5, y=0.5,
                              font=dict(size=14, color=INK), showarrow=False)]
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with c2:
        section_header("WTP Distribution", TEAL)
        if wtp_col in df1.columns:
            fig_hist = go.Figure(go.Histogram(
                x=df1[wtp_col].dropna(),
                nbinsx=20,
                marker_color=GOLD,
                opacity=0.85,
                hovertemplate="₹%{x}<br>Count: %{y}<extra></extra>"
            ))
            fig_hist.add_vline(x=avg_wtp, line_dash="dash", line_color=TEAL,
                               annotation_text=f"Median ₹{int(avg_wtp):,}",
                               annotation_font_color=TEAL)
            fig_hist.update_layout(
                height=300,
                xaxis_title="WTP (₹/session)",
                yaxis_title="Respondents",
                showlegend=False
            )
            st.plotly_chart(fig_hist, use_container_width=True)

    with c3:
        section_header("Model Comparison", INDIGO)
        model_names = list(clf_results.keys())
        accs = [clf_results[m]["accuracy"] * 100 for m in model_names]
        cvs  = [clf_results[m].get("cv_mean", clf_results[m]["accuracy"]) * 100 for m in model_names]

        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(name="Test Accuracy", x=model_names, y=accs,
                                  marker_color=GOLD, text=[f"{a:.1f}%" for a in accs],
                                  textposition="outside"))
        fig_bar.add_trace(go.Bar(name="CV Mean", x=model_names, y=cvs,
                                  marker_color=TEAL, text=[f"{c:.1f}%" for c in cvs],
                                  textposition="outside"))
        fig_bar.update_layout(
            barmode="group", height=300,
            yaxis_title="Accuracy (%)", yaxis_range=[0, 110],
            legend=dict(orientation="h", y=-0.2)
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # ── BUSINESS CONTEXT ─────────────────────────────────────
    section_header("Business Problem Statement", ORANGE)
    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:24px;">
        <div style="background:{SURFACE2};border:1px solid rgba(255,255,255,0.06);
        border-left:3px solid {GOLD};border-radius:8px;padding:20px;">
            <div style="color:{GOLD};font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
            font-weight:700;margin-bottom:12px;">The Opportunity</div>
            <div style="color:{MUTED};font-size:13px;line-height:1.8;">
                India's urban millennials and Gen Z consumers are experiencing a wellness-creativity gap.
                Stress levels are rising, yet accessible, affordable art experiences remain scarce.
                AURA proposes pod-based art sessions in high-footfall urban locations — malls, co-working
                spaces, transit hubs — at ₹200–₹1,200 per 45-minute session.
            </div>
        </div>
        <div style="background:{SURFACE2};border:1px solid rgba(255,255,255,0.06);
        border-left:3px solid {TEAL};border-radius:8px;padding:20px;">
            <div style="color:{TEAL};font-size:11px;letter-spacing:0.12em;text-transform:uppercase;
            font-weight:700;margin-bottom:12px;">Research Questions</div>
            <div style="color:{MUTED};font-size:13px;line-height:2.0;">
                RQ1 — Who is interested in AURA? (Classification)<br>
                RQ2 — How much will they pay? (Regression)<br>
                RQ3 — What customer personas exist? (Clustering)<br>
                RQ4 — What experiences bundle naturally? (ARM)<br>
                RQ5 — What is the optimal launch strategy? (Prescriptive)
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── PIPELINE OVERVIEW ─────────────────────────────────────
    section_header("4-Layer Analytics Pipeline", TEAL)
    layers = [
        (GOLD,   "01 Descriptive",  "WHO are these consumers?",
         "Demographic distributions, city-tier breakdown, art form preferences, stress profiles"),
        (TEAL,   "02 Diagnostic",   "WHY are they interested (or not)?",
         "Cross-tabulations, funnel analysis, correlation heatmap, barrier identification"),
        (ORANGE, "03 Predictive",   "WHAT will they do?",
         "K-Means clustering · Random Forest · XGBoost · Logistic Regression · Apriori ARM · Gradient Boosting"),
        (ROSE,   "04 Prescriptive", "WHAT should AURA do?",
         "Segment-specific pricing, pod location priority, A/B session simulator, new customer scoring"),
    ]
    cols = st.columns(4)
    for col, (color, title, q, desc) in zip(cols, layers):
        with col:
            st.markdown(f"""
            <div style="background:{SURFACE2};border:1px solid rgba(255,255,255,0.06);
            border-top:3px solid {color};border-radius:8px;padding:20px;height:200px;">
                <div style="color:{color};font-size:10px;letter-spacing:0.15em;
                text-transform:uppercase;font-weight:700;margin-bottom:8px;">{title}</div>
                <div style="color:{INK};font-size:13px;font-weight:600;margin-bottom:10px;">{q}</div>
                <div style="color:{MUTED};font-size:11px;line-height:1.7;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    info_card(
        "Key Takeaway",
        f"<b>{interested_pct:.1f}%</b> of 2,000 Indian consumers express interest in AURA, with a median WTP of "
        f"<b>₹{int(avg_wtp):,}/session</b>. Our best classification model achieves <b>{best_cv*100:.1f}% cross-validated accuracy</b>. "
        f"K-Means identifies <b>{best_k} distinct personas</b> (Silhouette = {max(silhouettes):.3f}), "
        "each requiring a tailored pricing, product, and channel strategy. AURA has a clear, data-backed path to launch.",
        GOLD
    )
