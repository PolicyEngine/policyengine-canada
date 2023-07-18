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
        age = person("age", period)

        age_eligible_dependant = age >= p.teen_age_amount
        age_eligible_children = age <= p.teen_age_amount

        # disability claims credit amount
        disability_claims = household.sum(dependant * disabled)
        disability_claims_amount = (
            disability_claims * p.self_and_dependant_disability_claim_credit
        )

        # disabled dependants credit amount
        disabled_dependants = household.sum(
            dependant * age_eligible_dependant * disabled
        )
        disabled_dependants_amount = (
            disabled_dependants * p.disabled_dependant_amount
        )

        # eligible dependant children credit amount
        eligible_children = household.sum(dependant * age_eligible_children)
        eligible_children_amount = (
            eligible_children * p.dependant_children_amount
        )

        # eligible dependant credit amount
        eligible_dependant = household.sum(dependant) > 0
        eligible_dependant_amount = (
            eligible_dependant * p.eligible_dependant_credit
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

        total_personal_tax_credit = total_credits - (
            p.family_income_rate_amount * net_income
        )

        return total_personal_tax_credit
