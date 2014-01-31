import psycopg2, csv

# Postgres connection and cursor
conn = psycopg2.connect("dbname=q12014 user=postgres password=08zerl!n@ps")
cur = conn.cursor()

# Get applications
cur.execute("SELECT * FROM applications;")
app_ids = [i[0] for i in cur]

# Insert into hrdb_lookups
for i in app_ids:
	sql = """
	      INSERT INTO hrdb_lookups (application_id)
	      VALUES (%s);
	      """
	values = i,
	cur.execute(sql, values)
conn.commit()

# Print applications to make sure they made it in
cur.execute("SELECT * FROM hrdb_lookups;")
for record in cur:
	print record
