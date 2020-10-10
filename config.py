import os	

api_key = "98ff232f9d7241e165225e7f42731c5d242c94d0aed9ba54b4276a0039bac746"
dbusr = "mxlaynocnogpnf"	
dbpwd = "251ebbe51259cb6370917438187fd23d573c541f9ab8115445f5f526b90581e0"	
dbhost = "ec2-107-20-104-234.compute-1.amazonaws.com"	
dbengine = "postgresql"	
db = "d68nfijiphnfv5"
cxnstring = (os.environ["DATABASE_URL"] if os.getenv("DATABASE_URL")	
    else f"{dbengine}://{dbusr}:{dbpwd}@{dbhost}/{db}")