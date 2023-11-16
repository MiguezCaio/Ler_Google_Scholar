## importações 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

##Criando a base de dados para salvar informações
pesquisadores_df = pd.DataFrame(columns=['ID', 'Nome', 'Afiliação', 'Link'])
coautores_df = pd.DataFrame(columns=['ID_Pesquisador', 'ID_Coautor'])
Pesquisadores_Label=pd.DataFrame(columns=['ID_Pesquisador', 'Label'])
Guia_bot_df=pd.DataFrame(columns=['Link', 'Ja_visto'])


link1="https://scholar.google.com/citations?user=BdmHCbcAAAAJ&hl=pt-BR&oi=ao"
def coletar_informacoes_pesquisador(link_pesquisador,Pesquisadores_Label, pesquisadores_df, coautores_df, Guia_bot_df):
    # Configura o driver do Selenium
    nav = webdriver.Chrome()
    nav.get(link_pesquisador)
    
    try:
        # Coleta informações do pesquisador principal
        Nome_pesquisador = nav.find_element(By.ID, "gsc_prf_in").text
        Afiliacao_pesquisador = nav.find_element(By.CLASS_NAME, "gsc_prf_ila").text
        labels_pesquisador=nav.find_elements(By.ID,"gsc_prf_int")

        # Verifique se o link do pesquisador principal já existe na base de dados
        if link not in pesquisadores_df['Link'].values:
        # Adicione o link do pesquisador principal à base de dados
            novo_id = len(pesquisadores_df) + 1
            pesquisadores_df = pesquisadores_df.append({'ID': novo_id, 'Nome': Nome_pesquisador, 'Afiliação': Afiliacao_pesquisador, 'Link': link}, ignore_index=True)
            for x in labels_pesquisador:
                label=x.text
                Pesquisadores_Label = Pesquisadores_Label.append({'ID_Pesquisador': novo_id, 'Label': label}, ignore_index=True)

        # Percorra a lista de coautores e adicione-os à base de dados de coautores
        for coautor in coautores:
            link_element = coautor.find_element(By.CSS_SELECTOR, 'a')
            link_coautor = link_element.get_attribute('href')
            if link_coautor not in Guia_bot_df['Link'].values:
                Guia_bot_df = Guia_bot_df.append({'Link': link_coautor, 'Ja_visto': False}, ignore_index=True)
    except Exception as e:
        print(f"Erro ao coletar informações do pesquisador {link_pesquisador}: {str(e)}")


      # Feche o navegador quando terminar
    nav.quit()
    return Pesquisadores_Label, pesquisadores_df, coautores_df, Guia_bot_df


coletar_informacoes_pesquisador(link1,Pesquisadores_Label, pesquisadores_df, coautores_df, Guia_bot_df)

# ... (continuação do código)

##coautores_df = coautores_df.append({'ID_Pesquisador': link, 'ID_Coautor': link_coautor}, ignore_index=True)


