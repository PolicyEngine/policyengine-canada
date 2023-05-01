from policyengine_canada.model_api import *


class ns_poverty_reduction_credit(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia Poverty Reduction Credit"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/coms/noteworthy/PovertyReductionCredit.html",
        "https://nslegislature.ca/sites/default/files/legc/statutes/income%20tax.pdf#page=121",
    )
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("count_children", period)
        income_assistance = household("ns_income_assistance", period)
        p = parameters(period).gov.provinces.ns.tax.income.credits.prc
        eligible = (
            (children == 0)
            & (income < p.income_threshold)
            & (income_assistance > 0)
        )
        return where(eligible, p.amount, 0)
