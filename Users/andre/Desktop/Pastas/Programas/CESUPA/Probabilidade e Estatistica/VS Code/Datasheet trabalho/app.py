import dash # Importa a biblioteca Dash, usada para criar paginas interativas
import dash_bootstrap_components as dbc # Essa biblioteca é usada para fornecer os componentes e outras configurações visuais

# Cria uma instância do aplicativo Dash
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

# Configura o servidor web para o aplicativo Dash
server = app.server