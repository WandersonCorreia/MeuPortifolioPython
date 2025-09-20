import pandas as pd
from plotly import express as px

df=pd.read_csv("C:\\workplace\\analise_dados\\grafico_pizza\\bd\\vendas_distribuicao.csv")

grafico=px.sunburst(df, path=['Continente', 'País'], values='Vendas (Milhões)',
                    color='Continente', title='Vendas Globais por Continente e País')
grafico.update_traces(textinfo='label+percent entry')
grafico.show()