```python
import pandas as pd
```


```python
df = pd.read_csv('dataset_light_2023_09_27.csv')
df.head()
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
df['ratio'] = df['nb_velos_dispo'] / (df['nb_velos_dispo'] + df['nb_places_dispo'])
df.head()
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
      <th>ratio</th>
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
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 05:32:00.631000+00:00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 02:37:01.470000+00:00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 07:02:06.403000+00:00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>50.641926</td>
      <td>3.075992</td>
      <td>2023-09-27 04:19:01.130000+00:00</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(inplace=True)
df.head()
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
      <th>ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>52</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>2023-09-27 08:04:01.643000+00:00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>53</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>2023-09-27 06:51:08.256000+00:00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>2023-09-27 07:51:00.940000+00:00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>55</th>
      <td>3</td>
      <td>18</td>
      <td>0</td>
      <td>50.636093</td>
      <td>3.050447</td>
      <td>2023-09-27 11:01:03.537000+00:00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>3</td>
      <td>18</td>
      <td>0</td>
      <td>50.636093</td>
      <td>3.050447</td>
      <td>2023-09-27 07:20:01.829000+00:00</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['time_index'] = df['record_timestamp'].apply(lambda x: pd.to_datetime(x).to_pydatetime().strftime('%H%M'))
```


```python
df.to_csv('dataset_light_2023_09_27.csv', index=False)
```


```python
df.head()
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
      <th>ratio</th>
      <th>time_index</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>52</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>1.0</td>
      <td>0804</td>
    </tr>
    <tr>
      <th>53</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>1.0</td>
      <td>0651</td>
    </tr>
    <tr>
      <th>54</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>1.0</td>
      <td>0751</td>
    </tr>
    <tr>
      <th>55</th>
      <td>3</td>
      <td>18</td>
      <td>0</td>
      <td>50.636093</td>
      <td>3.050447</td>
      <td>1.0</td>
      <td>1101</td>
    </tr>
    <tr>
      <th>56</th>
      <td>3</td>
      <td>18</td>
      <td>0</td>
      <td>50.636093</td>
      <td>3.050447</td>
      <td>1.0</td>
      <td>0720</td>
    </tr>
  </tbody>
</table>
</div>




```python
distincts_time_index = df['time_index'].unique()
distincts_time_index.sort()
distincts_time_index
```




    array(['0000', '0002', '0003', ..., '2357', '2358', '2359'], dtype=object)




```python
# set time_index as index
df.set_index('time_index', inplace=True)
df.head()
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
      <th>ratio</th>
    </tr>
    <tr>
      <th>time_index</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0804</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>0651</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>0751</th>
      <td>2</td>
      <td>31</td>
      <td>0</td>
      <td>50.632233</td>
      <td>3.046134</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1101</th>
      <td>3</td>
      <td>18</td>
      <td>0</td>
      <td>50.636093</td>
      <td>3.050447</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>0720</th>
      <td>3</td>
      <td>18</td>
      <td>0</td>
      <td>50.636093</td>
      <td>3.050447</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
!mkdir data_23_09_27
for time_index in distincts_time_index:
    df_time_index = df.loc[time_index]
    df_time_index.to_csv('data_23_09_27/{}.csv'.format(time_index))
```


```python

```
