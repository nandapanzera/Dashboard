from libraries import *

# Verifica se existem dados nulos no dataframe
def verifyNullData(df):
    valores_nulos = df.isna().sum() # Verifica se a soma dos valores nulos é 0

    if valores_nulos.sum() == 0: # Se for 0, não há valores nulos
        print("Não há valores nulos no DataFrame.") 
        
        return False
    else:
        # Se nao for 0, tem valores nulos
        print("Valores nulos encontrados em algumas colunas.")
        print(valores_nulos)

        return True

# Verifica se existem dados duplicados no dataframe
def verifyDuplicatedData(df):
    duplicatas = df.duplicated() # Salva os valores duplicados em uma variavel
    total_duplicatas = duplicatas.sum() # Soma todos os itens da variavel

    if total_duplicatas == 0: # Se for 0, não há duplicatas
        print("Não há dados duplicados no DataFrame.")

        return False
    else:
        # Se nao for 0, há duplicatas
        print(f"Encontradas {total_duplicatas} linhas duplicadas.")

        return True

# Explorar dados
def exploreData(df):
    print(df.head()) # Imprime as 5 primeiras linhas do dataframe
    print(df.info()) # Imprime informações sobre o dataframe
    print(df.describe()) # Calcula estatísticas descritivas para colunas numéricas do dataframe

def customSplit(artist):
        if artist == 'Tyler, The Creator': # Se o artista for Tyler, The Creator
            return artist.split(',')[1] if ',' in artist else artist # O nome do artista só será cortado na segunda virgula da string
        return artist.split(',')[0] if ',' in artist else artist # Se nao, o nome será cortado na primeira