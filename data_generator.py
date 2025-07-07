
import pandas as pd
import numpy as np

def generate_novation_steps():
    # Generate synthetic data for novation steps
    # Returns a list of dictionaries
    return [
        {'step_number': 1, 'title': 'Step 1: Trade executed on an SEF', 'description': 'Description of step 1', 'diagram_state': 'initial'},
        {'step_number': 2, 'title': 'Step 2: Trade submitted to CCP', 'description': 'Description of step 2', 'diagram_state': 'CCP_submitted'},
        {'step_number': 3, 'title': 'Step 3: Novation', 'description': 'Description of step 3', 'diagram_state': 'novated'}
    ]

def generate_risk_network_data(num_intermediaries):
    # Generate data for risk network visualization
    # Returns calculated bilateral and CCP links based on num_intermediaries
    return {}

def generate_hypothetical_risk_exposure(time_periods):
    # Creates a Pandas DataFrame simulating a reduction in systemic risk exposure over time with increased central clearing.
    dates = pd.date_range(start='2024-01-01', periods=time_periods, freq='M')
    risk_scores = np.linspace(100, 20, time_periods)
    df = pd.DataFrame({'Date': dates, 'Risk_Score': risk_scores})
    return df
