import sqlite3


connection = sqlite3.connect('../urls_database.db',)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE urls (
  url TEXT,
  id TEXT PRIMARY KEY,
  count INTEGER
)
""")
cursor.execute("INSERT INTO urls (url, id, count) VALUES ('https://wa.me/message/SG6D2NUNM5VIJ1', 'wa_delbuey_pag', 0)")

connection.commit()
connection.close()