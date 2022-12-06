from policyengine_canada.model_api import *


class dental_benefit(Variable):
    value_type = float
    entity = Household
    label = "Canada dental benefit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household.person("total_individual_pre_tax_income", period)
        p = parameters(period).gov.cra.benefits.dental_benefit
        cap = p.income_cap
        shared_custody_benefit = p.shared_custody_amount.calc(income)
        full_custody_benefit = p.full_custody_amount.calc(income)
        dental_benefit_children = household("dental_benefit_children", period)
