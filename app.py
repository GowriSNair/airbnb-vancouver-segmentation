import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── PAGE CONFIG ───────────────────────────────────────────
st.set_page_config(
    page_title="Airbnb Vancouver Dashboard",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CUSTOM CSS ────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .block-container { padding-top: 1.5rem; }
    .metric-card {
        background: #1e2130;
        border-radius: 12px;
        padding: 20px 24px;
        border-left: 4px solid;
        margin-bottom: 8px;
    }
    .metric-value { font-size: 2rem; font-weight: 700; color: #fff; }
    .metric-label { font-size: 0.85rem; color: #aaa; margin-top: 4px; }
    div[data-testid="stSidebar"] { background-color: #161929; }
</style>
""", unsafe_allow_html=True)

CLUSTER_COLORS = {
    '🟣 Budget':    '#9b59b6',
    '🔵 Mid-Range': '#3498db',
    '🟢 Premium':   '#2ecc71',
    '🟡 Long-Term': '#f1c40f',
}
SENTIMENT_COLORS = {
    'Positive': '#2ecc71',
    'Neutral':  '#95a5a6',
    'Negative': '#e74c3c',
}

# ── DATA LOADING ──────────────────────────────────────────
@st.cache_data
def load_data():
    listings = pd.read_csv('listings_processed.csv')
    reviews  = pd.read_csv('reviews_processed.csv')
    reviews['date'] = pd.to_datetime(reviews['date'], errors='coerce')
    reviews['year'] = reviews['date'].dt.year
    return listings, reviews

listings, reviews = load_data()

# ── SIDEBAR FILTERS ───────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏙️ Airbnb Vancouver")
    st.markdown("*Market Segmentation Dashboard*")
    st.divider()

    st.markdown("### 🔍 Filters")

    room_types = ['All'] + sorted(listings['room_type'].dropna().unique().tolist())
    selected_room = st.selectbox("Room Type", room_types)

    neighbourhoods = ['All'] + sorted(listings['neighbourhood'].dropna().unique().tolist())
    selected_neighbourhood = st.selectbox("Neighbourhood", neighbourhoods)

    clusters = ['All'] + sorted(listings['cluster_name'].dropna().unique().tolist())
    selected_cluster = st.selectbox("Market Segment", clusters)

    price_max = int(listings['price'].quantile(0.99))
    price_range = st.slider("Price Range ($/night)", 0, price_max, (0, price_max))

    st.divider()
    st.markdown("### 📊 Dataset")
    st.markdown(f"**{len(listings):,}** listings")
    st.markdown(f"**{len(reviews):,}** reviews")
    st.markdown("*Source: Inside Airbnb — Vancouver*")

# ── FILTER DATA ───────────────────────────────────────────
df = listings.copy()
if selected_room != 'All':        df = df[df['room_type'] == selected_room]
if selected_neighbourhood != 'All': df = df[df['neighbourhood'] == selected_neighbourhood]
if selected_cluster != 'All':     df = df[df['cluster_name'] == selected_cluster]
df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

rv = reviews.copy()
if selected_cluster != 'All':
    rv = rv[rv['cluster_name'] == selected_cluster]

# ── HEADER ────────────────────────────────────────────────
st.markdown("# 🏙️ Airbnb Vancouver — Market Segmentation Dashboard")
st.markdown("Interactive analysis of **pricing, market segments, and guest sentiment** across Vancouver's short-term rental market.")
st.divider()

# ── KPI METRICS ───────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"""
    <div class="metric-card" style="border-color:#3498db">
        <div class="metric-value">{len(df):,}</div>
        <div class="metric-label">📋 Active Listings</div>
    </div>""", unsafe_allow_html=True)

with k2:
    avg_price = df['price'].median()
    st.markdown(f"""
    <div class="metric-card" style="border-color:#2ecc71">
        <div class="metric-value">${avg_price:.0f}</div>
        <div class="metric-label">💰 Median Price/Night</div>
    </div>""", unsafe_allow_html=True)

with k3:
    avg_reviews = df['number_of_reviews'].mean()
    st.markdown(f"""
    <div class="metric-card" style="border-color:#9b59b6">
        <div class="metric-value">{avg_reviews:.0f}</div>
        <div class="metric-label">⭐ Avg Reviews/Listing</div>
    </div>""", unsafe_allow_html=True)

with k4:
    avg_avail = df['availability_365'].mean()
    st.markdown(f"""
    <div class="metric-card" style="border-color:#f1c40f">
        <div class="metric-value">{avg_avail:.0f}</div>
        <div class="metric-label">📅 Avg Availability (days)</div>
    </div>""", unsafe_allow_html=True)

with k5:
    pos_pct = (rv['sentiment'] == 'Positive').mean() * 100 if len(rv) > 0 else 0
    st.markdown(f"""
    <div class="metric-card" style="border-color:#e74c3c">
        <div class="metric-value">{pos_pct:.0f}%</div>
        <div class="metric-label">😊 Positive Sentiment</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")

# ── ROW 1: Price + Room Type ──────────────────────────────
st.subheader("📊 Price & Supply Analysis")
col1, col2 = st.columns([3, 2])

with col1:
    df_plot = df[df['price'] < df['price'].quantile(0.98)]
    fig = px.histogram(
        df_plot, x='price', nbins=60,
        color='room_type',
        title='Price Distribution by Room Type',
        labels={'price': 'Price ($/night)', 'count': 'Listings'},
        template='plotly_dark',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        bargap=0.05, legend_title='Room Type',
        plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
        font_color='#e0e0e0', title_font_size=14
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    room_counts = df['room_type'].value_counts().reset_index()
    room_counts.columns = ['Room Type', 'Count']
    fig2 = px.pie(
        room_counts, values='Count', names='Room Type',
        title='Room Type Share',
        template='plotly_dark',
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_layout(
        plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
        font_color='#e0e0e0', title_font_size=14,
        legend=dict(orientation='v', x=1.0)
    )
    st.plotly_chart(fig2, use_container_width=True)

# ── ROW 2: Neighbourhood ──────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    top_n = df['neighbourhood'].value_counts().head(12).reset_index()
    top_n.columns = ['Neighbourhood', 'Listings']
    fig3 = px.bar(
        top_n.sort_values('Listings'), x='Listings', y='Neighbourhood',
        orientation='h', title='Top 12 Neighbourhoods by Listing Count',
        template='plotly_dark', color='Listings',
        color_continuous_scale='Blues'
    )
    fig3.update_layout(
        plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
        font_color='#e0e0e0', title_font_size=14,
        coloraxis_showscale=False, yaxis_title=''
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    neigh_price = (
        df.groupby('neighbourhood')['price']
        .median().sort_values(ascending=False).head(12).reset_index()
    )
    neigh_price.columns = ['Neighbourhood', 'Median Price']
    fig4 = px.bar(
        neigh_price.sort_values('Median Price'), x='Median Price', y='Neighbourhood',
        orientation='h', title='Top 12 Neighbourhoods by Median Price',
        template='plotly_dark', color='Median Price',
        color_continuous_scale='Greens'
    )
    fig4.update_layout(
        plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
        font_color='#e0e0e0', title_font_size=14,
        coloraxis_showscale=False, yaxis_title=''
    )
    st.plotly_chart(fig4, use_container_width=True)

# ── ROW 3: MARKET SEGMENTS ────────────────────────────────
st.markdown("---")
st.subheader("🔍 Market Segmentation — K-Means (K=4)")

col5, col6 = st.columns([2, 3])

with col5:
    seg_counts = df['cluster_name'].value_counts().reset_index()
    seg_counts.columns = ['Segment', 'Count']
    seg_counts['Color'] = seg_counts['Segment'].map(CLUSTER_COLORS)
    fig5 = px.bar(
        seg_counts, x='Segment', y='Count',
        title='Listings per Market Segment',
        template='plotly_dark',
        color='Segment',
        color_discrete_map=CLUSTER_COLORS
    )
    fig5.update_layout(
        plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
        font_color='#e0e0e0', title_font_size=14,
        showlegend=False, xaxis_title='', xaxis_tickangle=-20
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    seg_profile = df.groupby('cluster_name').agg(
        Avg_Price=('price','median'),
        Avg_Min_Nights=('minimum_nights','mean'),
        Avg_Reviews=('number_of_reviews','mean'),
        Avg_Availability=('availability_365','mean'),
    ).round(1).reset_index()
    seg_profile.columns = ['Segment','Median Price','Avg Min Nights','Avg Reviews','Avg Avail (days)']

    fig6 = go.Figure(data=[go.Table(
        header=dict(
            values=list(seg_profile.columns),
            fill_color='#2e3250',
            font=dict(color='white', size=12),
            align='left', height=36
        ),
        cells=dict(
            values=[seg_profile[c] for c in seg_profile.columns],
            fill_color=[['#1e2130']*len(seg_profile)]*len(seg_profile.columns),
            font=dict(color='#e0e0e0', size=12),
            align='left', height=32
        )
    )])
    fig6.update_layout(
        title='Segment Profile Summary',
        template='plotly_dark',
        paper_bgcolor='#1e2130',
        font_color='#e0e0e0',
        title_font_size=14,
        margin=dict(t=50, b=0, l=0, r=0),
        height=260
    )
    st.plotly_chart(fig6, use_container_width=True)

# Price by segment box
fig7 = px.box(
    df[df['price'] < df['price'].quantile(0.95)],
    x='cluster_name', y='price',
    color='cluster_name',
    title='Price Distribution by Market Segment',
    template='plotly_dark',
    color_discrete_map=CLUSTER_COLORS,
    labels={'cluster_name':'Segment','price':'Price ($/night)'}
)
fig7.update_layout(
    plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
    font_color='#e0e0e0', title_font_size=14,
    showlegend=False, xaxis_title=''
)
st.plotly_chart(fig7, use_container_width=True)

# ── ROW 4: SENTIMENT ──────────────────────────────────────
st.markdown("---")
st.subheader("💬 Guest Sentiment Analysis — VADER NLP (80K reviews)")

col7, col8 = st.columns([1, 2])

with col7:
    sent_counts = rv['sentiment'].value_counts().reset_index()
    sent_counts.columns = ['Sentiment','Count']
    fig8 = px.pie(
        sent_counts, values='Count', names='Sentiment',
        title='Overall Sentiment Distribution',
        template='plotly_dark', hole=0.5,
        color='Sentiment', color_discrete_map=SENTIMENT_COLORS
    )
    fig8.update_layout(
        plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
        font_color='#e0e0e0', title_font_size=14
    )
    st.plotly_chart(fig8, use_container_width=True)

with col8:
    sent_cluster = (
        rv.dropna(subset=['cluster_name'])
        .groupby(['cluster_name','sentiment'])
        .size().reset_index(name='Count')
    )
    total = sent_cluster.groupby('cluster_name')['Count'].transform('sum')
    sent_cluster['Pct'] = (sent_cluster['Count'] / total * 100).round(1)

    fig9 = px.bar(
        sent_cluster, x='cluster_name', y='Pct', color='sentiment',
        title='Sentiment Distribution (%) by Market Segment',
        template='plotly_dark',
        color_discrete_map=SENTIMENT_COLORS,
        labels={'cluster_name':'Segment','Pct':'Percentage (%)','sentiment':'Sentiment'},
        barmode='stack'
    )
    fig9.update_layout(
        plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
        font_color='#e0e0e0', title_font_size=14,
        xaxis_title='', xaxis_tickangle=-20
    )
    st.plotly_chart(fig9, use_container_width=True)

# Sentiment over time
st.subheader("📅 Sentiment Trend Over Time")
rv_time = rv.dropna(subset=['year'])
rv_time = rv_time[rv_time['year'].between(2015, 2024)]
trend = (
    rv_time.groupby(['year','sentiment'])
    .size().reset_index(name='Count')
)
total_yr = trend.groupby('year')['Count'].transform('sum')
trend['Pct'] = (trend['Count'] / total_yr * 100).round(1)

fig10 = px.line(
    trend, x='year', y='Pct', color='sentiment',
    title='Sentiment Trend by Year',
    template='plotly_dark',
    color_discrete_map=SENTIMENT_COLORS,
    markers=True,
    labels={'year':'Year','Pct':'Percentage (%)','sentiment':'Sentiment'}
)
fig10.update_layout(
    plot_bgcolor='#1e2130', paper_bgcolor='#1e2130',
    font_color='#e0e0e0', title_font_size=14
)
st.plotly_chart(fig10, use_container_width=True)

# ── MAP ────────────────────────────────────────────────────
st.markdown("---")
st.subheader("🗺️ Listing Map — Geographic Distribution")

map_df = df.dropna(subset=['latitude','longitude','price']).copy()
map_df = map_df[map_df['price'] > 0]

fig_map = px.scatter_mapbox(
    map_df.sample(min(3000, len(map_df)), random_state=42),
    lat='latitude', lon='longitude',
    color='cluster_name',
    size='price',
    size_max=14,
    hover_name='neighbourhood',
    hover_data={'price':True,'room_type':True,'cluster_name':True,
                'latitude':False,'longitude':False},
    color_discrete_map=CLUSTER_COLORS,
    mapbox_style='carto-darkmatter',
    zoom=11,
    center={"lat": 49.2827, "lon": -123.1207},
    title='Vancouver Airbnb Listings by Market Segment',
    labels={'cluster_name':'Segment'}
)
fig_map.update_layout(
    paper_bgcolor='#1e2130',
    font_color='#e0e0e0',
    title_font_size=14,
    height=520,
    margin=dict(t=50, b=0, l=0, r=0)
)
st.plotly_chart(fig_map, use_container_width=True)

# ── FOOTER ────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666; font-size:0.85rem; padding: 12px 0'>
    Built by <strong>Gowri Sukumaran</strong> · 
    Data: Inside Airbnb (Vancouver) · 
    Tools: Python, Scikit-learn, VADER, Streamlit, Plotly
</div>
""", unsafe_allow_html=True)
