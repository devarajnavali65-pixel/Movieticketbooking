import os
import psycopg2

def clear_users():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("Error: DATABASE_URL environment variable is not set.")
        return

    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        print("Cleaning up users table...")
        cur.execute("TRUNCATE TABLE users RESTART IDENTITY CASCADE;")
        conn.commit()
        
        print("Success! All user sign-in details have been deleted.")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    clear_users()
