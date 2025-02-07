from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Define out task 1 
def preprocess_data():
    print("Preprocess Data...")


def train_model():
    print("Training Model...")


def evaluate_model():
    print("Evaluate Models...")



with DAG(
    "ml_pipeline",
    start_date = datetime(2024,1,1),
    schedule_interval = "@weekly"
) as dag:
    

    # Define the task with sequnce
    preprocess = PythonOperator(task_id= "preprocess_task", python_callable = preprocess_data)
    train = PythonOperator(task_id = "train_task", python_callable = train_model)
    evaluate = PythonOperator(task_id = "evaluate_task", python_callable= evaluate_model)

    # sequence
    # set dependencies
    preprocess >> train >> evaluate