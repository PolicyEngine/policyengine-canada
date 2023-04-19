from policyengine_canada.model_api import *


class qc_child_assistance_credit_children(Variable):
    value_type = int
    entity = Household
    label = "Children eligible for the Quebec Child Assitance Tax Credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    adds = ["qc_child_assistance_credit_child"]