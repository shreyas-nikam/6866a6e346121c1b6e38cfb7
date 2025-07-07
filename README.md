# CCP Novation & Risk Transfer Animator

## Project Title and Description

This Streamlit application provides a visual explanation of the central clearing process for derivatives, with a focus on the roles of Swap Execution Facilities (SEFs) and Central Counterparties (CCPs). It animates the 'novation' process, illustrating how counterparty credit risk is managed and transferred in centrally cleared markets. The application also visualizes the reduction in risk resulting from central clearing.

## Features

*   **Overview:** Introduces the core concepts of central clearing, novation, SEFs, and CCPs, and the risk reduction benefits of central clearing.
*   **Novation Process Animator:** (Placeholder) Will visually demonstrate the novation process, step-by-step, showing how the CCP interposes itself between the original counterparties.
*   **Risk Network Visualizer:** Visualizes the reduction in counterparty risk by comparing the network of bilateral relationships before and after the introduction of a CCP.  Allows users to adjust the number of financial intermediaries and see the corresponding change in network complexity.
*   **Hypothetical Risk Trends:** (Placeholder) Will display hypothetical risk trends over time, illustrating the potential impact of central clearing on systemic risk.
*   **Mathematical Formulas:** Includes the formulas to calculate the number of bilateral links before and after the introduction of a CCP.
*   **Interactive Number Input:** Users can adjust the number of intermediaries to see how it affects the network graphs and risk reduction calculations.

## Getting Started

These instructions will guide you on how to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python:** (Version 3.7 or higher recommended)
*   **Pip:** Python package installer (should come with Python)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd ccp-novation-risk-transfer-animator
    ```

    *(Replace `<repository_url>` with the actual URL of your repository.)*

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

    *   Activate the virtual environment:

        *   **On Windows:**

            ```bash
            venv\Scripts\activate
            ```

        *   **On macOS and Linux:**

            ```bash
            source venv/bin/activate
            ```

3.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    *(Create a `requirements.txt` file with the following content or run `pip freeze > requirements.txt` after installing the packages using pip)*

    ```
    streamlit
    pandas
    plotly
    numpy
    ```

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:** Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3.  **Interact with the application:** Use the sidebar navigation to explore the different sections of the application.  Adjust the number of intermediaries using the number input on the "Risk Network Visualizer" page.

## Project Structure

The project is organized as follows:

```
ccp-novation-risk-transfer-animator/
├── app.py                         # Main Streamlit application file
├── application_pages/
│   ├── page1.py                   # Content for the Overview page
│   └── page2.py                   # Content for the Risk Network Visualizer page
├── core_calculations.py           # Contains core calculation functions
├── visualizations.py              # Contains visualization functions
├── README.md                      # This file
├── requirements.txt               # List of Python dependencies
└── venv/                        # Virtual environment directory (optional, not committed to repo)
```

*   **`app.py`**: The main file that runs the Streamlit application.  It handles the overall layout, navigation, and calling of other modules.
*   **`application_pages/`**: Contains individual Streamlit pages as separate modules. This helps keep the main `app.py` file clean and organized.
*   **`core_calculations.py`**: Contains functions for performing key calculations related to bilateral and CCP links.
*   **`visualizations.py`**:  Contains functions for creating visualizations, like the risk network chart.
*   **`README.md`**: Provides documentation for the project.
*   **`requirements.txt`**: Lists the Python packages needed to run the application.
*   **`venv/`**:  A directory containing the virtual environment (not committed to the repository).

## Technology Stack

*   **Streamlit:** For building the interactive web application.
*   **Pandas:** For data manipulation and analysis (potential use for future expansion).
*   **Plotly:** For creating interactive visualizations.
*   **NumPy:** For numerical computations (potential use for future expansion).
*   **Python:** The programming language used for the entire application.

## Contributing

We welcome contributions to this project!  Here's how you can contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name` or `git checkout -b bugfix/your-bugfix-name`.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request to the main repository.

Please follow these guidelines when contributing:

*   Write clear and concise code.
*   Provide detailed commit messages.
*   Add comments to your code where necessary.
*   Test your changes thoroughly.

## License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.
( *Note: Create a LICENSE file in the project root if using a specific open-source license like MIT.* )

## Contact

For questions or inquiries, please contact:

*   [QuantUniversity](https://www.quantuniversity.com/) - This is where the educational lab was created.

