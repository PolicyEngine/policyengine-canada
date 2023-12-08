from policyengine_canada.model_api import *


class tax_exempt_dividend_income(Variable):
    value_type = float
    entity = Person
    label = "Taxable Dividends (Other Than Eligible)"
    unit = CAD
    definition_period = YEAR
    reference = "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=31"
