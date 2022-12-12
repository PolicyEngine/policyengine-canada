from policyengine_canada.model_api import *


class dental_benefit(Variable):
    value_type = float
    entity = Person
    label = "Canada dental benefit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        income = person.household("adjusted_family_net_income", period)
        p = parameters(period).gov.cra.benefits.dental_benefit
        eligible = person("dental_benefit_eligible", period)
        full_custody_amount = p.amount.calc(income)
        # Multiply by a factor for shared custody.
        amount = full_custody_amount * where(
            person("full_custody", period), 1, p.shared_custody_share
        )
        return eligible * amount
