__author__ = 'angelee'

def acquire(graph, json_obj, context, film_id):
    context[film_id] = graph[json_obj["params"]["vertex"]]
