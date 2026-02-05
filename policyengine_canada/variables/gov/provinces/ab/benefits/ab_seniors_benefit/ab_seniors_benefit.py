from policyengine_canada.model_api import *


class ab_seniors_benefit(Variable):
    value_type = float
    entity = Person
    label = "Alberta Seniors Benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB
    reference = "https://www.alberta.ca/alberta-seniors-benefit"

    def formula(person, period, parameters):
        base = person("ab_seniors_benefit_base", period)
        reduction = person("ab_seniors_benefit_reduction", period)
        eligible = person("ab_seniors_benefit_eligible", period)
        return where(eligible, max_(0, base - reduction), 0)
