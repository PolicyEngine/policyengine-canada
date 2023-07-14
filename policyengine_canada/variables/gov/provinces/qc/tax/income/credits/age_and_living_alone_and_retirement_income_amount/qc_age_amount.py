from policyengine_canada.model_api import *


class qc_age_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec age amount"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.age_and_living_alone_and_retirement_income_amount.age_amount

        person = household.members
        # if the household has spouse
        spouse = household("is_married", period)

        age_eligible = person("age", period) >= p.age_eligibility

        eligible_person = household.sum(age_eligible)

        return eligible_person * p.base
