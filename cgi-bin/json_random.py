#!/usr/bin/python

import random
import json
import os
import time

time.sleep(5)
print "Content-type: application/json"
print "Access-Control-Allow-Origin: *"
print

num = 10
if 'QUERY_STRING' in os.environ:
    foo,num = os.environ['QUERY_STRING'].split('=')
    if foo == 'length':
        num = int(num)

randlist = [random.randrange(1000) for x in range(num)]

print json.dumps(randlist)
