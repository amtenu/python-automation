import csv

employees = [
    {
        "id": 1,
        "name": "Alice",
        "role": "Frontend Developer",
        "department": "Engineering",
        "salary": 85000,
        "is_full_time": True
    },
    {
        "id": 2,
        "name": "Michael",
        "role": "Backend Developer",
        "department": "Engineering",
        "salary": 92000,
        "is_full_time": True
    },
    {
        "id": 3,
        "name": "Sarah",
        "role": "DevOps Engineer",
        "department": "Infrastructure",
        "salary": 98000,
        "is_full_time": True
    },
    {
        "id": 4,
        "name": "David",
        "role": "Product Manager",
        "department": "Product",
        "salary": 105000,

    }]

keys=["name","role","department"]

filtered_employees = [
    {key: emp.get(key) for key in keys}
    for emp in employees
]



with open('by_department.csv','w',newline='') as by_department:
    writer=csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()
    writer.writerows(filtered_employees)
