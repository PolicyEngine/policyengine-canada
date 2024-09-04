from policyengine_canada.model_api import *


class workers_compensation(Variable):
    value_type = float
    entity = Person
    label = "Worker's compensation"
    unit = CAD
    documentation = "Insurance for work-related injuries and illnesses, providing cash benefits and medical care"
    definition_period = YEAR
    reference = "https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=12143"
