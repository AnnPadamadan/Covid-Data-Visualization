import pandas as pd
import plotly.express as px

#line chart
df=pd.read_csv("covid.csv")
#px.line
#x=year, y=percapincome, color=country, title=percapitaincome
#px.bar
#x, y
fig=px.scatter(df, x="date", y="cases", color="country")
fig.show()
