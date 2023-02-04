from policyengine_canada.model_api import *


class on_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Benefit"
    unit = CAD
    documentation = (
        "Non taxable amount paid monthly per children under 18 years of age. "
    )
    definition_period = YEAR

    def formula(household, period, parameters):
        base = household("on_child_benefit_base", period)
        reduction = household("on_child_benefit_reduction", period)
        devsior = parameters(
            period
        ).gov.provinces.on.benefits.ocb.shared_custody_divisor
        has_any_full_custody_children = (
            add(household, period, ["full_custody"]) > 0
        )
        child_benefit_amount = max_(0, base - reduction)
        return where(
            has_any_full_custody_children,
            child_benefit_amount,
            child_benefit_amount / devsior,
        )
