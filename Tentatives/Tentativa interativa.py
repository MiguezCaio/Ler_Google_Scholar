import pandas as pd
import networkx as nx
import plotly.graph_objs as go

# Supondo que você já tenha preenchido os DataFrames pesquisadores_df e coautores_df
# Supondo que a coluna 'Link' em pesquisadores_df seja o identificador único de cada professor

# Crie um grafo vazio
G = nx.Graph()

# Crie um dicionário para armazenar o nome de cada professor
nome_professores = {}

# Adicione nós (professores) ao grafo a partir de pesquisadores_df
for index, row in pesquisadores_df.iterrows():
    professor_id = row['Link']
    professor_nome = row['Nome']
    nome_professores[professor_id] = professor_nome  # Armazene o nome do professor no dicionário
    G.add_node(professor_id)

# Adicione arestas (conexões entre professores) com base em coautores_df
for index, row in coautores_df.iterrows():
    link_pesquisador = row['Link_Pesquisador']
    link_coautor = row['Link_Coautor']
    if G.has_node(link_pesquisador) and G.has_node(link_coautor):
        G.add_edge(link_pesquisador, link_coautor)

# Crie uma lista de nós a serem exibidos inicialmente (com grau maior que 20)
nodos_iniciais = [node for node in G.nodes() if G.degree(node) > 20]

# Calcule o layout circular do gráfico
pos = nx.circular_layout(G)

# Crie um grafo Plotly
edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=10,
        colorbar=dict(
            thickness=15,
            title='Grau',
            xanchor='left',
            titleside='right'
        )
    )
)

for node in G.nodes():
    x, y = pos[node]
    node_trace['x'] += (x,)
    node_trace['y'] += (y,)
    node_trace['text'] += (nome_professores[node],)
    node_trace['marker']['color'] += (G.degree(node),)

# Crie uma figura Plotly
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=0, l=0, r=0, t=0),
                ))

# Exiba a figura
fig.show()
