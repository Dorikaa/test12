#!/usr/bin/env python3

import requests

a = []

for i in range(2000, 3201):
    if i // 7 and (i % 5 != 0):
        a.append(str(i))

# print(','.join(a))

r = requests.get("https://google.ro")
# print(r.status_code)

name = input("Your name? ")
print("your name is:", name)
