from data_treatment import * # Importa o tratamento de dados
from app import * # Importa a aplicação dash

from dash_bootstrap_templates import ThemeSwitchAIO # Importa os componentes para a mudança de tema

url_theme1 = dbc.themes.FLATLY # Tema claro
url_theme2 = dbc.themes.VAPOR # Tema escuro

template_theme1 = 'flatly' # Tema claro
template_theme2 = 'vapor' # Tema escuro

track_options = [{'label' : x, 'value': x} for x in df['Track Name'].unique()] # Pega todos os valores unicos de 'Track Name' e salva-os em uma variavel
artist_options = [{'label': x, 'value': x} for x in df['Artist Name'].unique()] # Pega todos os valores unicos de 'Artist Name' e salva-os em uma variavel
year_options = [{'label': x, 'value': x} for x in df['Released Year'].unique()] # Pega todos os valores unicos de 'Released Year' e salva-os em uma variavel

app.layout = dbc.Container([ # Container do Bootstrap para fazer o layout
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id = 'theme', themes = [url_theme1, url_theme2]), # Componente ThemeSwitchAIO para alternar entre temas
            html.H3('Most Streamed Spotify Songs', className = 'text-center'), # Titulo principal
            html.Br(), # Espaço entre os elementos
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Tracks x Streams', className = 'text-center'), # Titulo do grafico
            html.H3('Selected Tracks', className = 'text-center'), # Titulo do dropdown
            dcc.Dropdown(
                id = 'tracks', # id do Dropdown
                value = [track['label'] for track in track_options[:20]], # Valores iniciais do dropdown. Vai puxar os 20 primeiros valores das opções disponiveis
                multi = True, # Permite multiplos inputs
                options = track_options, # Opções do dropdown
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configurações visuais
            )
        ]),
        dbc.Row([
            html.Button("Show/Hide Tracks", id = "toggle-tracks-button", style = {'margin-left': '12px'}) # Botão usado para esconder e mostrar o dropdown
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'bar-graph'), # Local onde o grafico em barra será plotado
            html.Br(),
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Track x Streams (%)', className = 'text-center'), # Titulo do grafico
            html.H3('Selected Tracks', className = 'text-center'), # Titulo do dropdown
            dcc.Dropdown(
                id = 'tracks2', # id do dropdown
                value = [track['label'] for track in track_options[:10]], # Valores iniciais do dropdown. Vai puxar os primeiros 10 valores das opções disponiveis
                multi = True, # Permite multiplos inputs
                options = track_options, # Opcoes do dropdown
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configurações visuais
            )
        ]),
        dbc.Row([
            html.Button("Show/Hide Tracks", id = 'toggle-tracks-button2', style = {'margin-left': '12px'}) # Botao usado para esconder e mostrar o dropdown
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'pie-chart'), # Local onde será plotado o grafico pizza
            html.Br(),
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Date x BPM', className = 'text-center'), # Titulo do grafico
            html.H3('Selected Years', className = 'text-center'), # Titulo do dropdown
            dcc.Dropdown(
                id = 'year', # id do dropdown
                value = [year['label'] for year in year_options], # Valores iniciais do dropdown. Vai puxar todos os valores das opções disponiveis
                multi = True, # Permite multiplos inputs
                options = year_options, # Opcoes do dropdown
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configuracoes visuais
            )
        ]),
        dbc.Row([
            html.Button("Show/Hide Years", id = "toggle-years-button", style = {'margin-left': '12px'}) # Botao usado para esconder e mostrar o dropdown
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'scatter-chart'), # Local onde o scatter chart será plotado
            html.Br(),
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('BPM Average x Years', className = 'text-center'), # Titulo do grafico
            html.H3('Selected Years', className = 'text-center'), # Titulo do dropdown
            dcc.Dropdown(
                id = 'year2', # id do dropdown
                value = [year['label'] for year in year_options], # Valores iniciais do dropdown. Vai puxar todos os valores das opções disponiveis
                multi = True, # Permite multiplos inputs
                options = year_options, # Opções do dropdown
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configurações visuais
            )
        ]),
        dbc.Row([
            html.Button("Show/Hide Years", id = 'toggle-years-button2', style = {'margin-left': '12px'}) # Botao usado para esconder e mostrar o dropdown
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'bar-graph2'), # Local onde será plotado o grafico em barra
            html.Br(),
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Total number of tracks per Year', className = 'text-center'), # Titulo do grafico
            html.H3('Selected Years', className = 'text-center'), # Titulo do dropdown
            dcc.Dropdown(
                id = 'year3', # id do dropdown
                value = [years['label'] for years in year_options], # Valores iniciais do dropdown. Vai puxar todos os valores das opções disponiveis
                multi = True, # Permite multiplos inputs
                options = year_options, # Opções do dropdown
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configurações visuais
            )
        ]),
        html.Button("Show/Hide Years", id = 'toggle-years-button3', style = {'margin-left': '12px'}) # Botao usado para esconder e mostrar o dropdown
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'bar-graph3'), # Local onde será plotado o grafico em barra
            html.Br(),
            html.Br()
        ])
    ]),
    dbc.Row([
        html.H1('Search Artist or Track', className = 'text-center'),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Input(id = 'search', type = 'text', placeholder = 'Search'), width = {'size': 6, 'offset': 3}), # Barra de pesquisa
        dbc.Col(
            html.Button("Search", id = 'search-button'), width = {'size': 3}), # Botao para pesquisar
    ]),
    dbc.Row([
        dbc.Col(html.Div(id = 'results'), width = {'size': 6, 'offset': 3}, style = {'color': 'black'}), # Resultados da busca
    ]),
])

