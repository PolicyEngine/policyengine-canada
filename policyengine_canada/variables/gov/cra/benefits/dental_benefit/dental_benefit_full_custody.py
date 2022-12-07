from policyengine_canada.model_api import *


class dental_benefit_full_custody(Variable):
    value_type = float
    entity = Household
    label = "Canada dental benefit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.cra.benefits.dental_benefit
        full_custody_benefit = p.full_custody_amount.calc(income)
        dental_benefit_children = household("dental_benefit_children", period)
        dental_costs = household("child_dental_costs", period)
        insurance_plan = household(
            "child_private_dental_insurance_plan", period
        )
        full_custody = household("full_custody", period)
        eligibile_child = ~insurance_plan & (dental_costs > 0) & full_custody
        return eligibile_child * dental_benefit_children * full_custody_benefit
