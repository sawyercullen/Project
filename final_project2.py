import csv
import matplotlib.pyplot as plt

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
        print("No reservation file found. Starting with empty reservations.")


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
        print("No trip history found. Starting with empty trip history.")


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
    print("5. Revenue report")
    print("6. View charts")
    print("7. Save and exit")


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
        key=lambda river: river_totals[river]["people"]
    )

    print("Total trips:", total_trips)
    print("Total people rafting:", total_people)
    print("Average group size:", round(average_group_size, 2))
    print("Most popular river:", top_river)

    print("\nTotals by river:")

    for river, totals in river_totals.items():
        print("\n", river)
        print("  Trips:", totals["trips"])
        print("  People:", totals["people"])


def charts():
    print("\n--- Montana River Adventures Charts ---")

    if len(trips) == 0:
        print("No rafting trips available to create charts.")
        return

    river_totals = {}

    for trip in trips:
        river = trip["river"]
        people = trip["people"]

        if river not in river_totals:
            river_totals[river] = 0

        river_totals[river] += people

    rivers = list(river_totals.keys())
    people_by_river = list(river_totals.values())

    plt.figure()
    plt.bar(rivers, people_by_river)
    plt.title("People on Rafting Trips by River")
    plt.xlabel("River")
    plt.ylabel("Number of People")
    plt.tight_layout()
    plt.savefig("people_by_river.png")
    plt.show()

    print("Saved people_by_river.png")

    date_totals = {}

    for trip in trips:
        date = trip["date"]
        people = trip["people"]

        if date not in date_totals:
            date_totals[date] = 0

        date_totals[date] += people

    dates = sorted(date_totals.keys())
    people_by_date = []

    for date in dates:
        people_by_date.append(date_totals[date])

    plt.figure()
    plt.plot(dates, people_by_date, marker="o")
    plt.title("People on Rafting Trips by Date")
    plt.xlabel("Date")
    plt.ylabel("Number of People")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("people_by_date.png")
    plt.show()

    print("Saved people_by_date.png")


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
            charts()

        elif choice == "7":
            save_reservations()
            save_trips()
            print("All data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-7.")


main()