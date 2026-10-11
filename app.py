import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dengue in Bangladesh", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv("data/dengue_clean.csv", parse_dates=["date"])
    df["division"] = df["division"].str.strip()
    df["month_num"] = df["date"].dt.month
    return df


df = load_data()

st.title("Dengue in Bangladesh (2020-2025)")
st.caption("Source: Mendeley Data, monthly division-level dengue dataset")

# ---------- Sidebar filters ----------
st.sidebar.header("Filters")
all_divisions = sorted(df["division"].unique())
divisions = st.sidebar.multiselect("Division", all_divisions, default=all_divisions)
year_min, year_max = int(df["year"].min()), int(df["year"].max())
years = st.sidebar.slider("Year range", year_min, year_max, (year_min, year_max))

filtered = df[df["division"].isin(divisions) & df["year"].between(years[0], years[1])]

if filtered.empty:
    st.warning("No data for this selection. Change the filters.")
    st.stop()

# ---------- KPI cards ----------
total_cases = int(filtered["infected"].sum())
total_deaths = int(filtered["death"].sum())
death_rate = total_deaths / total_cases * 100 if total_cases else 0

c1, c2, c3 = st.columns(3)
c1.metric("Total cases", f"{total_cases:,}")
c2.metric("Total deaths", f"{total_deaths:,}")
c3.metric("Death rate", f"{death_rate:.2f}%")

# ---------- Charts ----------
left, right = st.columns(2)

with left:
    st.subheader("Cases by division")
    by_div = filtered.groupby("division")["infected"].sum().sort_values(ascending=False)
    st.bar_chart(by_div)

with right:
    st.subheader("Death rate by division (%)")
    g = filtered.groupby("division")[["infected", "death"]].sum()
    rate = (g["death"] / g["infected"] * 100).round(2).sort_values(ascending=False)
    st.bar_chart(rate)

left, right = st.columns(2)

with left:
    st.subheader("Cases by month (1 = January)")
    by_month = filtered.groupby("month_num")["infected"].sum()
    st.bar_chart(by_month)

with right:
    st.subheader("Cases by year")
    by_year = filtered.groupby("year")["infected"].sum()
    st.line_chart(by_year)

# ---------- Climate ----------
st.subheader("Climate vs cases (correlation)")
cols = ["infected", "death", "temperature", "humidity", "pressure"]
st.dataframe(filtered[cols].corr().round(2))
st.caption("Correlation is not causation. Climate columns show only weak same-month correlation with cases.")

# ---------- Raw data ----------
with st.expander("Show data"):
    st.dataframe(filtered)