
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# AIR AWARE — URBAN AIR INTELLIGENCE PLATFORM
# ============================================================

st.set_page_config(
    page_title="AirAware | Urban Air Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM LIGHT-GREEN UI
# ============================================================

st.markdown("""
<style>

    /* =====================================================
       AIR AWARE — LIGHT GREEN + WHITE CARD UI
       ALL TEXT BLACK
       ===================================================== */

    /* ---------- GLOBAL APP ---------- */

    .stApp {
        background: #EAF7EE !important;
        color: #000000 !important;
    }

    html, body {
        background: #EAF7EE !important;
        color: #000000 !important;
    }

    /* Force normal text to black */
    .stApp,
    .stApp p,
    .stApp span,
    .stApp div,
    .stApp label,
    .stApp li,
    .stApp small,
    .stMarkdown,
    .stMarkdown p,
    .stMarkdown span,
    .stMarkdown div,
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stText"],
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #000000 !important;
    }


    /* ---------- MAIN CONTENT ---------- */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }


    /* ---------- HERO SECTION ---------- */

    .hero {
        background: #FFFFFF !important;
        border: 2px solid #B7DCC0;
        border-radius: 24px;
        padding: 38px 42px;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(49, 104, 65, 0.10);
    }

    .hero h1 {
        color: #000000 !important;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .hero p {
        color: #000000 !important;
        font-size: 1.12rem;
        line-height: 1.7;
        margin-bottom: 0;
    }


    /* ---------- SECTION TITLES ---------- */

    .section-title {
        color: #000000 !important;
        font-size: 1.8rem;
        font-weight: 750;
        margin-top: 15px;
        margin-bottom: 8px;
    }

    .section-subtitle {
        color: #000000 !important;
        font-size: 1rem;
        margin-bottom: 18px;
    }


    /* ---------- WHITE ANALYSIS CARDS ---------- */

    .card {
        background: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #C9E2CE;
        border-radius: 18px;
        padding: 24px;
        margin: 12px 0;
        box-shadow: 0 5px 18px rgba(28, 75, 39, 0.08);
    }

    .card h1,
    .card h2,
    .card h3,
    .card h4,
    .card h5,
    .card h6,
    .card p,
    .card span,
    .card div {
        color: #000000 !important;
    }


    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background: #D8F0DE !important;
        border-right: 1px solid #B8DCC0;
    }

    section[data-testid="stSidebar"] * {
        color: #000000 !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: #000000 !important;
    }


    /* ---------- METRIC CARDS ---------- */

    div[data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid #C9E2CE;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 5px 18px rgba(28, 75, 39, 0.07);
    }

    div[data-testid="stMetric"] label {
        color: #000000 !important;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] {
        color: #000000 !important;
        font-weight: 800;
    }

    div[data-testid="stMetricDelta"] {
        color: #000000 !important;
    }


    /* ---------- BUTTONS ---------- */

    .stButton > button {
        background: #2E7D4F !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px;
        font-weight: 700;
        padding: 0.55rem 1.2rem;
    }

    .stButton > button p,
    .stButton > button span {
        color: #FFFFFF !important;
    }

    .stButton > button:hover {
        background: #245F3B !important;
        color: #FFFFFF !important;
    }


    /* ---------- INPUT BOXES ---------- */

    input,
    textarea {
        background: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #B8DCC0 !important;
    }

    input::placeholder,
    textarea::placeholder {
        color: #555555 !important;
    }


    /* ---------- SELECTBOX / DROPDOWN ---------- */

    [data-baseweb="select"] {
        background: #FFFFFF !important;
        color: #000000 !important;
    }

    [data-baseweb="select"] * {
        color: #000000 !important;
    }

    [data-baseweb="select"] > div {
        background: #FFFFFF !important;
        color: #000000 !important;
        border-color: #B8DCC0 !important;
    }


    /* ---------- MULTISELECT ---------- */

    [data-baseweb="tag"] {
        background: #D8F0DE !important;
        color: #000000 !important;
    }

    [data-baseweb="tag"] span {
        color: #000000 !important;
    }


    /* ---------- NUMBER INPUT ---------- */

    div[data-testid="stNumberInput"] input {
        background: #FFFFFF !important;
        color: #000000 !important;
    }


    /* ---------- RADIO BUTTONS ---------- */

    div[data-testid="stRadio"] label {
        color: #000000 !important;
    }

    div[data-testid="stRadio"] label span {
        color: #000000 !important;
    }


    /* ---------- CHECKBOX ---------- */

    div[data-testid="stCheckbox"] label {
        color: #000000 !important;
    }


    /* ---------- TABS ---------- */

    button[data-baseweb="tab"] {
        color: #000000 !important;
        font-weight: 650;
    }

    button[data-baseweb="tab"] p,
    button[data-baseweb="tab"] span {
        color: #000000 !important;
    }


    /* ---------- DATAFRAME ---------- */

    div[data-testid="stDataFrame"] {
        background: #FFFFFF !important;
        border-radius: 14px;
    }


    /* ---------- ALERTS ---------- */

    .stAlert {
        color: #000000 !important;
        border-radius: 12px;
    }

    .stAlert p,
    .stAlert span,
    .stAlert div {
        color: #000000 !important;
    }


    /* ---------- EXPANDERS ---------- */

    div[data-testid="stExpander"] {
        background: #FFFFFF !important;
        border: 1px solid #C9E2CE !important;
        border-radius: 14px;
    }

    div[data-testid="stExpander"] * {
        color: #000000 !important;
    }


    /* ---------- SLIDER ---------- */

    div[data-testid="stSlider"] label {
        color: #000000 !important;
    }


    /* ---------- FILE UPLOADER ---------- */

    div[data-testid="stFileUploader"] {
        background: #FFFFFF !important;
        border-radius: 14px;
    }

    div[data-testid="stFileUploader"] * {
        color: #000000 !important;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        padding: 30px 10px 10px;
        color: #000000 !important;
        font-size: 0.9rem;
    }

    .footer p,
    .footer span,
    .footer div,
    .footer b {
        color: #000000 !important;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

DATA_PATH = "data/air_quality.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Convert numeric columns where possible
    numeric_candidates = [
        "PM2.5", "PM10", "SO2", "NO2", "CO", "O3",
        "TEMP", "PRES", "DEWP", "RAIN", "WSPM"
    ]

    for col in numeric_candidates:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


try:
    df = load_data()
except Exception as e:
    st.error("Unable to load the air-quality dataset.")
    st.code(str(e))
    st.stop()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def available_columns(columns):
    return [c for c in columns if c in df.columns]


pollutants = available_columns(
    ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
)

weather_cols = available_columns(
    ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
)


def risk_level(pm25):
    if pm25 < 35:
        return "Low"
    elif pm25 < 75:
        return "Moderate"
    elif pm25 < 150:
        return "High"
    else:
        return "Very High"


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:15px 5px 20px;">
        <div style="font-size:3rem;">🌿</div>
        <h2 style="color:#123B20 !important; margin-bottom:2px;">
            AirAware
        </h2>
        <p style="color:#333333 !important;">
            Urban Air Intelligence
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Explore the platform",
    [
        "🌱 Mission Control",
        "📈 Pollution Patterns",
        "🌦️ Weather & Pollution",
        "📍 Station Intelligence",
        "🔬 Correlation Lab",
        "🧪 Air Risk Simulator",
        "📋 Data Quality"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div class="card" style="padding:16px;">
        <h3>🌍 Project Vision</h3>
        <p>
        AirAware transforms real-world environmental data into
        understandable insights about urban air quality.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <h1>🌿 AirAware</h1>
        <p>
            <b>Urban Air Intelligence Platform</b><br>
            Explore pollution patterns, environmental relationships,
            monitoring-station behavior and air-risk scenarios using
            real-world air-quality observations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MISSION CONTROL
# ============================================================

if page == "🌱 Mission Control":

    st.markdown(
        '<div class="section-title">🌱 Mission Control</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">A high-level view of the urban air-quality dataset.</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📊 Observations", f"{len(df):,}")

    with c2:
        if "station" in df.columns:
            st.metric("📍 Monitoring Stations", df["station"].nunique())
        else:
            st.metric("📍 Monitoring Stations", "N/A")

    with c3:
        st.metric("🧪 Pollutants Tracked", len(pollutants))

    with c4:
        if "timestamp" in df.columns:
            days = df["timestamp"].dt.date.nunique()
            st.metric("📅 Days Observed", f"{days:,}")
        else:
            st.metric("📅 Days Observed", "N/A")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h3>🌍 Why AirAware?</h3>
                <p>
                Air pollution changes across time, locations and
                environmental conditions. AirAware provides an interactive
                way to investigate these patterns rather than looking at
                isolated pollutant measurements.
                </p>
                <p>
                The platform can help students, analysts, researchers and
                future smart-city systems understand how pollution behaves.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3>🚀 Future-Ready Direction</h3>
                <p>
                AirAware can evolve from historical analysis into a
                real-time environmental intelligence system.
                </p>
                <p>
                Future extensions could include live sensor feeds,
                machine-learning forecasting, anomaly detection,
                personalized alerts and city-level pollution maps.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    if "timestamp" in df.columns and pollutants:

        daily = (
            df.set_index("timestamp")[pollutants]
            .resample("D")
            .mean()
            .reset_index()
        )

        selected_pollutant = st.selectbox(
            "Choose a pollutant for the trend",
            pollutants
        )

        fig = px.line(
            daily,
            x="timestamp",
            y=selected_pollutant,
            title=f"Daily Average {selected_pollutant}"
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#111111"),
            title_font=dict(color="#123B20", size=18),
            hovermode="x unified"
        )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# POLLUTION PATTERNS
# ============================================================

elif page == "📈 Pollution Patterns":

    st.markdown(
        '<div class="section-title">📈 Pollution Patterns</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Discover how pollutant concentrations change over time.</div>',
        unsafe_allow_html=True
    )

    if "timestamp" in df.columns and pollutants:

        pollutant = st.selectbox(
            "Select pollutant",
            pollutants
        )

        trend = (
            df.set_index("timestamp")[pollutant]
            .resample("D")
            .mean()
            .reset_index()
        )

        fig = px.line(
            trend,
            x="timestamp",
            y=pollutant,
            title=f"{pollutant} — Daily Pollution Trend"
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#111111"),
            title_font=dict(color="#123B20"),
            xaxis_title="Date",
            yaxis_title=pollutant
        )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Average",
                f"{df[pollutant].mean():.2f}"
            )

        with c2:
            st.metric(
                "Maximum",
                f"{df[pollutant].max():.2f}"
            )

        with c3:
            st.metric(
                "Minimum",
                f"{df[pollutant].min():.2f}"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if "hour" in df.columns:

            hourly = df.groupby("hour")[pollutant].mean().reset_index()

            fig2 = px.line(
                hourly,
                x="hour",
                y=pollutant,
                markers=True,
                title=f"Average {pollutant} by Hour"
            )

            fig2.update_layout(
                template="simple_white",
                paper_bgcolor="white",
                plot_bgcolor="white",
                font=dict(color="#111111"),
                title_font=dict(color="#123B20"),
                xaxis_title="Hour of Day",
                yaxis_title=f"Average {pollutant}"
            )

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# WEATHER & POLLUTION
# ============================================================

elif page == "🌦️ Weather & Pollution":

    st.markdown(
        '<div class="section-title">🌦️ Weather & Pollution</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Explore relationships between atmospheric conditions and pollution.</div>',
        unsafe_allow_html=True
    )

    if not weather_cols or not pollutants:
        st.warning("Weather or pollutant columns are unavailable.")
    else:

        weather = st.selectbox(
            "Select environmental factor",
            weather_cols
        )

        pollutant = st.selectbox(
            "Select pollutant",
            pollutants
        )

        plot_df = df[[weather, pollutant]].dropna()

        fig = px.scatter(
            plot_df.sample(min(10000, len(plot_df)), random_state=42),
            x=weather,
            y=pollutant,
            trendline="ols",
            opacity=0.55,
            title=f"{pollutant} vs {weather}"
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#111111"),
            title_font=dict(color="#123B20")
        )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        correlation = plot_df[weather].corr(plot_df[pollutant])

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(
            f"""
            <h3>🔎 Observed Relationship</h3>
            <p>
            The correlation between <b>{weather}</b> and
            <b>{pollutant}</b> in the selected observations is:
            </p>
            <h2 style="color:#2E7D4F !important;">
            {correlation:.3f}
            </h2>
            <p>
            Correlation indicates statistical association, not causation.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# STATION INTELLIGENCE
# ============================================================

elif page == "📍 Station Intelligence":

    st.markdown(
        '<div class="section-title">📍 Station Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Compare pollution behavior across monitoring stations.</div>',
        unsafe_allow_html=True
    )

    if "station" not in df.columns:
        st.warning("Station information is unavailable.")
    else:

        pollutant = st.selectbox(
            "Select pollutant",
            pollutants
        )

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
            title=f"Average {pollutant} by Monitoring Station"
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="#111111"),
            title_font=dict(color="#123B20"),
            xaxis_title="Monitoring Station",
            yaxis_title=f"Average {pollutant}"
        )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown("### 📊 Station Summary")

        summary = (
            df.groupby("station")[pollutants]
            .mean()
            .round(2)
        )

        st.dataframe(
            summary,
            use_container_width=True
        )

        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# CORRELATION LAB
