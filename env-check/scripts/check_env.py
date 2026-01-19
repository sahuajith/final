import os
import sys
required_vars=["DB_PASSWORD"]
missing_vars=[]
for var in required_vars:
    if os.getenv(var) is None:
        missing_vars.append(var)
if missing_vars:
    print("Error")
    for var in missing_vars:
        print(f"-{var}")
    sys.exit(1)
else:
    print("Success")
    sys.exit(0)