import streamlit as st


def show_home():

    # ── Page header ──
    st.markdown("""
    <div class="page-header">
        <div class="eyebrow">Moroccan Used Car Market</div>
        <h1>Vehicle Price <span class="gradient-text">Estimator</span></h1>
        <p>Random Forest model trained on 1 496 listings from moteur.ma · R² ≈ 0.66</p>
    </div>
    """, unsafe_allow_html=True)

    col_form, col_result = st.columns([3, 2], gap="large")

    # ── Left column: form ──
    with col_form:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="card-title">Vehicle Specifications</p>', unsafe_allow_html=True)

        left, right = st.columns(2, gap="medium")

        with left:
            brand = st.selectbox("Brand", [
                "Alfa", "Audi", "BMW", "Citroën", "Dacia", "Fiat", "Ford",
                "Hyundai", "Jaguar", "Jeep", "Kia", "Land Rover",
                "Mercedes-Benz", "Nissan", "Opel", "Peugeot", "Renault",
                "Seat", "Skoda", "Toyota", "Volkswagen", "Volvo", "Autre"
            ])

            year = st.slider("Year", min_value=2000, max_value=2026, value=2018)

            fuel = st.selectbox("Fuel type", ["Diesel", "Essence", "Electrifié"])

        with right:
            city = st.selectbox("City", [
                "Agadir", "Casablanca", "Marrakech", "Rabat", "Tanger", "Autres"
            ])

            mileage = st.number_input(
                "Mileage (km)",
                min_value=0, max_value=600_000,
                value=95_000, step=5_000
            )

            transmission = st.selectbox("Transmission", ["Automatique", "Manuelle"])

        st.markdown('</div>', unsafe_allow_html=True)

        # ── Predict button ──
        st.markdown("<div style='margin-top:4px;'>", unsafe_allow_html=True)
        predict_btn = st.button("→  Estimate Price", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Info strip ──
        st.markdown("""
        <div style="display:flex; gap:12px; margin-top:16px;">
            <div style="flex:1; background:#111827; border:1px solid #1E2A3A;
                        border-radius:8px; padding:12px 14px;">
                <div style="font-size:10px; color:#4A5568; letter-spacing:1px;
                             text-transform:uppercase; margin-bottom:4px;">Model</div>
                <div style="font-size:13px; font-weight:600; color:#94A3B8;">Random Forest</div>
            </div>
            <div style="flex:1; background:#111827; border:1px solid #1E2A3A;
                        border-radius:8px; padding:12px 14px;">
                <div style="font-size:10px; color:#4A5568; letter-spacing:1px;
                             text-transform:uppercase; margin-bottom:4px;">Training set</div>
                <div style="font-size:13px; font-weight:600; color:#94A3B8;">1 197 listings</div>
            </div>
            <div style="flex:1; background:#111827; border:1px solid #1E2A3A;
                        border-radius:8px; padding:12px 14px;">
                <div style="font-size:10px; color:#4A5568; letter-spacing:1px;
                             text-transform:uppercase; margin-bottom:4px;">R² Score</div>
                <div style="font-size:13px; font-weight:600; color:#10B981;">≈ 0.66</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Right column: result ──
    with col_result:
        st.markdown('<p class="card-title" style="margin-bottom:12px;">Valuation Result</p>',
                    unsafe_allow_html=True)

        if predict_btn:
            input_data = {
                "Marque": brand,
                "Ville": city,
                "Transmission": transmission,
                "Carburant": fuel,
                "Annee": year,
                "Kilometrage": mileage
            }

            with st.spinner("Running model inference…"):
                try:
                    from utils.prediction import predict_car_price
                    price = predict_car_price(input_data)
                    usage_intensity = round(mileage / (2026 - year + 1), 0)

                    st.markdown(f"""
                    <div class="result-card">
                        <p class="result-label">Estimated Market Value</p>
                        <p class="result-price">{price:,.0f}
                            <span class="result-currency"> MAD</span>
                        </p>
                        <div class="result-divider"></div>
                        <div class="result-meta">
                            <div class="result-meta-item">
                                <p class="meta-label">Brand</p>
                                <p class="meta-value">{brand}</p>
                            </div>
                            <div class="result-meta-item">
                                <p class="meta-label">Year</p>
                                <p class="meta-value">{year}</p>
                            </div>
                            <div class="result-meta-item">
                                <p class="meta-label">Usage Index</p>
                                <p class="meta-value">{usage_intensity:,.0f} km/yr</p>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as e:
                    st.markdown(f"""
                    <div class="result-card" style="border-color:#EF4444;">
                        <p style="color:#EF4444; font-size:13px; margin:0;">
                            ⚠️ Prediction error: {e}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="placeholder-card">
                <div class="placeholder-icon">🎯</div>
                <p>Fill in the vehicle details on the left,<br>
                   then click <strong style="color:#0E7C86;">Estimate Price</strong>
                   to get an instant valuation.</p>
            </div>
            """, unsafe_allow_html=True)

            # Tips
            st.markdown("""
            <div style="margin-top:16px;">
                <p style="font-size:11px; font-weight:700; letter-spacing:1.5px;
                           text-transform:uppercase; color:#4A5568; margin-bottom:10px;">
                    How it works
                </p>
                <div style="display:flex; flex-direction:column; gap:8px;">
                    <div style="display:flex; align-items:center; gap:10px;
                                 background:#111827; border:1px solid #1E2A3A;
                                 border-radius:8px; padding:10px 14px;">
                        <span style="font-size:16px;">1️⃣</span>
                        <span style="font-size:13px; color:#64748B;">Select brand, year, fuel & city</span>
                    </div>
                    <div style="display:flex; align-items:center; gap:10px;
                                 background:#111827; border:1px solid #1E2A3A;
                                 border-radius:8px; padding:10px 14px;">
                        <span style="font-size:16px;">2️⃣</span>
                        <span style="font-size:13px; color:#64748B;">Enter mileage & transmission type</span>
                    </div>
                    <div style="display:flex; align-items:center; gap:10px;
                                 background:#111827; border:1px solid #1E2A3A;
                                 border-radius:8px; padding:10px 14px;">
                        <span style="font-size:16px;">3️⃣</span>
                        <span style="font-size:13px; color:#64748B;">Get your instant market valuation</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)