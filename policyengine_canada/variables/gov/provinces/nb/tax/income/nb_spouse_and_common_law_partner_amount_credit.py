from policyengine_canada.model_api import *

class nb_spouse_and_common_law_partner_amount_credit(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick spouse and common-law partner amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NB
     

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.nb.tax.income.credits.spouse_or_common_law_partner_amount 

        spouse_income = add(household, period, ["spouse_income"])
        reduced_amount = max_(p.base_amount - spouse_income, 0)  
        return min(p.max_credit, reduced_amount)

