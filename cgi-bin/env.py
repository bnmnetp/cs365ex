#!/usr/bin/env python3

import os

print("Content-type: text/plain")
print("")


for key in sorted(os.environ):
    print(key, " : ", os.environ[key])
