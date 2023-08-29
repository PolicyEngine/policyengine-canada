from policyengine_canada.model_api import *


class qc_caregiver_living_with_disabled_carereceiver(Variable):
    value_type = float
    entity = Person
    label = "Quebec caregiver tax credit for caregivers living with disabled care receivers"
    definition_period = YEAR
    defined_for = "qc_caregiver_living_with_disabled_carereceiver_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.caregivers

        # care giver's income eligibility
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

        return base_credit + specialized_respite_services_credit
