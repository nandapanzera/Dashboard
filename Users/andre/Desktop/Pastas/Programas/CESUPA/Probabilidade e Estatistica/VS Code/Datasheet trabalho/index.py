from data_treatment import *
from app import *

from dash_bootstrap_templates import ThemeSwitchAIO

url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.VAPOR

template_theme1 = 'flatly'
template_theme2 = 'vapor'

artist_options = [{'label' : x, 'value': x} for x in df['Track Name'].unique()]

first_row = df.iloc[0]  # Pega a primeira linha do dfFrame
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
            dcc.Dropdown(
                id = 'tracks',
                value = [track['label'] for track in artist_options],
                multi = True,
                options = artist_options,
            ),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('Y axis options'),
            dcc.Dropdown(
                id = 'y-axis',
                value = column_options[0]['value'],
                options = column_options
            )
        ])
    ])
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Dropdown(
    #         id = 'entity1',
    #         value = entity_options[0]['label'],
    #         options = entity_options
    #         ),
    #         dcc.Graph(id = 'indicator1')
    #     ])
    # ]),
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Dropdown(
    #             id = 'entity2',
    #             value = entity_options[1]['label'],
    #             options = entity_options
    #         ),
    #         dcc.Graph(id = 'indicator2')
    #     ])
    # ])
])

@app.callback(
    Output('bar-graph', 'figure'),
    Input('tracks', 'value'),
    Input('y-axis', 'value'),
    Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
)
def bar(tracks, y_column_name, toggle):
    templates = template_theme1 if toggle else template_theme2

    df_data = df.copy(deep = True)
    mask = df_data['Track Name'].isin(tracks)

    max_x = df['Streams'].max()
    max_y = df_data[mask][y_column_name].max()

    fig = px.bar(df_data[mask], x = 'Streams', y = y_column_name, color = 'Artist Name', template = templates, range_x = [None, max_x], range_y = [None, max_y])

    return fig

# @app.callback(
#     Output('indicator1', 'figure'),
#     Output('indicator2', 'figure'),
#     Input('entity1', 'value'),
#     Input('entity2', 'value'),
#     Input('y-axis', 'value'),
#     Input(ThemeSwitchAIO.ids.switch('theme'), 'value')
# )

# def indicators(entity1, entity2, y_column_name, toggle):
#     templates = template_theme1 if toggle else template_theme2

#     df_df = df.copy(deep = True)

#     df_entity1 = df_df[df_df['Entity'].isin([entity1])]
#     df_entity2 = df_df[df_df['Entity'].isin([entity2])]

#     iterable = [(entity1, df_entity1), (entity2, df_entity2)]
#     indicators = []

#     for entity, df in iterable:
#         fig = go.Figure()
#         fig.add_trace(go.Indicator(
#             mode = 'number+delta',
#             title = {'text': entity},
#             value = df.at[df.index[-1], y_column_name],
#             delta = {'relative': True, 'valueformat': '.1%', 'reference': df.at[df.index[0], y_column_name]}
#         ))

#         fig.update_layout(template = templates)
#         indicators.append(fig)

#     return indicators

if __name__ == '__main__':
    app.run_server(debug = True, port = '8051')