import os
import psycopg2

def sync_db():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not set. Skipping sync.")
        return

    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # Read schema.sql from the db directory
        schema_path = os.path.join("..", "db", "schema.sql")
        if not os.path.exists(schema_path):
            # Try local path if running in backend dir
            schema_path = "schema.sql" 
        
        if os.path.exists(schema_path):
            with open(schema_path, "r") as f:
                schema_sql = f.read()
            
            cur.execute(schema_sql)
            conn.commit()
            print("Database schema synced successfully.")
        else:
            print(f"Schema file not found at {schema_path}. Skipping SQL apply.")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error syncing database: {e}")

if __name__ == "__main__":
    sync_db()
