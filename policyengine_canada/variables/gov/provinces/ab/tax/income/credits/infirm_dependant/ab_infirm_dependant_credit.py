from policyengine_canada.model_api import *


class ab_infirm_dependant_credit(Variable):
    value_type = float
    entity = Household
    label = "Alberta infirm dependant credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        person = household.members
        p = parameters(period).gov.provinces.ab.tax.income.credits.infirm_dependant
        eligible = person("is_infirm_dependant", period)
        infirm_dependant_income = person("infirm_dependant_income",period)
        income_level = infirm_dependant_income > p.low_income
        per_credit = where(income_level, max_(0, eligible * (20_190 - infirm_dependant_income)), eligible * p.base)
        total = household.sum(per_credit)
        return total