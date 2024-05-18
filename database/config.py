from sqlalchemy import create_engine

# Cria a conexão com o banco de dados
engine = create_engine('mssql+pyodbc://@Felipe/PRODUCAO?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

