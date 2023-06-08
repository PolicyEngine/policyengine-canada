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
        age = person("age", period)
        # Get the income
        spouse_income = person("spouse_income", period)
        personal_income = person("individual_net_income", period) * person("is_head", period)
        total_family_income = household.sum(spouse_income + personal_income)
        # Get an amount for spouse
        spouse_supplement = person("is_spouse", period) * p.spouse_amount
        # Base amount for self and spouse
        self_and_spouse_credit = p.basic_credit + spouse_supplement
        # Households can get an additional amount per child udner 19
        age_eligible = age < p.child_age_eligibility
        child_amount = household.sum(age_eligible) * p.child_amount
        # Households can receive an additional amount if received the disability tax credit
        disability_credit = person("disability_tax_credit", period)
        disability_amount = household.any(disability_credit) * p.disability_amount
        # Supplement phases in at 5.32% between $15,000 and $20,000 of income maxed at $266
        phased_in_income_supplement = min_(p.phase_in_rate.calc(total_family_income), p.income_supplement_max_amount)
        # Maximum credit
        max_amount = self_and_spouse_credit + phased_in_income_supplement + disability_amount + child_amount
        # Amount phases out at 9% over $40,000
        return max_(max_amount - p.phase_out_rate.calc(total_family_income), 0)
        




        
