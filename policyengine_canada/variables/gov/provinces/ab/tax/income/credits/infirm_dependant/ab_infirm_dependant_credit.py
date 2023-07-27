from policyengine_canada.model_api import *


class ab_infirm_dependant_credit(Variable):
    value_type = float
    entity = Household
    label = "Alberta infirm dependant credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.credits.infirm_dependant
        eligible = person("is_infirm_dependant", period)
        infirm_dependant_income = person("infirm_dependant_income", period)
        income_level_condition = infirm_dependant_income > p.phase_out_start
        max_credit = eligible * p.base
        partial_credit = eligible * (
            p.max_net_income - infirm_dependant_income
        )
        per_credit = where(
            income_level_condition,
            max_(0, partial_credit),
            max_credit,
        )
        return household.sum(per_credit)