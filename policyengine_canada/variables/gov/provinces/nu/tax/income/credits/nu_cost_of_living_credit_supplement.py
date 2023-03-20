from policyengine_canada.model_api import *


class nu_cost_of_living_credit_supplement(Variable):
    value_type = float
    entity = Person
    label = "Nunavut cost of living credit supplement"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.cost_of_living.supplement_for_single_parents
        income = person("individual_net_income", period)
        armed_deduction = person(
            "canadian_armed_forces_and_personnel_deduction", period
        )
        adjusted_income = max_(0, income - armed_deduction)

        return min_(max_(0, adjusted_income - p.income) * p.rate, p.max_amount)
