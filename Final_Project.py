
reservations = {
    "Sawyer Cullen": {
        "date": "2026-07-10",
        "people": 4,
        "trip": "Blackfoot"
    },
    "Teddy Higgins": {
        "date": "2026-07-11",
        "people": 6,
        "trip": "Clark Fork"
    },
    "Harry Higgins": {
        "date": "2026-07-12",
        "people": 3,
        "trip": "Blackfoot"
    }
}

def show_menu():
   def show_menu():
    print("\nMontana River Adventures")
    print("1. View reservations")
    print("2. Add or update reservation")
    print("3. Record a rafting trip")
    print("4. View trip history")
    print("5. Revenue report")
    print("6. Save and exit")


def view_reservations():
    print("\nRafting Reservations")

    for name, details in reservations.items():
        print("Customer:", name)
        print("Date:", details["date"])
        print("People:", details["people"])
        print("Trip:", details["trip"])
        print()

def add_reservation():
    name = input("Enter customer name: ").strip()

    if name == "":
        print("Customer name cannot be empty.")
        return

    if name in reservations:
        print("Updating existing reservation.")
    else:
        print("Adding new reservation.")

    date = input("Enter trip date (YYYY-MM-DD): ")
    
    while True:
        try:
            people = int(input("Enter number of people: "))

            if people > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    trip = input("Enter river (Blackfoot or Clark Fork): ")

    reservations[name] = {
        "date": date,
        "people": people,
        "trip": trip
    }
1

print("Reservation saved!")

def main():
    load_reservations()
    load_trips()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_reservations()

        elif choice == "2":
            add_reservation()

        elif choice == "3":
            record_trip()

        elif choice == "4":
            view_trips()

        elif choice == "5":
            revenue_report()

        elif choice == "6":
            save_reservations()
            save_trips()
            print("All data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-6.")

main()


import csv

reservations = {}


def load_reservations():
    global reservations

    try:
        with open("reservations.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                reservations[row["name"]] = {
                    "river": row["river"],
                    "date": row["date"],
                    "people": int(row["people"])
                }

    except FileNotFoundError:
        reservations = {
            "John Smith": {
                "river": "Blackfoot River",
                "date": "2026-07-10",
                "people": 4
            },
            "Sarah Jones": {
                "river": "Clark Fork River",
                "date": "2026-07-11",
                "people": 6
            },
            "Mike Wilson": {
                "river": "Blackfoot River",
                "date": "2026-07-12",
                "people": 3
            }
        }

        save_reservations()


def save_reservations():
    with open("reservations.csv", "w", newline="") as file:
        headings = ["name", "river", "date", "people"]
        writer = csv.DictWriter(file, fieldnames=headings)

        writer.writeheader()

        for name, details in reservations.items():
            writer.writerow({
                "name": name,
                "river": details["river"],
                "date": details["date"],
                "people": details["people"]
            })


def show_menu():
    print("\nMontana River Adventures")
    print("1. View reservations")
    print("2. Add or update reservation")
    print("3. Record a rafting trip - Coming soon")
    print("4. View trip history - Coming soon")
    print("5. Save and exit")


def view_reservations():
    print("\nCurrent Reservations")

    if len(reservations) == 0:
        print("No reservations found.")

    for name, details in reservations.items():
        print("\nCustomer:", name)
        print("River:", details["river"])
        print("Date:", details["date"])
        print("People:", details["people"])


def get_people():
    while True:
        try:
            people = int(input("Enter number of people: "))

            if people > 0:
                return people
            else:
                print("Enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def add_reservation():
    name = input("Enter customer name: ").strip()

    if name == "":
        print("Customer name cannot be empty.")
        return

    if name in reservations:
        print("Updating existing reservation.")
    else:
        print("Adding new reservation.")

    river = input("Enter river: ").strip()
    date = input("Enter trip date (YYYY-MM-DD): ").strip()
    people = get_people()

    if river == "" or date == "":
        print("River and date cannot be empty.")
        return

    reservations[name] = {
        "river": river,
        "date": date,
        "people": people
    }

    print("Reservation saved!")


def main():
    load_reservations()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_reservations()

        elif choice == "2":
            add_reservation()

        elif choice == "3" or choice == "4":
            print("Coming soon")

        elif choice == "5":
            save_reservations()
            print("Reservations saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-5.")


main()


import csv

reservations = {}

trips = []


def load_reservations():
    global reservations

    try:
        with open("reservations.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                reservations[row["name"]] = {
                    "river": row["river"],
                    "date": row["date"],
                    "people": int(row["people"])
                }

    except FileNotFoundError:
        reservations = {
            "John Smith": {
                "river": "Blackfoot River",
                "date": "2026-07-10",
                "people": 4
            },
            "Sarah Jones": {
                "river": "Clark Fork River",
                "date": "2026-07-11",
                "people": 6
            },
            "Mike Wilson": {
                "river": "Blackfoot River",
                "date": "2026-07-12",
                "people": 3
            }
        }

        save_reservations()


def save_reservations():
    with open("reservations.csv", "w", newline="") as file:
        headings = ["name", "river", "date", "people"]
        writer = csv.DictWriter(file, fieldnames=headings)

        writer.writeheader()

        for name, details in reservations.items():
            writer.writerow({
                "name": name,
                "river": details["river"],
                "date": details["date"],
                "people": details["people"]
            })


def load_trips():
    global trips

    try:
        with open("trips.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                trips.append({
                    "date": row["date"],
                    "name": row["name"],
                    "river": row["river"],
                    "people": int(row["people"])
                })

    except FileNotFoundError:
        trips = []


