from db import run_query
import streamlit as st
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Fraud Analytics System",
    page_icon="🔎",
    layout="wide"
)


# --------------------------------------------------
# APPLICATION TITLE
# --------------------------------------------------

st.title("Fraud Analytics System")

st.write(
    "Fraud detection, risk analysis, and business intelligence dashboard."
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Executive Overview",
        "Fraud Analysis",
        "Temporal & Risk Analysis",
        "Fraud Detection",
        "Risk Scoring & Alerts"
    ]
)


# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------

if page == "Executive Overview":

    st.header("Executive Overview")
    st.write("High-level fraud performance and key risk indicators.")

    query = """
    SELECT *
    FROM vw_core_kpis
    """

    kpi_data = run_query(query)

    if not kpi_data.empty:

        kpi = kpi_data.iloc[0]

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "Total Transactions",
                f"{kpi['total_transactions']:,}"
            )

        with col2:
            st.metric(
                "Fraud Transactions",
                f"{kpi['total_fraud_transactions']:,}"
            )

        with col3:
            st.metric(
                "Fraud Rate",
                f"{kpi['fraud_rate_percentage']:.2f}%"
            )

        with col4:
            st.metric(
                "Total Fraud Value",
                f"₹{kpi['total_fraud_value']:,.2f}"
            )

        with col5:
            st.metric(
                "Fraud Value %",
                f"{kpi['fraud_value_percentage']:.2f}%"
            )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("Fraud Transactions by Category")

        category_query = """
        SELECT *
        FROM vw_category_analysis
        ORDER BY fraud_transactions DESC
        """

        category_data = run_query(category_query)

        if not category_data.empty:
            st.bar_chart(
                category_data,
                x="category",
                y="fraud_transactions"
            )

    with col2:

        st.subheader("Risk Category Distribution")

        risk_query = """
        SELECT
            risk_category,
            SUM(transaction_count) AS transaction_count
        FROM vw_risk_analysis
        GROUP BY risk_category
        ORDER BY transaction_count DESC
        """

        risk_data = run_query(risk_query)

        if not risk_data.empty:
            fig = px.pie(
                risk_data,
                names="risk_category",
                values="transaction_count",
                hole=0.55
            )

            fig.update_traces(
                textposition="inside",
                textinfo="percent+label"
            )

            fig.update_layout(
                showlegend=True,
                margin=dict(t=20, b=20, l=20, r=20)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )








elif page == "Fraud Analysis":

    st.header("Fraud Analysis")
    st.write("Category, geographic, and demographic fraud analysis.")

elif page == "Temporal & Risk Analysis":

    st.header("Temporal & Risk Analysis")
    st.write("Fraud timing and risk distribution analysis.")

elif page == "Fraud Detection":

    st.header("Fraud Detection")
    st.write("Machine learning-based fraud detection.")

elif page == "Risk Scoring & Alerts":

    st.header("Risk Scoring & Alerts")
    st.write("Transaction risk scoring and alert generation.")