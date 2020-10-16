import os	

api_key = "98ff232f9d7241e165225e7f42731c5d242c94d0aed9ba54b4276a0039bac746"
dbusr = "postgres"	
dbpwd = "postgres"	
dbhost = "localhost"	
dbengine = "postgresql"	
db = "postgres"
cxnstring = (os.environ["DATABASE_URL"] if os.getenv("DATABASE_URL")	
    else f"{dbengine}://{dbusr}:{dbpwd}@{dbhost}/{db}")