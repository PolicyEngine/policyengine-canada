from policyengine_canada.model_api import *


class yt_childrens_fitness_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Yukon children fitness tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        total_children = household("yt_cftc_eligible_children", period)
        person = household.members
        fees = person("child_physical_activities_fees", period)
        disability_fees = household(
            "yt_childrens_fitness_tax_credit_disability_supplement", period
        )
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.childrens_fitness_tax_credit
        return min_(fees * p.rate, total_children * p.base) + disability_fees
