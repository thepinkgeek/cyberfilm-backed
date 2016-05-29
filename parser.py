__author__ = 'angelee'
from Acquire import acquire
from GetNearest import getNearest
from NewVariable import newVariable
from os import listdir
import json

mypath = "C:\\Users\\angelee\\Documents\\cyberfilm_data\\sample"
graph = "graph.json"


def main():
    with open(graph) as graph_file:
        graph_object = json.load(graph_file)

    context = {}
    files = listdir(mypath)
    films = []
    for file in files:
        with open("\\".join([mypath, file]), 'r') as json_file:
            films.append({"name" : file, "film" : json.load(json_file)})
            json_file.close()

    current_scene = 0
    while current_scene < len(films):
            film = films[current_scene]["film"]
            name = films[current_scene]["name"]
            get_handler(film)(graph_object,
                              film,
                              context,
                              name[0: name.index(".json")])
            current_scene += 1
            print(context)


def get_handler(obj):
    name = obj["name"]

    if name == "AcquireNode":
        return acquire
    elif name == "GetNearest":
        return getNearest
    else:
        return None

if __name__ == "__main__":
    main()
