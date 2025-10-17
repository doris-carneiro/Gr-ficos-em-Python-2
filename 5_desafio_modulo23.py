import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

df = pd.read_csv('C:/Users/Doris/Downloads/ecommerce_estatistica.csv')
print(df.head().to_string())

def cria_graficos(df):
    # Histograma
    fig1 = px.histogram(df, x='Nota', nbins=30, title='Distribuição das Notas dos Produtos')

    # Gráfico de pizza
    fig2 = px.pie(df, names='Gênero', color='Gênero', title='Participação dos Gêneros nas Vendas', color_discrete_sequence=px.colors.sequential.RdBu)

    # Gráfico de bolha
    fig3 = px.scatter(df, x='Nota', y='N_Avaliações', size='Qtd_Vendidos_Cod', color='Desconto', hover_name='Preço', size_max=60)
    fig3.update_layout(title='Número de Avaliações por nota e quantidade de produtos vendido')              # função hover: mostra o campo qdo o mouse é parado em cima

    # Gráfico de Linha
    fig4 = px.line(df, x='Preço', y='Qtd_Vendidos_Cod', color='N_Avaliações', facet_col='Nota')
    fig4.update_layout(
        title='Qtd. Vendidos por Preço e Número de avaliações para cada Nota',
        xaxis_title='Preço',
        yaxis_title='Qtd. Vendidos')

    # Gráfico #3D
    fig5 = px.scatter_3d(df, x='Preço', y='Qtd_Vendidos_Cod', z='N_Avaliações', color='Nota')

    # Gráfico de Barra
    fig6 = px.bar(df, x='Marca', y='Qtd_Vendidos_Cod', color='Gênero', barmode='group', color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig6.update_layout(
        title='Quantidade de Vendidos por Marca',
        xaxis_title='Marca',
        yaxis_title='Quantidade de Vendidos',
        plot_bgcolor='rgba(222, 255, 253. 1)',   # Fundo interno
        paper_bgcolor='rgba(186, 245, 241, 1)'   # Fundo externo
    )

    return fig1, fig2, fig3, fig4, fig5, fig6

def cria_app(df):
    # cria APP
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)
    ])

    return app

# Executa App
if __name__ == '__main__':
    app = cria_app(df)
    app.run(debug=True, port=8050)