import os
# Define a relative path (current code)
RELATIVE_PATH = os.path.dirname(os.path.abspath(__file__))

# Utilizando a plotagem com pandas, reproduzam as visualizações abaixo, tentando deixá-las o mais próximas quanto possível da maneira 
# como estão postas. Para isso, atentem-se às personalizações dos gráficos, como títulos, legendas, eixos e outros tipos possíveis de 
# formatações e preferências de visualizações dos dados. Também é interessante que vocês discutam possíveis pontos de melhorias dessas 
# visualizações!

#-----------------------------------------------------------------------------------------------------------------------------------#
# 1. Reproduza o gráfico de barras abaixo, em que cada barra representa um dos 10 países com mais casos confirmados de 
#    COVID no dataset, e a "quebra" em cada cor indica a predominância de casos confirmados em cada mês.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(RELATIVE_PATH + '/Datasets/Covid_19_Countrywise_timeseries.csv')

df['date'] = pd.to_datetime(df['ObservationDate'])

df1 = df['2020-01' in df['date']]
df2 = df['2020-02' in df['date']]
df3 = df['2020-03' in df['date']]

ax1 = df.groupby("country")['Confirmed'].sum().sort_values(ascending = False)[0:10].plot(kind='barh')
df2.groupby("country")['Confirmed'].sum().sort_values(ascending = False)[0:10].plot(kind='barh', ax=ax1, color='r')
df3.groupby("country")['Confirmed'].sum().sort_values(ascending = False)[0:10].plot(kind='barh', ax=ax1, stacked=True, color='g')

plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------#
# 2. Reproduza o gráfico de linhas abaixo, que representa a série temporal da evolução de emissões de CO2 no Brasil.



#-----------------------------------------------------------------------------------------------------------------------------------#
# 3. Uma visualização muito similar à anterior, mas com a adição da média global de emissão de CO2 (o Brasil deve ser incluído na 
#    linha da média global?).



#-----------------------------------------------------------------------------------------------------------------------------------#
# 4. Os 10 países que mais aumentaram, percentualmente, a emissão de CO2 entre os anos de 2018 e 2019, na forma de um gráfico de 
#    barras horizontal.

