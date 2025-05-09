class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(data: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in data]
    for i in range(len(data)):
        if "wife" in data[i]:
            if data[i]["wife"] is not None:
                wife = data[i].get("wife")
                persons[i].wife = Person.people[wife]
            else:
                delattr(persons[i], "wife")
        elif "husband" in data[i]:
            if data[i]["husband"] is not None:
                husband = data[i].get("husband")
                persons[i].husband = Person.people[husband]
            else:
                delattr(persons[i], "husband")
    return persons
