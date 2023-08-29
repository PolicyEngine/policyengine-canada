from policyengine_canada.model_api import *


class bc_climate_action_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "British Columbia climate action tax credit"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR
    defined_for = ProvinceCode.BC

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        married = household("is_married", period)
        single_parent = household(
            "bc_climate_action_tax_credit_single_parent_household", period
        )
        family = married | single_parent
        base = household("bc_climate_action_tax_credit_base", period)
        p = parameters(period).gov.provinces.bc.tax.income.credits.bccatc
        reduction = where(
            family,
            p.reduction_rate.family.calc(income),
            p.reduction_rate.single.calc(income),
        )
        return max_(base - reduction, 0)