@app.callback(
    Output('tracks', 'style'), # Define como saida o estilo do dropdown com id = tracks
    Input('toggle-tracks-button', 'n_clicks'), # Define como entrada o numero de clicks dado no botao
    State('tracks', 'style') # Verificação do estado do dropdown
)
def toggle_tracks_dropdown(n_clicks, current_style):
    if n_clicks is None: # Se o botao não for clicado
        return current_style # Dropdown continua igual

    # Clicou no botão
    if current_style.get('display') == 'none': # Se o estilo atual dele for 'none', o que significa que ele esta escondido
        new_style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configura o estilo do dropdown para aparecer na tela
    else:
        new_style = {'display': 'none'} # Caso contrario, o estilo do dropdown é configurado como none

    return new_style # Retorna o estilo

@app.callback(
    Output('tracks2', 'style'), # Define como saida o estilo do dropdown com id = tracks2
    Input('toggle-tracks-button2', 'n_clicks'), # Define como entrada o numero de clicks dado no botao
    State('tracks2', 'style') # Verificação do estado do dropdown
)
def toggle_tracks_dropdown2(n_clicks, current_style):
    if n_clicks is None: # Se o botao não for clicado
        return current_style # Dropdown continua igual

    if current_style.get('display') == 'none': # Se o estilo atual dele for 'none', o que significa que ele esta escondido
        new_style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configura o estilo do dropdown para aparecer na tela
    else:
        new_style = {'display': 'none'} # Caso contrario, o estilo do dropdown é configurado como none

    return new_style # Retorna o estilo

@app.callback(
    Output('year', 'style'), # Define como saida o estilo do dropdown com id = year
    Input('toggle-years-button', 'n_clicks'), # Define como entrada o numero de clicks dado no botao
    State('year', 'style') # Verificação do estado do dropdown
)

def toggle_years_dropdown(n_clicks, current_style):
    if n_clicks is None: # Se o botao não for clicado
        return current_style # Dropdown continua igual

    if current_style.get('display') == 'none': # Se o estilo atual dele for 'none', o que significa que ele esta escondido
        new_style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configura o estilo do dropdown para aparecer na tela
    else:
        new_style = {'display': 'none'} # Caso contrario, o estilo do dropdown é configurado como none

    return new_style # Retorna o estilo

@app.callback(
    Output('year2', 'style'), # Define como saida o estilo do dropdown com id = year
    Input('toggle-years-button2', 'n_clicks'), # Define como entrada o numero de clicks dado no botao
    State('year2', 'style') # Verificação do estado do dropdown 
)

def toggle_years_dropdown2(n_clicks, current_style):
    if n_clicks is None: # Se o botao não for clicado
        return current_style # Dropdown continua igual

    if current_style.get('display') == 'none': # Se o estilo atual dele for 'none', o que significa que ele esta escondido
        new_style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configura o estilo do dropdown para aparecer na tela
    else:
        new_style = {'display': 'none'} # Caso contrario, o estilo do dropdown é configurado como none

    return new_style # Retorna o estilo

