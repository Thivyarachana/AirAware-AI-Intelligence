
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# ============================================================
# AIR AWARE — URBAN AIR INTELLIGENCE PLATFORM
# ============================================================

st.set_page_config(
    page_title="AirAware | Urban Air Intelligence",
    page_icon="🌿",
    layout="wide"
)

# -----------------------------
# Custom styling
# -----------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #e8f5e9 0%,
        #f1f8f4 45%,
        #ffffff 100%
    );
}

.main-title {
    font-size: 3rem;
    font-weight: 800;
    color: #14532d;
    margin-bottom: 0;
}

.subtitle {
    font-size: 1.15rem;
    color: #3f5f4b;
    margin-top: 5px;
}

.section-title {
    color: #14532d;
    font-size: 1.8rem;
    font-weight: 750;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(20, 83, 45, 0.08);
    border: 1px solid #dcefe1;
    margin-bottom: 18px;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #dcefe1;
    box-shadow: 0 4px 15px rgba(20, 83, 45, 0.07);
}

.metric-value {
    font-size: 2rem;
    font-weight: 800;
    color: #166534;
}

.metric-label {
    color: #52705c;
    font-size: 0.9rem;
}

.warning-box {
    background: #fff8e1;
    border-left: 5px solid #f59e0b;
    padding: 15px;
    border-radius: 10px;
}

