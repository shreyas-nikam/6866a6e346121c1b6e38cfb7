
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from data_generator import generate_novation_steps, generate_risk_network_data, generate_hypothetical_risk_exposure
from core_calculations import calculate_bilateral_links, calculate_ccp_links
from visualizations import create_novation_animation, create_risk_network_chart, create_risk_trend_chart

st.set_page_config(layout="wide", page_title="CCP Novation & Risk Transfer Animator")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Novation Process Animator", "Risk Network Visualizer", "Hypothetical Risk Trends"])

if page == "Overview":
    # Display overall description, learning outcomes, etc.
    st.title("CCP Novation & Risk Transfer Animator")
    st.header("Overview")
    st.markdown("""
    This Streamlit application visually explains the central clearing process for derivatives,
    with a specific focus on the roles of the Swap Execution Facility (SEF) and the Central Counterparty (CCP).
    The application animates the 'novation' process, illustrating how counterparty credit risk is managed
    and transferred in centrally cleared markets. It aims to transform complex financial concepts into
    interactive and easily understandable visualizations, leveraging synthetic data to demonstrate core principles.

    **Key Concepts:**

    *   **Central Clearing:** A post-trade mechanism where a Central Counterparty (CCP) steps in between the original counterparties to a trade.
    *   **Swap Execution Facility (SEF):** A trading platform where derivatives, particularly swaps, are executed.
    *   **Novation:** The legal process by which the original bilateral contract between two parties is discharged and replaced by two new contracts with the CCP.
    *   **Counterparty Credit Risk Reduction:** A key benefit of central clearing.

    **Learning Outcomes:**

    *   Understand the novation process in central clearing.
    *   Visualize the reduction in counterparty risk through CCPs.
    *   Explore hypothetical risk trends with increased central clearing.

    **References:**

    *   [1] Section 'Central Clearing' & Exhibit 6: Central Clearing for Interest Rate Swaps, Derivatives.pdf.
    *   [2] Training - Data Innovations, https://www.datainnovations.com/training.
    """)

elif page == "Novation Process Animator":
    st.header("Central Clearing: The Novation Process")
    novation_steps = generate_novation_steps()
    
    # Control for animation steps
    current_step_index = st.slider("Select Step", 0, len(novation_steps) - 1, 0)
    
    current_step = novation_steps[current_step_index]
    
    st.subheader(current_step['title'])
    st.markdown(current_step['description'])
    
    # Placeholder for the animated diagram/visualization
    animation_placeholder = st.empty()
    with animation_placeholder.container():
        create_novation_animation(current_step['diagram_state']) # This function would draw the diagram

elif page == "Risk Network Visualizer":
    st.header("Counterparty Risk Network Visualizer")
    st.markdown("""
    This section demonstrates how a CCP reduces the number of bilateral credit relationships.

    **Bilateral Links Formula:**
    The number of direct bilateral links in a network of $N$ financial intermediaries is calculated using:

    $$\text{Bilateral Links} = \frac{N(N-1)}{2}$$

    **CCP Links Formula:**
    When a Central Counterparty (CCP) is introduced, the number of direct links becomes:

    $$\text{CCP Links} = N$$
    """)
    
    num_intermediaries = st.number_input("Number of Financial Intermediaries (N)", min_value=2, max_value=20, value=5, step=1)
    
    bilateral_links = calculate_bilateral_links(num_intermediaries)
    ccp_links = calculate_ccp_links(num_intermediaries)
    
    st.markdown(f"Without a CCP, there are $\frac{{N(N-1)}}{{2}} = {bilateral_links}$ bilateral links.")
    st.markdown(f"With a CCP, there are only $N = {ccp_links}$ links.")
    
    # Visualize network comparison
    create_risk_network_chart(num_intermediaries)

elif page == "Hypothetical Risk Trends":
    st.header("Hypothetical Systemic Risk Trends")
    st.markdown("This chart illustrates a hypothetical reduction in overall counterparty risk with increased central clearing adoption.")
    
    num_periods = st.slider("Number of Periods", min_value=12, max_value=60, value=24, step=1)
    risk_df = generate_hypothetical_risk_exposure(num_periods)
    
    fig_risk_trend = create_risk_trend_chart(risk_df)
    st.plotly_chart(fig_risk_trend, use_container_width=True)

# Footer/References
st.sidebar.markdown("---")
st.sidebar.markdown("**References**")
st.sidebar.markdown("[1] Section 'Central Clearing' & Exhibit 6: Central Clearing for Interest Rate Swaps, Derivatives.pdf.")
st.sidebar.markdown("[2] Training - Data Innovations, https://www.datainnovations.com/training.")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
