from policyengine_canada.model_api import *


class ns_taxable_income(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia taxable income"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenue.pa.gov/FormsandPublications/FormsforIndividuals/PIT/Documents/2021/2021_pa-40in.pdf#page=8"
    defined_for = ProvinceCode.NS
    adds = ["total_individual_pre_tax_income"]
