from policyengine_canada.model_api import *


class sk_senior_supplementary_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Sasktachewan senior supplementary tax credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.sk_senior_supplementary
        age = person("age", period)
        return age >= p.age_threshold
