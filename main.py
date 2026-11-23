import trips
import reports


def show_menu():
    print("\nMontana River Adventures")
    print("1. View reservations")
    print("2. Add or update reservation")
    print("3. Record a rafting trip")
    print("4. View trip history")
    print("5. Revenue report")
    print("6. View charts")
    print("7. Save and exit")


def main():
    trips.load_reservations()
    trips.load_trips()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            trips.view_reservations()

        elif choice == "2":
            trips.add_reservation()

        elif choice == "3":
            trips.record_trip()

        elif choice == "4":
            trips.view_trips()

        elif choice == "5":
            reports.revenue_report()

        elif choice == "6":
            reports.charts()

        elif choice == "7":
            trips.save_reservations()
            trips.save_trips()
            print("All data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-7.")


main()