id: 6866a6e346121c1b6e38cfb7_documentation
summary: Derivative Instrument and  Derivative Market Features Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# CCP Novation & Risk Transfer Animator Codelab

This codelab guides you through the "CCP Novation & Risk Transfer Animator" application, which provides a visual and interactive explanation of central clearing processes and the risk mitigation benefits offered by Central Counterparties (CCPs). Understanding these concepts is crucial for anyone involved in financial markets, especially those dealing with derivatives. This application simplifies the complex processes of novation and risk transfer, making them accessible to developers, financial professionals, and students alike. By the end of this codelab, you'll understand the application's structure, the core calculations, and how it visualizes risk reduction.

## Project Setup and Overview
Duration: 00:05

Before diving into the code, let's get an overview of the project structure. The application is built using Streamlit, a Python library for creating interactive web applications.

The project consists of the following files:

*   `app.py`: The main application file that orchestrates the different sections of the application.
*   `application_pages/page1.py`: Contains the overview page.
*   `application_pages/page2.py`: Contains the Risk Network Visualizer page, which visualizes the risk reduction due to CCPs.
*   `core_calculations.py`: Includes functions for calculating bilateral and CCP links.
*   `visualizations.py`: Contains functions for creating the novation animation and risk network chart.

## Understanding the Main Application (app.py)
Duration: 00:15

The `app.py` file serves as the entry point for the Streamlit application. Let's break down its key components:

```python
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

st.sidebar.markdown("")
st.sidebar.markdown("**References**")
st.sidebar.markdown("[1] Section 'Central Clearing' & Exhibit 6: Central Clearing for Interest Rate Swaps, Derivatives.pdf.")
st.sidebar.markdown("[2] Training - Data Innovations, https://www.datainnovations.com/training.")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
```

Here's a breakdown:

*   **Imports:** Necessary libraries like `streamlit`, `pandas`, `plotly`, and `numpy` are imported.
*   **Page Configuration:**  `st.set_page_config` sets the title and layout of the Streamlit app.
*   **Title and Introduction:**  The application's title, a brief introduction, core concepts, and mathematical formulas are displayed using `st.markdown`. This provides users with context and key information about central clearing and novation.
*   **Navigation:** A sidebar is created using `st.sidebar.radio` to allow users to navigate between different sections of the application: "Overview", "Novation Process Animator", "Risk Network Visualizer", and "Hypothetical Risk Trends".
*   **Page Content:**  The `if/elif` block determines which content to display based on the selected page. Each page displays a header and a placeholder message.  In a complete application, you'd replace these placeholders with the actual content and functionality for each section.
*   **References and Footer:** The sidebar includes references, a divider, a copyright notice, and a caption indicating the educational purpose of the demonstration and disclaimers related to the use of AI models in its creation.

## Exploring the Overview Page (application_pages/page1.py)
Duration: 00:05

The `application_pages/page1.py` file contains the content for the "Overview" section.

```python
import streamlit as st

def run_page1():
    st.header("Overview")
    st.markdown("This section provides an overview of the application and the core concepts.")
    st.markdown("More detailed information will be added here.")

if __name__ == "__main__":
    run_page1()
```

The `run_page1` function uses `st.header` and `st.markdown` to display the page's title and a brief description. In a fully developed application, this section would contain comprehensive information about central clearing, novation, and the benefits of using a CCP.

## Diving into the Risk Network Visualizer (application_pages/page2.py)
Duration: 00:20

The `application_pages/page2.py` file implements the "Risk Network Visualizer," which showcases the reduction in risk through central clearing.

```python
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
```

Key components:

*   **Imports:** Includes necessary libraries, as well as imports from `core_calculations.py` (for calculating the number of links) and `visualizations.py` (for creating the network chart).
*   **User Input:**  `st.number_input` allows the user to specify the number of financial intermediaries.
*   **Calculations:** The `calculate_bilateral_links` and `calculate_ccp_links` functions (from `core_calculations.py`) are used to calculate the number of links with and without a CCP.
*   **Display Results:** The calculated number of links is displayed using `st.markdown`.
*   **Visualization:** The `create_risk_network_chart` function (from `visualizations.py`) is called to generate and display the risk network visualization.

## Understanding the Core Calculations (core_calculations.py)
Duration: 00:10

The `core_calculations.py` file contains the functions for calculating the number of bilateral links and CCP links.

```python
def calculate_bilateral_links(num_intermediaries):
    """Calculates the number of bilateral links in a network."""
    return num_intermediaries * (num_intermediaries - 1) // 2

def calculate_ccp_links(num_intermediaries):
    """Calculates the number of links to a CCP."""
    return num_intermediaries
```

The `calculate_bilateral_links` function implements the formula $N(N-1)/2$, where $N$ is the number of financial intermediaries.  This represents the number of direct connections in a network where every participant is connected to every other participant.

The `calculate_ccp_links` function simply returns the number of intermediaries, since each intermediary only has a single connection to the CCP.

## Visualizations (visualizations.py)
Duration: 00:20

The `visualizations.py` file contains the functions for creating the visualizations used in the application.

```python
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
```

Here's a breakdown:

*   **`create_novation_animation`:** This function is a placeholder for the novation animation.  Currently, it only displays the animation state. In a real application, you would use a library like Plotly or Matplotlib to create an animated visual representation of the novation process.
*   **`create_risk_network_chart`:** This function generates a network chart that visualizes the reduction in bilateral links when a CCP is introduced. It uses `plotly.graph_objects` to create the chart.  The chart displays two networks side-by-side: one representing the bilateral links between intermediaries before a CCP, and the other showing the links between each intermediary and the CCP after central clearing.  The number of intermediaries is determined by user input.
*   **`create_risk_trend_chart`:**  This function creates a line chart showing hypothetical risk exposure over time. It takes a Pandas DataFrame as input, with columns for "Date" and "Risk_Score", and uses `plotly.express` to generate the chart.

## Running the Application
Duration: 00:05

To run the application, save all the files in the appropriate directory structure and navigate to the project directory in your terminal. Then, run the command:

```console
streamlit run app.py
```

This will start the Streamlit server and open the application in your web browser. You can then interact with the application, change the number of intermediaries, and observe the changes in the risk network visualization.

## Extending the Application
Duration: 00:30

This application provides a solid foundation for understanding central clearing and risk transfer. Here are some ways you can extend it:

*   **Implement the Novation Animation:** Replace the placeholder in `create_novation_animation` with an actual animated visualization of the novation process. This could involve showing the flow of contracts and obligations between the original counterparties and the CCP at each step.
*   **Add Data Input for Risk Trends:** Allow users to input or upload their own risk exposure data to generate custom risk trend charts.
*   **Develop "Hypothetical Risk Trends" page**: Currently, this page is a placeholder. This page can be further enhanced by adding a risk model and risk simulation module that generates hypothetical risk scores and trends given model parameters like volatility, correlation, etc.
*   **Interactive Network:** Improve the network graph by adding node labels, tooltips on hover, and the ability to drag and rearrange the nodes.
*   **Detailed Explanations:** Add more detailed explanations and annotations to the visualizations to provide a deeper understanding of the concepts.
*   **Implement other pages**: The pages other than Risk Network Visualizer are not implemented. These pages can be implemented.
*   **More detailed overview**: The Overview page can be improved with more details on central clearing, SEF, novation etc.

<aside class="positive">
This application offers a valuable tool for visualizing and understanding the complex world of central clearing and risk management. By building upon this foundation, you can create a powerful educational resource for anyone involved in financial markets.
</aside>
