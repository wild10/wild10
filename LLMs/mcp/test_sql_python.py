from sqlalchemy import create_engine, text


DATABASE_URL = "postgresql+psycopg2://hotel_user:hotel_123@localhost:5432/hotel_db"


engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    results = conn.execute(text("SELECT*FROM habitaciones; "))
    # Convertir el resultado a una lista.
    for row in results:
        print(row)
