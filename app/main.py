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
            wife = data[i].get("wife")
            if data[i]["wife"] is not None and wife in Person.people:
                wife = data[i].get("wife")
                persons[i].wife = Person.people[wife]
            else:
                persons[i].wife = None
        elif "husband" in data[i]:
            husband = data[i].get("husband")
            if data[i]["husband"] is not None and husband in Person.people:
                persons[i].husband = Person.people[husband]
            else:
                persons[i].husband = None
    return persons
