from policyengine_canada.model_api import *


class benefits(Variable):
    value_type = float
    entity = Household
    label = "benefits"
    unit = CAD
    definition_period = YEAR
    adds = [
        "canada_child_benefit",
        "child_disability_benefit",
        "canada_workers_benefit",
        "dental_benefit",
        "old_age_security_pension",
        # Ontario programs.
        "on_child_benefit",
        "on_sales_tax_credit",
    ]
