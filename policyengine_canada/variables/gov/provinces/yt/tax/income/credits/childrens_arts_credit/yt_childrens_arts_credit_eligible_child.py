from policyengine_canada.model_api import *


class yt_childrens_arts_credit_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Yukon childrens arts credit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(
                period
            ).gov.provinces.yt.tax.income.credits.childrens_arts_credit.child_age_eligibility
        )
