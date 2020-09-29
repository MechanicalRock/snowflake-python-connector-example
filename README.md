# snowflake-python-connection-example

### To get started you will need to follow below steps:

1. Open src/service_user_rsa_key.p8 file and place your private key in it
2. Open src/snowflake.py and update your private key path (line 11)
3. Open src/snowflake.py and update your snowflake connection details: accountname, region, database, warehouse and table name
4. Add an environment variable for your private key pass phrase. In bash terminal you can run 
   ```
   export PRIVATE_KEY_PASSPHRASE=<your pass phrase>
   ```

Once the above setup is completed you should be good to run the test. 


### To install dependencies and run the test you can use the following commands:

To create a python virtual environment run:

```
python3 -m venv .venv
source ./.venv/bin/activate
```

To install dependencies run: 
```
pip3 install -r requirements.txt
```

To run your tests:
```
python3 -m unittest
```

To turn off virtual env  run "deactivate" or close the terminal 