@app.callback(
    Output('year3', 'style'), # Define como saida o estilo do dropdown com id = year3
    Input('toggle-years-button3', 'n_clicks'), # Define como entrada o numero de clicks dado no botao
    State('year3', 'style') # Verificação do estado do dropdown
)

def toggle_years_dropdown3(n_clicks, current_style):
    if n_clicks is None: # Se o botao não for clicado
        return current_style # Dropdown continua igual

    if current_style.get('display') == 'none': # Se o estilo atual dele for 'none', o que significa que ele esta escondido
        new_style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'} # Configura o estilo do dropdown para aparecer na tela
    else:
        new_style = {'display': 'none'} # Caso contrario, o estilo do dropdown é configurado como none

    return new_style # Retorna o estilo

@app.callback(
    Output('bar-graph', 'figure'), # Define o bar graph como uma figura
    Input('tracks', 'value'), # Define os inputs como os valores do dropdown tracks
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value') # Input para a troca do tema
)
def bar(tracks, toggle):
    templates = template_theme1 if toggle else template_theme2 # Se toggle estiver ligado, tema claro, se nao, tema escuro

    df_data = df.copy(deep = True) # Faz uma copia profunda do dataframe
    mask = df_data['Track Name'].isin(tracks) # Mascara para filtrar as opções disponiveis

    max_name_length = 10 # Tamanho máximo para o nome da musica
    
    # Se o nome da musica ultrapassar 10 caracters, o nome será cortado e '...' será adicionado ao final
    df_data['Tracks'] = df_data['Track Name'].apply(lambda name: name[:max_name_length] + '...' if len(name) > max_name_length else name)

    # Se tiver uma virgula no nome do artista, os outros nomes serão cortados, com uma exceção, Tyler, The Creator
    df_data['Artists'] = df_data['Artist Name'].apply(customSplit)

    # Plota o grafico (x: Musicas | y: Quantas vezes foi ouvida no Spotify)
    fig = px.bar(df_data[mask], x = 'Tracks', y = 'Streams', color = 'Artists', template = templates, text = 'Artists', hover_data = {'Artist Name': True, 'Track Name': True, 'Tracks': False, 'Artists': False})

    return fig # Retorna o grafico

@app.callback(
    Output('scatter-chart', 'figure'), # Define o scatter graph como uma figura
    Input('year', 'value'), # Define os inputs como os valores do dropdown year
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value') # Input para a troca do tema
)

def scatter(years, toggle):
    templates = template_theme1 if toggle else template_theme2 # Se toggle estiver ligado, tema claro, se nao, tema escuro

    df_data = df.copy(deep = True) # Faz uma copia profunda do dataframe
    mask = df_data['Released Year'].isin(years) # Mascara para filtrar as opções disponiveis

    max_name_length = 10 # Tamanho máximo para o nome da musica

    # Se o nome da musica ultrapassar 10 caracters, o nome será cortado e '...' será adicionado ao final
    df_data['Tracks'] = df_data['Track Name'].apply(lambda name: name[:max_name_length] + '...' if len(name) > max_name_length else name)
    
    # Se tiver uma virgula no nome do artista, os outros nomes serão cortados, com uma exceção, Tyler, The Creator
    df_data['Artists'] = df_data['Artist Name'].apply(customSplit)

    # Define Date como uma coluna com o dia/mes/ano que a musica foi lançada, neste formato
    df_data['Date'] = df_data['Released Day'].astype(str) + '/' + df_data['Released Month'].astype(str) + '/' + df_data['Released Year'].astype(str)
    df_data['Date'] = pd.to_datetime(df_data['Date'], format = '%d/%m/%Y') # Converte para tipo data

    # Plota o grafico (x: Datas de lançamento das musicas | BPM/Ritimo da musica)
    fig = px.scatter(df_data[mask], x = 'Date', y = 'BPM', color = 'Tracks', template = templates, hover_data = {'Tracks': False, 'Track Name': True, 'Artist Name': True, 'Artists': False})

    return fig # Retorna o grafico

