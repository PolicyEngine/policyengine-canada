from policyengine_canada.model_api import *


class spouse_or_common_law_partner_amount(Variable):
    value_type = float
    entity = Person
    label = "Spouse or common-law partner amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s5/5000-s5-22e.pdf - Line 30300"

    def formula(person, period, parameters):
        spouse_income = person("spouse_net_income", period)
        basic_personal_amount = person("basic_personal_amount", period)
        disabled_spouse = person(
            "eligible_spouse_for_canada_caregiver_amount", period
        )
        supplement_amount = (
            disabled_spouse
            * parameters(
                period
            ).gov.cra.tax.income.credits.canada_caregiver_amount.spouse_or_common_law_partner_amount.supplement
        )
        eligible = person(
            "spouse_or_common_law_partner_amount_eligible_spouse", period
        )
        return eligible * max_(
            0, basic_personal_amount + supplement_amount - spouse_income
        )


# TODO: add to net income tree
