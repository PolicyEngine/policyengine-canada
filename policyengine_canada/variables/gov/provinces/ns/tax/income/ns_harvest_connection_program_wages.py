from policyengine_canada.model_api import *


class ns_harvest_connection_program_wages(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia harvest connection program wages"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/coms/employment/income_assistance/HarvestConnectionProgram.html"
    defined_for = ProvinceCode.NS
