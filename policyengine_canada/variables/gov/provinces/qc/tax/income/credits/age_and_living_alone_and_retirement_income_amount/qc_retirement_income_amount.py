from policyengine_canada.model_api import *


class qc_retirement_income_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec amount for retirement income"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.age_and_living_alone_and_retirement_income_amount.retirement_income_amount

        person = household.members
        # if the household has spouse
        spouse = household("is_married", period)

        age_eligible = person("age", period) >= p.age_eligibility
        pension_and_savings_plan_income = age_eligible * person(
            "pension_and_savings_plan_income", period
        )

        return household.sum(pension_and_savings_plan_income)