.info-box {
    background: #e8f5e9;
    border-left: 5px solid #22c55e;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

DATA_FILE = Path(__file__).parent / "data" / "air_quality.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_FILE)

    data["timestamp"] = pd.to_datetime(
        data["timestamp"],
        errors="coerce"
    )

    numeric_columns = [
        "PM2.5",
        "PM10",
        "SO2",
        "NO2",
        "CO",
        "O3",
        "TEMP",
        "PRES",
        "DEWP",
        "RAIN",
        "WSPM"
    ]

    for column in numeric_columns:
        if column in data.columns:
            data[column] = pd.to_numeric(
                data[column],
                errors="coerce"
            )

    return data


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <h2 style='color:#166534;'>🌿 AirAware</h2>
    <p style='color:#52705c;'>
    Urban Air Intelligence Platform
    </p>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Explore AirAware",
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

st.sidebar.info(
    "Real-world dataset: Beijing Multi-Site Air Quality "
    "(2013–2017)."
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    "<div class='main-title'>🌿 AirAware</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Urban Air Intelligence Platform — "
    "Explore pollution patterns, environmental drivers and "
    "air-risk scenarios.</div>",
    unsafe_allow_html=True
)

st.markdown("---")


# ============================================================
# MISSION CONTROL
# ============================================================

if page == "🌱 Mission Control":

    st.markdown(
        "<div class='section-title'>🌱 Mission Control</div>",
        unsafe_allow_html=True
    )

    st.write(
        "A real-world exploration of how air pollution changes "
        "across time, monitoring stations and environmental conditions."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Monitoring Stations",
            df["station"].nunique()
        )

    with col2:
        st.metric(
            "Observations",
            f"{len(df):,}"
        )

    with col3:
        st.metric(
            "Average PM2.5",
            f"{df['PM2.5'].mean():.1f}"
        )

    with col4:
        st.metric(
            "Pollutants Tracked",
            "6"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Daily trend
    daily = (
        df.groupby(
            pd.Grouper(key="timestamp", freq="D")
        )["PM2.5"]
        .mean()
        .reset_index()
    )

    fig = px.area(
        daily,
        x="timestamp",
        y="PM2.5",
        title="🌫️ Daily Average PM2.5"
    )

    fig.update_layout(
        template="plotly_white",
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Monthly profile
    monthly = (
        df.groupby("month")["PM2.5"]
        .mean()
        .reset_index()
    )

    fig2 = px.line(
        monthly,
        x="month",
        y="PM2.5",
        markers=True,
        title="📅 Average PM2.5 by Month"
    )

    fig2.update_layout(
        template="plotly_white",
        xaxis_title="Month",
        yaxis_title="PM2.5"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ============================================================
# POLLUTION PATTERNS
# ============================================================

elif page == "📈 Pollution Patterns":

    st.markdown(
        "<div class='section-title'>📈 Pollution Patterns</div>",
        unsafe_allow_html=True
    )

    pollutant = st.selectbox(
        "Select pollutant",
        [
            "PM2.5",
            "PM10",
            "SO2",
            "NO2",
            "CO",
            "O3"
        ]
    )

    station = st.selectbox(
        "Select monitoring station",
        ["All Stations"] + sorted(df["station"].dropna().unique())
    )

    filtered = df.copy()

    if station != "All Stations":
        filtered = filtered[
            filtered["station"] == station
        ]

    daily = (
        filtered.groupby(
            pd.Grouper(key="timestamp", freq="D")
        )[pollutant]
        .mean()
        .reset_index()
    )

    fig = px.line(
        daily,
        x="timestamp",
        y=pollutant,
        title=f"🌫️ Daily {pollutant} Trend"
    )

    fig.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        monthly = (
            filtered.groupby("month")[pollutant]
            .mean()
            .reset_index()
        )

        fig2 = px.bar(
            monthly,
            x="month",
            y=pollutant,
            title=f"📅 {pollutant} by Month"
        )

        fig2.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    with col2:

        hourly = (
            filtered.groupby("hour")[pollutant]
            .mean()
            .reset_index()
        )

        fig3 = px.line(
            hourly,
            x="hour",
            y=pollutant,
            markers=True,
            title=f"⏰ {pollutant} by Hour"
        )

        fig3.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )


# ============================================================
# WEATHER & POLLUTION
# ============================================================

elif page == "🌦️ Weather & Pollution":

    st.markdown(
        "<div class='section-title'>🌦️ Weather & Pollution</div>",
        unsafe_allow_html=True
    )

    pollutant = st.selectbox(
        "Pollutant",
        ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
    )

    weather_variable = st.selectbox(
        "Environmental variable",
        [
            "TEMP",
            "PRES",
            "DEWP",
            "RAIN",
            "WSPM"
        ]
    )

    sample = df[
        [weather_variable, pollutant]
    ].dropna()

    if len(sample) > 5000:
        sample = sample.sample(
            5000,
            random_state=42
        )

    fig = px.scatter(
        sample,
        x=weather_variable,
        y=pollutant,
        trendline="ols",
        opacity=0.45,
        title=f"🌦️ {weather_variable} vs {pollutant}"
    )

    fig.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    correlation = sample[
        [weather_variable, pollutant]
    ].corr().iloc[0, 1]

    st.metric(
        f"Correlation: {weather_variable} vs {pollutant}",
        f"{correlation:.3f}"
    )


# ============================================================
# STATION INTELLIGENCE
# ============================================================

elif page == "📍 Station Intelligence":

    st.markdown(
        "<div class='section-title'>📍 Station Intelligence</div>",
        unsafe_allow_html=True
    )

    station_summary = (
        df.groupby("station")
        .agg(
            Average_PM25=("PM2.5", "mean"),
            Average_PM10=("PM10", "mean"),
            Average_NO2=("NO2", "mean"),
            Observations=("PM2.5", "count")
        )
        .reset_index()
    )

    station_summary = station_summary.sort_values(
        "Average_PM25",
        ascending=False
    )

    st.dataframe(
        station_summary,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        station_summary,
        x="station",
        y="Average_PM25",
        title="📍 Average PM2.5 by Monitoring Station"
    )

    fig.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# CORRELATION LAB
# ============================================================

elif page == "🔬 Correlation Lab":

    st.markdown(
        "<div class='section-title'>🔬 Correlation Lab</div>",
        unsafe_allow_html=True
    )

    columns = [
        "PM2.5",
        "PM10",
        "SO2",
        "NO2",
        "CO",
        "O3",
        "TEMP",
        "PRES",
        "DEWP",
        "RAIN",
        "WSPM"
    ]

    correlation = df[columns].corr()

    fig = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto",
        title="🔬 Pollution & Environment Correlation Matrix"
    )

    fig.update_layout(
        template="plotly_white",
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info(
        "Correlation indicates statistical association, "
        "not causation."
    )


# ============================================================
# AIR RISK SIMULATOR
# ============================================================

elif page == "🧪 Air Risk Simulator":

    st.markdown(
        "<div class='section-title'>🧪 Air Risk Simulator</div>",
        unsafe_allow_html=True
    )

    st.write(
        "Enter environmental readings to explore a transparent "
        "screening score."
    )

    st.markdown(
        """
        <div class='warning-box'>
        ⚠️ This simulator is an educational analytical tool.
        It is <b>not an official AQI calculator</b>, regulatory
        measurement, medical assessment, or emergency warning system.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        pm25 = st.number_input(
            "PM2.5",
            min_value=0.0,
            max_value=1000.0,
            value=35.0
        )

        pm10 = st.number_input(
            "PM10",
            min_value=0.0,
            max_value=1000.0,
            value=50.0
        )

    with col2:

        no2 = st.number_input(
            "NO2",
            min_value=0.0,
            max_value=1000.0,
            value=30.0
        )

        o3 = st.number_input(
            "O3",
            min_value=0.0,
            max_value=1000.0,
            value=40.0
        )

    with col3:

        temperature = st.number_input(
            "Temperature °C",
            min_value=-30.0,
            max_value=60.0,
            value=20.0
        )

        wind = st.number_input(
            "Wind Speed",
            min_value=0.0,
            max_value=50.0,
            value=2.0
        )

    # Transparent screening formula
    pollution_component = (
        0.40 * min(pm25 / 150, 1) +
        0.20 * min(pm10 / 200, 1) +
        0.15 * min(no2 / 150, 1) +
        0.15 * min(o3 / 160, 1)
    )

    weather_component = 0.10 * (
        1 - min(wind / 8, 1)
    )

    score = 100 * (
        pollution_component +
        weather_component
    )

    score = max(0, min(score, 100))

    if score < 25:
        category = "Low"
    elif score < 50:
        category = "Moderate"
    elif score < 75:
        category = "High"
    else:
        category = "Very High"

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Screening Score",
            f"{score:.1f} / 100"
        )

    with c2:
        st.metric(
            "Risk Category",
            category
        )

    st.progress(
        int(score)
    )


# ============================================================
# DATA QUALITY
# ============================================================

elif page == "📋 Data Quality":

    st.markdown(
        "<div class='section-title'>📋 Data Quality</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Rows",
            f"{len(df):,}"
        )

    with col2:
        st.metric(
            "Columns",
            len(df.columns)
        )

    with col3:
        missing = int(df.isnull().sum().sum())

        st.metric(
            "Missing Values",
            f"{missing:,}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    missing_table = (
        df.isnull()
        .sum()
        .reset_index()
    )

    missing_table.columns = [
        "Column",
        "Missing Values"
    ]

    missing_table["Missing %"] = (
        missing_table["Missing Values"]
        / len(df)
        * 100
    ).round(2)

    st.dataframe(
        missing_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        """
        <div class='info-box'>
        <b>Dataset provenance:</b><br>
        Beijing Multi-Site Air Quality dataset,
        collected from multiple monitoring stations between
        March 2013 and February 2017.
        </div>
        """,
        unsafe_allow_html=True
    )
