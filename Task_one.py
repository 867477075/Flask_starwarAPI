"""
----------------------
PROBLEM STATEMENT
----------------------

The Star Wars API lists 82 main characters in the Star Wars saga.

For the first task, we would like you to use a random number generator
that picks a number between 1-82.

Using these random numbers you will be pulling 15 characters
from the API using Python.

"""
from flask import Flask ,render_template
from Task_two import blueprints_object
import random
import requests

app = Flask(__name__)

app.register_blueprint(blueprints_object)

URL_ = "https://swapi.dev/api/people/{}/"


def random_number_generator(n: int = 15):
    numbers_list = []
    i = 0
    while i < n:
        numbers_list.append(random.randint(1,82))
        i += 1
    return numbers_list


def hit_url(url):
    response = requests.get(url)
    response = response.json()

    return response


@app.route("/task_one")
def pull_character_data():
    random_number = random_number_generator()
    name_of_characters = []
    for number in random_number:
        url = URL_.format(number)
        result = hit_url(url)

        name_of_characters.append(result.get("name"))

    return render_template("task_one.html",characters=name_of_characters)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)


