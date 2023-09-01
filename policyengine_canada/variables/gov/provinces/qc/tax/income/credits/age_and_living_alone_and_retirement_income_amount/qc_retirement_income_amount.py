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

        pension_and_savings_plan_income = person(
            "pension_and_savings_plan_income", period
        )

        # todo: retirement_income_amount
        # https://docs.google.com/document/d/1IyQijGMiBVOA9sZGP2orNrezIHonGgwaHccmUHWJlPI/edit

        return min_(p.amount_limit, p.rate * retirement_income_amount)
