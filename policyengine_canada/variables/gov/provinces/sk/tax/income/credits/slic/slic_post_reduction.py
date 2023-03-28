from policyengine_canada.model_api import *


class slic_post_reduction(Variable):
    value_type = float
    entity = Household
    label = "Sasktachewan low income tax credit post reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.slic
        base = household("slic_base", period)
        income = household("adjusted_family_net_income", period)
        return max_(0, base - p.phase_out.calc(income))


# 40_000 : BASE - (  (40_000 - 35_902) * 0.0275 + (35_902 - 0) * 0  )
