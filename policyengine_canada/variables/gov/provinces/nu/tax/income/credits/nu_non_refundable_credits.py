from policyengine_canada.model_api import *


class nu_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "NU non refundable credits"
    documentation = "Nunavut non refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.nu.tax.income.credits.non_refundable"
