from policyengine_canada.model_api import *


class nl_physical_activity_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Newfoundland Physical activity tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nl.tax.income.credits.physical_activity_tax_credit
        expense = person("individual_net_income", period)

        return expense * p.rate
