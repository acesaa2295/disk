count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")

def greet(first_name, last_name):
    print(f"hy {first_name} {last_name}")
    print("iron throne is yours!")


greet("rhanerya", "targaryen")
greet("jon", "snow")
greet("daenerys", "targaryen")

def greet(name):
    print(f"hy {name}")

print(greet("Daemon"))\


def cole(number, by):
    return number + by

print(cole(10, 5))

def multi(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multi(2, 3, 4, 5))

def baddie(text):
        message = f"{text} is baddie"

        print(message)

baddie("Aaisha")