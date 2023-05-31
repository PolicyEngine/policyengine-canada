from policyengine_canada.model_api import *


class qc_sa_single(Variable):
    value_type = bool
    entity = Household
    label = "Quebec senior assistance tax credits eligible senior did not have a spouse"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        person = household.members

        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        age_eligible = person("age", period) >= p.age_eligibility

        return age_eligible & ~person("is_spouse", period)
