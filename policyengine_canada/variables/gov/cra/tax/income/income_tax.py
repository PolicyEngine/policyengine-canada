from policyengine_canada.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Person
    label = "Income tax"
    unit = CAD
    documentation = "Example income tax regime"
    definition_period = YEAR

    def formula(person, period, parameters):
        income = person("total_individual_pre_tax_income", period)
        gov = parameters(period).gov.cra.tax.income
        return gov.income_tax_schedule.calc(income)
