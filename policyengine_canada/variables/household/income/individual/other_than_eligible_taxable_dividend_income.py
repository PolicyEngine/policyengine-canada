from policyengine_canada.model_api import *


class other_than_eligible_taxable_dividend_income(Variable):
    value_type = float
    entity = Person
    label = "Taxable Dividends (Other Than Eligible)"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-d/5008-d-22e.pdf#page=3"
