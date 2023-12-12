import pendulum
from datetime import datetime
from airflow import DAGS
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# timezone 한국시간으로 변경
kst = pendulum.timezon("Asia/Seoul")

# 기본 args 생성
default_args = {
    'owner' : "Hello world",
    'email' : ['airflow@airflow.com'],
    'email_on_failure':False,
}

# DAG 생성
with DAG(
    dag_id ='ex_hello_world',
    default_args=default_args,
    start_date=datetime(2023,11,28, tzinfo=kst),
    schedule_interval='@once',
    tags=['test']
) as dag:
    
    def print_hello():
        print('hello world')
    
    t1 = DummyOperator(
        task_id='dummy_task_id',
        retries=5,
    )

    t2 = PythonOperator(
        task_id='Hello_World',
        python_callable=print_hello
    )

    t1 >> t2
