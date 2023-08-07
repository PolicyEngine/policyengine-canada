from policyengine_canada.model_api import *


class days_owning_education_property(Variable):
    value_type = float
    entity = Person
    label = "Number of days at addresses of education property owned"
    unit = CAD
    definition_period = YEAR
