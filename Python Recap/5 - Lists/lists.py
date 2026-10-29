tasks = ["read file", "clean data", "generate report", "send email"]
print(tasks)

print(tasks[0])
print(tasks[-1])
print(tasks[1:3])

tasks.append("backup database")
tasks.insert(2, "validate data")
print(tasks)

tasks.remove("clean data")
completed = tasks.pop()
print("Completed:", completed)
print(tasks)

scores = [85, 42, 99, 71, 63]
scores.sort()
print(scores)

scores.reverse()
print(scores)

doubled = [n * 2 for n in range(1, 6)]
print(doubled)
