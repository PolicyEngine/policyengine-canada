from policyengine_canada.model_api import *


class mb_personal_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Manitoba personal tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.personal_tax_credit

        person = household.members

        # check if dependant
        dependant = person("is_dependant", period)
        # disablity
        disabled = person("is_disabled", period)
        # age
        year_of_birth = person("born_year", period)

        age_eligible_dependant = year_of_birth <= p.age.teen_age
        age_eligible_children = year_of_birth >= p.age.teen_age

        # disability claims credit amount
        disability_claims = household.sum(dependant * disabled)
        disability_claims_amount = (
            disability_claims
            * p.amount.self_and_dependant_disability_claim_credit
        )

        # disabled dependants credit amount
        disabled_dependants = household.sum(
            dependant * age_eligible_dependant * disabled
        )
        disabled_dependants_amount = (
            disabled_dependants * p.amount.disabled_dependant_credit
        )

        # eligible dependant children credit amount
        eligible_children = household.sum(dependant * age_eligible_children)
        eligible_children_amount = (
            eligible_children * p.amount.dependant_children_credit
        )

        # eligible dependant credit amount
        eligible_dependant = household.sum(dependant) > 0
        eligible_dependant_amount = (
            eligible_dependant * p.amount.eligible_dependant_credit
        )

        # calculation of total credit amount
        total_credits = (
            person("mb_head_and_spouse_amount", period)
            + eligible_dependant_amount
            + disability_claims_amount
            + disabled_dependants_amount
            + eligible_children_amount
        )

        # household net income
        net_income = household("adjusted_family_net_income", period)

        return total_credits - (p.amount.family_income_rate * net_income)
