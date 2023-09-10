from policyengine_canada.model_api import *


class qc_age_and_living_alone_and_retirement_income_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec age amount, amount for a person living alone and amount for retirement income"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.age_and_living_alone_and_retirement_income_amount
        income = household("adjusted_family_net_income", period)

        # income eligibility
        married = household("is_married", period)
        maximum_income = where(
            married, p.maximum_income.married, p.maximum_income.single
        )
        income_eligible = income <= maximum_income

        total_amount = income_eligible * (
            household("qc_age_amount", period)
            + household("qc_person_living_alone_amount", period)
            + household("qc_retirement_income_amount", period)
        )

        return max_(total_amount - p.reduction.calc(income), 0)
