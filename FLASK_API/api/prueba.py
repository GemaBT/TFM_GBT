"""from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://api_user:api_password@localhost:3307/api_security")
conn = engine.connect()
result = conn.execute("SELECT * FROM users").fetchall()
print(result)
conn.close()

"""

from sqlalchemy import create_engine, text

# Conexión a la base de datos
engine = create_engine("mysql+pymysql://api_user:api_password@localhost:3307/api_security")
conn = engine.connect()

# Ejecuta la consulta correctamente usando text()
result = conn.execute(text("SELECT * FROM users")).mappings().all()

# Imprime cada fila como diccionario
for row in result:
    print(dict(row))

# Cierra la conexión
conn.close()