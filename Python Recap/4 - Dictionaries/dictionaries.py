user = {
    "name": "Ian",
    "role": "Developer",
    "level": "Junior",
    "experience_years": 1
}

print(user["name"])
print(user.get("role"))
print(user.get("location", "Not specified"))

user["location"] = "Nairobi"
user["experience_years"] = 2
print(user)

user.pop("level")
print(user)

print(list(user.keys()))
print(list(user.values()))

for key, value in user.items():
    print(f"{key}: {value}")

employees = {
    "emp1": {"name": "Ian", "department": "IT"},
    "emp2": {"name": "Sarah", "department": "Marketing"},
    "emp3": {"name": "Kevin", "department": "Finance"}
}

for emp_id, info in employees.items():
    print(emp_id, info["name"], info["department"])
