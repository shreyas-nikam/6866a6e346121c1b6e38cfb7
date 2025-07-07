
from typing import List, Dict, Union

def generate_novation_steps() -> List[Dict[str, Union[int, str]]]:
    """    Generates a list of dictionaries, each representing a distinct step in the novation process for derivatives central clearing. This data includes step numbers, titles, detailed descriptions, and simple diagram states to drive animation.
Arguments:
  None
Output:
  A list of dictionaries, where each dictionary contains 'step_number', 'title', 'description', and 'diagram_state' keys.
"""
    steps_data: List[Dict[str, Union[int, str]]] = [
        {
            "step_number": 1,
            "title": "Step 1: Trade Executed on SEF",
            "description": (
                "A new derivatives trade is executed on a Swap Execution Facility (SEF) "
                "between two parties, Party A and Party B. This initiates the clearing process "
                "and forms the original bilateral contract."
            ),
            "diagram_state": 1
        },
        {
            "step_number": 2,
            "title": "Step 2: Submission to Central Counterparty (CCP)",
            "description": (
                "The executed trade details are electronically submitted by both Party A and "
                "Party B (or their clearing members) to the Central Counterparty (CCP) for "
                "clearing eligibility assessment and acceptance. This is a critical gateway."
            ),
            "diagram_state": "submission"
        },
        {
            "step_number": 3,
            "title": "Step 3: Novation and Contract Replacement",
            "description": (
                "Upon acceptance by the CCP, the original bilateral trade between Party A and "
                "Party B is extinguished. Through the legal process of **novation**, two new, "
                "identical contracts are created: one between Party A and the CCP, and another "
                "between Party B and the CCP. The CCP becomes the central guarantor."
            ),
            "diagram_state": 3
        },
        {
            "step_number": 4,
            "title": "Step 4: Ongoing Risk Management by CCP",
            "description": (
                "The CCP continuously monitors and manages the risk of the cleared contracts. "
                "This involves daily mark-to-market calculations, collection of margin (initial "
                "and variation), and default management procedures to ensure the stability "
                "and integrity of the financial system."
            ),
            "diagram_state": "risk_management"
        }
    ]
    return steps_data
