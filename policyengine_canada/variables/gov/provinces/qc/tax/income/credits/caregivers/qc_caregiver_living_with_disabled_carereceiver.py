from policyengine_canada.model_api import *


class qc_caregiver_living_with_disabled_carereceiver(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregiver tax credit for caregivers living with disabled care receivers"
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
        cohabiting = person("lived_together", period)

        eligible = disabled & carereceiver & age_eligible & cohabiting

        # care giver's income eligibility (line 254)
        income_eligible = max_(
            person("individual_net_income", period)
            - p.eligibility.income_limit,
            0,
        )

        base_credit = p.disabled_cohabiting_carereceiver_credit_limit - min_(
            income_eligible * p.rate, p.base_amount
        )

        #  an additional amount for expenses you incurred for specialized respite services for an eligible care receiver you lived with who is disabled
        specialized_respite_services_expenses = min_(
            person("specialized_respite_services_expenses", period),
            p.specialized_respite_services.expenses_limit,
        )
        specialized_respite_services_credit = (
            p.specialized_respite_services.rate
            * specialized_respite_services_expenses
        )

        return eligible * (base_credit + specialized_respite_services_credit)
