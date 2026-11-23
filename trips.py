import csv

reservations = {}
trips = []


def load_reservations():
    global reservations

    reservations = {}

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
        print("No reservation file found.")


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

    trips = []

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
        print("No trip history found.")


def save_trips():
    with open("trips.csv", "w", newline="") as file:
        headings = ["date", "name", "river", "people"]

        writer = csv.DictWriter(file, fieldnames=headings)
        writer.writeheader()

        for trip in trips:
            writer.writerow(trip)


def view_reservations():
    print("\nCurrent Reservations")

    if len(reservations) == 0:
        print("No reservations found.")
        return

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
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


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
        return

    for trip in trips:
        print("\nCustomer:", trip["name"])
        print("Date:", trip["date"])
        print("River:", trip["river"])
        print("People:", trip["people"])