"""
given:
    since modern computers can execute >1 billion instructions per second.
objective:
    Does it a modern computer 10 seconds to iterate 10000000000 times?
NB: Python is was not a good language for this test.
    It constructs a range object which takes time.
"""

from datetime import datetime

start_time = datetime.now()
print(f"starting computation: {start_time}")

n = 10000000000
for i in range(0, n):
    i

end_time = datetime.now()
print(f"computation completed: {end_time}")

print(f"{end_time - start_time=}")
