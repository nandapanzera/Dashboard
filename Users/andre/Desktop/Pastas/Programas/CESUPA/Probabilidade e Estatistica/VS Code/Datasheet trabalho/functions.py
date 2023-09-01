from libraries import *

# Verifica se existem dados nulos no Dataframe
def verifyNullData(df):
    valores_nulos = df.isna().sum()

    if valores_nulos.sum() == 0:
        print("Não há valores nulos no DataFrame.")
        
        return False
    else:
        print("Valores nulos encontrados em algumas colunas.")
        print(valores_nulos)

        return True

# Verifica se existem dados duplicados no Dataframe
def verifyDuplicatedData(df):
    duplicatas = df.duplicated()
    total_duplicatas = duplicatas.sum()

    if total_duplicatas == 0:
        print("Não há dados duplicados no DataFrame.")

        return False
    else:
        print(f"Encontradas {total_duplicatas} linhas duplicadas.")

        return True

# Explorar dados
def exploreData(df):
    print(df.head())
    print(df.info())
    print(df.describe())

# Retorna uma lista dos artistas que mais aparecem no Dataframe
def artistsFrequency(df):
    # Obter uma lista ordenada de artistas únicos
    # artist = sorted(df['Artist Name'].unique())
    # print(f"Lista de Artistas:\n{artist}\n")

    # Contar a frequência de cada artista
    artist_f = df['Artist Name'].value_counts()
    artistas_por_frequencia = artist_f.sort_values(ascending = False)

    return artistas_por_frequencia

# Porcentagem dos 3 Artistas que mais aparecem

def artistFrequencyPercentage(df):
    taylorSwift = df[df['Artist Name'] == "Taylor Swift"]['Artist Name'].count()
    tsPorcentagem = (taylorSwift/df['Track Name'].shape) * 100
    # print(f"1- Taylor Swift: {taylorSwift}, {tsPorcentagem}%")

    theWeeknd = df[df['Artist Name'] == "The Weeknd"]['Artist Name'].count()
    twPorcentagem = (theWeeknd/df['Track Name'].shape) * 100
    # print(f"2- The Weeknd: {theWeeknd}, {twPorcentagem}%")

    badBunny = df[df['Artist Name'] == "Bad Bunny"]['Artist Name'].count()
    bbPorcentagem = (badBunny/df['Track Name'].shape) * 100
    # print(f"3- Bad Bunny: {badBunny}, {bbPorcentagem}%")

    outros = 100 - tsPorcentagem - twPorcentagem - bbPorcentagem
    # print(f"Outros: {outros}%")

    data = {
        "ArtistName": ["Taylor Swift", "The Weeknd", "Bad Bunny", "Outros"],
        "Value": [tsPorcentagem, twPorcentagem, bbPorcentagem, outros]
    }

    return data

def customSplit(artist):
        if artist == 'Tyler, The Creator':
            return artist.split(',')[1] if ',' in artist else artist
        return artist.split(',')[0] if ',' in artist else artist

def sortByStreams(df):
    df = df.sort_values(by = 'Streams', ascending = True)
    df = df.reset_index(drop = True)

def sortByDate(df):
    df = df.sort_values(by = 'Date', ascending = True)
    df = df.reset_index(drop = True)