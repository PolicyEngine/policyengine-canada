from policyengine_canada.model_api import *


class low_income_workers_tax_credit_eligible_people(Variable):
    value_type = float
    entity = Household
    label = (
        "Sum of eligible people for the Ontario Low-Income Workers Tax Credit"
    )
    unit = CAD
    definition_period = YEAR

    adds = ["low_income_workers_tax_credit_eligible"]
