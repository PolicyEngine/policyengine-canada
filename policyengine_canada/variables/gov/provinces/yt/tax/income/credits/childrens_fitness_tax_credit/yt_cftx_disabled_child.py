from policyengine_canada.model_api import *


class yt_cftx_disabled_child(Variable):
    value_type = bool
    entity = Person
    label = "Yukon Disabled Child"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("is_disabled", period)
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.childrens_fitness_tax_credit.disability_supplement
        return age < p.age_eligibility