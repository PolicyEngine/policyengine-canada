from policyengine_canada.model_api import *


class qc_children_activities_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec children's activities tax credit"
    definition_period = YEAR
    defined_for = "qc_children_activities_credit_eligible"

    adds = [
        "qc_non_disabled_children_activities_credit",
        "qc_disabled_children_activities_credit",
    ]
