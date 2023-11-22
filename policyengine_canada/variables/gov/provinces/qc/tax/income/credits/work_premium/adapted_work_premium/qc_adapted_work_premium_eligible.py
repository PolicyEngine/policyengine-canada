from policyengine_canada.model_api import *


class qc_adapted_work_premium_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Quebec adapted work premium tax credit eligibility"
    definition_period = YEAR
    defined_for = "qc_work_premium_eligible"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.adapted_work_premium

        person = household.members
        is_head_or_spouse = person("is_head_or_spouse", period)

        # You or your spouse is disabled
        disabled = person("is_disabled", period)

        # Your or your spouse's annual work income is over $1,200.
        work_income_eligible = (
            person("working_income", period) > p.work_income_requirement
        )

        return household.any(
            is_head_or_spouse & disabled & work_income_eligible
        )
