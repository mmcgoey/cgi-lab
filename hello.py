#!/usr/bin/env python3

import os
import json


env ={}
for env_key, env_value in os.environ.items():
    env[env_key] = env_value


print("Content-Type: application/json")
print()



print(json.dumps(env))

print("Content-Type: text/html")
print()

print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")

