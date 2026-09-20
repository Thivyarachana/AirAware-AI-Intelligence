import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# AIR AWARE - URBAN AIR INTELLIGENCE PLATFORM
# Clean white cards + black text + green background
# ============================================================

st.set_page_config(
    page_title="AirAware | Urban Air Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CLEAN UI THEME
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #EAF7EE !important;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* All normal text */
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6,
    .stApp p,
    .stApp label {
        color: #000000 !important;
    }

    /* White hero/card */
    .hero-card,
    .info-card {
        background: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #C9E2CE !important;
        border-radius: 18px !important;
        padding: 25px 30px !important;
        margin: 10px 0 22px 0 !important;
        box-shadow: 0 5px 18px rgba(0,0,0,0.07) !important;
    }

    .hero-card h1,
    .hero-card h2,
    .hero-card h3,
    .hero-card p,
    .info-card h1,
    .info-card h2,
    .info-card h3,
    .info-card p {
        color: #000000 !important;
        background: transparent !important;
    }

    .hero-card h1 {
        font-size: 2.8rem !important;
        margin-bottom: 8px !important;
    }

    .hero-card p,
    .info-card p {
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #D8F0DE !important;
    }

    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }

    /* Dropdown selected value */
    div[data-baseweb="select"] {
        background: #FFFFFF !important;
    }

    div[data-baseweb="select"] > div {
        background: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #AFCDB6 !important;
    }

    div[data-baseweb="select"] span,
    div[data-baseweb="select"] input {
        color: #000000 !important;
    }

    /* Dropdown menu/options */
    div[role="listbox"] {
        background: #FFFFFF !important;
    }

    div[role="option"] {
        background: #FFFFFF !important;
        color: #000000 !important;
    }

    div[role="option"] * {
        color: #000000 !important;
    }

    div[role="option"]:hover {
        background: #EAF7EE !important;
    }

    /* Inputs */
    input,
    textarea {
        background: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #AFCDB6 !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #555555 !important;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid #C9E2CE !important;
        border-radius: 16px !important;
        padding: 18px !important;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05) !important;
    }

    div[data-testid="stMetric"] label,
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricDelta"] {
        color: #000000 !important;
    }

    /* Buttons */
    .stButton > button {
        background: #2E7D4F !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
    }

    .stButton > button * {
        color: #FFFFFF !important;
    }

    /* Expanders */
    div[data-testid="stExpander"] {
        background: #FFFFFF !important;
        border: 1px solid #C9E2CE !important;
        border-radius: 14px !important;
    }

    div[data-testid="stExpander"] * {
        color: #000000 !important;
    }

    /* Radio */
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] span {
        color: #000000 !important;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: #000000 !important;
        padding: 25px 10px 10px 10px;
        font-size: 0.9rem;
    }

    .footer-text p {
        color: #000000 !important;
        margin: 5px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# DATA LOADING
# ============================================================

DATA_PATH = "data/air_quality.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    # Make sure timestamp is available
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    else:
        date_cols = [c for c in ["year", "month", "day", "hour"] if c in df.columns]
        if len(date_cols) == 4:
            df["timestamp"] = pd.to_datetime(
                dict(
                    year=pd.to_numeric(df["year"], errors="coerce"),
                    month=pd.to_numeric(df["month"], errors="coerce"),
                    day=pd.to_numeric(df["day"], errors="coerce"),
                    hour=pd.to_numeric(df["hour"], errors="coerce"),
                ),
                errors="coerce",
            )

    numeric_cols = [
        "PM2.5", "PM10", "SO2", "NO2", "CO", "O3",
        "TEMP", "PRES", "DEWP", "RAIN", "WSPM"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "station" in df.columns:
        df["station"] = df["station"].astype(str)

    df = df.dropna(subset=["timestamp"]).sort_values("timestamp").reset_index(drop=True)

    df["hour"] = df["timestamp"].dt.hour
    df["month"] = df["timestamp"].dt.month
    df["year"] = df["timestamp"].dt.year
    df["month_name"] = df["timestamp"].dt.strftime("%b")
    df["day_name"] = df["timestamp"].dt.day_name()

    return df


try:
    df = load_data()
except Exception as e:
    st.error("The dataset could not be loaded.")
    st.code(str(e))
    st.info("Make sure the GitHub repository contains: data/air_quality.csv")
    st.stop()

# ============================================================
# AVAILABLE COLUMNS
# ============================================================

POLLUTANTS = [c for c in ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"] if c in df.columns]
ENVIRONMENTAL = [c for c in ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"] if c in df.columns]

if not POLLUTANTS:
    st.error("No pollutant columns were found in the dataset.")
    st.stop()

# ============================================================
# PLOTLY STYLE HELPERS
# ============================================================

def style_figure(fig, show_legend=True):
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="black"),
        title_font=dict(color="black", size=18),
        legend=dict(
            font=dict(color="black"),
            bgcolor="rgba(255,255,255,0.8)"
        ),
        xaxis=dict(
            title_font=dict(color="black"),
            tickfont=dict(color="black"),
            gridcolor="#E5E5E5",
            zerolinecolor="#CCCCCC",
        ),
        yaxis=dict(
            title_font=dict(color="black"),
            tickfont=dict(color="black"),
            gridcolor="#E5E5E5",
            zerolinecolor="#CCCCCC",
        ),
        margin=dict(l=55, r=30, t=65, b=55),
        showlegend=show_legend,
    )
    return fig


def add_black_labels(fig, text_values=None, position="outside", size=11):
    if text_values is not None:
        fig.update_traces(
            text=text_values,
            textposition=position,
            textfont=dict(color="black", size=size),
            cliponaxis=False,
        )
    else:
        fig.update_traces(
            textfont=dict(color="black", size=size),
            cliponaxis=False,
        )
    return fig


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.markdown(
    """
    <div style="
        background:#FFFFFF;
        border:1px solid #B7DCC0;
        border-radius:16px;
        padding:18px;
        margin-bottom:18px;
    ">
        <h2 style="color:#000000; margin:0;">🌿 AirAware</h2>
        <p style="color:#000000; margin:6px 0 0 0;">
            Urban Air Intelligence
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

page = st.sidebar.selectbox(
    "Navigate",
    [
        "🌱 Mission Control",
        "📈 Pollution Patterns",
        "🌦️ Weather & Pollution",
        "📍 Station Intelligence",
        "🔬 Correlation Lab",
        "🧪 Air Risk Simulator",
        "📋 Data Quality",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"**Records:** {len(df):,}  \n"
    f"**Stations:** {df['station'].nunique() if 'station' in df.columns else 'N/A'}"
)

# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero-card">
        <h1>🌿 AirAware</h1>
        <p>
            <b>Urban Air Intelligence Platform</b><br>
            Explore real-world pollution patterns, environmental
            relationships, monitoring-station behavior and air-risk
            scenarios through interactive data analytics.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# PAGE 1 - MISSION CONTROL
# ============================================================

if page == "🌱 Mission Control":

    st.markdown("## 🌱 Mission Control")
    st.write("A high-level view of the urban air-quality environment.")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Total Records", f"{len(df):,}")

    with c2:
        stations = df["station"].nunique() if "station" in df.columns else 0
        st.metric("Monitoring Stations", f"{stations}")

    with c3:
        start_date = df["timestamp"].min()
        st.metric("Data Start", start_date.strftime("%b %Y") if pd.notna(start_date) else "N/A")

    with c4:
        end_date = df["timestamp"].max()
        st.metric("Data End", end_date.strftime("%b %Y") if pd.notna(end_date) else "N/A")

    selected_pollutant = st.selectbox(
        "Select Pollutant",
        POLLUTANTS,
        key="mission_pollutant",
    )

    daily = (
        df.set_index("timestamp")[selected_pollutant]
        .resample("D")
        .mean()
        .dropna()
        .reset_index()
    )

    # Sample daily points for readable labels
    daily_plot = daily.iloc[::max(1, len(daily) // 40)].copy()

    fig = px.line(
        daily_plot,
        x="timestamp",
        y=selected_pollutant,
        markers=True,
        title=f"Daily Average {selected_pollutant}",
        text=selected_pollutant,
    )

    fig.update_traces(
        mode="lines+markers+text",
        texttemplate="%{text:.1f}",
        textposition="top center",
        textfont=dict(color="black", size=9),
        cliponaxis=False,
    )

    style_figure(fig)
    st.plotly_chart(fig, use_container_width=True)

    avg_value = df[selected_pollutant].mean()

    st.markdown(
        f"""
        <div class="info-card">
            <h3>💡 Air Quality Insight</h3>
            <p>
                The average recorded {selected_pollutant} concentration
                in the available dataset is <b>{avg_value:.2f}</b>.
            </p>
            <p>
                AirAware transforms historical observations into
                interactive intelligence that can support future
                real-time environmental monitoring systems.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# PAGE 2 - POLLUTION PATTERNS
# ============================================================

elif page == "📈 Pollution Patterns":

    st.markdown("## 📈 Pollution Patterns")
    st.write("Explore how pollutant concentrations change across time.")

    selected_pollutant = st.selectbox(
        "Select Pollutant",
        POLLUTANTS,
        key="patterns_pollutant",
    )

    daily = (
        df.set_index("timestamp")[selected_pollutant]
        .resample("D")
        .mean()
        .dropna()
        .reset_index()
    )

    daily_plot = daily.iloc[::max(1, len(daily) // 45)].copy()

    fig1 = px.line(
        daily_plot,
        x="timestamp",
        y=selected_pollutant,
        markers=True,
        text=selected_pollutant,
        title=f"Daily {selected_pollutant} Trend",
    )

    fig1.update_traces(
        mode="lines+markers+text",
        texttemplate="%{text:.1f}",
        textposition="top center",
        textfont=dict(color="black", size=9),
        cliponaxis=False,
    )

    style_figure(fig1)
    st.plotly_chart(fig1, use_container_width=True)

    hourly = (
        df.groupby("hour")[selected_pollutant]
        .mean()
        .reset_index()
    )

    fig2 = px.line(
        hourly,
        x="hour",
        y=selected_pollutant,
        markers=True,
        text=selected_pollutant,
        title=f"Average {selected_pollutant} by Hour",
    )

    fig2.update_traces(
        mode="lines+markers+text",
        texttemplate="%{text:.1f}",
        textposition="top center",
        textfont=dict(color="black", size=10),
        cliponaxis=False,
    )

    style_figure(fig2)
    fig2.update_xaxes(dtick=1)
    st.plotly_chart(fig2, use_container_width=True)

    monthly = (
        df.groupby(["year", "month"])[selected_pollutant]
        .mean()
        .reset_index()
    )

    monthly["period"] = (
        monthly["year"].astype(str)
        + "-"
        + monthly["month"].astype(str).str.zfill(2)
    )

    fig3 = px.bar(
        monthly,
        x="period",
        y=selected_pollutant,
        text=selected_pollutant,
        title=f"Monthly Average {selected_pollutant}",
    )

    fig3.update_traces(
        texttemplate="%{text:.1f}",
        textposition="outside",
        textfont=dict(color="black", size=9),
        cliponaxis=False,
    )

    style_figure(fig3)
    st.plotly_chart(fig3, use_container_width=True)

# ============================================================
# PAGE 3 - WEATHER & POLLUTION
# ============================================================

elif page == "🌦️ Weather & Pollution":

    st.markdown("## 🌦️ Weather & Pollution")
    st.write("Explore relationships between environmental conditions and pollutant concentrations.")

    env = st.selectbox(
        "Select Environmental Variable",
        ENVIRONMENTAL,
        key="environment",
    )

    pollutant = st.selectbox(
        "Select Pollutant",
        POLLUTANTS,
        key="weather_pollutant",
    )

    plot_df = df[[env, pollutant]].dropna()

    # Keep the scatter readable for browser performance
    if len(plot_df) > 6000:
        plot_df = plot_df.sample(6000, random_state=42)

    fig = px.scatter(
        plot_df,
        x=env,
        y=pollutant,
        trendline="ols",
        opacity=0.55,
        title=f"{pollutant} vs {env}",
    )

    # Scatter has too many observations to display a label on every point.
    # Values remain available on hover.
    fig.update_traces(
        marker=dict(size=7),
        hovertemplate=f"{env}: %{{x:.2f}}<br>{pollutant}: %{{y:.2f}}<extra></extra>",
    )

    style_figure(fig)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        <div class="info-card">
            <h3>🌦️ Environmental Relationship</h3>
            <p>
                The trend line helps identify whether changes in the
                selected environmental variable are associated with
                changes in pollutant concentration.
            </p>
            <p>
                This relationship is descriptive and does not by itself
                prove that one variable causes the other.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# PAGE 4 - STATION INTELLIGENCE
# ============================================================

elif page == "📍 Station Intelligence":

    st.markdown("## 📍 Station Intelligence")
    st.write("Compare pollution levels across monitoring stations.")

    pollutant = st.selectbox(
        "Select Pollutant",
        POLLUTANTS,
        key="station_pollutant",
    )

    if "station" in df.columns:

        station_avg = (
            df.groupby("station")[pollutant]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            station_avg,
            x="station",
            y=pollutant,
            text=pollutant,
            title=f"Average {pollutant} by Monitoring Station",
        )

        fig.update_traces(
            texttemplate="%{text:.2f}",
            textposition="outside",
            textfont=dict(color="black", size=12),
            cliponaxis=False,
        )

        style_figure(fig, show_legend=False)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📊 Station Summary")

        summary = station_avg.copy()
        summary[pollutant] = summary[pollutant].round(2)

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.warning("The dataset does not contain a station column.")

# ============================================================
# PAGE 5 - CORRELATION LAB
# ============================================================

elif page == "🔬 Correlation Lab":

    st.markdown("## 🔬 Correlation Lab")
    st.write("Examine relationships between pollutants and environmental variables.")

    correlation_columns = [
        c for c in POLLUTANTS + ENVIRONMENTAL
        if c in df.columns
    ]

    corr = df[correlation_columns].corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Environmental Correlation Matrix",
    )

    fig.update_traces(
        textfont=dict(color="black", size=11),
        hovertemplate="%{x} vs %{y}<br>Correlation: %{z:.2f}<extra></extra>",
    )

    style_figure(fig)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        <div class="info-card">
            <h3>🔎 How to read this matrix</h3>
            <p>
                Values closer to +1 indicate a stronger positive linear
                association, values closer to -1 indicate a stronger
                negative linear association, and values near 0 indicate
                a weaker linear association.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# PAGE 6 - AIR RISK SIMULATOR
# ============================================================

elif page == "🧪 Air Risk Simulator":

    st.markdown("## 🧪 Air Risk Simulator")
    st.write("Enter pollutant values to explore an educational air-risk scenario.")

    c1, c2, c3 = st.columns(3)

    with c1:
        pm25 = st.number_input(
            "PM2.5",
            min_value=0.0,
            value=50.0,
            step=1.0,
        )

    with c2:
        pm10 = st.number_input(
            "PM10",
            min_value=0.0,
            value=80.0,
            step=1.0,
        )

    with c3:
        no2 = st.number_input(
            "NO2",
            min_value=0.0,
            value=40.0,
            step=1.0,
        )

    score = (
        min(pm25 / 150.0, 1.0) * 50
        + min(pm10 / 250.0, 1.0) * 30
        + min(no2 / 200.0, 1.0) * 20
    )

    if score < 25:
        level = "Lower"
        message = "The entered scenario represents a relatively lower pollution level."
    elif score < 50:
        level = "Moderate"
        message = "The entered scenario represents a moderate pollution level."
    elif score < 75:
        level = "Elevated"
        message = "The entered scenario represents an elevated pollution level."
    else:
        level = "High"
        message = "The entered scenario represents a high pollution level."

    st.markdown(
        f"""
        <div class="info-card">
            <h2>Air-Risk Scenario: {level}</h2>
            <p><b>Scenario score:</b> {score:.1f} / 100</p>
            <p>{message}</p>
            <p>
                This simulator is an educational data-analysis feature,
                not a medical or regulatory air-quality classification.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(min(int(score), 100))

# ============================================================
# PAGE 7 - DATA QUALITY
# ============================================================

elif page == "📋 Data Quality":

    st.markdown("## 📋 Data Quality")
    st.write("Inspect the structure and completeness of the real-world dataset.")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Rows", f"{len(df):,}")

    with c2:
        st.metric("Columns", f"{len(df.columns):,}")

    with c3:
        missing_values = int(df.isna().sum().sum())
        st.metric("Missing Values", f"{missing_values:,}")

    quality = pd.DataFrame({
        "Column": df.columns,
        "Data Type": [str(df[c].dtype) for c in df.columns],
        "Missing Values": [int(df[c].isna().sum()) for c in df.columns],
        "Missing %": [
            round(float(df[c].isna().mean() * 100), 2)
            for c in df.columns
        ],
    })

    st.dataframe(
        quality,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown(
        """
        <div class="info-card">
            <h3>📌 Dataset Note</h3>
            <p>
                AirAware uses real-world multi-station urban air-quality
                observations. Missing values are retained where present
                in the source data, and charts use available numeric
                observations for each analysis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer-text">
        <p>🌿 <b>AirAware</b> - Urban Air Intelligence Platform</p>
        <p>Built with Python • Pandas • Plotly • Streamlit</p>
        <p>Real-world air-quality data analytics for smarter environmental insight.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
