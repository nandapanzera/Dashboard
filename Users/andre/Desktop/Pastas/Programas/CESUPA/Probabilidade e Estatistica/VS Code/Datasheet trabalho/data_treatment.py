from functions import *

# Importando o CSV
df = pd.read_csv('https://raw.githubusercontent.com/nandapanzera/Dashboard/main/spotify-2023.csv', encoding = 'ISO-8859-1')

# Renomeando colunas
df.rename(columns = {'track_name': 'Track Name'}, inplace = True)
df.rename(columns = {'artist(s)_name': 'Artist Name'}, inplace = True)
df.rename(columns = {'artist_count': 'Artist Count'}, inplace = True)
df.rename(columns = {'released_year': 'Released Year'}, inplace = True)
df.rename(columns = {'released_month': 'Released Month'}, inplace = True)
df.rename(columns = {'released_day': 'Released Day'}, inplace = True)
df.rename(columns = {'in_spotify_playlists': 'In Spotify Playlists'}, inplace = True)
df.rename(columns = {'in_spotify_charts': 'In Spotify Charts'}, inplace = True)
df.rename(columns = {'streams': 'Streams'}, inplace = True)
df.rename(columns = {'in_apple_playlists': 'In Apple Playlists'}, inplace = True)
df.rename(columns = {'in_apple_charts': 'In Apple Charts'}, inplace = True)
df.rename(columns = {'in_deezer_playlists': 'In Deezer Playlists'}, inplace = True)
df.rename(columns = {'in_deezer_charts': 'In Deezer Charts'}, inplace = True)
df.rename(columns = {'in_shazam_charts': 'In Shazam Charts'}, inplace = True)
df.rename(columns = {'bpm': 'BPM'}, inplace = True)
df.rename(columns = {'key': 'Key'}, inplace = True)
df.rename(columns = {'mode': 'Mode'}, inplace = True)
df.rename(columns = {'danceability_%': 'Danceability (%)'}, inplace = True)
df.rename(columns = {'valence_%': 'Valence (%)'}, inplace = True)
df.rename(columns = {'energy_%': 'Energy (%)'}, inplace = True)
df.rename(columns = {'acousticness_%': 'Acousticness (%)'}, inplace = True)
df.rename(columns = {'instrumentalness_%': 'Instrumentalness (%)'}, inplace = True)
df.rename(columns = {'liveness_%': 'Liveness (%)'}, inplace = True)
df.rename(columns = {'speechiness_%': 'Speechiness (%)'}, inplace = True)

# Explorando os dados do Dataframe
exploreData(df)

# Verificando se existem valores não numericos na coluna Streams
df['Streams'] = df['Streams'].str.replace(r'\D', '', regex = True)

# Se existirem dados nulos, eles serão preenchidos com 0
if verifyNullData(df):
    df = df.fillna(0)
    verifyNullData(df) # Verifica se restaram dados nulos

# Se existirem dados duplicados, eles serão removidos do Dataframe
if verifyDuplicatedData(df):
    df = df.drop_duplicates()
    verifyDuplicatedData(df) # Verifica se restaram dados duplicados

df['Streams'] = df['Streams'].astype(float)

# Removendo outliers
mask = (df['Streams'] > 2762) & (df['Streams'] < 11053756970173)
df = df[mask]

df = df.sort_values(by = 'Streams', ascending = True)
df = df.reset_index(drop = True)