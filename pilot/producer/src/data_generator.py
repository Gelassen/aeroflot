import random
import string

flights = [
    "(U6) URAL AIRLINES 2411", 
    "(S7) S7 AIRLINES 1055", 
    "(S7) S7 AIRLINES 3045",
    "(S7) S7 AIRLINES 3031",
    "(Z7) AVIA TRAFFIC COMPANY 959", 
    "(TYA) NORDSTAR 403", 
    "(LY) EL AL 611", 
    "(SU) AEROFLOT 6159"
] 

# keep time in seconds instead of ms in range, otherwise app crashes with OOM
time = list(range(1715272583, 1715572583)) 

departures = list(range(1715572583, 1715877462))

flight_booking_class = [
    "F", "A", "P", "R", "I", "D", "Z", "C", "J", "W", 
    "S", "Y", "B", "H", "K", "L", "M", "N", "Q", "T", "V", "G", "X", "E", "U" 
    ]

idle_seats = list(range(0, 42))

def wrap_data_in_kafka_connect_format(data) -> dict:
    return {
        "schema": {
            "type": "struct",
            "fields": [
            {"type": "int64", "optional": False, "field": "time"},
            {"type": "string", "optional": False, "field": "flight"},
            {"type": "int64", "optional": False, "field": "departure"},
            {"type": "string", "optional": False, "field": "flight_booking_class"},
            {"type": "int32", "optional": False, "field": "idle_seats_count"}
            ],
            "optional": False,
            "name": "InventorySchema"
        },
        "payload": data
    }


def generate_inventory() -> dict:
    idle_seats_count = random.choice(idle_seats)
    data = {
        "time" : random.choice(time) * 1000, # return back to ms
        "flight" : random.choice(flights),
        "departure" : random.choice(departures) * 1000, # return back to ms
        "flight_booking_class" : random.choice(flight_booking_class),
        "idle_seats_count" : idle_seats_count 
    }
    return wrap_data_in_kafka_connect_format(data)