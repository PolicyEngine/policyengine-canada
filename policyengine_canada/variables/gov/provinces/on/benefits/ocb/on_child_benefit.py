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
    defined_for = ProvinceCode.ONT

    def formula(household, period, parameters):
        base = household("on_child_benefit_base", period)
        reduction = household("on_child_benefit_reduction", period)
        shared_custody_divisor = parameters(
            period
        ).gov.provinces.on.benefits.ocb.shared_custody_divisor
        has_any_full_custody_children = (
            add(household, period, ["full_custody"]) > 0
        )
        divisor = where(
            has_any_full_custody_children, 1, shared_custody_divisor
        )
        child_benefit_amount = max_(0, base - reduction)
        return child_benefit_amount / divisor
