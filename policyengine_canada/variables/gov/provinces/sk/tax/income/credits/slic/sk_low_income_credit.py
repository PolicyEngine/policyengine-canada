from policyengine_canada.model_api import *


class sk_low_income_credit(Variable):
    value_type = float
    entity = Household
    label = "Sasktachewan low income tax credit post reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.slic
        base = household("sk_low_income_credit_base", period)
        income = household("adjusted_family_net_income", period)
        return max_(0, base - p.phase_out.calc(income))
