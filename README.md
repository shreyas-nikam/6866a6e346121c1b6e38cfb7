# CCP Novation & Risk Transfer Animator

## Project Title and Description

This Streamlit application provides an interactive visualization of the central clearing process for derivatives, focusing on the role of Central Counterparties (CCPs) and Swap Execution Facilities (SEFs). The application demonstrates the novation process, illustrating how counterparty credit risk is managed and transferred in centrally cleared markets.  It aims to make complex financial concepts understandable through interactive visualizations and synthetic data.

## Features

*   **Overview**: A summary of the core concepts behind central clearing, novation, and risk reduction.
*   **Novation Process Animator**: A step-by-step animation of the novation process, visually explaining the role of the CCP. Users can step through the process with a slider.
*   **Risk Network Visualizer**: Illustrates how a CCP reduces the number of bilateral credit relationships, contrasting the network before and after CCP implementation.  Includes calculation of the number of bilateral links and CCP links based on the number of intermediaries.
*   **Hypothetical Risk Trends**: Shows a hypothetical reduction in systemic risk exposure over time with increased central clearing adoption.  Users can adjust the number of time periods displayed.

## Getting Started

### Prerequisites

*   Python 3.6 or higher
*   pip package installer

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url> # Replace with your repository URL.  If you don't have a repository, create one and add these files.
    cd <repository_name>      # Replace with your repository name
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat # On Windows
    ```

3.  **Install the required packages:**

    ```bash
    pip install streamlit pandas plotly networkx
    ```

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**

    Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

3.  **Explore the Application:**

    *   Use the sidebar navigation to switch between the different sections of the application (Overview, Novation Process Animator, Risk Network Visualizer, Hypothetical Risk Trends).
    *   In the **Novation Process Animator**, use the slider to step through the animation and read the descriptions of each step.
    *   In the **Risk Network Visualizer**, adjust the number of financial intermediaries and observe the impact on the number of bilateral links.
    *   In the **Hypothetical Risk Trends** section, change the number of periods to adjust the length of the risk trend shown.

## Project Structure

```
.
├── app.py                  # Main Streamlit application file
├── data_generator.py       # Generates synthetic data for the application
├── core_calculations.py    # Contains core calculation functions
├── visualizations.py       # Contains functions for creating visualizations (Plotly charts)
├── README.md               # This file
└── venv/                   # Virtual environment directory (optional)
```

## Technology Stack

*   **Python:** Programming language
*   **Streamlit:** Web framework for building interactive applications
*   **Pandas:** Data analysis library
*   **Plotly:** Graphing library for creating interactive charts
*   **NumPy:** Library for numerical computing
*   **networkx:** Library for creating and manipulating graphs

## Contributing

We welcome contributions to improve this application! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and ensure they are well-documented.
4.  Submit a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details (Add a LICENSE file to your repo with the MIT License).  If you don't want to use the MIT license, replace with your desired license.

## Contact

For questions or suggestions, please contact:

*   [QuantUniversity](https://www.quantuniversity.com/)

```
