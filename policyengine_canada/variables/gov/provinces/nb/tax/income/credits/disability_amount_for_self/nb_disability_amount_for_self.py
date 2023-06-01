from policyengine_canada.model_api import *

class nb_disability_amount_for_self(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick disability amount for self"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.low_income_tax_reduction
        age = household("under_18", period)
        
        return min_(
            p.base.total_max_amount,
            p.base.base
            + max_amount 
            - total_expense + expense_threshold,
        )