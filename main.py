import datetime, os
with open("README.md", 'a') as f:
    f.write(f"{datetime.datetime.now()}\n")

print('exiting...')
