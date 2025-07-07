
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

def create_novation_animation(diagram_state):
    """Generates a visual representation of the current animation step."""
    # Placeholder implementation - replace with actual visualization
    st.write(f"Animation Step: {diagram_state}")

def create_risk_network_chart(num_intermediaries):
    """Visualizes the reduction in bilateral links using Plotly."""
    # Create data for the "before CCP" network
    nodes_before = list(range(num_intermediaries))
    edges_before = []
    for i in range(num_intermediaries):
        for j in range(i + 1, num_intermediaries):
            edges_before.append((i, j))

    # Create data for the "after CCP" network
    nodes_after = list(range(num_intermediaries + 1))  # +1 for the CCP node
    edges_after = []
    for i in range(num_intermediaries):
        edges_after.append((i, num_intermediaries))  # Connect each intermediary to the CCP

    # Create Plotly figures
    fig = go.Figure()

    # Add traces for the "before CCP" network
    for edge in edges_before:
        fig.add_trace(go.Scatter(x=[edge[0], edge[1]], y=[0, 0], mode='lines', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=nodes_before, y=[0]*len(nodes_before), mode='markers', marker=dict(size=20, color='red')))

    # Add traces for the "after CCP" network (shifted to the right)
    for edge in edges_after:
        fig.add_trace(go.Scatter(x=[edge[0]+num_intermediaries+2, edge[1]+num_intermediaries+2], y=[0, 0], mode='lines', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=[node+num_intermediaries+2 for node in nodes_after[:-1]], y=[0]*len(nodes_after[:-1]), mode='markers', marker=dict(size=20, color='red')))
    fig.add_trace(go.Scatter(x=[nodes_after[-1]+num_intermediaries+2], y=[0], mode='markers', marker=dict(size=20, color='purple')))  # CCP node

    # Update layout
    fig.update_layout(showlegend=False, xaxis_visible=False, yaxis_visible=False)
    st.plotly_chart(fig, use_container_width=True)


def create_risk_trend_chart(df_risk_exposure):
    """Generates a line chart showing hypothetical risk exposure over time."""
    fig = px.line(df_risk_exposure, x="Date", y="Risk_Score", title="Hypothetical Risk Trend")
    st.plotly_chart(fig, use_container_width=True)
