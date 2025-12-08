from sqlmodel import text
from api.db import engine

def fix():
    with engine.connect() as conn:
        # We need to commit the transaction for DDL or data changes
        conn.execute(text("DROP TABLE IF EXISTS charmessages"))
        conn.commit()
    print("Dropped table charmessages.")

if __name__ == "__main__":
    fix()
