import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv('C:\\workplace\\analise_dados\\grafico_barras\\bd\\vendas_paises.csv')

# Configurar o grafico
grafico = px.bar(df,x='Vendas',y='País', orientation='h', color='País',
                 text='Vendas',
                 range_x=[0, df['Vendas'].max() + 100],
                 animation_frame=df['Ano'], animation_group=df['País'],
                 title='Vendas por País',
                 labels={'Vendas':'Total de Vendas','País':'Países'},
                 text_auto=True)

# grafico.show() #para exibir o gráfico
grafico.write_html('C:\\workplace\\analise_dados\\grafico_barras\\fam_internet\\grafico_vendas_paises.html', auto_open=True)

