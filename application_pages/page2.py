
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from core_calculations import calculate_bilateral_links, calculate_ccp_links
from visualizations import create_risk_network_chart


def run_page2():
    st.header("Counterparty Risk Network Visualizer")
    st.markdown("This section demonstrates how a CCP reduces the number of bilateral credit relationships.")
    
    num_intermediaries = st.number_input("Number of Financial Intermediaries (N)", min_value=2, max_value=20, value=5, step=1)
    
    bilateral_links = calculate_bilateral_links(num_intermediaries)
    ccp_links = calculate_ccp_links(num_intermediaries)
    
    st.markdown(f"Without a CCP, there are $N(N-1)/2 = {bilateral_links}$ bilateral links.")
    st.markdown(f"With a CCP, there are only $N = {ccp_links}$ links.")
    
    # Visualize network comparison
    create_risk_network_chart(num_intermediaries)

if __name__ == "__main__":
    run_page2()
