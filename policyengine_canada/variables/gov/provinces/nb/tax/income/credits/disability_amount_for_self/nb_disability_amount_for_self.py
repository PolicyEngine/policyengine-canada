from policyengine_canada.model_api import *

class nb_disability_amount_for_self(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick disability amount for self"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        eligible = household("nb_disability_amount_eligible")
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.disability_amount
        expenses = household(""childcare costs", period)
        expense_threshold = max_(expenses - p.younger_amount.expense_threshold, 0)
        total_max_amount = max_(p.younger_amount.max_amount - expense_threshold, 0)
        
        return eligible * min_(p.base + total_max_amount, p.younger_amount.total_max_amount)