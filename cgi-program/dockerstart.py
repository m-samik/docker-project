#!/usr/bin/python3
import cgi
import os
import subprocess as sp

print("content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()
cname = f.getvalue("cname")
iname = f.getvalue("iname")
out = sp.getoutput(f"sudo docker run -dit --name {cname} {iname}")

print("""<p>""")

print(out)
print("""</p>""")
