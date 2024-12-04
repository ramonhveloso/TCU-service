base_config = {
    "sheet_name_journeys": "Jornadas",
    "table_name_journeys": "journeys",
    "sheet_name_payments": "Pagamentos",
    "table_name_payments": "payments",
    "sheet_name_extra_expenses": "Gastos Extras",
    "table_name_extra_expenses": "extra_expenses",
    "sheet_name_hourly_rates": "Valor Hora",
    "table_name_hourly_rates": "hourly_rates",
    "process_jorneys": True,
    "process_payments": True,
    "process_hourly_rates": True,
    "process_extra_expenses": True,
}

users = [
    {
        "user_id": 8,
        "name": "Matheus Prates",
        "excel_path": "data_loader/data/Matheus_Banco_de_Horas.xlsx",
    },
    {
        "user_id": 7,
        "name": "Mathias Luz",
        "excel_path": "data_loader/data/Mathias_Banco_de_Horas.xlsx",
    },
    {
        "user_id": 5,
        "name": "Ramon Veloso",
        "excel_path": "data_loader/data/Ramon_Banco_de_Horas.xlsx",
    },
    {
        "user_id": 9,
        "name": "Junior Lima",
        "excel_path": "data_loader/data/Junior_Banco_de_Horas.xlsx",
    },
    {
        "user_id": 10,
        "name": "Caio Jhony",
        "excel_path": "data_loader/data/Caio_Banco_de_Horas.xlsx",
    },
]

configs = [
    {**base_config, **user} for user in users
]
