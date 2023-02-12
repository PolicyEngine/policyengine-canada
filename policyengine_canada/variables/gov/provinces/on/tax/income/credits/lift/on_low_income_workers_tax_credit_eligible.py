from policyengine_canada.model_api import *


class on_low_income_workers_tax_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible person for the Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        has_employment_income = person("employment_income", period) > 0
        return in_ontario & has_employment_income
