######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = ("OUL", "1", "14-09-2026")

allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}

restricted_destinations = {"Moscow", "Pyongyang"}

flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": [
            "Alice Wong",
            "David Kim",
            "Fatima Ali"
        ]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": [
            "Chen Wei",
            "George Smith"
        ]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": [
            "Hana Lee",
            "Maria Garcia",
            "Noah Wilson"
        ]
    }
}


## Logic to find if a flight exists
def find_flight(flights, flight_number):
    if flight_number is None:
        return None

    normalized = flight_number.strip().upper()

    for existing in flights:
        if existing.strip().upper() == normalized:
            return existing

    return None


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    if passenger_name is None:
        return False

    target = passenger_name.strip().lower()

    for name in passengers:
        if name.strip().lower() == target:
            return True

    return False


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    if passenger_name is None or passenger_name.strip() == "":
        return "EMPTY_NAME"

    flight = flights[key]
    clean_name = passenger_name.strip().title()

    destination = flight.get("destination", "").strip().lower()
    for restricted in restricted_destinations:
        if restricted.strip().lower() == destination:
            return "RESTRICTED"

    if passenger_exists(flight["passengers"], clean_name):
        return "DUPLICATE"

    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"

    flight["passengers"].append(clean_name)
    return "OK"


## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    if passenger_name is None:
        return "PASSENGER_NOT_FOUND"

    target = passenger_name.strip().lower()
    passengers = flights[key]["passengers"]

    for i, name in enumerate(passengers):
        if name.strip().lower() == target:
            passengers.pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    if new_gate is None:
        return "INVALID_GATE"

    clean_gate = new_gate.strip().upper()

    normalized_allowed = {g.strip().upper() for g in allowed_gates}

    if clean_gate not in normalized_allowed:
        return "INVALID_GATE"

    # Preserve the case from allowed_gates if possible
    for g in allowed_gates:
        if g.strip().upper() == clean_gate:
            flights[key]["gate"] = g
            return "OK"

    flights[key]["gate"] = clean_gate
    return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    capacity = flight["capacity"]
    count = len(flight["passengers"])

    if capacity <= 0:
        return "AVAILABLE"

    percentage = count / capacity * 100

    if percentage >= 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    key = find_flight(flights, flight_number)

    if key is None:
        return None

    return sorted(flights[key]["passengers"])


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    total = 0
    for flight in flights.values():
        total += len(flight["passengers"])
    return total


# Logic to check if any flight is full
def any_full_flight(flights):
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True
    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False
    return True