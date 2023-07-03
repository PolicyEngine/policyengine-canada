from policyengine_canada.model_api import *


class sk_disability_amount(Variable):
    value_type = float
    entity = Person
    label = "SK Disability Amount Tax Credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.sk_disability_amount
        eligibility = person("is_disable_certificate", period)
        return where(eligibility == 1, p.amount, 0)
