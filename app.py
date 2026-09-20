import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AirAware | Urban Air Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* =====================================================
       AIR AWARE — LIGHT GREEN + WHITE CARD UI
       ALL TEXT BLACK
       ===================================================== */

    .stApp {
        background: #EAF7EE !important;
        color: #000000 !important;
    }

    html, body {
        background: #EAF7EE !important;
        color: #000000 !important;
    }

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
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1450px;
    }

    /* ---------- HERO ---------- */

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

    /* ---------- WHITE CARDS ---------- */

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

    /* ---------- INPUTS ---------- */

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

    /* ---------- SELECTBOX ---------- */

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

    /* ---------- RADIO ---------- */

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
# DATA PATH
# ============================================================

DATA_PATH = "data/air_quality.csv"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)

    # Convert timestamp
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            errors="coerce"
        )

    # Convert numeric columns
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
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # Create time features if missing
    if "timestamp" in df.columns:

        if "hour" not in df.columns:
            df["hour"] = df["timestamp"].dt.hour

        if "month" not in df.columns:
            df["month"] = df["timestamp"].dt.month

        if "year" not in df.columns:
            df["year"] = df["timestamp"].dt.year

        if "day_name" not in df.columns:
            df["day_name"] = df["timestamp"].dt.day_name()

        if "season" not in df.columns:
            df["season"] = df["month"].map({
                12: "Winter",
                1: "Winter",
                2: "Winter",
                3: "Spring",
                4: "Spring",
                5: "Spring",
                6: "Summer",
                7: "Summer",
                8: "Summer",
                9: "Autumn",
                10: "Autumn",
                11: "Autumn"
            })

    return df


# ============================================================
# LOAD DATA SAFELY
# ============================================================

try:

    df = load_data()

except Exception as e:

    st.error(
        "Unable to load the dataset. "
        "Please make sure data/air_quality.csv exists in the GitHub repository."
    )

    st.code(str(e))

    st.stop()


# ============================================================
# AVAILABLE POLLUTANTS
# ============================================================

pollutants = [
    column
    for column in [
        "PM2.5",
        "PM10",
        "SO2",
        "NO2",
        "CO",
        "O3"
    ]
    if column in df.columns
]


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <h2>🌿 AirAware</h2>
    <p>
    Urban Air Intelligence Platform
    </p>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
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

if pollutants:

    selected_pollutant = st.sidebar.selectbox(
        "Select Pollutant",
        pollutants,
        index=0
    )

else:

    selected_pollutant = None

