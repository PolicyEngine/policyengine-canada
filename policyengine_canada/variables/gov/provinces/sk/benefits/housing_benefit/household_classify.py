from policyengine_canada.model_api import *


class household_classify(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan Household classification"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p1 = parameters(period).gov.provinces.sk.benefits.housing_benefit
        where(count_dependants=0, annual_income_threshold = p1.income_limit.no_dependants, 
        where(count_dependants=1, annual_income_threshold = p1.income_limit.one_dependants,annual_income_threshold = p1.income_limit.two_or_more_dependants))
        return annual_income_threshold