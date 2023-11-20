### 1. Init config


```python
from google.cloud import bigquery
import os
import pandas as pd
import datetime
```


```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

client = bigquery.Client()

project_id = "zapart-data-vlille"
dataset_id = "vlille_dataset"
```

### 2. Stations query - dim table


```python
table_name = "stations"

table_ref = client.get_table(f'{project_id}.{dataset_id}.{table_name}')
schema = table_ref.schema

for field in schema:
    print(field.name, field.field_type)

```

    id INTEGER
    nom STRING
    adresse STRING
    commune STRING
    type STRING
    latitude FLOAT
    longitude FLOAT



```python
sql = f"""
SELECT *
FROM `{project_id}.{dataset_id}.stations`
"""

df_stations = client.query(sql).to_dataframe()
```


```python
df_stations.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>nom</th>
      <th>adresse</th>
      <th>commune</th>
      <th>type</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>136</td>
      <td>RUE CHAMBORD</td>
      <td>RUE CHAMBORD</td>
      <td>VILLENEUVE D'ASCQ</td>
      <td>SANS TPE</td>
      <td>50.629720</td>
      <td>3.133873</td>
    </tr>
    <tr>
      <th>1</th>
      <td>270</td>
      <td>PAVÉ DE LILLE</td>
      <td>Rue Jean Bart</td>
      <td>WASQUEHAL</td>
      <td>AVEC TPE</td>
      <td>50.664211</td>
      <td>3.130098</td>
    </tr>
    <tr>
      <th>2</th>
      <td>35</td>
      <td>LECLERC</td>
      <td>24 PLACE MARECHAL LECLERC</td>
      <td>LILLE</td>
      <td>AVEC TPE</td>
      <td>50.628990</td>
      <td>3.043307</td>
    </tr>
    <tr>
      <th>3</th>
      <td>44</td>
      <td>GAMBETTA UTRECHT</td>
      <td>199 RUE LEON GAMBETTA</td>
      <td>LILLE</td>
      <td>AVEC TPE</td>
      <td>50.629063</td>
      <td>3.053711</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11</td>
      <td>NOUVEAU SIECLE</td>
      <td>10 RUE DE PAS</td>
      <td>LILLE</td>
      <td>AVEC TPE</td>
      <td>50.637340</td>
      <td>3.060977</td>
    </tr>
  </tbody>
</table>
</div>




```python
# add a column 'geo' [latitude, longitude]
df_stations['geo'] = df_stations.apply(lambda row: str(row['latitude']) + "," + str(row['longitude']), axis=1)
df_stations.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>nom</th>
      <th>adresse</th>
      <th>commune</th>
      <th>type</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>geo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>136</td>
      <td>RUE CHAMBORD</td>
      <td>RUE CHAMBORD</td>
      <td>VILLENEUVE D'ASCQ</td>
      <td>SANS TPE</td>
      <td>50.629720</td>
      <td>3.133873</td>
      <td>50.62972,3.133873</td>
    </tr>
    <tr>
      <th>1</th>
      <td>270</td>
      <td>PAVÉ DE LILLE</td>
      <td>Rue Jean Bart</td>
      <td>WASQUEHAL</td>
      <td>AVEC TPE</td>
      <td>50.664211</td>
      <td>3.130098</td>
      <td>50.664211,3.130098</td>
    </tr>
    <tr>
      <th>2</th>
      <td>35</td>
      <td>LECLERC</td>
      <td>24 PLACE MARECHAL LECLERC</td>
      <td>LILLE</td>
      <td>AVEC TPE</td>
      <td>50.628990</td>
      <td>3.043307</td>
      <td>50.62899,3.043307</td>
    </tr>
    <tr>
      <th>3</th>
      <td>44</td>
      <td>GAMBETTA UTRECHT</td>
      <td>199 RUE LEON GAMBETTA</td>
      <td>LILLE</td>
      <td>AVEC TPE</td>
      <td>50.629063</td>
      <td>3.053711</td>
      <td>50.629063,3.053711</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11</td>
      <td>NOUVEAU SIECLE</td>
      <td>10 RUE DE PAS</td>
      <td>LILLE</td>
      <td>AVEC TPE</td>
      <td>50.637340</td>
      <td>3.060977</td>
      <td>50.63734,3.060977</td>
    </tr>
  </tbody>
</table>
</div>




```python
# save dataframe to csv
df_stations.to_csv('stations.csv', index=False)
```

### 3. Records query - fact table


```python
table_name = "records"

table_ref = client.get_table(f'{project_id}.{dataset_id}.{table_name}')
schema = table_ref.schema

for field in schema:
    print(field.name, field.field_type)

```

    station_id INTEGER
    etat STRING
    nb_velos_dispo INTEGER
    nb_places_dispo INTEGER
    etat_connexion STRING
    derniere_maj TIMESTAMP
    record_timestamp TIMESTAMP



