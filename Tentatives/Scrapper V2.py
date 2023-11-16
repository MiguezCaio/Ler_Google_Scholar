## importações 
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

##Criando a base de dados para salvar informações
pesquisadores_df = pd.DataFrame({
    'ID': [1],
    'Nome': ['Pesquisador A'],
    'Afiliação': ['Universidade X'],
    'Área de Pesquisa': ['Ciência da Computação']
})
coautores_df = pd.DataFrame({
    'ID_Pesquisador': [1, 1, 2, 3],
    'ID_Coautor': [2, 3, 1, 2]
})
Pesquisadores_Label=pd.DataFrame({
    'ID_Pesquisador': "",
    'Label': ""
    })





nav=webdriver.Chrome() #abrir o navegador
nav.get("https://scholar.google.com/citations?user=BdmHCbcAAAAJ&hl=pt-BR&oi=ao") #Entra no site do professor

#Primeiro vamos pegar as características básicas dele

Nome_pesquisador= nav.find_element(By.ID,"gsc_prf_in").text
Afiliacao_pesquisador= nav.find_element(By.CLASS_NAME,"gsc_prf_ila").text
labels_pesquisador=nav.find_elements(By.ID,"gsc_prf_int")


# Localize o elemento ul com a classe desejada
lista_pesquisadores = nav.find_element(By.CSS_SELECTOR, 'ul.gsc_rsb_a')

# Dentro da lista de pesquisadores, encontre todos os elementos li que representam cada pesquisador
pesquisadores = lista_pesquisadores.find_elements(By.CSS_SELECTOR, 'li')

# Para cada pesquisador, localize o elemento a que contém o link da página de perfil
for pesquisador in pesquisadores:
    link_element = pesquisador.find_element(By.CSS_SELECTOR, 'a')
    link = link_element.get_attribute('href')
    print("Link do pesquisador:", link)
