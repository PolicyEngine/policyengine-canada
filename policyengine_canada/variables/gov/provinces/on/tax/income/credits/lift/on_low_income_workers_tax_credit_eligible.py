from policyengine_canada.model_api import *


class on_low_income_workers_tax_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible person for the Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.ONT

    def formula(person, period, parameters):
        return person("employment_income", period) > 0
