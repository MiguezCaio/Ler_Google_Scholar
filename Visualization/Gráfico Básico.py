
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Supondo que você já tenha preenchido os DataFrames pesquisadores_df e coautores_df
# Supondo que a coluna 'Link' em pesquisadores_df seja o identificador único de cada professor
# Supondo que a coluna 'Nome' em pesquisadores_df contenha o nome de cada professor

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

# Calcule o tamanho (proporcional ao grau) de cada nó
node_size = [G.degree(node) * 20 for node in G.nodes()]

# Defina cores diferentes para os nós com base na afiliação dos pesquisadores
afiliacoes_unicas = pd.unique(pesquisadores_df['Afiliação'])
color_map = {}
for i, afiliacao in enumerate(afiliacoes_unicas):
    color_map[afiliacao] = plt.cm.tab20(i)

node_colors = [color_map[pesquisadores_df.at[node, 'Afiliação']] for node in G.nodes()]

# Remova rótulos de nós com menos de 20 conexões
nos_com_menos_de_20_conexoes = [node for node in G.nodes() if G.degree(node) < 10]
labels = {node: nome_professores[node] if node not in nos_com_menos_de_20_conexoes else '' for node in G.nodes()}

# Agora você tem um grafo onde todos os pesquisadores são exibidos com nomes como rótulos e nós coloridos com base na afiliação dos pesquisadores

# Você pode visualizar o grafo usando Matplotlib
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Define a disposição dos nós
nx.draw(G, pos, labels=labels, node_size=node_size, node_color=node_colors, font_size=8)
plt.title("Grafo de Coautores com Nomes como Rótulos e Cores de Afiliação")
plt.show()
