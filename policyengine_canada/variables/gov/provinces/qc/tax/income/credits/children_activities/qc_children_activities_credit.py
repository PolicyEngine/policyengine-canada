from policyengine_canada.model_api import *


class qc_children_activities_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec children's activities tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.children_activities

        # income eligibility
        income_eligible = household("adjusted_family_net_income", period) < p.income_limit

        person = household.members
        fee = person("children_activities_fees", period)
        
        # child elibility
        child_eligible = person("is_dependant", period)

        # age elibility
        age = person("age", period)
        disabled = person("is_disabled", period)





