#!/usr/bin/python3

import cgi
import os
import subprocess as sp

print("content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()
dstop = f.getvalue("dstop")
out = sp.getoutput(f"sudo docker stop {dstop}")

print("""<p>""")

print(out)
print("""</p>""")
