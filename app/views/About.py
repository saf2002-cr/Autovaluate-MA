import streamlit as st


def show_about():

    # ── Page header ──
    st.markdown("""
    <div class="page-header">
        <div class="eyebrow">Technical Documentation</div>
        <h1>Model <span class="gradient-text">Architecture</span></h1>
        <p>End-to-end pipeline: data collection, preprocessing, feature engineering and ensemble modeling.</p>
    </div>
    """, unsafe_allow_html=True)

    col_main, col_side = st.columns([3, 1], gap="large")

    with col_main:

        # Pipeline steps
        steps = [
            {
                "n": "1",
                "title": "Data Collection — Web Scraping",
                "body": (
                    "Multi-threaded scraper targeting <code>moteur.ma</code> "
                    "(67 pages, ~2 010 raw listings). "
                    "Used <code>ThreadPoolExecutor</code> with 10 parallel workers to fetch detail pages, "
                    "reducing collection time from ~26 min to under 3 min. "
                    "Fields extracted: brand, model, price, city, year, mileage, fuel, transmission."
                )
            },
            {
                "n": "2",
                "title": "Cleaning & Outlier Removal",
                "body": (
                    "Dropped 391 rows with missing price (target). "
                    "Applied IQR filter to remove extreme price outliers. "
                    "Fixed a parsing error on <em>Land Rover</em> brand. "
                    "Removed constant-value columns (<em>Etat</em>) and near-empty columns "
                    "(<em>Puissance_fiscale</em> 98.6 % missing, <em>Nombre_portes</em> 69 % missing)."
                )
            },
            {
                "n": "3",
                "title": "Train / Test Split — Anti-Leakage",
                "body": (
                    "80 / 20 split (<code>random_state=42</code>) performed <strong>before</strong> "
                    "any imputation or scaling. All group statistics (median, mode) were computed "
                    "on the training set only, then applied to the test set — preventing data leakage."
                )
            },
            {
                "n": "4",
                "title": "Imputation & Feature Engineering",
                "body": (
                    "Missing values imputed by <em>(Brand, Model)</em> group: median for Year, "
                    "mode for City / Transmission / Fuel. "
                    "New feature: <code>Usage_Intensity = Mileage / (2026 − Year + 1)</code> "
                    "to capture mechanical depreciation rate. "
                    "Rare brands/cities (< 1 % frequency) grouped into <em>Autre / Autres</em>. "
                    "<code>StandardScaler</code> applied to numerical features (fit on train only)."
                )
            },
            {
                "n": "5",
                "title": "Target Transformation",
                "body": (
                    "Price distribution is strongly right-skewed. "
                    "Applied <code>log1p(Price) → Price_Log</code> as the regression target "
                    "to normalize the distribution and reduce heteroscedasticity. "
                    "Predictions are back-transformed with <code>expm1()</code> for display."
                )
            },
            {
                "n": "6",
                "title": "Encoding & Final Dataset",
                "body": (
                    "One-Hot Encoding on Brand (23), City (6), Transmission (2), Fuel (3). "
                    "Test columns aligned to training schema (<code>reindex, fill_value=0</code>). "
                    "Final dataset: <strong>1 496 observations × 39 features</strong>."
                )
            },
            {
                "n": "7",
                "title": "Ensemble Modeling — Random Forest Regressor",
                "body": (
                    "Three models compared via 5-fold cross-validation: "
                    "Linear Regression (R² ≈ 0.60), Random Forest (R² ≈ 0.61), "
                    "Gradient Boosting (R² ≈ 0.60). "
                    "Random Forest selected for hyperparameter tuning with "
                    "<code>RandomizedSearchCV</code> (20 iterations) → "
                    "best params: <code>n_estimators=300, min_samples_split=5, max_features='sqrt'</code>. "
                    "Final CV R² ≈ 0.647, test set R² ≈ 0.66."
                )
            },
        ]

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="card-title">Pipeline Steps</p>', unsafe_allow_html=True)

        for step in steps:
            st.markdown(f"""
            <div class="pipeline-step">
                <div class="step-number">{step["n"]}</div>
                <div class="step-body">
                    <p class="step-title">{step["title"]}</p>
                    <p class="step-desc">{step["body"]}</p>
                </div>
            </div>
            {"<div style='height:1px;background:#1A2332;margin:4px 0 16px 56px;'></div>"
              if step["n"] != "7" else ""}
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ── Right sidebar: quick stats ──
    with col_side:

        st.markdown("""
        <div class="card">
            <p class="card-title">Dataset Stats</p>
            <div style="display:flex;flex-direction:column;gap:12px;">
                <div>
                    <div style="font-size:10px;color:#4A5568;text-transform:uppercase;
                                 letter-spacing:1px;margin-bottom:3px;">Raw listings</div>
                    <div style="font-size:22px;font-weight:700;color:#F8FAFC;">2 010</div>
                </div>
                <div style="height:1px;background:#1A2332;"></div>
                <div>
                    <div style="font-size:10px;color:#4A5568;text-transform:uppercase;
                                 letter-spacing:1px;margin-bottom:3px;">After cleaning</div>
                    <div style="font-size:22px;font-weight:700;color:#F8FAFC;">1 496</div>
                </div>
                <div style="height:1px;background:#1A2332;"></div>
                <div>
                    <div style="font-size:10px;color:#4A5568;text-transform:uppercase;
                                 letter-spacing:1px;margin-bottom:3px;">Features</div>
                    <div style="font-size:22px;font-weight:700;color:#F8FAFC;">39</div>
                </div>
                <div style="height:1px;background:#1A2332;"></div>
                <div>
                    <div style="font-size:10px;color:#4A5568;text-transform:uppercase;
                                 letter-spacing:1px;margin-bottom:3px;">Unique brands</div>
                    <div style="font-size:22px;font-weight:700;color:#F8FAFC;">58</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-top:16px;">
            <p class="card-title">Model Results</p>
            <div style="display:flex;flex-direction:column;gap:10px;">
                <div style="background:#0E2830;border:1px solid #0E7C86;
                             border-radius:8px;padding:10px 12px;">
                    <div style="font-size:10px;color:#0E7C86;text-transform:uppercase;
                                 letter-spacing:1px;margin-bottom:4px;">R² (test set)</div>
                    <div style="font-size:20px;font-weight:700;color:#10B981;">0.658</div>
                </div>
                <div style="background:#111827;border:1px solid #1E2A3A;
                             border-radius:8px;padding:10px 12px;">
                    <div style="font-size:10px;color:#4A5568;text-transform:uppercase;
                                 letter-spacing:1px;margin-bottom:4px;">CV R² (5-fold)</div>
                    <div style="font-size:20px;font-weight:700;color:#94A3B8;">0.647</div>
                </div>
                <div style="background:#111827;border:1px solid #1E2A3A;
                             border-radius:8px;padding:10px 12px;">
                    <div style="font-size:10px;color:#4A5568;text-transform:uppercase;
                                 letter-spacing:1px;margin-bottom:4px;">RMSE</div>
                    <div style="font-size:20px;font-weight:700;color:#94A3B8;">59.6K MAD</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style="margin-top:16px;">
            <p class="card-title">Roadmap</p>
            <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:#64748B;">
                <div>🔄 Daily scrape pipeline (cron)</div>
                <div>⚡ XGBoost / LightGBM upgrade</div>
                <div>🖼️ CV damage detection module</div>
                <div>🌍 National coverage expansion</div>
            </div>
        </div>
        """, unsafe_allow_html=True)