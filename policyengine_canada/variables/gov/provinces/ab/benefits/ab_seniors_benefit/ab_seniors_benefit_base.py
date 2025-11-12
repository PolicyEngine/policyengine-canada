from policyengine_canada.model_api import *


class ab_seniors_benefit_base(Variable):
    value_type = float
    entity = Person
    label = "Alberta Seniors Benefit base amount"
    unit = CAD
    documentation = "Maximum Alberta Seniors Benefit amount before income reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        household = person.household
        is_married = household("is_married", period)

        p = parameters(period).gov.provinces.ab.benefits.seniors_benefit

        # Different maximum amounts for single vs couple
        return where(is_married, p.max_amount.couple, p.max_amount.single)
