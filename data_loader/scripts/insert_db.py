import os
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from data_loader.config.conf_insert_db import configs

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("A variável de ambiente DATABASE_URL não está definida.")

engine = create_engine(DATABASE_URL)

def process_and_insert_jorneys(config):
    print(f"Iniciando processamento para {config['name']}...")
    
    df = pd.read_excel(config["excel_path"], sheet_name=config["sheet_name_journeys"])
    
    df = df.rename(
        columns={
            "Data": "start_date",
            "Início": "start_time",
            "Final": "end_time",
            "Atividade": "description",
            "Duração": "hours_worked",
            "Valor da Hora": "hourly_rate",
        }
    )
        
    df["start"] = pd.to_datetime(df["start_date"].astype(str) + " " + df["start_time"].astype(str))
    df["end"] = pd.to_datetime(df["start_date"].astype(str) + " " + df["end_time"].astype(str))

    df["hours_worked"] = df["hours_worked"].astype(float)
    df["hourly_rate"] = df["hourly_rate"].astype(float)
    df["created_at"] = datetime.now()
    df["last_modified"] = datetime.now()
    df["user_id"] = config["user_id"]

    df = df[["user_id", "start", "end", "hours_worked", "hourly_rate", "description", "created_at", "last_modified"]]

    tabela_destino = config["table_name_journeys"]
    with engine.begin() as connection: 
        df.to_sql(tabela_destino, con=connection, if_exists="append", index=False)
        print(f"Dados para {config['name']} inseridos com sucesso!")

    print(f"Dados para {config['name']} inseridos com sucesso!")

def process_and_insert_payments(config):
    print(f"Iniciando processamento de pagamentos para {config['name']}...")

    df = pd.read_excel(config["excel_path"], sheet_name=config["sheet_name_payments"])

    df = df.rename(
        columns={
            "Data": "date",
            "Valor": "amount",
            "Descrição": "description",
        }
    )
    
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = df["amount"].astype(float)
    df["created_at"] = datetime.now()
    df["last_modified"] = datetime.now()
    df["user_id"] = config["user_id"]

    df = df[["user_id", "amount", "date", "description", "created_at", "last_modified"]]

    tabela_destino = config["table_name_payments"]
    with engine.begin() as connection: 
        df.to_sql(tabela_destino, con=connection, if_exists="append", index=False)
        print(f"Dados para {config['name']} inseridos com sucesso!")

    print(f"Pagamentos para {config['name']} inseridos com sucesso!")

def process_and_insert_hourly_rates(config):
    print(f"Iniciando processamento de valores por hora para {config['name']}...")

    df = pd.read_excel(config["excel_path"], sheet_name=config["sheet_name_hourly_rates"])

    df = df.rename(
        columns={
            "Inicio": "start_date",
            "Fim": "end_date",
            "Valor": "rate",
            "Status": "status",
            "Data Solicitação": "request_date",
        }
    )

    df["start_date"] = pd.to_datetime(df["start_date"])
    df["end_date"] = pd.to_datetime(df["end_date"])
    df["request_date"] = pd.to_datetime(df["start_date"])
    df["rate"] = df["rate"].astype(float)
    df["created_at"] = datetime.now()
    df["last_modified"] = datetime.now()
    df["user_id"] = config["user_id"]

    df = df[
        [
            "user_id",
            "rate",
            "start_date",
            "end_date",
            "status",
            "request_date",
            "created_at",
            "last_modified",
        ]
    ]

    tabela_destino = config["table_name_hourly_rates"]
    with engine.begin() as connection: 
        df.to_sql(tabela_destino, con=connection, if_exists="append", index=False)
        print(f"Dados para {config['name']} inseridos com sucesso!")

    print(f"Valores por hora para {config['name']} inseridos com sucesso!")

def process_and_insert_extra_expenses(config):
    print(f"Iniciando processamento de gastos extras para {config['name']}...")

    df = pd.read_excel(config["excel_path"], sheet_name=config["sheet_name_extra_expenses"])

    df = df.rename(
        columns={
            "Data": "date",
            "Valor": "amount",
            "Descrição": "description",
            "Status": "status",
        }
    )

    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = df["amount"].astype(float)
    df["created_at"] = datetime.now()
    df["last_modified"] = datetime.now()
    df["user_id"] = config["user_id"]

    df = df[
        ["user_id", "amount", "description", "date", "status", "created_at", "last_modified"]
    ]

    tabela_destino = config["table_name_extra_expenses"]
    with engine.begin() as connection: 
        df.to_sql(tabela_destino, con=connection, if_exists="append", index=False)
        print(f"Dados para {config['name']} inseridos com sucesso!")

    print(f"Gastos extras para {config['name']} inseridos com sucesso!")

for config in configs:
    if config["process_jorneys"]:
        process_and_insert_jorneys(config)
        # try:
        #     process_and_insert_jorneys(config)
        # except Exception as e:
        #     print(f"Erro ao processar dados journeys para {config['name']}: {e}")
            
    if config["process_payments"]:
        try:
            process_and_insert_payments(config)
        except Exception as e:
            print(f"Erro ao processar dados payments para {config['name']}: {e}")
            
    if config["process_hourly_rates"]:
        try:
            process_and_insert_hourly_rates(config)
        except Exception as e:
            print(f"Erro ao processar dados hourly_rates para {config['name']}: {e}")
            
    if config["process_extra_expenses"]:
        try:
            process_and_insert_extra_expenses(config)
        except Exception as e:
            print(f"Erro ao processar dados extra_expenses para {config['name']}: {e}")
