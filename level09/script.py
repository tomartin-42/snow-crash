#!/usr/bin/python
i = 0
response = ""

try:
    f = open("/home/user/level09/token")
    data = f.read()
    print(data)
    for l in data:
            response += chr(ord(l) - i))
            i += 1
    print(response)
except:
    print(response)
