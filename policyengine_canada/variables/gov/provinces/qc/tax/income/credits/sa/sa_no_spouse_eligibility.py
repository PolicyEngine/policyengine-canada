from policyengine_canada.model_api import *


class sa_no_spouse_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Quebec senior assistance tax credits eligible senior did not have a spouse"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        person = household.members

        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        head = person("sa_age_eligibility", period)

        if_spouse = person("is_spouse", period)

        eligible = head & (~if_spouse)

        return household.any(eligible)


# make it to head instead of no spouse

