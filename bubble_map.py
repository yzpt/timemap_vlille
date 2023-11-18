import pandas as pd
import plotly.express as px
import plotly.io as pio

df = pd.read_csv('stations.csv')
print(df.head())

fig = px.scatter_mapbox(
    df, 
    lat="latitude", 
    lon="longitude",
    color_discrete_sequence=["fuchsia"], 
    zoom=12.5, 
    height=600,
    width=600,
    center={"lat": 50.63237, "lon": 3.05816}
)

fig.update_layout(mapbox_style="open-street-map")    
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Save figure to PNG
pio.write_image(fig, 'output.png')

