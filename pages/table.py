import dash
from dash import Dash, dcc, html, callback, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_dash

dash.register_page(
    __name__,
    path='/table',
    title='tabela indicadores',
    name='tabela',
    order=2,
)

# read_csv read no PyCharm!!
df_todos_indicadores = pd.read_csv('data/scrapped_indicadores.csv')
usf_ucsp_para_idg = pd.read_csv('data/usf_ucsp_indicadores_2022_comimpactoIDG.csv')
#usf_ucsp_sem_idg = pd.read_csv('data/usf_ucsp_indicadores_2022_semimpactoIDG.csv')

# read_csv read no PythonAnywhere!!
'''
df_todos_indicadores = pd.read_csv('/home/diogocarapito/bi_indicadores/data/scrapped_indicadores.csv')
usf_ucsp_para_idg = pd.read_csv('/home/diogocarapito/bi_indicadores/data/usf_ucsp_indicadores_2022_comimpactoIDG.csv')
usf_ucsp_sem_idg = pd.read_csv('/home/diogocarapito/bi_indicadores/data/usf_ucsp_indicadores_2022_semimpactoIDG.csv')
'''

df_todos_indicadores_filtered = df_todos_indicadores[df_todos_indicadores['id'].isin(usf_ucsp_para_idg['indicador'].values.tolist())]

#table = dash_table.DataTable(df_todos_indicadores.to_dict('records'), [{"name": i, "id": i} for i in df_todos_indicadores.columns])


'''
table = dbc.Table.from_dataframe(
    df_todos_indicadores_filtered,
    striped=True,
    bordered=True,
    hover=False,
    id='tabela_indicadores'
)
'''

'''
table = dash_table.DataTable(
    id='tabela_indicadores',
    columns=[
        {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
        if i == "iso_alpha3" or i == "year" or i == "id"
        else {"name": i, "id": i, "deletable": True, "selectable": True}
        for i in df_todos_indicadores_filtered.columns
    ],
    data=df_todos_indicadores_filtered.to_dict('records'),  # the contents of the table
    editable=True,              # allow editing of data inside all cells
    filter_action="native",     # allow filtering of data by user ('native') or not ('none')
    sort_action="native",       # enables data to be sorted per-column by user or not ('none')
    sort_mode="single",         # sort across 'multi' or 'single' columns
    column_selectable="multi",  # allow users to select 'multi' or 'single' columns
    row_selectable="multi",     # allow users to select 'multi' or 'single' rows
    row_deletable=True,         # choose if user can delete a row (True) or not (False)
    selected_columns=[],        # ids of columns that user selects
    selected_rows=[],           # indices of rows that user selects
    page_action="native",       # all data is passed to the table up-front or not ('none')
    page_current=0,             # page number that user is on
    page_size=6,                # number of rows visible per page
    style_cell={                # ensure adequate header width when text is shorter than cell's text
        'minWidth': 95, 'maxWidth': 95, 'width': 95
    },
    style_cell_conditional=[    # align text columns to left. By default they are aligned to right
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['country', 'iso_alpha3']
    ],
    style_data={                # overflow cells' content into multiple lines
        'whiteSpace': 'normal',
        'height': 'auto'
    }
),
'''
table = dash_table.DataTable(
    id='tabela_indicadores',
    data=df_todos_indicadores_filtered.to_dict('records'),
    columns=[{"name": i, "id": i} for i in df_todos_indicadores_filtered.columns],
    page_size=10,
    style_cell={  # ensure adequate header width when text is shorter than cell's text
        'minWidth': 30, 'maxWidth': 360, 'width': 95
    },
    style_data={  # overflow cells' content into multiple lines
        'whiteSpace': 'normal',
        'height': 'auto'
    }
)

table_filters = ['todos', 'USF/UCSP com impacto IDG', 'USF/UCSP sem impacto IDG']

filters = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                options=table_filters,
                value=table_filters[0],
                inline=True,
                id='radio_tabela'
            )
        ])
    ])
])

container_1 = dbc.Container([
    html.H3('dashboard'),
    html.Br(),
    filters,
    dbc.Container([table]),
], fluid=True,)


def layout():
    return html.Div([
        dbc.Row([
            dbc.Col([
                container_1,
                html.Br(),
            ], width={"size": 10, "offset": 0},)
        ])

    ])


'''@callback(
    Output('tabela_indicadores', 'data'),
    Input('radio_tabela', 'value'),
)


def table_update(radio_tabela):

    if radio_tabela == 'Todos':
        df_todos_indicadores_novo = df_todos_indicadores
    elif radio_tabela == 'USF/UCSP com impacto IDG':
        df_todos_indicadores_novo = df_todos_indicadores
    elif radio_tabela == 'USF/UCSP sem impacto IDG':
        df_todos_indicadores_novo = df_todos_indicadores
    tabela_indicadores = dash_table.DataTable(

    )

    return tabela_indicadores'''