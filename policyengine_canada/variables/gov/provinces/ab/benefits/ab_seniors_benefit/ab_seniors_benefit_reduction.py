from policyengine_canada.model_api import *


class ab_seniors_benefit_reduction(Variable):
    value_type = float
    entity = Person
    label = "Alberta Seniors Benefit reduction"
    unit = CAD
    documentation = "Reduction to Alberta Seniors Benefit based on income"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        household = person.household
        is_married = household("is_married", period)

        p = parameters(period).gov.provinces.ab.benefits.seniors_benefit

        # Income threshold differs for single vs couple
        threshold = where(is_married, p.threshold.couple, p.threshold.single)

        # Reduction is $0.1561 for every $1 of income
        excess_income = max_(0, income - threshold)
        return excess_income * p.reduction_rate
