from policyengine_canada.model_api import *


class mb_caregiver_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba caregiver amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.caregiver_amount

        dependent_income = individual("individual_net_income", period)

        caregiver = person("is_caregiver", period)

        dependent_parent_eligible = person("mb_dependent_parents_eligible", period)
        dependent_grandparent_eligible = person("mb_dependent_grandparents_eligible", period)
        dependent_infirm_relative = person("is_infirm_relative", period)

        eligible_dependent_income_max = dependent_income <= 12_312
        eligible_dependent_income = dependent_income <= 15_917 & dependent_income >= 12_312
        ineligible_dependent_income = dependent_income > 12_312

        return 
###


A = min_(p.max_amount,p.max_amount * (dependent_parent_eligible + dependent_grandparent_eligible + dependent_infirm_relative))

caregiver * A #3605 or 0

(caregiver * A) | eligible_dependent_income_max #3605 or 0
min_((dependent_income - line7 age amount), (caregiver * A) | eligible_dependent_income) #somewhere between 0-3605
min_(0,(caregiver * A)| ineligible_dependent_income_max) # 0