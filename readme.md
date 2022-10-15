# Mee6 DB Dumper

This python script is small but mighty! It can dump the levels database of any mee6 enabled server.

*most other tools for interacting with the mee6 api have been depricated by mee6*

```
Step 1: Download main.py // `git clone https://github.com/NebulaBC/mee6-db-dump`.
Step 2: Run `pip3 install -r requirements.txt`
Step 3: Run `python3 main.py`.
Step 4: When you are prompted for your server id, go to https://mee6.xyz/dashboard/ and click go on your desired server.
Step 5: Take the server's mee6 id from the URL (E.g. https://x.neb.cx/u/kHyEWe.png)
Step 6: When prompted for your user token, open inspect element on your mee6 tab. Click the "Storage" category inside inspect element. Now on the left hand side click Local Storage -> https://mee6.xyz -> now take the value (without the double quotes) from the "token" field. That is your user token.
Step 7: Profit!
```
