import sqlite3, csv

# Config
db_path = 'master.db'
schema_path = 'schema.sql'

def db_con():
    return sqlite3.connect(db_path)
def db_cursor(db):
    return db_con().cursor()
def db_init():
    with open(schema_path) as my_schema:
        script = my_schema.read()
    db = db_con()
    dbc1 = db_cursor(db)
    dbc1.execute(script)
    db.commit()
    print 'App DB has been created'
def query_apps(app = None):
    db1 = sqlite3.connect(db_path)
    dbc1 = db1.cursor()
    if not app:
        dbc1.execute('SELECT * FROM applications')
    if app:
        params = (app,)
        dbc1.execute('SELECT * FROM applications WHERE appname = ?', params)
    return dbc1.fetchall()
def add_app(appname):
    db1 = sqlite3.connect(db_path)
    dbc1 = db1.cursor()
    sql = "INSERT INTO applications VALUES (NULL, ?)"
    params = (appname,)
    dbc1.execute(sql, params)
    db1.commit()
    app_info = query_apps(app = appname)
    print 'Application {} was added with ID {}'.format(app_info[0][1], app_info[0][0])

def add_userlist(app, file):
    db1 = sqlite3.connect(db_path)
    dbc1 = db1.cursor()
    with open(file) as users_file:
        my_reader = csv.reader(users_file)
        user_list = [i for i in my_reader]
    for i in user_list:
        sql = """
              INSERT INTO accounts
              VALUES (NULL, ?, ?, ?, ?)
              """
        params = (i[0], i[1], app, i[2])
        db1.execute(sql, params)
    db1.commit()

def query_accounts(app = None):
    db1 = sqlite3.connect(db_path)
    dbc1 = db1.cursor()
    if not app:
        dbc1.execute('SELECT * FROM account_owners')
    if app:
        params = (app,)
        dbc1.execute('SELECT * FROM account_owners WHERE appname = ?', params)
    return dbc1.fetchall()

if __name__ == '__main__':
    db_init()
