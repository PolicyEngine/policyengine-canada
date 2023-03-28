from policyengine_canada.model_api import *


class ntcb_older_base(Variable):
    value_type = float
    entity = Household
    label = "Base amount for all older children under the NTCB"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.benefits.child_benefit.older.base
        children = household("ntcb_older_eligible_children", period)
        return (
            (p.one_child * (children > 0))
            + (p.two_children * (children > 1))
            + (p.three_children * (children > 2))
            + (p.four_children * (children > 3))
            + (p.five_or_more_children * (children > 4))
        )
