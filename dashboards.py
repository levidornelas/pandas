#Criação de dashboards interativos com python por meio das bibliotecas plotly e pandas. Existem inferências sobre os gráficos, interpretando as informações fornecidas pelo código.



import pandas as pd
import plotly.express as px

#Remover a linha 'CustomerID' da tabela:
tab = pd.read_csv('cancelamentos.csv')
tab = tab.drop(columns = 'CustomerID')

#Adquirir as informações sobre a tabela:
print(tab.info())

#Remover as linhas da tabela que estão vazias:
tab = tab.dropna()


print(tab.info())


#Saber o percentual de quantos clientes cancelaram o serviço:
print(tab['cancelou'].value_counts(normalize=True))


#Criar os gráficos da aplicação:


#Azul = Clientes que cancelaram. Vermelho = clientes ativos.
for coluna in tab.columns:

    grafico = px.histogram(tab,x=coluna, color='cancelou', text_auto=True)


    grafico.show()

#Todos os clientes do contrato mensal cancelaram o produto.
#Se o cliente ligar mais de 5 vezes para o callcenter, ele cancelará.
#No momento em que ele ligar 3 vezes para o callcenter, ele receberá prioridade para a resolução do problema.
#Todos os clientes acima de 50 anos cancelam.
#Todos os clientes que atrasam mais de 20 dias, cancelam.
