from policyengine_canada.model_api import *


class sk_low_income_credit_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Sasktachewan low income tax credit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(
                period
            ).gov.provinces.sk.tax.income.credits.slic.child.ineligible_age
        )
