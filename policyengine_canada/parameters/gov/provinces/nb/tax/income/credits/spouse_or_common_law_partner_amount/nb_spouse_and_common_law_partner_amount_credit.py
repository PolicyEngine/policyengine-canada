from policyengine_canada.model_api import *

class nb_spouse_and_common_law_partner_amount_credit(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick spouse and common-law partner amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NB
    
    p = parameters(period).gov.provinces.nb.tax.income.credits.spouse_or_common_law_partner_amount 
    base_amount = p.base_amount  
    max_credit = p.max_credit  

    def formula(household, period, parameters):
        year = period.start.year
        if year == 2022:
            base_amount = 10_105
            max_credit = 9_186
        elif year == 2023:
            base_amount = 10_741
            max_credit = 9_764
        elif year == 2024:
            base_amount = 11_246
            max_credit = 10_223
        else:
            raise ValueError(f"Year {year} not supported.")

        spouse_income = add(household, period, ["spouse_income"])
        result = base_amount - spouse_income
        return min(max_credit, max(0, result))

