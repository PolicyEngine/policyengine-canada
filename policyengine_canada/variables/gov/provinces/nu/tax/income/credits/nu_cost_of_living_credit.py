from policyengine_canada.model_api import *


class nu_cost_of_living_credit(Variable):
    value_type = float
    entity = Person
    label = "Nunavut cost of living credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.cost_of_living
        income = person("individual_net_income", period)
        armed_deduction = person(
            "canadian_armed_forces_and_personnel_deduction", period
        )
        adjusted_income = max_(0, income - armed_deduction)
        return min_(p.max_amount, adjusted_income * p.rate)


#TODO: include in net income tree