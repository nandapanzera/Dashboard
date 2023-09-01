from data_treatment import *
from app import *

from dash_bootstrap_templates import ThemeSwitchAIO

url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.VAPOR

template_theme1 = 'flatly'
template_theme2 = 'vapor'

track_options = [{'label' : x, 'value': x} for x in df['Track Name'].unique()]
artist_options = [{'label': x, 'value': x} for x in df['Artist Name'].unique()]
year_options = [{'label': x, 'value': x} for x in df['Released Year'].unique()]

# first_row = df.iloc[0]  # Pega a primeira linha do dataframe
# column_options = [{'label': column, 'value': column} for column in first_row.index]

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id = 'theme', themes = [url_theme1, url_theme2]),
            html.H3('Most Streamed Spotify Songs', className = 'text-center'),
            html.Br(),
            html.Br()
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Tracks x Streams', className = 'text-center'),
            html.H3('Selected Music', className = 'text-center'),
            dcc.Dropdown(
                id = 'tracks',
                value = [track['label'] for track in track_options[:20]],
                multi = True,
                options = track_options,
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'}
            ),
            html.Button("Show/Hide Tracks", id = "toggle-tracks-button")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'bar-graph'),
            html.Br(),
            html.Br(),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Date x BPM', className = 'text-center'),
            html.H3('Selected Years', className = 'text-center'),
            dcc.Dropdown(
                id = 'year',
                value = [year['label'] for year in year_options],
                multi = True,
                options = year_options,
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'}
            ),
        ]),
        dbc.Row([
            html.Button("Show/Hide Years", id = "toggle-years-button", style = {'margin-left': '12px'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'scatter-chart')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id = 'track3',
                value = [track['label'] for track in track_options[:3]],
                multi = True,
                options = track_options
            ),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3('Pizza'),
            dcc.Graph(id = 'pie-chart')
        ])
    ]),
])

@app.callback(
    Output('tracks', 'style'),
    Input('toggle-tracks-button', 'n_clicks'),
    State('tracks', 'style'),
)
def toggle_tracks_dropdown(n_clicks, current_style):
    if n_clicks is None:
        return current_style

    if current_style.get('display') == 'none':
        new_style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'}
    else:
        new_style = {'display': 'none'}

    return new_style

@app.callback(
    Output('year', 'style'),
    Input('toggle-years-button', 'n_clicks'),
    State('year', 'style'), 
)

def toggle_years_dropdown(n_clicks, current_style):
    if n_clicks is None:
        return current_style

    if current_style.get('display') == 'none':
        new_style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'}
    else:
        new_style = {'display': 'none'}

    return new_style

@app.callback(
    Output('bar-graph', 'figure'),
    Input('tracks', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def bar(tracks, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Track Name'].isin(tracks)

    max_name_length = 10
    df_data['Short Track Name'] = df_data['Track Name'].apply(lambda name: name[:max_name_length] + '...' if len(name) > max_name_length else name)

    df_data['Short Artist Name'] = df_data['Artist Name'].apply(lambda artist: artist.split(',')[0])

    fig = px.bar(df_data[mask], x = 'Short Track Name', y = 'Streams', color = 'Short Artist Name', template = templates, text = 'Short Artist Name', hover_data = {'Artist Name': True, 'Track Name': True, 'Short Track Name': False, 'Short Artist Name': False})

    fig.update_xaxes(title_text = 'Tracks')

    return fig

@app.callback(
    Output('scatter-chart', 'figure'),
    Input('year', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)

def scatter(years, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Released Year'].isin(years)

    max_name_length = 10
    df_data['Short Track Name'] = df_data['Track Name'].apply(lambda name: name[:max_name_length] + '...' if len(name) > max_name_length else name)

    df_data['Short Artist Name'] = df_data['Artist Name'].apply(customSplit)

    df_data['Date'] = df_data['Released Day'].astype(str) + '/' + df_data['Released Month'].astype(str) + '/' + df_data['Released Year'].astype(str)
    df_data['Date'] = pd.to_datetime(df_data['Date'], format = '%d/%m/%Y')

    fig = px.scatter(df_data[mask], x = 'Date', y = 'BPM', color = 'Short Track Name', template = templates)

    return fig

@app.callback(
    Output('pie-chart', 'figure'),
    Input('track3', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)

def pie(tracks, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Track Name'].isin(tracks)

    max_name_length = 10
    df_data['Short Track Name'] = df_data['Track Name'].apply(lambda name: name[:max_name_length] + '...' if len(name) > max_name_length else name)

    fig = px.pie(df_data[mask], names = 'Short Track Name', values = 'Streams', color = 'Track Name', custom_data = ['Artist Name', 'Track Name', 'Streams'], template = templates)

    fig.update_traces(
        hovertemplate = 'Artist Name: %{customdata[0][0]}<br>Track Name: %{customdata[0][1]}<br>Streams: %{customdata[0][2]}<br>Percent in relation to other selected songs: %{percent}',
        text = df_data[mask]['Short Track Name'],
        textinfo = 'text'
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug = True, port = '8051')