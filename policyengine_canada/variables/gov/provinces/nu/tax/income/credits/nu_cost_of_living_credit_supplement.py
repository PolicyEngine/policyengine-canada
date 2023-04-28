from policyengine_canada.model_api import *


class nu_cost_of_living_credit_supplement(Variable):
    value_type = float
    entity = Person
    label = "Nunavut cost of living credit supplement for single parents"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.cost_of_living.supplement_for_single_parents
        adjusted_income = person(
            "nu_cost_of_living_credit_adjusted_net_income", period
        )
        excess = max_(0, adjusted_income - p.income)
        uncapped = excess * p.rate
        return min_(uncapped, p.max_amount)
