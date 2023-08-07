from policyengine_canada.model_api import *


class months_living_in_rentals(Variable):
    value_type = int
    entity = Person
    label = "Time Livining in Rentals"
    documentation = "Total number of months living in rental places"
    definition_period = YEAR
