import streamlit as st


def show_dashboard():

    # ── Page header ──
    st.markdown("""
    <div class="page-header">
        <div class="eyebrow">Model Performance</div>
        <h1>Analytics <span class="gradient-text">Dashboard</span></h1>
        <p>Statistical validation of the Random Forest regression model on the test set (299 listings).</p>
    </div>
    """, unsafe_allow_html=True)

    # ── KPI row ──
    m1, m2, m3, m4 = st.columns(4, gap="small")

    with m1:
        st.markdown("""
        <div class="metric-card green">
            <p class="label">R² Coefficient</p>
            <p class="value green">0.658</p>
            <p class="sub">Variance explained</p>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown("""
        <div class="metric-card red">
            <p class="label">RMSE</p>
            <p class="value red">59.6K <span style="font-size:14px;color:#4A5568;">MAD</span></p>
            <p class="sub">Root mean sq. error</p>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown("""
        <div class="metric-card blue">
            <p class="label">Mean Abs. Error</p>
            <p class="value blue">41.2K <span style="font-size:14px;color:#4A5568;">MAD</span></p>
            <p class="sub">Average deviation</p>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown("""
        <div class="metric-card amber">
            <p class="label">Training Records</p>
            <p class="value amber">1 197</p>
            <p class="sub">After preprocessing</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # ── Charts row 1 ──
    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="chart-title">Actual vs. Predicted Prices</p>', unsafe_allow_html=True)
        try:
            from utils.charts import generate_actual_vs_pred
            st.plotly_chart(generate_actual_vs_pred(), use_container_width=True, config={"displayModeBar": False})
        except Exception as e:
            _placeholder_chart(f"Chart unavailable: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="chart-title">Price Distribution (MAD)</p>', unsafe_allow_html=True)
        try:
            from utils.charts import generate_price_dist
            st.plotly_chart(generate_price_dist(), use_container_width=True, config={"displayModeBar": False})
        except Exception as e:
            _placeholder_chart(f"Chart unavailable: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Charts row 2 ──
    c3, c4 = st.columns(2, gap="medium")

    with c3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="chart-title">Top 10 Brands by Listing Volume</p>', unsafe_allow_html=True)
        try:
            from utils.charts import generate_brand_dist
            st.plotly_chart(generate_brand_dist(), use_container_width=True, config={"displayModeBar": False})
        except Exception as e:
            _placeholder_chart(f"Chart unavailable: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="chart-title">Listings by City</p>', unsafe_allow_html=True)
        try:
            from utils.charts import generate_city_dist
            st.plotly_chart(generate_city_dist(), use_container_width=True, config={"displayModeBar": False})
        except Exception as e:
            _placeholder_chart(f"Chart unavailable: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ── CV summary strip ──
    st.markdown("""
    <div class="card" style="margin-top:4px;">
        <p class="card-title">Cross-Validation Summary — 5-Fold KFold</p>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
            <div style="flex:1; min-width:160px; text-align:center;
                         background:#0D1117; border:1px solid #1E2A3A;
                         border-radius:8px; padding:14px 10px;">
                <div style="font-size:10px; color:#4A5568; text-transform:uppercase;
                             letter-spacing:1px; margin-bottom:6px;">Linear Regression</div>
                <div style="font-size:20px; font-weight:700; color:#94A3B8;">R² ≈ 0.602</div>
                <div style="font-size:11px; color:#4A5568; margin-top:3px;">RMSE ≈ 0.320</div>
            </div>
            <div style="flex:1; min-width:160px; text-align:center;
                         background:#0E2830; border:1px solid #0E7C86;
                         border-radius:8px; padding:14px 10px;">
                <div style="font-size:10px; color:#0E7C86; text-transform:uppercase;
                             letter-spacing:1px; margin-bottom:6px;">Random Forest ✓ Selected</div>
                <div style="font-size:20px; font-weight:700; color:#10B981;">R² ≈ 0.647</div>
                <div style="font-size:11px; color:#4A5568; margin-top:3px;">RMSE ≈ 0.318</div>
            </div>
            <div style="flex:1; min-width:160px; text-align:center;
                         background:#0D1117; border:1px solid #1E2A3A;
                         border-radius:8px; padding:14px 10px;">
                <div style="font-size:10px; color:#4A5568; text-transform:uppercase;
                             letter-spacing:1px; margin-bottom:6px;">Gradient Boosting</div>
                <div style="font-size:20px; font-weight:700; color:#94A3B8;">R² ≈ 0.598</div>
                <div style="font-size:11px; color:#4A5568; margin-top:3px;">RMSE ≈ 0.322</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def _placeholder_chart(msg: str):
    st.markdown(f"""
    <div style="height:200px; display:flex; align-items:center; justify-content:center;
                 background:#0D1117; border:1px dashed #1E2A3A; border-radius:8px;
                 color:#4A5568; font-size:13px;">
        {msg}
    </div>
    """, unsafe_allow_html=True)