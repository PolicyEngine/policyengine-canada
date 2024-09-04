from policyengine_canada.model_api import *


class qc_caregiver_not_living_with_disabled_carereceiver(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregiver tax cresit for caregivers not living with disabled care receivers"
    definition_period = YEAR
    defined_for = "qc_caregiver_not_living_with_disabled_carereceiver_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers

        # care giver's income eligibility (line 354)
        income_eligible = max_(
            person("individual_net_income", period)
            - p.eligibility.income_limit,
            0,
        )

        return p.base_amount - min_(income_eligible * p.rate, p.base_amount)
