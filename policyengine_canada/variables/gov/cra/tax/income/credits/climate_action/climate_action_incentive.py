from policyengine_canada.model_api import *


class climate_action_incentive(Variable):
    value_type = float
    entity = Person
    label = "Canada Climate Action Incentive"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        gov = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action.amount


# TODO: state codes for Canada + select statements based on the states

# TODO: 10% supplement of the base amount for residents in rural communities
# TODO: select if single parent
