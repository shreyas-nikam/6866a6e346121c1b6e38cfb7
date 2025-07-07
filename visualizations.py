
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx

def create_novation_animation(diagram_state):
    # Generates a visual representation of the current animation step
    # This could involve dynamically updating text and static images/diagrams or using Plotly go.Figure with frames.
    fig = go.Figure()
    fig.update_layout(title=f"Novation Animation - State: {diagram_state}")
    return fig

def create_risk_network_chart(num_intermediaries):
    # Visualizes the reduction in bilateral links by showing a "before CCP" (dense network) and "after CCP" (star network) state.
    # This will use Plotly for node-link diagrams.

    # Before CCP: Fully connected graph
    G_before = nx.complete_graph(num_intermediaries)
    pos_before = nx.spring_layout(G_before, seed=42)  # Layout for better visualization

    edge_x_before = []
    edge_y_before = []
    for edge in G_before.edges():
        x0, y0 = pos_before[edge[0]]
        x1, y1 = pos_before[edge[1]]
        edge_x_before.append(x0)
        edge_y_before.append(y0)
        edge_x_before.append(x1)
        edge_y_before.append(y1)
        edge_x_before.append(None)
        edge_y_before.append(None)

    edge_trace_before = go.Scatter(
        x=edge_x_before, y=edge_y_before,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x_before = []
    node_y_before = []
    for node in G_before.nodes():
        x, y = pos_before[node]
        node_x_before.append(x)
        node_y_before.append(y)

    node_trace_before = go.Scatter(
        x=node_x_before, y=node_y_before,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_adjacencies_before = []
    node_text_before = []
    for node, adjacencies in enumerate(G_before.adjacency()):
        node_adjacencies_before.append(len(adjacencies[1]))
        node_text_before.append(f"Intermediary #{node}<br># of connections: {len(adjacencies[1])}")

    node_trace_before.marker.color = node_adjacencies_before
    node_trace_before.text = node_text_before

    # After CCP: Star graph
    G_after = nx.star_graph(num_intermediaries)
    pos_after = nx.spring_layout(G_after, seed=42)

    edge_x_after = []
    edge_y_after = []
    for edge in G_after.edges():
        x0, y0 = pos_after[edge[0]]
        x1, y1 = pos_after[edge[1]]
        edge_x_after.append(x0)
        edge_y_after.append(y0)
        edge_x_after.append(x1)
        edge_y_after.append(y1)
        edge_x_after.append(None)
        edge_y_after.append(None)

    edge_trace_after = go.Scatter(
        x=edge_x_after, y=edge_y_after,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x_after = []
    node_y_after = []
    for node in G_after.nodes():
        x, y = pos_after[node]
        node_x_after.append(x)
        node_y_after.append(y)

    node_trace_after = go.Scatter(
        x=node_x_after, y=node_y_after,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_adjacencies_after = []
    node_text_after = []
    for node, adjacencies in enumerate(G_after.adjacency()):
        node_adjacencies_after.append(len(adjacencies[1]))
        if node == 0:
            node_text_after.append(f"CCP<br># of connections: {len(adjacencies[1])}")
        else:
            node_text_after.append(f"Intermediary #{node}<br># of connections: {len(adjacencies[1])}")

    node_trace_after.marker.color = node_adjacencies_after
    node_trace_after.text = node_text_after
    
    # Combine the Before CCP and After CCP graphs into subplots
    fig = go.Figure(data=[edge_trace_before, node_trace_before, edge_trace_after, node_trace_after],
                 layout=go.Layout(
                    title='Before CCP (left) vs After CCP (right)',
                    titlefont_size=16,
                    showlegend=False,
                    width=1200,
                    height=600,
                    margin=dict(b=20, l=5, r=5, t=40),
                    annotations=[ dict(text="Before CCP",
                                         showarrow=False,
                                         xref="paper", yref="paper",
                                         x=0.25, y= -0.1),
                                  dict(text="After CCP",
                                         showarrow=False,
                                         xref="paper", yref="paper",
                                         x=0.75, y= -0.1)
                                 ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                    )
                 )

    return fig

def create_risk_trend_chart(df_risk_exposure):
    # Generates a line chart showing hypothetical risk exposure over time.
    fig = px.line(df_risk_exposure, x="Date", y="Risk_Score", title="Risk Trend")
    return fig
