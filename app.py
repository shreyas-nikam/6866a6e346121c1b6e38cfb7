
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="CCP Novation & Risk Transfer Animator", layout="wide")
st.sidebar.title("Navigation")

st.markdown("""
# CCP Novation & Risk Transfer Animator

This application visually explains the central clearing process for derivatives, with a specific focus on the roles of the Swap Execution Facility (SEF) and the Central Counterparty (CCP). It animates the 'novation' process, illustrating how counterparty credit risk is managed and transferred in centrally cleared markets.

## Core Concepts

*   **Central Clearing:** A post-trade mechanism where a Central Counterparty (CCP) steps in between the original counterparties to a trade, becoming the buyer to every seller and the seller to every buyer.

*   **Swap Execution Facility (SEF):** A trading platform where derivatives, particularly swaps, are executed.

*   **Novation:** The legal process by which the original bilateral contract between two parties is discharged and replaced by two new contracts: one between the first party and the CCP, and another between the second party and the CCP.

*   **Counterparty Credit Risk Reduction:** A key benefit of central clearing. Instead of each participant facing every other participant bilaterally, they only face the CCP.

## Mathematical Foundations

### Bilateral Links Formula
The number of direct bilateral links in a network of $N$ financial intermediaries is calculated using:

$$\text{Bilateral Links} = \frac{N(N-1)}{2}$$

Where:
- $N$: The number of financial intermediaries

### CCP Links Formula
When a Central Counterparty (CCP) is introduced, each intermediary only has a direct relationship with the CCP. The number of direct links becomes:

$$\text{CCP Links} = N$$

Where:
- $N$: The number of financial intermediaries
""")

page = st.sidebar.radio("Go to", ["Overview", "Novation Process Animator", "Risk Network Visualizer", "Hypothetical Risk Trends"])

if page == "Overview":
    st.header("Overview")
    st.markdown("This section provides an overview of the application and the core concepts.")

elif page == "Novation Process Animator":
    st.header("Novation Process Animator")
    st.markdown("This section animates the novation process.")
    # Placeholder for the novation animation

elif page == "Risk Network Visualizer":
    st.header("Risk Network Visualizer")
    st.markdown("This section visualizes the reduction in risk due to central clearing.")
    # Placeholder for the risk network visualization

elif page == "Hypothetical Risk Trends":
    st.header("Hypothetical Risk Trends")
    st.markdown("This section shows hypothetical risk trends over time.")
    # Placeholder for the risk trend visualization

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
