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