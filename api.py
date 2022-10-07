import requests
import pandas as pd
import itertools

lista_cep = pd.read_csv("D:\\Lucas Caldeira\\Documents\\Projetos Banco de dados\\Repositorio de dados\\Cep_nome_sexo\\apidoc.txt", sep ="\t").astype('str')
lista_cep1 = lista_cep.head()

def populate_cep(df):

    data_frame = pd.DataFrame()

    for row in df.itertuples():
        r = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(row.CEP)).json()
        r_df = pd.json_normalize(r)

        data_frame = data_frame.append(r_df)

    return data_frame

df = populate_cep(lista_cep1)

df_total = lista_cep1.merge(df, how='left', left_on='CEP', right_on='cep')
df_total.drop(['cep'], axis=1, inplace=True)
df_total.to_csv("C:\\Users\\Lucas Caldeira\Desktop\\api\\arquivo_final\\df_total.csv", sep=';')



