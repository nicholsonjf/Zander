
CREATE TABLE IF NOT EXISTS applications
(appid integer PRIMARY KEY AUTOINCREMENT,
appname text);

CREATE TABLE IF NOT EXISTS accounts (
record_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id TEXT,
permission TEXT,
user_app INTEGER,
hrid INTEGER,
FOREIGN KEY(user_app) REFERENCES applications(appid)
FOREIGN KEY(hrid) REFERENCES emp_info(empid)
);

CREATE VIEW account_owners AS
SELECT a.appname AS APPLICATION, b.user_id AS APP_ID,
b.permission AS PERM, c.first_name || ' ' || c.last_name AS FULL_NAME,
c.email AS EMAIL
FROM applications AS a
LEFT JOIN accounts AS b ON a.appid = b.user_app
LEFT JOIN emp_info AS c ON b.hrid = c.emp_id
