import sqlite3

def log_message(user, message, timestamp):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (user, message, timestamp) VALUES (?, ?, ?)", 
              (user, message, str(timestamp)))
    conn.commit()
    conn.close()
