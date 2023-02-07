from policyengine_canada.model_api import *


class low_income_workers_tax_credit_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Eligible household for the Ontario Low-Income Workers Tax Credit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        province = household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        family_employment_income = household(
            "family_employment_income", period
        )
        return in_ontario & family_employment_income > 0
