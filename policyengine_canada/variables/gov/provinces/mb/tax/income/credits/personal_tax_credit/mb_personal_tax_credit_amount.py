from policyengine_canada.model_api import *


class mb_personal_tax_credit_amount(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba personal tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.personal_tax_credit

        spouse = person("is_spouse", period)
        head = person("is_head", period)

        has_spouse = person("is_married", period)

        age_eligibility = person("age", period) >= 65

        age_eligible_head = head & age_eligibility
        age_eligible_head_amount = age_eligible_head * p.age_credit

# calculation of head and spouse credit amount 
        head_spouse_amount = (head + has_spouse) * p.basic_credit + age_eligible_head_amount + person("mb_spouse_credit_amount", period) 

# calculation of other credit amount 

        #eligible dependant credit amount
        eligible_dependant = person("count_dependants", period) > 0
        eligible_dependant_amount = eligible_dependant * p.eligible_dependant_credit
        
        #disability claims credit amount
        disability_claims = person("count_disability_claims", period)
        disability_claims_amount = disability_claims * p.self_and_dependant_disability_claim_credit

        #disabled dependants credit amount
        disabled_dependants = person("count_adult_disability_dependants", period)
        disabled_dependants_amount = disabled_dependants * p.disabled_dependant_amount

        #eligible dependant children credit amount
        eligible_children = person("count_children", period)
        eligible_children_amount = eligible_children * p.dependant_children_amount

# calculation of total credit amount 
        total_credits = head_spouse_amount + eligible_dependant_amount + disability_claims_amount + disabled_dependants_amount + eligible_children_amount

        #household net income
        net_income = household("household_net_income", period)

        total_personal_tax_credit = total_credits - (0.01 * net_income)


        return total_personal_tax_credit