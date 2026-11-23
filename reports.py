import matplotlib.pyplot as plt
import trips


def revenue_report():
    print("\n--- Rafting Business Report ---")

    if len(trips.trips) == 0:
        print("No rafting trips have been recorded yet.")
        return

    total_trips = len(trips.trips)
    total_people = 0

    river_totals = {}

    for trip in trips.trips:
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

    if len(trips.trips) == 0:
        print("No rafting trips available to create charts.")
        return

    river_totals = {}

    for trip in trips.trips:
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

    for trip in trips.trips:
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