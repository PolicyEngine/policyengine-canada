from policyengine_canada.model_api import *


class non_refundable_tax_credits(Variable):
    value_type = float
    entity = Person
    label = "Non-refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.cra.tax.income.credits.non_refundable"
