from policyengine_canada.model_api import *


class qc_adapted_work_premium_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Quebec adapted work premium tax credit eligibility"
    definition_period = YEAR
    defined_for = "qc_work_premium_eligibility"

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.work_premium

        person = household.members

        # You or your spouse is disabled
        disabled = person("is_disabled", period)

        return household.any(disabled)
