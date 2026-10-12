# --------------------------------------------------
# IMPORTS
# --------------------------------------------------
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
                f"₹{kpi['total_fraud_value'] / 1_000_000:.2f}M"
            )
        with col5:
            st.metric(
                "Fraud Value %",
                f"{kpi['fraud_value_percentage']:.2f}%"
            )
            
    col1, col2 = st.columns(2)
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
                height=350,
                autosize=True,
                margin=dict(l=20, r=20, t=30, b=20),
                legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.02
            ))
            st.plotly_chart(
                fig,
                use_container_width=True
            )

    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Top 10 States by Fraud Transactions")
        state_query = """
        SELECT *
        FROM vw_geographic_analysis
        ORDER BY fraud_transactions DESC
        LIMIT 10
        """
        state_data = run_query(state_query)
        if not state_data.empty:
            fig = px.bar(
                state_data,
                x="fraud_transactions",
                y="state",
                orientation="h"
            )
            fig.update_layout(
                yaxis={"categoryorder": "total ascending"},
                xaxis_title="Fraud Transactions",
                yaxis_title="State"
            )
            st.plotly_chart(
                fig,
                use_container_width=True
            )
    with col4:
        st.subheader("Monthly Fraud Trend")
        monthly_query = """
        SELECT *
        FROM vw_monthly_fraud_analysis
        """
        monthly_data = run_query(monthly_query)
        if not monthly_data.empty:
            month_order = [
                "January", "February", "March",
                "April", "May", "June",
                "July", "August", "September",
                "October", "November", "December"
            ]
            month_numbers = {
                month: index
                for index, month in enumerate(month_order)
            }
            monthly_data["month_number"] = (
                monthly_data["transaction_month"].map(month_numbers)
            )
            monthly_data = monthly_data.sort_values("month_number")
            fig = px.line(
                monthly_data,
                x="transaction_month",
                y="fraud_transactions",
                markers=True,
                text="fraud_transactions"
            )
            fig.update_traces(
                line=dict(width=3),
                marker=dict(size=7),
                textposition="top center",
                hovertemplate=(
                    "Month: %{x}<br>"
                    "Fraud Transactions: %{y}"
                    "<extra></extra>"
                )
            )
            fig.update_layout(
                xaxis_title="Month",
                yaxis_title="Fraud Transactions",
                xaxis=dict(
                    categoryorder="array",
                    categoryarray=month_order,
                    tickangle=-35
                ),
                showlegend=False,
                margin=dict(t=20, b=50, l=10, r=10)
            )
            st.plotly_chart(
                fig,
                use_container_width=True
            )
    
elif page == "Fraud Analysis":
    st.header("Fraud Analysis")
    st.write("Category, geographic, and demographic fraud analysis.")

    st.subheader("Fraud Percentage by Category")
    category_query = """
    SELECT
        category,
        fraud_rate_percentage
    FROM vw_category_analysis
    ORDER BY fraud_rate_percentage DESC
    """
    category_data = run_query(category_query)
    if not category_data.empty:
        fig = px.bar(
            category_data,
            x="fraud_rate_percentage",
            y="category",
            orientation="h",
            text="fraud_rate_percentage"
        )
        fig.update_traces(
            marker_color="#A8323E",
            texttemplate="%{text:.1f}",
            textposition="outside",
            cliponaxis=False,
            hovertemplate=(
                "Category: %{y}<br>"
                "Fraud Percentage: %{x:.2f}%"
                "<extra></extra>"
            )
        )
        fig.update_layout(
            xaxis_title="Fraud Percentage (%)",
            yaxis_title="",
            yaxis={
                "categoryorder": "total ascending"
            },
            showlegend=False,
            margin=dict(l=10, r=40, t=20, b=20)
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )
    else:
        st.info("No category fraud data available.")

    
    st.subheader("Fraud Value by Category")

    fraud_value_query = """
    SELECT
        category,
        total_fraud_value
    FROM vw_category_analysis
    ORDER BY total_fraud_value DESC
    """

    fraud_value_data = run_query(fraud_value_query)

    if not fraud_value_data.empty:
        fig = px.bar(
            fraud_value_data,
            x="total_fraud_value",
            y="category",
            orientation="h",
            text="total_fraud_value"
        )

        fig.update_traces(
            marker_color="#A8323E",
            texttemplate="%{text:,.2s}",
            textposition="outside",
            cliponaxis=False,
            hovertemplate=(
                "Category: %{y}<br>"
                "Fraud Value: ₹%{x:,.2f}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            xaxis_title="Total Fraud Value (₹)",
            yaxis_title="",
            yaxis={
                "categoryorder": "total ascending"
            },
            showlegend=False,
            margin=dict(l=10, r=60, t=20, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
    else:
        st.info("No category fraud value data available.")

    st.subheader("Fraud Percentage by State")

    state_query = """
    SELECT
        state,
        fraud_rate_percentage
    FROM vw_geographic_analysis
    ORDER BY fraud_rate_percentage DESC
    LIMIT 10
    """

    state_data = run_query(state_query)

    if not state_data.empty:
        fig = px.bar(
            state_data,
            x="fraud_rate_percentage",
            y="state",
            orientation="h",
            text="fraud_rate_percentage"
        )

        fig.update_traces(
            marker_color="#A8323E",
            texttemplate="%{text:.2f}",
            textposition="outside",
            cliponaxis=False,
            hovertemplate=(
                "State: %{y}<br>"
                "Fraud Percentage: %{x:.2f}%"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            xaxis_title="Fraud Percentage (%)",
            yaxis_title="",
            yaxis={
                "categoryorder": "total ascending"
            },
            showlegend=False,
            margin=dict(l=10, r=50, t=20, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
    else:
        st.info("No state fraud data available.")





elif page == "Temporal & Risk Analysis":
    st.header("Temporal & Risk Analysis")
    st.write("Fraud timing and risk distribution analysis.")

elif page == "Fraud Detection":
    st.header("Fraud Detection")
    st.write("Machine learning-based fraud detection.")

elif page == "Risk Scoring & Alerts":
    st.header("Risk Scoring & Alerts")
    st.write("Transaction risk scoring and alert generation.")