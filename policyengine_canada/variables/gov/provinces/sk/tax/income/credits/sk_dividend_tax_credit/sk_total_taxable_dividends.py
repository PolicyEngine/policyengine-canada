from policyengine_canada.model_api import *


class sk_total_taxable_dividends(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan Taxable Dividends (eligible and other than eligible)"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-d/5008-d-22e.pdf#page=3"
    defined_for = ProvinceCode.SK
