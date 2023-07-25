
def student(*fname):  # if we are not sure how many arguments we will have we use arg *
    print("Students name is " + fname[1])


student("Fili", "Kili", "Bofur", "Bifur")


def pupil(**name):  # if we have multiple keyword arguments
    print("Pupils last name is " + name["last_name"])


pupil(first_name="Thorin", last_name="Oakenshield")


def empty_function():
    pass  # if we want to avoid error and want an empty function


def tuple_args(days):
    for(x) in days:
        print(x)


weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# if you put set you get randomized days =unordered variables
# tuple and list will print in the following order
tuple_args(weekdays)

# dictionary
Killer_whale = {
    "Domain": "Eukaryota",
    "Kingdom": "Animalia",
    "Class": "Mammalia",
    "Family": "Delphinidae"
}
# Nested dictionary
Animals = {
    "Dolphin": {
     "Class": "Mammalia",
     "Family": "Delphinidae"
    },  "Shrimp": {
            "Class": "Malacostraca",
            "Family": "Crangonidae"
    },  "Gull": {
            "Class": "Aves",
            "Family": "Laridae"
    }
}
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(Killer_whale["Class"])
print(len(Killer_whale))

print(Animals["Gull"]["Class"])
print(Animals.keys())

print(car.get("model"))


