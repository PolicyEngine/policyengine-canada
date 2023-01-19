from policyengine_canada.model_api import *


class on_grants(Variable):
    value_type = float
    entity = Household
    label = "ON grants"
    documentation = "Ontario grants"
    unit = CAD
    definition_period = YEAR

    adds = "gov.province.on.tax.grants"
