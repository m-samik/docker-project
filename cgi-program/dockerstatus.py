#!/usr/bin/python3

import cgi
import os
import subprocess as sp

print("content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("cmd")

out = sp.getoutput(f"sudo docker {cmd}")

print("""<p>""")

print(out)
print("""</p>""")
