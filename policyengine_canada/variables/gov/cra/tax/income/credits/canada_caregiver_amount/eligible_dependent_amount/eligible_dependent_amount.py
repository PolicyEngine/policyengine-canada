from policyengine_canada.model_api import *


class eligible_dependent_amount(Variable):
    value_type = float
    entity = Person
    label = "Eligible dependent amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s5/5000-s5-22e.pdf - Line 30400"

    def formula(person, period, parameters):
        spouse_amount = person("spouse_or_common_law_partner_amount", period)
        dependent_income = person("dependent_net_income", period)
        basic_personal_amount = person("basic_personal_amount", period)
        disabled_dependent = person("is_disabled", period)
        supplement_amount = (
            disabled_dependent
            * parameters(
                period
            ).gov.cra.tax.income.credits.canada_caregiver_amount.eligible_dependent_amount.supplement
        )
        eligible = person(
            "eligible_dependent_for_eligible_dependent_amount", period
        )
        return where(
            spouse_amount == 0,
            eligible
            * max_(
                0, basic_personal_amount + supplement_amount - dependent_income
            ),
            0,
        )


# TODO: add to net income tree
