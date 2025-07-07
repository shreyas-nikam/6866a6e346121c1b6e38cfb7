
# CCP Novation & Risk Transfer Animator

This Streamlit application visually explains the central clearing process for derivatives, focusing on the roles of the Swap Execution Facility (SEF) and the Central Counterparty (CCP). It animates the 'novation' process and illustrates how counterparty credit risk is managed.

## Overview

The application is structured into distinct sections, navigable via a sidebar:

*   **Overview**: Provides an introduction to central clearing, SEFs, and novation.
*   **Novation Process Animator**: Animates the step-by-step novation process.
*   **Risk Network Visualizer**: Visualizes the reduction in counterparty risk through central clearing.
*   **Hypothetical Risk Trends**: Shows hypothetical risk trends over time.

## Setup

1.  Clone the repository.
2.  Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application locally:

## Docker

To run the application using Docker:

1.  Build the Docker image:
    ```bash
    docker build -t ccp-novation .
    ```
2.  Run the Docker container:
    ```bash
    docker run -p 8501:8501 ccp-novation
    ```

## References

*   [1] Section 'Central Clearing' & Exhibit 6: Central Clearing for Interest Rate Swaps, Derivatives.pdf
*   [2] Training - Data Innovations, https://www.datainnovations.com/training

