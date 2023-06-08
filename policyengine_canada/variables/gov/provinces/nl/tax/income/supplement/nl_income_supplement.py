from policyengine_canada.model_api import *

class nl_income_supplement(Variable):
    value_type = float
    entity = Household
    label = "Newfoundland and Labrador Income Supplement"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.gov.nl.ca/fin/tax-programs-incentives/personal/income-supplement/"
    defined_for = ProvinceCode.NL

    def formula(household, period, parameters):
        person = household.members
        p = parameters(period).gov.provinces.nl.tax.income.supplement.income_supplement

        # Get the income
        spouse_income = person("spouse_income", period) * person("is_spouse", period)
        personal_income = person("individual_net_income", period)
        total_family_income = household.sum(spouse_income + personal_income)

        spouse_supplement = person("is_spouse", period) * p.spouse_amount

        basic_income_supplement = (p.basic_credit + spouse_supplement) * (total_family_income <= p.phase_in_income_threshold)
        
        phase_in_income_supplement = (total_family_income - p.lower_income_threshold) * p.phase_in_rate * ((total_family_income > p.lower_income_threshold) & (total_family_income <= p.phase_in_income_threshold))
        
        max_amount = (p.maximum_credit + spouse_supplement) * (total_family_income > p.phase_in_income_threshold)
        
        phase_out_income_supplement = (total_family_income - p.phase_out_income_threshold) * p.phase_out_rate * (total_family_income > p.phase_out_income_threshold)
        
        total_income_supplement = household.max(basic_income_supplement + phase_in_income_supplement + max_amount - phase_out_income_supplement)

        return max_(total_income_supplement, 0)
        




        
