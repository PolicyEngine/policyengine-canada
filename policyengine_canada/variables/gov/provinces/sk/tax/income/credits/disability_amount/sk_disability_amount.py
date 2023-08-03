from policyengine_canada.model_api import *


class sk_disability_amount(Variable):
    value_type = float
    entity = Person
    unit: CAD
    label = "Saskatchewan Disability Amount Tax Credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.disability_amount
        disabled = person("is_disabled", period)
        is_head = person("is_head", period)
        eligbile = is_head & disabled
        return where(eligbile, p.amount, 0)
