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
        # Divide by two if shared custody.
        full_custody = person("full_custody", period)
        shared_custody_reduction = p.shared_custody_reduction
        amount = full_custody_amount * where(
            full_custody, 1, shared_custody_reduction
        )
        return eligible * amount
