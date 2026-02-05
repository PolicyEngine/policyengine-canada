from policyengine_canada.model_api import *


class nt_child_benefit_older_base(Variable):
    value_type = float
    entity = Household
    label = "Base amount for all older children under the Northwest Territories Child Benefit"
    definition_period = YEAR
    unit = CAD
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.benefits.child_benefit.older.base
        children = household(
            "nt_child_benefit_older_eligible_children", period
        )

        return (
            (p.calc(children) * (children > 0))
            + (p.calc(children) * (children > 1))
            + (p.calc(children) * (children > 2))
            + (p.calc(children) * (children > 3))
            # Multiply the 5th plus child amount by the number of children exceeding 4.
            + (p.calc(children) * max_(children - 4, 0))
        )
