from data_treatment import *
from app import *

from dash_bootstrap_templates import ThemeSwitchAIO

url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.VAPOR

template_theme1 = 'flatly'
template_theme2 = 'vapor'

track_options = [{'label' : x, 'value': x} for x in df['Track Name'].unique()]
artist_options = [{'label': x, 'value': x} for x in df['Artist Name'].unique()]

first_row = df.iloc[0]  # Pega a primeira linha do dataframe
column_options = [{'label': column, 'value': column} for column in first_row.index]

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id = 'theme', themes = [url_theme1, url_theme2]),
            html.H3('Most Streamed Spotify Songs'),
            dcc.Graph(id = 'bar-graph'),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Music Selected'),
            html.Button("Mostrar/Ocultar Dropdown de Faixas", id = "toggle-tracks-button"),
            dcc.Dropdown(
                id = 'tracks',
                value = [track['label'] for track in track_options[:20]],
                multi = True,
                options = track_options,
                style = {'display': 'block', 'overflow': 'visible', 'height': 'auto'}
            ),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3('Pizza'),
            dcc.Graph(id = 'pie-graph')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id = 'artists',
                value = [artist['label'] for artist in artist_options[:3]],
                multi = True,
                options = artist_options
            )
        ])
    ])
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

    fig = px.bar(df_data[mask], x = 'Short Track Name', y = 'Streams', color = 'Short Artist Name', template = templates, text = 'Short Artist Name', hover_data={'Track Name': True, 'Short Track Name': False, 'Short Artist Name': False})

    fig.update_xaxes(title_text = 'Tracks')

    return fig

@app.callback(
    Output('pie-graph', 'figure'),
    Input('artists', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)

def pie(artists, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Artist Name'].isin(artists)

    df_data['Artist Count'] = df_data['Artist Name'].value_counts()
    # df_data = df_data.sort_values(by = 'Artist Name', ascending = False)

    fig = px.pie(df_data[mask].unique(), values = 'Artist Count', template = templates)

    return fig

if __name__ == '__main__':
    app.run_server(debug = True, port = '8051')