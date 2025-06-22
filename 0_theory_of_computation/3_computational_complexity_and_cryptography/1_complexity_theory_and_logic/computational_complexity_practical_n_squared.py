from datetime import datetime

print("what n² looks like for 10000 input size")

start_time = datetime.now()
print(f"starting computation: {start_time}")

n = 100
for i in range(0, n):
    for j in range(0, n):
        i * j

end_time = datetime.now()
print(f"computation completed: {end_time}")

print(f"{end_time - start_time = }")
