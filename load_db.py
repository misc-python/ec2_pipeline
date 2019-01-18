from sqlalchemy import create_engine
import pandas as pd
import os


csv_data = pd.read_csv('assets/ks-projects-201801.csv')

# .tail(5) will retrie only the first 5 entries for testing purpose:
df = pd.DataFrame(csv_data).head(100)

df.rename(columns={'ID': 'kickstarter_id',
                   'usd pledged': 'usd_pledged'},
          inplace=True)

db_protocol = 'postgresql'
db_host = os.environ.get('DB_HOST', '')
db_user = os.environ.get('DB_USER', '')
db_password = os.environ.get('DB_PASSWORD', '')
db_name = os.environ.get('DB_NAME', '')


engine = create_engine('{}://{}:{}@{}:5432/{}'.format(
    db_protocol, db_user, db_password, db_host, db_name
))

df.to_sql("project_data_kickstarter", engine, if_exists='append', index=False)
