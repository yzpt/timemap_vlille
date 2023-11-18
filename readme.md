# Temporal insights visualization: bubble map with vlille_gcp project data on Looker

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