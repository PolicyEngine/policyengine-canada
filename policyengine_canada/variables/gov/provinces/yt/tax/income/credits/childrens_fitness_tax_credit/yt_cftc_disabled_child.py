from policyengine_canada.model_api import *


class yt_cftx_disabled_child(Variable):
    value_type = bool
    entity = Person
    label = "Yukon Child Fitness Tax Credit disabled child"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        disabled = person("is_disabled", period)
        age = person("age", period)
        return (
            disabled & age
            < parameters(
                period
            ).gov.provinces.yt.tax.income.credits.childrens_fitness_tax_credit.disability_supplement.age_eligibility
        )
