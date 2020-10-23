import datetime, os
with open(f'{datetime.datetime.now()}.txt', 'w') as f:
    f.write(f'written from {os.path.abspath(__file__)}')

print("Hello from the script")