from datetime import datetime
from airflow import DAG

config = {
    'dag_id_1': {'schedule_interval': None, "start_date": datetime(2018, 11, 11)},  
    'dag_id_2': {'schedule_interval': None, "start_date": datetime(2018, 11, 11)},  
    'dag_id_3': {'schedule_interval': None, "start_date": datetime(2018, 11, 11)}}

for dict in config:
    with DAG(dict, start_date=config[dict]['start_date'], schedule=config[dict]['schedule_interval']) as dict: pass