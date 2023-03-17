"""
The task 2 goes like following:
Pull data for the first movie in star wars
Write the json data into a file named output.txt


SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

from flask import Flask,jsonify
from flask import Blueprint
import json
import requests
FIRST_FILM_URL = "https://swapi.dev/api/films/{}/"

blueprints_object = Blueprint("task_two_app",__name__,url_prefix="/task_two")


def hit_url(url):
    response = requests.get(url)
    response = response.json()

    return response


def write_data_into_file(data:dict)-> None:
    with open("film_data.txt",'w') as file_obj:
        data = json.dumps(data)
        file_obj.write(data)


@blueprints_object.route("/film/<int:number>")
def get_and_write_data_into_file(number):
    url = FIRST_FILM_URL.format(number)
    get_data = hit_url(url)
    write_data_into_file(get_data)
    return jsonify(get_data)


@blueprints_object.route("/film/<int:number>/characters")
def characters_name(number):
    char_names = []
    char_data = hit_url(FIRST_FILM_URL.format(number))
    char_data = char_data.get("characters")
    for char in char_data:
        result = hit_url(char)
        char_names.append(result.get("name"))
    return "{}".format(char_names)


@blueprints_object.route("/film/<int:number>/vehicles")
def vehicles_names(number):
    vehicle_data = []
    get_vehicle = hit_url(FIRST_FILM_URL.format(number))
    get_vehicle = get_vehicle.get("vehicles")
    for vehicle in get_vehicle:
        result = hit_url(vehicle)
        vehicle_data.append(result.get("name"))
    return "{}".format(vehicle_data)


@blueprints_object.route("/film/<int:number>/planets")
def planet_names(number):
    planet_data = []
    get_planet = hit_url(FIRST_FILM_URL.format(number))
    get_planet = get_planet.get("planets")
    for planet in get_planet:
        result = hit_url(planet)
        planet_data.append(result.get("name"))
    return "{}".format(planet_data)


if __name__ == "__main__":
    blueprints_object.run()