def save_trips():
    with open("trips.csv", "w", newline="") as file:
        headings = ["date", "name", "river", "people"]
        writer = csv.DictWriter(file, fieldnames=headings)

        writer.writeheader()

        for trip in trips:
            writer.writerow(trip)


def show_menu():
    print("\nMontana River Adventures")
    print("1. View reservations")
    print("2. Add or update reservation")
    print("3. Record a rafting trip")
    print("4. View trip history")
    print("5. Save and exit")


def view_reservations():
    print("\nCurrent Reservations")

    if len(reservations) == 0:
        print("No reservations found.")

    for name, details in reservations.items():
        print("\nCustomer:", name)
        print("River:", details["river"])
        print("Date:", details["date"])
        print("People:", details["people"])


def get_people():
    while True:
        try:
            people = int(input("Enter number of people: "))

            if people > 0:
                return people
            else:
                print("Enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


def add_reservation():
    name = input("Enter customer name: ").strip()

    if name == "":
        print("Customer name cannot be empty.")
        return

    if name in reservations:
        print("Updating existing reservation.")
    else:
        print("Adding new reservation.")

    river = input("Enter river: ").strip()
    date = input("Enter trip date (YYYY-MM-DD): ").strip()

    if river == "" or date == "":
        print("River and date cannot be empty.")
        return

    people = get_people()

    reservations[name] = {
        "river": river,
        "date": date,
        "people": people
    }

    print("Reservation saved!")


def record_trip():
    name = input("Enter customer name: ").strip()

    if name not in reservations:
        print("Customer does not have a reservation.")
        return

    details = reservations[name]

    print("River:", details["river"])
    print("Reserved group size:", details["people"])

    people = get_people()

    if people > details["people"]:
        print("Cannot record more people than the reservation allows.")
        return

    date = input("Enter trip date (YYYY-MM-DD): ").strip()

    if date == "":
        print("Date cannot be empty.")
        return

    trip = {
        "date": date,
        "name": name,
        "river": details["river"],
        "people": people
    }

    trips.append(trip)

    print("Rafting trip recorded successfully!")


def view_trips():
    print("\nRafting Trip History")

    if len(trips) == 0:
        print("No trips have been recorded yet.")

    for trip in trips:
        print("\nCustomer:", trip["name"])
        print("Date:", trip["date"])
        print("River:", trip["river"])
        print("People:", trip["people"])


def main():
    load_reservations()
    load_trips()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_reservations()

        elif choice == "2":
            add_reservation()

        elif choice == "3":
            record_trip()

        elif choice == "4":
            view_trips()

        elif choice == "5":
            save_reservations()
            save_trips()
            print("All data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-5.")


main()

def revenue_report():
    print("\n--- Rafting Business Report ---")

    if len(trips) == 0:
        print("No rafting trips have been recorded yet.")
        return

    total_trips = len(trips)
    total_people = 0
    river_totals = {}

    for trip in trips:
        river = trip["river"]
        people = trip["people"]

        total_people += people

        if river not in river_totals:
            river_totals[river] = {
                "trips": 0,
                "people": 0
            }

        river_totals[river]["trips"] += 1
        river_totals[river]["people"] += people

    average_group_size = total_people / total_trips

    top_river = max(
        river_totals,
        key=lambda river: river_totals[river]["trips"]
    )

    print("Total trips:", total_trips)
    print("Total people rafting:", total_people)
    print("Average group size:", round(average_group_size, 2))
    print("Most popular river:", top_river)

    print("\nTrips by river:")

    for river, totals in river_totals.items():
        print(river)
        print("  Trips:", totals["trips"])
        print("  People:", totals["people"])