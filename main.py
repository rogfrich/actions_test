import datetime, os
with open("README.md", 'w') as f:
    f.write(f"{datetime.datetime.now()}")

print('exiting...')
