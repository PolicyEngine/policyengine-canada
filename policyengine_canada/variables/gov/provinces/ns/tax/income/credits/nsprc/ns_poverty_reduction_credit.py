from policyengine_canada.model_api import *


class ns_poverty_reduction_credit(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia Poverty Reduction Credit"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://novascotia.ca/coms/noteworthy/PovertyReductionCredit.html"
    )
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("count_children", period)
        p = parameters(period).gov.provinces.ns.tax.credits.nsprc
        eligible = (children == 0) & (income < p.income_threshold)
        return where(eligible, p.amount, 0)
