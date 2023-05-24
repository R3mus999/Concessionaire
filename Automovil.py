import json


class Automovil:

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price


class CodificadorAutomovil(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Automovil):
            return o.__dict__
        return super().default(o)