st.sidebar.markdown(
    """
    <div class="card">
        <b>Dataset</b><br>
        Real-world Beijing multi-site air-quality observations.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">

        <h1>🌿 AirAware</h1>

        <p>
        <b>Urban Air Intelligence Platform</b><br>
        Explore real-world pollution patterns, environmental
        relationships, monitoring-station behavior and air-risk
        scenarios through interactive data analytics.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE 1 — MISSION CONTROL
# ============================================================

if page == "🌱 Mission Control":

    st.markdown(
        '<div class="section-title">🌱 Mission Control</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
        A high-level view of the urban air-quality environment.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- METRICS ----------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Records",
            f"{len(df):,}"
        )

    with col2:

        if "station" in df.columns:
            st.metric(
                "Monitoring Stations",
                f"{df['station'].nunique():,}"
            )

    with col3:

        if "timestamp" in df.columns:

            start_date = df["timestamp"].min()

            st.metric(
                "Data Start",
                start_date.strftime("%b %Y")
                if pd.notna(start_date)
                else "N/A"
            )

    with col4:

        if "timestamp" in df.columns:

            end_date = df["timestamp"].max()

            st.metric(
                "Data End",
                end_date.strftime("%b %Y")
                if pd.notna(end_date)
                else "N/A"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- DAILY TREND ----------------

    if selected_pollutant and "timestamp" in df.columns:

        daily = (
            df.groupby(
                df["timestamp"].dt.date
            )[selected_pollutant]
            .mean()
            .reset_index()
        )

        daily.columns = [
            "date",
            selected_pollutant
        ]

        daily["date"] = pd.to_datetime(
            daily["date"]
        )

        fig = px.line(
            daily,
            x="date",
            y=selected_pollutant,
            title=f"Daily Average {selected_pollutant}"
        )

        fig.update_traces(
            mode="lines+markers",
            marker=dict(size=5),
            hovertemplate=(
                "Date: %{x}<br>"
                f"{selected_pollutant}: %{{y:.2f}}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="black"),
            title_font=dict(
                color="black",
                size=18
            ),
            xaxis=dict(
                title="Date",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            ),
            yaxis=dict(
                title=selected_pollutant,
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ---------------- INSIGHT ----------------

    if selected_pollutant:

        average_value = df[selected_pollutant].mean()

        st.markdown(
            f"""
            <div class="card">

            <h3>💡 Air Quality Insight</h3>

            <p>
            The average recorded <b>{selected_pollutant}</b>
            concentration in the available dataset is
            <b>{average_value:.2f}</b>.
            </p>

            <p>
            AirAware transforms historical observations into
            interactive intelligence that can support future
            real-time environmental monitoring systems.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# PAGE 2 — POLLUTION PATTERNS
# ============================================================

elif page == "📈 Pollution Patterns":

    st.markdown(
        '<div class="section-title">📈 Pollution Patterns</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
        Discover how pollution changes across time and hours of the day.
        </div>
        """,
        unsafe_allow_html=True
    )

    if selected_pollutant and "timestamp" in df.columns:

        # ---------------- DAILY ----------------

        trend = (
            df.groupby(
                df["timestamp"].dt.date
            )[selected_pollutant]
            .mean()
            .reset_index()
        )

        trend.columns = [
            "timestamp",
            selected_pollutant
        ]

        trend["timestamp"] = pd.to_datetime(
            trend["timestamp"]
        )

        fig = px.line(
            trend,
            x="timestamp",
            y=selected_pollutant,
            title=f"{selected_pollutant} — Daily Pollution Trend"
        )

        fig.update_traces(
            mode="lines+markers",
            marker=dict(size=5),
            hovertemplate=(
                "Date: %{x}<br>"
                f"{selected_pollutant}: %{{y:.2f}}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="black"),
            title_font=dict(
                color="black",
                size=18
            ),
            xaxis=dict(
                title="Date",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            ),
            yaxis=dict(
                title=selected_pollutant,
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ---------------- HOURLY ----------------

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
            title=f"Average {selected_pollutant} by Hour"
        )

        fig2.update_traces(
            mode="lines+markers+text",
            text=hourly[selected_pollutant].round(2),
            textposition="top center",
            textfont=dict(
                color="black",
                size=11
            ),
            hovertemplate=(
                "Hour: %{x}<br>"
                f"{selected_pollutant}: %{{y:.2f}}"
                "<extra></extra>"
            )
        )

        fig2.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="black"),
            title_font=dict(
                color="black",
                size=18
            ),
            xaxis=dict(
                title="Hour of Day",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            ),
            yaxis=dict(
                title=f"Average {selected_pollutant}",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            )
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        # ---------------- MONTHLY ----------------

        monthly = (
            df.groupby(
                ["year", "month"]
            )[selected_pollutant]
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
            title=f"Average {selected_pollutant} by Month",
            text=selected_pollutant
        )

        fig3.update_traces(
            texttemplate="%{text:.2f}",
            textposition="outside",
            textfont=dict(
                color="black",
                size=11
            ),
            cliponaxis=False
        )

        fig3.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="black"),
            title_font=dict(
                color="black",
                size=18
            ),
            xaxis=dict(
                title="Month",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            ),
            yaxis=dict(
                title=f"Average {selected_pollutant}",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            )
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )


# ============================================================
# PAGE 3 — WEATHER & POLLUTION
# ============================================================

elif page == "🌦️ Weather & Pollution":

    st.markdown(
        '<div class="section-title">🌦️ Weather & Pollution</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
        Explore relationships between environmental conditions
        and pollutant concentrations.
        </div>
        """,
        unsafe_allow_html=True
    )

    weather_variables = [
        column
        for column in [
            "TEMP",
            "PRES",
            "DEWP",
            "RAIN",
            "WSPM"
        ]
        if column in df.columns
    ]

    if weather_variables and selected_pollutant:

        weather = st.selectbox(
            "Select Environmental Variable",
            weather_variables
        )

        plot_df = df[
            [weather, selected_pollutant]
        ].dropna()

        scatter_data = plot_df.sample(
            min(10000, len(plot_df)),
            random_state=42
        )

        fig = px.scatter(
            scatter_data,
            x=weather,
            y=selected_pollutant,
            trendline="ols",
            opacity=0.55,
            title=f"{selected_pollutant} vs {weather}"
        )

        fig.update_traces(
            marker=dict(size=7),
            hovertemplate=(
                f"{weather}: %{{x:.2f}}"
                f"<br>{selected_pollutant}: %{{y:.2f}}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="black"),
            title_font=dict(
                color="black",
                size=18
            ),
            xaxis=dict(
                title=weather,
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            ),
            yaxis=dict(
                title=selected_pollutant,
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ---------------- WEATHER SUMMARY ----------------

        st.markdown(
            """
            <div class="card">

            <h3>🌦️ Environmental Context</h3>

            <p>
            Weather conditions can influence pollutant dispersion,
            accumulation and atmospheric behavior.
            </p>

            <p>
            This visualization helps identify potential relationships
            between environmental conditions and air pollution.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# PAGE 4 — STATION INTELLIGENCE
# ============================================================

elif page == "📍 Station Intelligence":

    st.markdown(
        '<div class="section-title">📍 Station Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
        Compare pollution levels across monitoring stations.
        </div>
        """,
        unsafe_allow_html=True
    )

    if (
        "station" in df.columns
        and selected_pollutant
    ):

        station_avg = (
            df.groupby("station")[selected_pollutant]
            .mean()
            .reset_index()
            .sort_values(
                selected_pollutant,
                ascending=False
            )
        )

        # ---------------- BAR CHART ----------------

        fig = px.bar(
            station_avg,
            x="station",
            y=selected_pollutant,
            title=f"Average {selected_pollutant} by Monitoring Station",
            text=selected_pollutant
        )

        fig.update_traces(
            texttemplate="%{text:.2f}",
            textposition="outside",
            textfont=dict(
                color="black",
                size=13
            ),
            cliponaxis=False,
            hovertemplate=(
                "Station: %{x}<br>"
                f"Average {selected_pollutant}: %{{y:.2f}}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            template="simple_white",
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color="black"),
            title_font=dict(
                color="black",
                size=18
            ),
            xaxis=dict(
                title="Monitoring Station",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            ),
            yaxis=dict(
                title=f"Average {selected_pollutant}",
                title_font=dict(color="black"),
                tickfont=dict(color="black")
            ),
            uniformtext_minsize=9,
            uniformtext_mode="hide"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ---------------- TOP STATION ----------------

        top_station = station_avg.iloc[0]

        st.markdown(
            f"""
            <div class="card">

            <h3>📍 Station Insight</h3>

            <p>
            The station with the highest average
            <b>{selected_pollutant}</b> in the available dataset is
            <b>{top_station["station"]}</b>.
            </p>

            <p>
            Recorded average:
            <b>{top_station[selected_pollutant]:.2f}</b>
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------- STATION TABLE ----------------

        st.markdown(
            "### 📊 Station Comparison"
        )

        display_station = station_avg.copy()

        display_station[selected_pollutant] = (
            display_station[selected_pollutant]
            .round(2)
        )

        st.dataframe(
            display_station,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# PAGE 5 — CORRELATION LAB
# ============================================================

elif page == "🔬 Correlation Lab":

    st.markdown(
        '<div class="section-title">🔬 Correlation Lab</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
        Examine relationships between pollutants and environmental variables.
        </div>
        """,
        unsafe_allow_html=True
    )

    correlation_columns = [
        column
        for column in [
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
        if column in df.columns
    ]

    corr = df[correlation_columns].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Environmental Correlation Matrix"
    )

    fig.update_traces(
        textfont=dict(
            color="black",
            size=11
        )
    )

    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="black"),
        title_font=dict(
            color="black",
            size=18
        ),
        xaxis=dict(
            title="Variables",
            title_font=dict(color="black"),
            tickfont=dict(color="black")
        ),
        yaxis=dict(
            title="Variables",
            title_font=dict(color="black"),
            tickfont=dict(color="black")
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        """
        <div class="card">

        <h3>🔎 How to read this matrix</h3>

        <p>
        Correlation values closer to <b>+1</b> indicate a strong
        positive relationship, while values closer to <b>-1</b>
        indicate a strong negative relationship.
        </p>

        <p>
        Values close to <b>0</b> indicate a weaker linear relationship.
        Correlation does not by itself prove causation.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PAGE 6 — AIR RISK SIMULATOR
# ============================================================

elif page == "🧪 Air Risk Simulator":

    st.markdown(
        '<div class="section-title">🧪 Air Risk Simulator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
        Enter pollutant observations to explore a simple
        educational air-risk scenario.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        pm25_input = st.number_input(
            "PM2.5",
            min_value=0.0,
            value=35.0,
            step=1.0
        )

    with col2:

        pm10_input = st.number_input(
            "PM10",
            min_value=0.0,
            value=50.0,
            step=1.0
        )

    with col3:

        no2_input = st.number_input(
            "NO2",
            min_value=0.0,
            value=40.0,
            step=1.0
        )

    # ---------------- RISK LOGIC ----------------

    risk_score = (
        (pm25_input / 35)
        + (pm10_input / 50)
        + (no2_input / 40)
    ) / 3

    if risk_score < 0.8:

        risk_level = "Low"

        explanation = (
            "The entered values represent a relatively lower "
            "pollution scenario based on this simple educational model."
        )

    elif risk_score < 1.5:

        risk_level = "Moderate"

        explanation = (
            "The entered values represent a moderate pollution "
            "scenario. Monitoring trends can provide additional context."
        )

    elif risk_score < 2.5:

        risk_level = "High"

        explanation = (
            "The entered values represent a higher pollution scenario "
            "under this simplified model."
        )

    else:

        risk_level = "Very High"

        explanation = (
            "The entered values represent a very high pollution "
            "scenario under this simplified model."
        )

    st.markdown(
        f"""
        <div class="card">

        <h2>🌿 Estimated Scenario: {risk_level}</h2>

        <p>
        {explanation}
        </p>

        <p>
        <b>Important:</b> This simulator is an educational
        data-analytics feature and is not a medical or regulatory
        air-quality warning system.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- INPUT SUMMARY ----------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "PM2.5",
            f"{pm25_input:.1f}"
        )

    with col2:

        st.metric(
            "PM10",
            f"{pm10_input:.1f}"
        )

    with col3:

        st.metric(
            "NO2",
            f"{no2_input:.1f}"
        )


# ============================================================
# PAGE 7 — DATA QUALITY
# ============================================================

elif page == "📋 Data Quality":

    st.markdown(
        '<div class="section-title">📋 Data Quality</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-subtitle">
        Understand the structure and completeness of the dataset.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- DATASET METRICS ----------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Rows",
            f"{df.shape[0]:,}"
        )

    with col2:

        st.metric(
            "Columns",
            f"{df.shape[1]:,}"
        )

    with col3:

        missing_values = int(
            df.isna().sum().sum()
        )

        st.metric(
            "Missing Values",
            f"{missing_values:,}"
        )

    with col4:

        memory_mb = (
            df.memory_usage(deep=True)
            .sum()
            / (1024 ** 2)
        )

        st.metric(
            "Memory Usage",
            f"{memory_mb:.2f} MB"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- MISSING VALUE TABLE ----------------

    st.markdown(
        "### 🔍 Missing Values by Column"
    )

    missing_df = (
        df.isna()
        .sum()
        .reset_index()
    )

    missing_df.columns = [
        "Column",
        "Missing Values"
    ]

    missing_df["Missing %"] = (
        missing_df["Missing Values"]
        / len(df)
        * 100
    ).round(2)

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True
    )

    # ---------------- DATA PREVIEW ----------------

    st.markdown(
        "### 👀 Dataset Preview"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <p>
        🌿 <b>AirAware</b> — Urban Air Intelligence Platform
        </p>

        <p>
        Built with Python • Pandas • Plotly • Streamlit
        </p>

        <p>
        Real-world air-quality data analytics for
        smarter environmental insight.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)