@app.callback(
    Output('bar-graph2', 'figure'), # Define o bar graph2 como uma figura
    Input('year2', 'value'), # Define os inputs como os valores do dropdown year
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value') # Input para a troca do tema
)
def bar2(years, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Released Year'].isin(years)

    # Calcula a média de bpm de cada ano e reseta os indices
    bpm_average_per_year = df_data.groupby('Released Year')['BPM'].mean().reset_index()

    # Renomeia as colunas para Year e BPM Average
    bpm_average_per_year.columns = ['Year', 'BPM Average']

    # Salva os valores da coluna Year da variavel no dataframe
    df_data['Year'] = bpm_average_per_year['Year']

    # Salva os valores da coluna BPM Average da variavel no dataframe
    df_data['BPM Average'] = bpm_average_per_year['BPM Average']

    # Plota o grafico (x: Ano em que a musica foi lançada | y: Ritimo médio da musica)
    fig = px.bar(df_data[mask], x = 'Year', y = 'BPM Average', template = templates)

    return fig # Retorna o grafico

@app.callback(
    Output('pie-chart', 'figure'), # Define o pie chart como uma figura
    Input('tracks2', 'value'), # Define os inputs como os valores do dropdown year
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value') # Input para a troca do tema
)

def pie(tracks, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Track Name'].isin(tracks)

    max_name_length = 10
    df_data['Tracks'] = df_data['Track Name'].apply(lambda name: name[:max_name_length] + '...' if len(name) > max_name_length else name)

    # Plota o grafico (Numero de streams e a sua % em relação as outras musicas selecionadas)
    fig = px.pie(df_data[mask], names = 'Tracks', values = 'Streams', color = 'Track Name', custom_data = ['Artist Name', 'Track Name', 'Streams'], template = templates)

    # Configuração visuais do grafico
    fig.update_traces(
        # Mostra esses dados quando passa o mouse em cima do grafico
        hovertemplate = 'Artist Name: %{customdata[0][0]}<br>Track Name: %{customdata[0][1]}<br>Streams: %{customdata[0][2]}<br>Percent in relation to other selected songs: %{percent}',
        text = df_data[mask]['Tracks'], # Configura o texto que aparece em cada fatia como o nome da musica cortado
        textinfo = 'text' # Define o que vai aparecer no text
    )

    return fig # Retorna o grafico

@app.callback(
    Output('bar-graph3', 'figure'), # Define o bar graph3 como uma figura
    Input('year3', 'value'), # Define os inputs como os valores do dropdown year
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value') # Input para a troca do tema
)

def bar3(years, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Released Year'].isin(years)
    
    # Conta quantas musicas foram lançadas por ano
    total_tracks = df_data.groupby('Released Year')['Track Name'].count().reset_index()
    total_tracks.columns = ['Year', 'Total Tracks'] # Renomeia as colunas pra Year e Total Tracks

    # Salva os valores da coluna Year no dataframe
    df_data['Year'] = total_tracks['Year']

    # Salva os valores da coluna Total Tracks no dataframe
    df_data['Total Tracks'] = total_tracks['Total Tracks']
    
    # Plota o grafico (x: Ano de lançamento da musica | y: Total de musicas lançadas)
    fig = px.bar(df_data[mask], x = 'Year', y = 'Total Tracks', template = templates)

    return fig

@app.callback(
    Output('results', 'children'), # Atualiza o componente 'results' com os resultados da pesquisa
    [Input('search-button', 'n_clicks')], # Define como entrada o numero de cliques dado no botao
    [State('search', 'value')] # Verifica a valor atual do campo 'search'
)
def search(n_clicks, query):
    df_data = df.copy(deep = True)

    df_data['Artists'] = df_data['Artist Name'].apply(customSplit)

    # Se não houver nada escrito
    if not query:
        return '' # Retorna uma string vazia

    # Realiza a pesquisa nos dados com base na consulta inserida pelo usuário
    results = df_data[(df_data['Artists'].str.contains(query, case = False)) |
                 (df['Track Name'].str.contains(query, case = False))]

    # Verifica se a pesquisa esta vazia
    if not results.empty:
        # Se houver resultados, cria uma tabela interativa usando Dash DataTable
        return dash_table.DataTable(
            columns = [{'name': col, 'id': col} for col in results.columns], # Define as colunas da tabela
            data = results.to_dict('records') # Converte os resultados em um formato adequado para a tabela
        )
    else:
        return 'No results found' # Se não houver resultados, informa ao usuário que não foram encontrados resultados

if __name__ == '__main__':
    app.run_server(debug = True, port = '8051')