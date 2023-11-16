## importações 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

from scholarly import scholarly

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results

##Criando a base de dados para salvar informações
pesquisadores_df = pd.DataFrame(columns=['ID', 'Nome', 'Afiliação', 'Link'])
coautores_df = pd.DataFrame(columns=['Link_Pesquisador', 'Link_Coautor'])
Pesquisadores_Label=pd.DataFrame(columns=['Link_Pesquisador', 'Label'])
Guia_bot_df=pd.DataFrame(columns=['Link', 'Ja_visto'])

# Retrieve the first result from the iterator

start_professor='Carlos Eugênio da Costa'

limit_search=2
loop=0

while loop < limit_search:
    if loop == 0:
        start_professor=start_professor
        search_query = scholarly.search_author(start_professor)
    else:
        # Filtrar a base Guia_bot_df para obter o primeiro valor com Ja_visto igual a False
        primeiro_link_nao_visto = Guia_bot_df.loc[Guia_bot_df['Ja_visto'] == False, 'Link'].iloc[0]

        # Marcar o primeiro link como visto (alterar o valor de Ja_visto para True)
        Guia_bot_df.loc[Guia_bot_df['Link'] == primeiro_link_nao_visto, 'Ja_visto'] = True
        start_professor_id=primeiro_link_nao_visto #### trocar pra filtro de já visto
        search_query = scholarly.search_author_id(start_professor_id)
    
        
    first_author_result = next(search_query)
    print(first_author_result)
    link=first_author_result['scholar_id']

    if link not in pesquisadores_df['Link'].values:
        novo_id = len(pesquisadores_df) + 1
        Nome_pesquisador = first_author_result['name']
        Afiliacao_pesquisador = first_author_result['affiliation']
    
            # Crie um DataFrame temporário para os novos dados
        novo_pesquisador = pd.DataFrame({
                'ID': [novo_id],
                'Nome': [Nome_pesquisador],
                'Afiliação': [Afiliacao_pesquisador],
                'Link': [link]
            })

            # Concatene o novo DataFrame com pesquisadores_df
        pesquisadores_df = pd.concat([pesquisadores_df, novo_pesquisador], ignore_index=True)

  

            # Loop para coautores
        coautores=scholarly.fill(first_author_result, sections=['coauthors'])['coauthors']
        for coautor in coautores:
            link_coautor = coautor['scholar_id']
            if link_coautor not in Guia_bot_df['Link'].values:
                novo_coautor = pd.DataFrame({
                        'Link': [link_coautor],
                        'Ja_visto': [False]
                    })
                Guia_bot_df = pd.concat([Guia_bot_df, novo_coautor], ignore_index=True)
            if link_coautor not in pesquisadores_df['Link'].values:
                novo_id = len(pesquisadores_df) + 1
                Nome_pesquisador = coautor['name']
                Afiliacao_pesquisador = coautor['affiliation']
        

                    # Crie um DataFrame temporário para os novos dados
                novo_pesquisador = pd.DataFrame({
                        'ID': [novo_id],
                        'Nome': [Nome_pesquisador],
                        'Afiliação': [Afiliacao_pesquisador],
                        'Link': [link_coautor]
                    })
                pesquisadores_df = pd.concat([pesquisadores_df, novo_pesquisador], ignore_index=True)
            pd_temp_pesquisador_coautor=pd.DataFrame({
                'Link_Pesquisador': [link],
                'Link_Coautor': [link_coautor],
               })
            coautores_df = pd.concat([coautores_df, pd_temp_pesquisador_coautor], ignore_index=True)
    if link not in Pesquisadores_Label['Link_Pesquisador'].values:

        labels_pesquisador=first_author_result['interests']
                  # Loop para labels_pesquisador
        for x in labels_pesquisador:
            label = x
            novo_label = pd.DataFrame({
                    'ID_Pesquisador': [novo_id],
                    'Label': [label]
                })
            Pesquisadores_Label = pd.concat([Pesquisadores_Label, novo_label], ignore_index=True)

    loop=loop+1





coautores=scholarly.fill(first_author_result, sections=['coauthors'])['coauthors']
for coautor in coautores:
            link_coautor = coautor['scholar_id']
            print(link_coautor)
            print(10)