from policyengine_canada.model_api import *


class climate_action_single_parent(Variable):
    value_type = float
    entity = Household
    label = "Canada Climate Action single parent amount"
    unit = CAD
    documentation = "Determination wether the filer is a single parent eligible for the climate action incentive"
    definition_period = YEAR

    def formula(household, period, parameters):
        single_parent = household("is_single_parent", period)
        province = household("province_str", period)
        children_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action.amount.first_child_in_single_parent_family[
            province
        ]
        children = household("climate_action_children", period)
        return where(
            single_parent,
            children + (single_parent * children_amount),
            children,
        )
