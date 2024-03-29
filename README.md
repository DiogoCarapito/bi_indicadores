##NOTE
precursor project of [mgfhub](https://github.com/DiogoCarapito/mgfhub) that was deployed with [pythonanywhere.com](https://www.pythonanywhere.com)




# bi_indicadores

## Problema
- A compreensão e visualização da forma como os inidcadores de desempenho funcionam nos cuidados de saúde primários é difícil
- É dificil compreender que indicadores existem
- É dificil entender como o IDG é calculado e de que forma é que cada indicador o influência
- Saber quais as áreas necessitam de ser optimizadas não é apresentada de forma clara, tornado dificil tomar decisões de como gerir os recursos
<img width="394" alt="Captura de ecrã 2022-11-15, às 20 41 15" src="https://user-images.githubusercontent.com/43778648/202021100-7f83e3fd-1c82-4938-8c33-e89c9f4dee2e.png">
lol


## Objectivo
- Produzir uma ferramenta de analise dos indicadores das unidades de saude familiares dos cuidados de saude primários
- Oferecer uma vizualização intiuitiva, que permite exploração da forma como o desempenho é medido e calculado
- auxiliar na toma de decisão para otimizar os recursos tendo como base o principio dos incentivos existente nos cuidados de saude primários. 

## Origem dos dados
- SDM (webscrapping)
- BI-CSP (por intermédio de upload)
- Documentação da ACSS (Operacionalização da Contratualização nos Cuidados de Saúde Primários)

## To-do List
  - [x] escrever o README.md 

extração de dados
  - [x] web scrapper dos 448 indicadores do SDM para csv
  - [x] extrair tabela das paginas 76-80 do pdf das contratualizações para csv com os intervalos aceitavel e esperado em 4 colunas
  - [x] extrair (com scrapper) indicadores com impacto e sem impacto no IDG


layout
  - [x] setup da pagina no pythonanywere pelo framework flask
  - [x] setup do ambiente dash, num sistema de multipaginas
  - [x] deploy das principais visualizaçõs
  - [ ] adicionar foot notes


pagina 'indicadores'
  - [x] organização dos indicadores existentes em tabela, com campo de filtro e pesquisa
  - [x] incluir link para o SDM em cada indicador na tabela
  - [ ] pensar noutros filtros possíveis
  - [ ] otimizar o campo de pesquisa para sucesos quando se pesquisa pelo numero de indicador
  - [ ] otimizar quantas colunas e quais colunas


pagina 'sunburst'
  - [x] sunburst com pesos dos indicadores e areas corretas
  - [x] dropdown menu ligado ao upload 
  - [x] conecção entre upload e sunburst
  - [x] modificar as cores
  - [ ] mudar fundo para mesmo da pagina


pagina 'upload'
  - [x] configurar a ferramenta de upload
  - [x] confirmação se é a tabela correta
  - [ ] pssobilidade de fazer upload de indicadores da unidade ou por médico
  - [x] processamento do doc upload em dataframe
  - [x] construir a visualização (sunburst+tabela, lado lado e fundir com a pagina sunburst)


pagina 'blog'
  - [x] definir um for loop para por a partir de um csv com cada entrada de blog em dash/html
  - [ ] escrever as entradas do blog em atraso


pagina 'about'
  - [ ] escrever a pagina about

