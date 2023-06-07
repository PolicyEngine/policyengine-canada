from policyengine_canada.model_api import *


class ns_age_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Age tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        age = person("age", period)
        income = person("ns_taxable_income", period)
        p = parameters(period).gov.provinces.ns.tax.income.credits.age
        eligibility = (age >= p.age_eligibility) & (
            income < p.income_eligibility
        )

        return eligibility * p.amount
