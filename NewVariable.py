__author__ = 'angelee'

def newVariable(graph, json_obj, context, film_id):
    context[json_obj["params"]["name"]] = json_obj["params"]["value"]
