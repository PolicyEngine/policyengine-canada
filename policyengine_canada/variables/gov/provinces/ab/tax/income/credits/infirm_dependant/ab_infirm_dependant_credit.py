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

        reduced_threshold = max_(
            0, p.income_threshold - infirm_dependant_income
        )

        partial_credit = eligible * reduced_threshold

        capped_credit = where(
            income_level_condition,
            partial_credit,
            max_credit,
        )
        return household.sum(capped_credit)
