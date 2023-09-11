import os
from dotenv import load_dotenv

load_dotenv()

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
PGPORT = str(os.getenv("PGPORT"))
ip = str(os.getenv("ip"))
POSTGRES_URI_DEFAULT = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/postgres"
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
