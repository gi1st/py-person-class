class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            wife = people[i].get("wife")
            persons[i].wife = Person.people[wife]
        elif "husband" in people[i] and people[i]["husband"] is not None:
            husband = people[i].get("husband")
            persons[i].husband = Person.people[husband]
    return persons
