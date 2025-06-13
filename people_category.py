people = [
    {"name": "Ali", "age": 25, "country": "Uzbekistan"},
    {"name": "Laylo", "age": 17, "country": "Uzbekistan"},
    {"name": "Malika", "age": 12, "country": "Uzbekistan"},
    {"name": "Jasur", "age": 30, "country": "Uzbekistan"},
    {"name": "Dildora", "age": 19, "country": "Uzbekistan"}
]

def show_info(person):
    for key in person:
        print(f"{key}: {person[key]}")

def check_category(age):
    if age >= 18:
        return "Adult"
    elif 13 <= age <= 17:
        return "Teen"
    else:
        return "Child"

for person in people:
    show_info(person)
    category = check_category(person["age"])
    print("Category:", category)
    print("-" * 20)
