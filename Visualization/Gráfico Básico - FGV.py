import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Supondo que você já tenha preenchido os DataFrames pesquisadores_df e coautores_df
# Supondo que a coluna 'Link' em pesquisadores_df seja o identificador único de cada professor
# Supondo que a coluna 'Nome' em pesquisadores_df contenha o nome de cada professor
# Supondo que a coluna 'Afiliação' em pesquisadores_df contenha a afiliação de cada professor

# Filtrar pesquisadores com afiliação na FGV
pesquisadores_fgv =pesquisadores_df[
    (pesquisadores_df['Afiliação'].str.contains('FGV')) |
    (pesquisadores_df['Afiliação'].str.contains('EPGE'))
]

co_autores_fgv = coautores_df[coautores_df["Link_Pesquisador"].isin(pesquisadores_fgv["Link"].values)]

pesquisadores_fgv_e_agregados = pesquisadores_df[
    (pesquisadores_df['Link'].isin(co_autores_fgv["Link_Pesquisador"].values)) |
    (pesquisadores_df['Link'].isin(co_autores_fgv["Link_Coautor"].values))
]


import networkx as nx
import matplotlib.pyplot as plt

# Supondo que você já tenha preenchido os DataFrames pesquisadores_df, coautores_df,
# pesquisadores_fgv, e co_autores_fgv conforme mencionado

# Crie um grafo vazio
G = nx.Graph()

# Adicione nós (pesquisadores) ao grafo a partir de pesquisadores_fgv_e_agregados
for index, row in pesquisadores_fgv_e_agregados.iterrows():
    professor_id = row['Link']
    professor_nome = row['Nome']
    G.add_node(professor_id, label=professor_nome)  # Use um atributo 'label' para armazenar o nome do professor

# Adicione arestas (conexões entre pesquisadores) com base em co_autores_fgv
for index, row in co_autores_fgv.iterrows():
    link_pesquisador = row['Link_Pesquisador']
    link_coautor = row['Link_Coautor']
    if G.has_node(link_pesquisador) and G.has_node(link_coautor):
        G.add_edge(link_pesquisador, link_coautor)

# Crie o gráfico
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Define a disposição dos nós
labels = nx.get_node_attributes(G, 'label')  # Obtém os nomes dos professores a partir do atributo 'label'
nx.draw(G, pos, labels=labels, node_size=100, font_size=8, with_labels=True)

plt.title("Grafo de Coautores com Nomes como Rótulos")
plt.show()

coautores_df[coautores_df["Link_Pesquisador"]=="UryHd5AAAAAJ"]