from policyengine_canada.model_api import *


class yt_childrens_fitness_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Yukon children fitness tax credit"
    definition_period = YEAR
    unit = CAD
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        total_children = household("yt_cftc_eligible_children", period)
        person = household.members
        fees = person("physical_activities_fees", period)
        disability_supplement = household(
            "yt_childrens_fitness_tax_credit_disability_supplement", period
        )
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.childrens_fitness
        # maximum of $ 1,000 per child tof eligible fees can be multiplied by
        # the refundable rate of % 6.4
        maximum_fees = total_children * p.base
        refundable_portion = fees * p.rate
        per_supplement_amount = min_(refundable_portion, maximum_fees)
        return per_supplement_amount + disability_supplement
