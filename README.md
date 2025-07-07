
# CCP Novation & Risk Transfer Animator

This Streamlit application visually explains the central clearing process for derivatives, with a specific focus on the roles of the Swap Execution Facility (SEF) and the Central Counterparty (CCP).

## How to run

1.  Build the Docker image:

    ```bash
    docker build -t ccp-novation-animator .
    ```

2.  Run the Docker container:

    ```bash
    docker run -p 8501:8501 ccp-novation-animator
    ```

3.  Open your browser and go to `http://localhost:8501`.
