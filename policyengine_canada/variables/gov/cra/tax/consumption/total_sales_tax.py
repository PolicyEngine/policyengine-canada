from policyengine_canada.model_api import *


class total_sales_tax(Variable):
    value_type = float
    entity = Household
    label = "Total sales tax paid"
    definition_period = YEAR
    unit = CAD
    documentation = "Total sales tax paid including GST/HST and PST"
    adds = ["gst_hst", "provincial_sales_tax"]