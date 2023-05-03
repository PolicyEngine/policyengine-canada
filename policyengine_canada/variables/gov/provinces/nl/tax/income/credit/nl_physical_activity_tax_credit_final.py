from policyengine_canada.model_api import *


class nl_physical_activity_tax_credit_final(Variable):
    value_type = float
    entity = Person
    label = "Newfoundland Physical activity tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.nl.tax.income.credits
        calcualted_credit = person("nl_physical_activity_tax_credit", period)

        return min_(calcualted_credit, p.max_credit)
