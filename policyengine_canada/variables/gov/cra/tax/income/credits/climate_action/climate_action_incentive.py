from policyengine_canada.model_api import *


class climate_action_incentive(Variable):
    value_type = float
    entity = Person
    label = "Canada Climate Action Incentive"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        return sum_of_variables(
            [
                "climate_action_children",
                "climate_action_single_parent",
                "climate_action_married",
                "climate_action_individual",
            ]
        )


# TODO: 10% supplement of the base amount for residents in rural communities
