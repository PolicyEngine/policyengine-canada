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
        # Determine eligibility.
        dental_expenses = person("dental_expenses", period)
        has_private_insurance = person("has_private_dental_insurance", period)
        age_eligible = person("age", period) < p.ineligible_age
        # The amount does not vary with the dental costs.
        # Child only needs to have received some dental care.
        eligible = ~insurance_plan & (dental_expenses > 0)
        full_custody_amount = p.amount.calc(income)
        # Divide by two if shared custody.
        full_custody = person("full_custody", period)
        amount = full_custody_amount / where(full_custody, 1, 2)
        return eligibile_child * dental_benefit_children * full_custody_benefit
