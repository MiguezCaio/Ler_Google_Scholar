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

start_professor='Daron Acemoglu'
start_professor_id="l9Or8EMAAAAJ"

limit_search=10
loop=0

while loop < limit_search:
    if loop == 0:
        #start_professor = start_professor
        start_professor_id=start_professor_id
        search_query = scholarly.search_author_id(start_professor_id)
        first_author_result=search_query
        print(loop)
        print(first_author_result['name'])
    else:
        # Filtrar a base Guia_bot_df para obter o primeiro valor com Ja_visto igual a False
        primeiro_link_nao_visto = Guia_bot_df.loc[Guia_bot_df['Ja_visto'] == False, 'Link'].iloc[0]

        # Marcar o primeiro link como visto (alterar o valor de Ja_visto para True)
        Guia_bot_df.loc[Guia_bot_df['Link'] == primeiro_link_nao_visto, 'Ja_visto'] = True
        start_professor_id = primeiro_link_nao_visto  # trocar para filtro de já visto
        search_query = scholarly.search_author_id(start_professor_id)
        first_author_result=search_query
        print(first_author_result['name'])
        print(loop)
    try:
        
        link = first_author_result['scholar_id']

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
        coautores = scholarly.fill(first_author_result, sections=['coauthors'])['coauthors']
        for coautor in coautores:
            link_coautor = coautor['scholar_id'] #
            if link_coautor not in Guia_bot_df['Link'].values:
                novo_coautor = pd.DataFrame({
                        'Link': [link_coautor],
                        'Ja_visto': [False]
                    })
                Guia_bot_df = pd.concat([Guia_bot_df, novo_coautor], ignore_index=True)#
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
            pd_temp_pesquisador_coautor = pd.DataFrame({
                    'Link_Pesquisador': [link],
                    'Link_Coautor': [link_coautor],
                })
            coautores_df = pd.concat([coautores_df, pd_temp_pesquisador_coautor], ignore_index=True)
        if link not in Pesquisadores_Label['Link_Pesquisador'].values:

            labels_pesquisador = first_author_result.get('interests', [])  # Certifique-se de lidar com o caso em que 'interests' pode ser ausente
            # Loop para labels_pesquisador
            for label in labels_pesquisador:
                novo_label = pd.DataFrame({
                    'Link_Pesquisador': [link],
                    'Label': [label]
                })
                Pesquisadores_Label = pd.concat([Pesquisadores_Label, novo_label], ignore_index=True)

        loop = loop + 1
    except StopIteration:
        if loop == 0: 
            erro=1
            print("A pesquisa não retornou resultados para:", start_professor)
        else:
            erro=2
            print("A pesquisa não retornou resultados para:", start_professor_id)
        loop = loop + 1
        continue  # Continue com a próxima iteração do loop se não houver mais resultados de pesquisa





# Supondo que você tenha preenchido as quatro bases de dados pesquisadores_df, coautores_df, Pesquisadores_Label e Guia_bot_df

# Supondo que você tenha preenchido as quatro bases de dados pesquisadores_df, coautores_df, Pesquisadores_Label e Guia_bot_df

# Especifique o caminho completo para a pasta onde deseja salvar os arquivos CSV
caminho_pasta = r'C:\Users\migue\OneDrive - Fundacao Getulio Vargas - FGV\Projetos\Scrapper Google Scholar\Scrapper_Google_Sholar\Data'

# Salve as bases de dados em arquivos CSV com codificação UTF-8
pesquisadores_df.to_csv(f'{caminho_pasta}/pesquisadores.csv', index=False, encoding='utf-8')
coautores_df.to_csv(f'{caminho_pasta}/coautores.csv', index=False, encoding='utf-8')
Pesquisadores_Label.to_csv(f'{caminho_pasta}/pesquisadores_label.csv', index=False, encoding='utf-8')
Guia_bot_df.to_csv(f'{caminho_pasta}/guia_bot.csv', index=False, encoding='utf-8')




print(titulo)
search_query_2 = scholarly.search_pubs(titulo)
len(search_query_2)

##Salvar as bases













