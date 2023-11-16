# Ler_Google_Scholar
Tentativa de extrair dados do google scholar de modo a obter uma conexão entre professores

## Objetivo inicial
A ideia começou com uma pergunta: Como posso saber quão bem conectado um professor é?

A resposta para essa pergunta pode ser particularmente interessante se essa conectividade representar um poder maior para uma recomendação ou indicação dentro do mundo acadêmico. Se você for um aluno que trabalhou com diversos professores e está interessado em ingressar na universidade X, faz sentido procurar, dentre os professores com os quais você teve contato, aqueles que possuem uma conexão mais forte com esta universidade para, assim, definir qual a melhor carta ou recomendação a ser utilizada em cada situação.

## Conexões
O que define uma conexão? Pesquisadores podem se conhecer em congressos, palestras, terem trabalhado juntos, etc. Porém tais formas de conexão podem ser muito difíceis de se mensurar. Assim, a forma que mensuramos aqui se define como "Houve artigo em coautoria destes pesquisadores? Se sim, há uma conexão"

## Google Scholar
O Scholar é um repositório com muita informação sobre artigos, citações e pesquisadores. No entanto, é conhecido por ser difícil de se extrair informação, com diversas limitações no scrap de dados, por exemplo.

## Tentativa
Utilizando a biblioteca Scholarly, consigo acessar a página de um determinado pesquisador e extrair todos os coautores listados ali. A partir daí, busca-se as informações desses coautores e seus coautores, em um processo recursivo. Com isso, conseguimos ver quais pesquisadores de uma determinada universidade trabalharam com pesquisadores de outra universidade e em quais temas. O objetivo é gerar uma extensa base de dados com pesquisadores e seus coautores.

## Limitações

### Conexões
Definir conexões como coautorias pode não ser significativo no mundo real. Além de estar enviesado para pesquisadores mais experientes em detrimento dos mais jovens, há outras formas de pesquisadores possuírem conexões que não exploraremos neste repositório.

### Coautores
Para que seja definida uma conexão, o pesquisador deve listar em seu Google Scholar os coautores com quem trabalhou (tal listagem não é automática). Com isso, diversos professores não utilizam a ferramenta de forma extensa e, consequentemente, não possuem seus coautores listados.

### Artigo por Artigo
Ao ler Pesquisador por Pesquisador, não enfrentamos nenhuma limitação do Scholar. No entanto, caso quiséssemos analisar artigo por artigo, tal limitação apareceria.
