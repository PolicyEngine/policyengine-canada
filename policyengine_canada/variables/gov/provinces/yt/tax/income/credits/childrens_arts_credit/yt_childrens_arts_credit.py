from policyengine_canada.model_api import *


class yt_childrens_arts_credit(Variable):
    value_type = float
    entity = Household
    label = "Yukon childrens arts credit"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        children = household(
            "yt_childrens_arts_credit_eligible_children", period
        )
        expenses = household("yt_childrens_arts_credit_expenses", period)
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.childrens_arts_credit
        return min_(expenses, children * p.amount)
