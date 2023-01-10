from policyengine_canada.model_api import *


class working_income(Variable):
    value_type = float
    entity = Person
    label = "Working income"
    unit = CAD
    documentation = "Income from employment and self-employment"
    definition_period = YEAR

    adds = "gov.cra.benefits.cwb.working_income_sources"
