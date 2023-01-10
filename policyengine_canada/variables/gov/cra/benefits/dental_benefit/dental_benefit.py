from policyengine_canada.model_api import *


class dental_benefit(Variable):
    value_type = float
    entity = Person
    label = "Canada dental benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = "dental_benefit_eligible"

    def formula(person, period, parameters):
        income = person.household("adjusted_family_net_income", period)
        p = parameters(period).gov.cra.benefits.dental_benefit
        full_custody_amount = p.amount.calc(income)
        # Multiply by a factor for shared custody.
        return full_custody_amount * where(
            person("full_custody", period), 1, p.shared_custody_share
        )
