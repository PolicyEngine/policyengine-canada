from policyengine_canada.model_api import *


class nu_cost_of_living_basic_credit(Variable):
    value_type = float
    entity = Person
    label = "Nunavut cost of living basic credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.cost_of_living
        adjusted_income = person(
            "nu_cost_of_living_credit_adjusted_net_income", period
        )
        return min_(p.max_amount, adjusted_income * p.rate)
