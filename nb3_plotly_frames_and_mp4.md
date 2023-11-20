```python
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
```


```python
# Get the list of files in the "data" folder
folder_path = 'data_23_09_27/'
file_list = os.listdir(folder_path)
file_list.sort()
```


```python
dir = 'img_23_09_27/'
```


```python
os.system('rm -r ' + dir)

# os mkdir img_7h:
os.mkdir(dir)

# Loop through each file in the folder
for file_name in file_list[360:540]:
# for file_name in file_list:
    # Construct the file path
    file_path = os.path.join(folder_path, file_name)
    
    # Read the file into a dataframe
    df = pd.read_csv(file_path)

    # remove line with ratio == null
    df = df[df['ratio'].notna()]



    fig = px.scatter_mapbox(
    df, 
    lat="latitude", 
    lon="longitude",
    size="nb_velos_dispo",
    # size_min=10,
    size_max=40,
    # color="rgb(66, 133, 244)",
    # color_continuous_scale=[[0, 'rgb(66, 133, 244)'], [0.5, 'rgb(244, 180,0)'] [1, 'rgb(15, 157, 88)']],
    # color_continuous_scale=['red', 'orange', 'green' ],
    # color_continuous_scale='Portland',
    
    zoom=12, 
    height=400,
    width=400,
    center={"lat": 50.63237, "lon": 3.05816}
    )

    fig.update_layout(mapbox_style="open-street-map")    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_coloraxes(showscale=False)

    # Add file name on top left of the large-sized figure
    fig.add_annotation(
        x=0.07,
        y=0.88,
        xref="paper",
        yref="paper",
        text=file_name[:2] + ':' + file_name[2:4],
        showarrow=False,
        font=dict(size=50)
    )
    

    # Save figure to PNGsize_max=40
    pio.write_image(fig, dir + file_name[:-4] +'.png')


```


```python
!pip install imageio
!pip install imageio-ffmpeg
!pip install av
```


```python
import os
import imageio

path = dir

initial_files = os.listdir(path)
images = sorted([img for img in os.listdir(path) if img.endswith(".png")])
image_files = [imageio.imread(path + '/' + img) for img in images]

imageio.mimsave('output/' + path[:-1] + '.mp4', image_files, fps=24)  # fps specifies the frames per second
```

    /tmp/ipykernel_10702/2872751158.py:8: DeprecationWarning:
    
    Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread. To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.
    



```python

```


```python

```