```python
sql = f"""
SELECT *
FROM 
    `{project_id}.{dataset_id}.{table_name}`
WHERE
    station_id = 25
    AND DATE(record_timestamp) = "2023-09-27"
"""

df_records = client.query(sql).to_dataframe()

# remove duplicate rows
df_records = df_records.drop_duplicates()
df_records.sort_values(by=['record_timestamp'], inplace=True)
df_records.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station_id</th>
      <th>etat</th>
      <th>nb_velos_dispo</th>
      <th>nb_places_dispo</th>
      <th>etat_connexion</th>
      <th>derniere_maj</th>
      <th>record_timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>231</th>
      <td>25</td>
      <td>EN SERVICE</td>
      <td>0</td>
      <td>32</td>
      <td>CONNECTÉ</td>
      <td>2023-11-12 23:56:10+00:00</td>
      <td>2023-11-13 00:00:06.624000+00:00</td>
    </tr>
    <tr>
      <th>232</th>
      <td>25</td>
      <td>EN SERVICE</td>
      <td>0</td>
      <td>32</td>
      <td>CONNECTÉ</td>
      <td>2023-11-12 23:56:10+00:00</td>
      <td>2023-11-13 00:01:01.149000+00:00</td>
    </tr>
    <tr>
      <th>233</th>
      <td>25</td>
      <td>EN SERVICE</td>
      <td>0</td>
      <td>32</td>
      <td>CONNECTÉ</td>
      <td>2023-11-12 23:56:10+00:00</td>
      <td>2023-11-13 00:02:01.485000+00:00</td>
    </tr>
    <tr>
      <th>234</th>
      <td>25</td>
      <td>EN SERVICE</td>
      <td>0</td>
      <td>32</td>
      <td>CONNECTÉ</td>
      <td>2023-11-12 23:56:10+00:00</td>
      <td>2023-11-13 00:03:01.494000+00:00</td>
    </tr>
    <tr>
      <th>235</th>
      <td>25</td>
      <td>EN SERVICE</td>
      <td>0</td>
      <td>32</td>
      <td>CONNECTÉ</td>
      <td>2023-11-12 23:56:10+00:00</td>
      <td>2023-11-13 00:04:00.899000+00:00</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql = f"""
SELECT station_id, nom, nb_velos_dispo, nb_places_dispo, record_timestamp, adresse, commune, latitude, longitude, type, etat, etat_connexion, derniere_maj
FROM 
    `{project_id}.{dataset_id}.stations`, 
    `{project_id}.{dataset_id}.records`
WHERE
    `{project_id}.{dataset_id}.stations`.id = `{project_id}.{dataset_id}.records`.station_id
    AND DATE(record_timestamp) = "2023-09-27"
"""

df_full = client.query(sql).to_dataframe()
```


```python
df_full.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station_id</th>
      <th>nom</th>
      <th>nb_velos_dispo</th>
      <th>nb_places_dispo</th>
      <th>record_timestamp</th>
      <th>adresse</th>
      <th>commune</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>type</th>
      <th>etat</th>
      <th>etat_connexion</th>
      <th>derniere_maj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>METROPOLE EUROPEENNE DE LILLE</td>
      <td>0</td>
      <td>0</td>
      <td>2023-09-27 10:00:42.773000+00:00</td>
      <td>MEL RUE DU BALLON</td>
      <td>LILLE</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>AVEC TPE</td>
      <td>RÉFORMÉ</td>
      <td>DÉCONNECTÉ</td>
      <td>2022-11-29 09:47:16+00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>METROPOLE EUROPEENNE DE LILLE</td>
      <td>0</td>
      <td>0</td>
      <td>2023-09-27 15:19:00.882000+00:00</td>
      <td>MEL RUE DU BALLON</td>
      <td>LILLE</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>AVEC TPE</td>
      <td>RÉFORMÉ</td>
      <td>DÉCONNECTÉ</td>
      <td>2022-11-29 09:47:16+00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>METROPOLE EUROPEENNE DE LILLE</td>
      <td>0</td>
      <td>0</td>
      <td>2023-09-27 20:28:01.143000+00:00</td>
      <td>MEL RUE DU BALLON</td>
      <td>LILLE</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>AVEC TPE</td>
      <td>RÉFORMÉ</td>
      <td>DÉCONNECTÉ</td>
      <td>2022-11-29 09:47:16+00:00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>METROPOLE EUROPEENNE DE LILLE</td>
      <td>0</td>
      <td>0</td>
      <td>2023-09-27 01:30:10.842000+00:00</td>
      <td>MEL RUE DU BALLON</td>
      <td>LILLE</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>AVEC TPE</td>
      <td>RÉFORMÉ</td>
      <td>DÉCONNECTÉ</td>
      <td>2022-11-29 09:47:16+00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>METROPOLE EUROPEENNE DE LILLE</td>
      <td>0</td>
      <td>0</td>
      <td>2023-09-27 16:08:00.744000+00:00</td>
      <td>MEL RUE DU BALLON</td>
      <td>LILLE</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>AVEC TPE</td>
      <td>RÉFORMÉ</td>
      <td>DÉCONNECTÉ</td>
      <td>2022-11-29 09:47:16+00:00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_full.shape
```




    (415871, 13)




```python
df_full['geo'] = df_full.apply(lambda row: str(row['latitude']) + "," + str(row['longitude']), axis=1)
```


```python
df_light = df_full[['station_id', 'nb_velos_dispo', 'nb_places_dispo', 'latitude', 'longitude', 'record_timestamp']]
```


```python
df_light.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station_id</th>
      <th>nb_velos_dispo</th>
      <th>nb_places_dispo</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>record_timestamp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 18:18:01.557000+00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 05:32:00.631000+00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 02:37:01.470000+00:00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 07:02:06.403000+00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 04:19:01.130000+00:00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_light.to_csv('dataset_light_2023_09_27.csv', index=False)
```


```python
df_full.to_csv('datataset_full.csv', index=False)
```
