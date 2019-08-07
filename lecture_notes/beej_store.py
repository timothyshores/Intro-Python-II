import sys
import department from Department


class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        """Human-readable string version of the object."""
        s = self.name + ":"
        for n in range(len(self.departments)):
            s += f" {n+1}:{self.departments[n]}"
        return s

    def __repr__(self):
        """Python-readable string version of the object."""
        return f'Store({repr(self.name)}, {repr(self.departments)})'


if __name__ == "__main__":  # "if we're running this from the command line
    s = Store("Beej's store", [
        Department("Dept1"),
        Department("Dept2")
    ])

    done = False

    while not done:
        print()
        print(s)
        print()

        selection = input("Select department number: ")

        try:
            selection = int(selection) - 1
        except ValueError:
            print("Enter a valid number")

    if selection < 0 or selection >= len(s.departments):
        print("No such department")
        sys.exit(1)

    print(f"Here are all the products in {s.departments[selection]}:")
