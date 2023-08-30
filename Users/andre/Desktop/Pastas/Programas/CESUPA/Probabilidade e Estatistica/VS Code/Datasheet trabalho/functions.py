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
    artist = sorted(df['artist(s)_name'].unique())
    print(f"Lista de Artistas:\n{artist}\n")

    # Contar a frequência de cada artista
    artist_f = df['artist(s)_name'].value_counts()
    artistas_por_frequencia = artist_f.sort_values(ascending=False)

    return artistas_por_frequencia

# # Retorna a porcentagem dos 3 artistas que mais aparecem
# def artistsFrequencyPercentage(df):
#     taylorSwift = df[df['artist(s)_name'] =="Taylor Swift"]['artist(s)_name'].count()
#     tsPorcentagem = (taylorSwift/df['track_name'].shape) * 100
#     print(f"1- Taylor Swift: {taylorSwift}, {tsPorcentagem}%")

#     theWeeknd = df[df['artist(s)_name'] =="The Weeknd"]['artist(s)_name'].count()
#     twPorcentagem = (theWeeknd/df['track_name'].shape) * 100
#     print(f"2- The Weeknd: {theWeeknd}, {twPorcentagem}%")

#     badBunny = df[df['artist(s)_name'] =="Bad Bunny"]['artist(s)_name'].count()
#     bbPorcentagem = (badBunny/df['track_name'].shape) * 100
#     print(f"3- Bad Bunny: {badBunny}, {bbPorcentagem}%")

#     outros = 100 - tsPorcentagem - twPorcentagem - bbPorcentagem
#     print(f"Outros: {outros}%")