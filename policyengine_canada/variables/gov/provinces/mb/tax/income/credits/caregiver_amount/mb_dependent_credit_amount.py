from policyengine_canada.model_api import *


class mb_dependent_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba caregiver amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.caregiver_amount

        # dependent relative condition
        parent_eligible = person('is_parent', period)

        grandparent = person("is_grandparent", period)
        grandparent_age = person("age", period) >= p.grandparents_age_eligibility
        grandparent_eligible = grandparent & grandparent_age

        infirm_relative_eligible = person("is_relative", period) & person("is_adult", period) & person("is_disabled", period)

        dependent_eligible = parent_eligible | grandparent_eligible | infirm_relative_eligible

        # if lived together
        live_together = person("lived_together", period)

        eligibility = dependent_eligible & live_together 

        income = person("individual_net_income", period)

        credit = eligibility * min_(p.dependent_max_net_income_eligibility - income, p.max_amount)

        return credit 

        # ToDo： age amount reduction 