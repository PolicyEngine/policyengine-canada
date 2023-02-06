from policyengine_canada.model_api import *


class bc_climate_action_tax_credit_person(Variable):
    value_type = float
    entity = Person
    label = "British Columbia Climate Action amount per individual"
    unit = CAD
    documentation = "Determination of the amount per individual"
    definition_period = YEAR

    def formula(person, period, parameters):
        category = person("bc_climate_action_incentive_category", period)
        amounts = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.bccatc.amount
        return amounts[category]
