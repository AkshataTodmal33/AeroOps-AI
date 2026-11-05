from flight_data import get_flight_data


flights = get_flight_data()

print("Total flights:", len(flights))

for flight in flights:
    print(flight)