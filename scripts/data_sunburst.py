import pandas as pd
import plotly.graph_objects as go
import numpy as np


pythonanywhere_file_tree = ''
#pythonanywhere_file_tree = '/home/diogocarapito/bi_indicadores/'

df_todos_indicadores = pd.read_csv(pythonanywhere_file_tree + 'data/scrapped_indicadores.csv')
usf_ucsp_para_idg = pd.read_csv(pythonanywhere_file_tree + 'data/usf_ucsp_indicadores_2022_comimpactoIDG.csv')
df_todos_indicadores_filtrado = df_todos_indicadores[df_todos_indicadores['id'].isin(usf_ucsp_para_idg['indicador'].values.tolist())]
df = df_todos_indicadores_filtrado.drop(columns=['codigo','codigo_siars','objetivo','formula','unidade_de_medida', 'output','estado_do_indicador','tipo_de_indicador','area_clinica','inclusao_de_utentes_no_indicador','prazo_para_registos','link'])

df_area = pd.DataFrame({
    'id_indicador':[1001,1002,1003,1004],
    'id':df.area.drop_duplicates(),
    'label':df.area.drop_duplicates(),
    'parent':[np.nan for each in df.area.drop_duplicates()],
    'value':[50,10,20,10],
    'tipo': ['área' for each in df.area.drop_duplicates()],
})
df_area_2 = pd.DataFrame({
    'id_indicador':[1005],
    'id': ['Atividade Científica'],
    'label': ['Atividade Científica'],
    'parent':[np.nan],
    'value':[10],
    'tipo': ['área'],
})
df_area = pd.concat([df_area,df_area_2])

df_subarea = pd.DataFrame({
    'id_indicador':[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
    'id':df.subarea.drop_duplicates(),
    'label':df.subarea.drop_duplicates(),
    'parent':[df.loc[each]['area'] for each in df.subarea.drop_duplicates().index],
    'value':[10,10,10,10,8,2,8,8,8,4],
    'tipo': ['subárea' for each in df.subarea.drop_duplicates().index],
})
df_subarea_2 = pd.DataFrame({
    'id':[
        'Satisfação de Utentes',
        'Formação Externa',
        'Autoria de Artigos Escritos',
        'Trabalhos de Investigação',
    ],
    'id_indicador':[
        2021,
        2022,
        2023,
        2024],
    'label':[
        'Satisfação de Utentes',
        'Formação Externa',
        'Autoria de Artigos Escritos',
        'Trabalhos de Investigação'],
    'parent':[
        'Desempenho',
        'Formação',
        'Atividade Científica',
        'Atividade Científica'],
    'value':[
        10,
        2,
        5,
        5],
    'tipo':['subárea','subárea','subárea','subárea']
})
df_subarea = pd.concat([df_subarea,df_subarea_2])


df_dimensao = pd.DataFrame({
    'id_indicador':range(2025,2048),
    'id':df.dimensao.drop_duplicates(),
    'label':df.dimensao.drop_duplicates(),
    'parent':[df.loc[each]['subarea'] for each in df.dimensao.drop_duplicates().index],
    'value':[
        1, #Personalização
        1, #Cobertura ou Utilização
        2.5, #Saúde da Mulher
        2.5, #Hipertensão Arterial
        2.5, #Saúde do Idoso
        2.5, #Saúde do Adulto
        2.5, #Diabetes Mellitus
        2.5, #Doenças Aparelho Respiratório
        2.5, #Saúde Infantil e Juvenil
        5, #Prescrição Farmacoterapêutica
        3, #Prescrição MCDT
        4, #Tempos Máximos de Resposta Garantidos Acesso
        1, #Consulta no Próprio Dia
        1, #Distribuição das Consultas Presenciais no Dia
        2.5, #Multimorbilidade e Outros Tipos de Doenças
        8, #Serviços Assistenciais
        1.6, #Governação Clínica
        2, #Acesso
        6, #Prog. Melh. Contínua Qual. e Proc. Assist. Int...
        4, #Formação da Equipa Multiprofissional
        4, #Formação de Internos e Alunos
        3.2, #Segurança de Utentes
        4, #Participação do Cidadão
    ],
    'tipo':['dimensão' for each in df.dimensao.drop_duplicates().index],
})

df_dimensao = df_dimensao.drop(index=[378,376])
df_dimensao_2 = pd.DataFrame({
    'id_indicador':[2049, 2050],
    'id':['Serviços de Carácter Assistencial','Acesso MCQ'],
    'label':['Serviços de Carácter Assistencial','Acesso MCQ'],
    'parent':['Serviços Assistenciais','Melhoria Contínua'],
    'value':[8,2],
    'tipo':['dimensão','dimensão']
    },index=[376,378],
)

df_dimensao_3 = pd.DataFrame({
    'id':[
        'Atendimento Telefónico',
        'Trajeto do Utente na Unidade Funcional',
        'Prescrição de Cuidados',
        'Outras Atividades não Assistenciais',
        'Segurança de Profissionais',
        'Gestão do Risco',],
    'id_indicador':[2051,2052, 2053, 2054, 2055, 2056],
    'label':[
        'Atendimento Telefónico',
        'Trajeto do Utente na Unidade Funcional',
        'Prescrição de Cuidados',
        'Outras Atividades não Assistenciais',
        'Segurança de Profissionais',
        'Gestão do Risco',
    ],
    'parent':[
        'Acesso',
        'Acesso',
        'Qualificação da Prescrição',
        'Serviços não Assistenciais',
        'Segurança',
        'Segurança',

    ],
    'value':[
        1,
        1,
        2,
        0.4,
        2.4,
        2.4,],
    'tipo':['dimensão','dimensão','dimensão','dimensão','dimensão','dimensão'],

},
    index=[0,0,0,0,0,0]
)
df_dimensao = pd.concat([df_dimensao,df_dimensao_2,df_dimensao_3])

print(df_dimensao)

df_indicadores = pd.DataFrame({
    'id_indicador': df.id.drop_duplicates(),
    'id':df.nome_abreviado.drop_duplicates(),
    'label':[str(row['id']) + ' - ' + row['nome_abreviado'] for index, row in df.drop_duplicates().iterrows()],
    'parent':[df.loc[each]['dimensao'] for each in df.nome_abreviado.drop_duplicates().index],
    'tipo': ['indicador' for each in df.nome_abreviado.drop_duplicates().index],
})


lista = []
for each, item in df_indicadores.iterrows():
    #print(item['parent'])
    denominador = df_indicadores[df_indicadores['parent'] == item['parent']]['parent'].count()
    try:
        numerador = float(df_dimensao[df_dimensao['label'] == item['parent']]['value'].values)
    except:
        numerador = 0
    valor = numerador / denominador
    lista.append(valor)

df_indicadores['value'] = lista


df_sunburst = pd.concat([df_area,df_subarea,df_dimensao,df_indicadores])
#df_sunburst = pd.concat([df_area,df_subarea,df_dimensao])
#df_sunburst = pd.concat([df_area,df_subarea])
#df_sunburst = df_area

df_sunburst = df_sunburst.set_index('id_indicador')
print(df_sunburst)
df_sunburst.to_csv('../data/sunburst_data.csv',index=True)