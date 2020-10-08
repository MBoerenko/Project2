import os

dbusr = "postgres"
dbpwd = "$sbn655B"
dbhost = "localhost"
dbengine = "postgresql"
db = "postgres"
cxnstring = (os.environ["DATABASE_URL"] if os.getenv("DATABASE_URL")
    else f"{dbengine}://{dbusr}:{dbpwd}@{dbhost}/{db}")

