import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/vehicles"                  #updated


def update_vehicle(vehicle_data, vehicle_id):                #updated
    url = "%s/%s/" % (URL, vehicle_id)                 #updated
    response = requests.put(url, json=vehicle_data)    #updated
    if response.status_code == 204:
        print("Successfully updated vehicle.")
    else:
        print("Something went wrong while trying to update vehicle")


def get_vehicle(vehicle_id):
    url = "%s/%s/" % (URL, vehicle_id)                 #updated
    response = requests.get(url)                    #updated
    if response.status_code == 200:
        print("Vehicle: ")
        pprint(response.json())
        return response.json().get("vehicle")       #updated
    else:
        print("Something went wrong while trying to retrieve the vehicle.")
        return ""

if __name__ == "__main__":
    vehicle_id = input("Type in the vehicle id: ")
    target_vehicle = get_vehicle(int(vehicle_id))
    color = input("Type in the new color (or leave blank): ")
    license_plate = input("Type in the new license plate (or leave blank): ")
    v_type = input ("Type in the new vehicle type (or leave blank): ")
    if color:
        target_vehicle["color"] = color
    if license_plate:
        target_vehicle["license_plate"] = license_plate
    if v_type:
        target_vehicle["v_type"] = v_type
    update_vehicle(target_vehicle, vehicle_id)                           #updated
    option = input("Would you like to see the updated vehicle? [y/N]: ")
    if option == "y" or option == "Y":
        get_vehicle(vehicle_id)