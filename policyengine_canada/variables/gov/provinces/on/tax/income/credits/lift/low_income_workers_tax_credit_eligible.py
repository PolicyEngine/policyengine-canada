from policyengine_canada.model_api import *


class low_income_workers_tax_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible person for the Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        return employment_income > 0
