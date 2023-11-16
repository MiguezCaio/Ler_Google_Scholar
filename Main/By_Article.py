## importações 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

from scholarly import scholarly

# Especifique o caminho completo para cada arquivo CSV
caminho_pesquisadores = r'C:\Users\migue\OneDrive - Fundacao Getulio Vargas - FGV\Projetos\Scrapper Google Scholar\Scrapper_Google_Sholar\Data\pesquisadores.csv'
caminho_coautores = r'C:\Users\migue\OneDrive - Fundacao Getulio Vargas - FGV\Projetos\Scrapper Google Scholar\Scrapper_Google_Sholar\Data\coautores.csv'
caminho_pesquisadores_label = r'C:\Users\migue\OneDrive - Fundacao Getulio Vargas - FGV\Projetos\Scrapper Google Scholar\Scrapper_Google_Sholar\Data\pesquisadores_label.csv'
caminho_guia_bot = r'C:\Users\migue\OneDrive - Fundacao Getulio Vargas - FGV\Projetos\Scrapper Google Scholar\Scrapper_Google_Sholar\Data\guia_bot.csv'

# Leia os arquivos CSV com a codificação UTF-8
pesquisadores_df = pd.read_csv(caminho_pesquisadores, encoding='utf-8')
coautores_df = pd.read_csv(caminho_coautores, encoding='utf-8')
pesquisadores_label_df = pd.read_csv(caminho_pesquisadores_label, encoding='utf-8')
guia_bot_df = pd.read_csv(caminho_guia_bot, encoding='utf-8')


 #Filtrar pesquisadores com afiliação na FGV
pesquisadores_fgv =pesquisadores_df[
    (pesquisadores_df['Afiliação'].str.contains('FGV')) |
    (pesquisadores_df['Afiliação'].str.contains('EPGE'))
]

publicacoes=pd.DataFrame(columns=['ID', 'Titulo', 'Autores_id', 'Autores','Ano','abstract','revista','citacoes_num','citado_por'])

co_autores_fgv = coautores_df[coautores_df["Link_Pesquisador"].isin(pesquisadores_fgv["Link"].values)]

pesquisadores_fgv_teste=pesquisadores_fgv.head(2)
pesquisadores_fgv_teste

for ind in pesquisadores_fgv_teste.index:
    print(ind)
    print(pesquisadores_fgv_teste["Nome"][ind])
    search_query = scholarly.search_author_id(pesquisadores_fgv_teste["Link"][ind])
    author=search_query
    teste=scholarly.fill(author, sections=['publications'])["publications"]
    print(teste)
    for x in teste:
        titulo=x["bib"]["title"]
        ano=x["bib"]["pub_year"]
        if titulo not in publicacoes['Titulo'].values:
            novo_id=len(publicacoes)+1
            try:
        
                search_query_2 = scholarly.search_pubs(titulo)
                pub=next(search_query_2)
                autores=pub["bib"]["author"]
                novo_id=len(publicacoes)+1
                abstract=pub["bib"]["abstract"]
                revista=pub["bib"]["venue"]
                autores_id=pub["author_id"]
                citacoes_num=pub["num_citations"]
                cited_by=pub["citedby_url"]


            #dataframe temporário

                publicacao = pd.DataFrame({
                    'ID': [novo_id],
                    'Titulo': [titulo],
                    'Autores_id': [autores_id],
                    'Autores': [autores],
                    'Ano': [ano],
                    'Abstract': [abstract],
                    'Revista': [revista],
                    'Citacoes_num': [citacoes_num],
                    'Citado_por': [cited_by]
                })

                publicacoes = pd.concat([publicacoes, publicacao], ignore_index=True)

            except StopIteration:
                print(f"Não foi possível encontrar informações para a publicação: {titulo}")
            
                ano=x["bib"]["pub_year"]
            
                publicacao_erro = pd.DataFrame({
                    'ID': [novo_id],
                    'Titulo': [titulo],
                    'Ano': [ano]
                })

                publicacoes = pd.concat([publicacoes, publicacao_erro], ignore_index=True)

print(author)
teste=scholarly.fill(author, sections=['publications'])["publications"]
teste