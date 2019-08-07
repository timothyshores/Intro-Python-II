import sys


class Store:
   def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        # Human readable string version of the object
        store = self.name + ":"
        for department_num in range(len(self.departments)):
            store += f" {department_num + 1}: {self.departments[n]}"
        return store

    def __repr__(self):
        # Python readable string version of the object
        return f'Store({repr(self.name)}, {repr(self.departments)})'


if __name__ == "__main__":
    store1 = Store("Tim's store", ["Department 1", "Department 2"])

    print(store1)  # returns "Tim's store: Department 1, Department 2"
    print(repr(store1))  # returns "Store("Tim's store", ['Department 1', 'Department 2'])

    selection = input("Select department number: ")

    if int(selection) < 1 or int(selection) >= len(s.departments):
        print(f"Department {selection} does not exist")
        sys.exit(1)

    print(f"Here are all ")
