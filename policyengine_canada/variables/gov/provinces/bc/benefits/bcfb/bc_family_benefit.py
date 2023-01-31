from policyengine_canada.model_api import *


class bc_family_benefit(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit second reduction"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.bc.benefits.bcfb
        reduced_amount = household("bc_family_benefit_first_reduction", period)
        second_reduction = p.second_reduction.rate.calc(income)
        return max_(reduced_amount - second_reduction, 0)
