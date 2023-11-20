# Temporal insights visualization: Plotply bubble map of vlille_gcp project dataset



https://github.com/yzpt/timemap_vlille/assets/140260395/cb0c194c-00e8-4d28-8ef2-76d4499cb2cd



```bash
gcloud config list
PROJECT_ID=zapart-data-vlille
gcloud config set project $PROJECT_ID

SERVICE_ACCOUNT_EMAIL=SA-vlille@zapart-data-vlille.iam.gserviceaccount.com

# generate key
gcloud iam service-accounts keys create key.json --iam-account=$SERVICE_ACCOUNT_EMAIL

touch bigquery_requests.py
code bigquery_requests.py

# Venv
python3 -m venv venv
source venv/bin/activate

# pip
pip install google-cloud-bigquery
pip install pandas
pip install ipykernel
pip install db-dtypes

```
# --- See nb*.ipynb ---

