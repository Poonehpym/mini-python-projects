def ask_number(question, minimum):
    while True:
        try:
            number = int(input(question))
            if number < minimum:
                print(f"Please enter a number >= {minimum}")
            else:
                return number
        except ValueError:
            print("Please enter digits only (like 2000000)")


print("=== Dong Calculator ===")

bill = ask_number("Total bill (Toman): ", 1)
service = ask_number("Service/tip percent: ", 0)
people = ask_number("Number of people: ", 1)

total = bill + (bill * service / 100)
per_person = total / people

print(f"Total with service: {int(total):,} Toman")
print(f"Each person pays: {int(per_person):,} Toman")