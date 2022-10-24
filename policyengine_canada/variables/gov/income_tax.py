from policyengine_canada.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Person
    label = "Income tax"
    unit = CAD
    documentation = "Example income tax regime"
    definition_period = YEAR

    def formula(person, period, parameters):
        income = person("total_individual_pre_tax", period)
        age = person("age", period)
        gov = parameters(period).gov
        tax = gov.income_tax_schedule.calc(income)
        is_exempt = age >= gov.age_exemption
        return where(is_exempt, 0, tax)
