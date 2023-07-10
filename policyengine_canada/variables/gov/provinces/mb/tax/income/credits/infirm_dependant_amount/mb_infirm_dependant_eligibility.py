from policyengine_canada.model_api import *


class mb_infirm_dependant_eligibility(Variable):
    value_type = float
    entity = Person
    label = "Manitoba infirm dependant supporter eligibility"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.infirm_dependant_amount

        # dependent relative condition
        relative_eligible = person("is_relative", period) 

        # dependant adult condition

        relative_eligible = person("is_adult", period) 

        # dependant infirm condition

        infirm_eligible = person("is_disabled", period)

        # overall dependant eligibility 

        eligibility = relative_eligible & relative_eligible & infirm_eligible

        income = person("individual_net_income", period)

        credit = eligibility * min_(p.income_max_amount - income, p.max_amount)

        return credit 

        # ToDo： age amount reduction & caregiver amount eligibility tests 