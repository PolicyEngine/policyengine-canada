from policyengine_canada.model_api import *


class ns_income_assistance(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia Income Assistance"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/coms/employment/income_assistance/Eligibility.html#19"
    defined_for = ProvinceCode.NS
