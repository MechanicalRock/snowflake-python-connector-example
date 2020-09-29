import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import pandas as pd  

def snowflake_connection():
  # change the file path to the full path on your machine to service_user_rsa_key.p8 file
  with open("/Users/.../src/service_user_rsa_key.p8", "rb") as key:
      p_key= serialization.load_pem_private_key(
          key.read(),
          password=os.environ['PRIVATE_KEY_PASSPHRASE'].encode(),
          backend=default_backend()
      )
  pkb = p_key.private_bytes(
      encoding=serialization.Encoding.DER,
      format=serialization.PrivateFormat.PKCS8,
      encryption_algorithm=serialization.NoEncryption())
  
  ctx = snowflake.connector.connect(
      user='<user>',
      account='<accountname>.<region>', # example:   myaccount.us-east-1
      private_key=pkb,
      warehouse='<warehouse>',
      database='<database>',
      schema='<schema>'
      )

  cs = ctx.cursor()
  allrows=cs.execute("select * from <tablename> limit 10")
  data = pd.DataFrame(allrows)
  return len(data)
