import datetime
header = """
# TEST README

Last edit:\n
"""

with open("README.md", "w") as f:
    f.write(header)
    f.write(str(datetime.datetime.today()))
