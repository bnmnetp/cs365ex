#!/usr/bin/env python3

# debugging tip from cl:  QUERY_STRING=foo ./cgi-bin/formtest.py
import os

print("Content-type: text/html")
print("")

if os.environ['QUERY_STRING'] == "":
    print('''
<form method="get">

<input type="text" name="firstname" />
<input type="text" name="lastname" />
<input type="submit" value="submit" />

</form>
''')

if 'QUERY_STRING' in os.environ:
    if os.environ["QUERY_STRING"] != "":
        print("<code>", os.environ['QUERY_STRING'], "</code>")


    