# ============================================================

elif page == "🔬 Correlation Lab":

    st.markdown(
        '<div class="section-title">🔬 Correlation Lab</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Investigate relationships between pollutants and environmental variables.</div>',
        unsafe_allow_html=True
    )

    correlation_cols = pollutants + weather_cols

    corr = df[correlation_cols].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Environmental Correlation Matrix"
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="#111111"),
        title_font=dict(color="#123B20")
    )

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
            <h3>🧠 How to read this</h3>
            <p>
            Values closer to <b>+1</b> indicate a stronger positive
            association, while values closer to <b>-1</b> indicate a
            stronger negative association.
            </p>
            <p>
            A value near <b>0</b> indicates a weaker linear association.
            Correlation alone does not establish cause and effect.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# AIR RISK SIMULATOR
# ============================================================

elif page == "🧪 Air Risk Simulator":

    st.markdown(
        '<div class="section-title">🧪 Air Risk Simulator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Enter pollutant values to explore a simple educational risk scenario.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <h3>🌱 Try Your Own Scenario</h3>
            <p>
            Enter approximate pollutant concentrations and AirAware will
            classify the PM2.5 scenario into a simple educational risk level.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        pm25 = st.number_input(
            "PM2.5",
            min_value=0.0,
            max_value=1000.0,
            value=35.0,
            step=1.0
        )

    with col2:
        pm10 = st.number_input(
            "PM10",
            min_value=0.0,
            max_value=1500.0,
            value=50.0,
            step=1.0
        )

    with col3:
        no2 = st.number_input(
            "NO2",
            min_value=0.0,
            max_value=500.0,
            value=20.0,
            step=1.0
        )

    level = risk_level(pm25)

    if level == "Low":
        message = "The entered PM2.5 value falls into the lower-risk scenario range."
    elif level == "Moderate":
        message = "The entered PM2.5 value represents a moderate pollution scenario."
    elif level == "High":
        message = "The entered PM2.5 value represents a high pollution scenario."
    else:
        message = "The entered PM2.5 value represents a very high pollution scenario."

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="card" style="text-align:center;">
            <div style="font-size:3rem;">🌿</div>
            <h2 style="color:#123B20 !important;">
                {level} Risk Scenario
            </h2>
            <p>{message}</p>
            <hr>
            <p>
                <b>PM2.5:</b> {pm25:.1f}
                &nbsp;&nbsp; | &nbsp;&nbsp;
                <b>PM10:</b> {pm10:.1f}
                &nbsp;&nbsp; | &nbsp;&nbsp;
                <b>NO2:</b> {no2:.1f}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "Educational simulator only. This is not an official AQI calculator, "
        "medical assessment or regulatory air-quality warning system."
    )


# ============================================================
# DATA QUALITY
# ============================================================

elif page == "📋 Data Quality":

    st.markdown(
        '<div class="section-title">📋 Data Quality</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Understand the structure and completeness of the dataset.</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Rows", f"{len(df):,}")

    with c2:
        st.metric("Columns", len(df.columns))

    with c3:
        missing_pct = df.isna().mean().mean() * 100
        st.metric("Overall Missingness", f"{missing_pct:.2f}%")

    st.markdown("<br>", unsafe_allow_html=True)

    missing = (
        df.isna()
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    missing.columns = ["Column", "Missing Values"]

    missing["Missing %"] = (
        missing["Missing Values"] / len(df) * 100
    ).round(2)

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown("### 🔍 Missing-Value Analysis")

    st.dataframe(
        missing,
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown("### 👀 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🌿 <b>AirAware — Urban Air Intelligence Platform</b><br>
        Built with Python, Pandas, Plotly and Streamlit<br>
        Real-world environmental data • Exploratory Data Analysis • Interactive Analytics
    </div>
    """,
    unsafe_allow_html=True
)
