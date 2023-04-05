from policyengine_canada.model_api import *


class yt_cftc_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Yukon Normal Fitness Fee eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(
                period
            ).gov.provinces.yt.credits.childrens_fitness_tax_credit.child_age_eligibility
        )
