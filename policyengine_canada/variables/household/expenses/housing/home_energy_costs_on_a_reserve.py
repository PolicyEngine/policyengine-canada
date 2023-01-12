from policyengine_canada.model_api import *


class home_energy_costs_on_a_reserve(Variable):
    value_type = float
    entity = Household
    label = "Amounts paid for energy on a reserve"
    unit = CAD
    definition_period = YEAR
