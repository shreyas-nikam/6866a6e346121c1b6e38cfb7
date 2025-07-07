id: 6866a6e346121c1b6e38cfb7_user_guide
summary: Derivative Instrument and  Derivative Market Features User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# CCP Novation & Risk Transfer Animator: A User Guide

This codelab provides a comprehensive guide to understanding and using the "CCP Novation & Risk Transfer Animator" application. This application is designed to visually explain the central clearing process for derivatives, focusing on the roles of the Swap Execution Facility (SEF) and the Central Counterparty (CCP). It aims to demystify complex financial concepts through interactive visualizations and synthetic data, illustrating how counterparty credit risk is managed and transferred in centrally cleared markets. By the end of this guide, you will understand the novation process, visualize the reduction in counterparty risk, and explore hypothetical risk trends.

## Overview of the Application
Duration: 00:05

The application consists of four main sections, accessible through the sidebar navigation:

*   **Overview:** Provides context, learning outcomes, and key concepts related to central clearing.
*   **Novation Process Animator:** Illustrates the step-by-step novation process with interactive animation.
*   **Risk Network Visualizer:** Visually compares risk networks before and after the introduction of a CCP, demonstrating the reduction in bilateral links.
*   **Hypothetical Risk Trends:** Shows a hypothetical reduction in overall counterparty risk with increased central clearing adoption.

The application uses interactive elements such as sliders and number inputs to allow users to explore different scenarios and parameters.

## Exploring the Overview Page
Duration: 00:03

The "Overview" page serves as the starting point, providing essential background information.

1.  Navigate to the "Overview" section using the sidebar.
2.  Read the description to understand the purpose of the application.
3.  Review the "Key Concepts" to familiarize yourself with terms like Central Clearing, SEF, Novation, and Counterparty Credit Risk Reduction.
4.  Understand the "Learning Outcomes" to know what you should be able to do after using the application.
5.  Refer to the provided references for more in-depth information on the topics covered.

<aside class="positive">
The Overview page provides a strong foundation for understanding the rest of the application. Spend some time here to ensure you grasp the key concepts.
</aside>

## Using the Novation Process Animator
Duration: 00:10

The "Novation Process Animator" visualizes the step-by-step process of novation in central clearing.

1.  Navigate to the "Novation Process Animator" section using the sidebar.
2.  Use the slider labeled "Select Step" to move through the different stages of the novation process.
3.  Read the title and description for each step to understand what is happening.
4.  Observe the animated diagram/visualization (placeholder in the current version) to see a visual representation of each step.

The animator is designed to help you understand the sequence of events that occur during novation, and how the CCP steps in to intermediate the trade.

<aside class="negative">
Currently, the animated diagram is a placeholder. Future versions will include a dynamic visualization.
</aside>

## Interacting with the Risk Network Visualizer
Duration: 00:15

The "Risk Network Visualizer" demonstrates how a CCP reduces the number of bilateral credit relationships in a network of financial intermediaries.

1.  Navigate to the "Risk Network Visualizer" section using the sidebar.
2.  Read the introduction to understand the purpose of this section.
3.  Note the Bilateral Links and CCP Links Formulas, which mathematically explain the reduction in connections.

    *   **Bilateral Links Formula:** $\text{Bilateral Links} = \frac{N(N-1)}{2}$
    *   **CCP Links Formula:** $\text{CCP Links} = N$
4.  Use the number input labeled "Number of Financial Intermediaries (N)" to change the number of intermediaries in the network. Observe how the number of links changes with and without a CCP.
5.  Examine the network diagrams to visually see the difference between a fully connected network (before CCP) and a star network (after CCP).

<aside class="positive">
By increasing the number of intermediaries, you'll see an exponential increase in bilateral links without a CCP. This visually highlights the risk reduction benefit of central clearing.
</aside>

## Analyzing Hypothetical Risk Trends
Duration: 00:07

The "Hypothetical Risk Trends" section presents a chart illustrating a hypothetical reduction in overall counterparty risk with increased central clearing adoption over time.

1.  Navigate to the "Hypothetical Risk Trends" section using the sidebar.
2.  Read the introduction to understand the context of the chart.
3.  Use the slider labeled "Number of Periods" to adjust the time frame of the simulation.
4.  Observe the line chart, which shows a declining "Risk Score" over time, representing the reduction in counterparty risk.

This section provides a visual representation of how central clearing can contribute to a more stable financial system by reducing systemic risk.

## Conclusion
Duration: 00:02

You have now completed the user guide for the "CCP Novation & Risk Transfer Animator" application. You should now have a better understanding of the central clearing process, the role of CCPs in reducing counterparty risk, and how to visualize these concepts using interactive tools. Feel free to explore the application further and experiment with different parameters to deepen your understanding.
