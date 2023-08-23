from policyengine_canada.model_api import *


class qc_caregiver_not_living_with_disabled_carereceiver(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregiver tax cresit for caregivers not living with disabled care receivers"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers
        # with an impairment
        disabled = person("is_disabled", period)
        # is care receiver
        carereceiver = person("is_carereceiver", period)
        # age eligibility
        age_eligible = person("age", period) >= p.eligibility.carereceiver_age
        # lived together
        not_cohabiting = ~person("lived_together", period)

        eligible = disabled & carereceiver & age_eligible & not_cohabiting

        # care giver's income eligibility (line 354)
        income_eligible = max_(
            person("individual_net_income", period)
            - p.eligibility.income_limit,
            0,
        )

        credit = p.base_amount - min_(income_eligible * p.rate, p.base_amount)

        return eligible * credit
