import psycopg2, csv

# Postgres connection and cursor
conn = psycopg2.connect("dbname=q12014 user=postgres password=08zerl!n@ps")
cur = conn.cursor()

# Delete applications if they are already in table
cur.execute("DELETE FROM applications;")

# CSV with application names and batch id
with open('applications.csv') as app_file:
	lol = [i for i in csv.reader(app_file)]

# Insert applications into Postgres localhost.q12014.applications table
for i in lol:
	sql = """
	      INSERT INTO applications (application_name, batch_name)
	      VALUES (%s, %s);
	      """
	values = i[0], i[1]
	cur.execute(sql, values)
conn.commit()

# Print applications to make sure they made it in
cur.execute("SELECT * FROM applications;")
for record in cur:
	print record
