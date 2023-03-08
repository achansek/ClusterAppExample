import dash
from dash.exceptions import PreventUpdate
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import base64
import numpy as np
# Create dash app
app = dash.Dash(__name__)
# Generate dataframe
kmdf = pd.read_csv('Fgrow10_3_kmdf.csv',index_col=0)
print(kmdf)
# Create scatter plot with x and y coordinates
fig = px.scatter(kmdf, x="Actin occupied Surface Fraction", 
                 y="Mean number of unique actin filaments per VASP",
                 custom_data=["images"],color="Predicted Cluster",
                 labels ={
               "Mean number of unique actin filaments per VASP":
                 'Mean number of unique <br>  actin filaments per VASP',
                 },)

fig.update_layout(
    font=dict(
        family="Arial",
        size=18,  # Set the font size here
        color="Black"
    )
)

# Update layout and update traces
fig.update_layout(clickmode='event+select')
fig.update_traces(marker_size=10)

# Create app layout to show dash graph
app.layout = html.Div(
   [
      dcc.Graph(
         id="graph_interaction",
         figure=fig,
      ),
      html.Img(id='image', src='')
   ]
)

# html callback function to hover the data on specific coordinates
@app.callback(
   Output('image', 'src'),
   Input('graph_interaction', 'hoverData'))

def open_url(hoverData):
   if hoverData:
      return hoverData["points"][0]["customdata"][0]
   else:
      raise PreventUpdate

if __name__ == '__main__':
   app.run_server(debug=False)