from policyengine_canada.model_api import *


class qc_solidarity_housing_component(Variable):
    value_type = float
    entity = Household
    label = "Quebec Solidarity Tax Credit - Housing Component"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.solidarity.housing

        # Base amounts differ by family composition
        household_size = household("household_size", period)
        is_married = household("is_married", period)

        # Simplified formula - actual formula is more complex
        base_amount = where(
            is_married,
            p.couple_base,
            where(household_size > 1, p.single_parent_base, p.single_base),
        )

        # Income-tested reduction
        income = household("adjusted_family_net_income", period)
        reduction = p.reduction_rate * max_(0, income - p.threshold)

        return max_(0, base_amount - reduction)
