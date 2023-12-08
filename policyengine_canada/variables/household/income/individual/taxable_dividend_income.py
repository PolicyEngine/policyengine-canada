from policyengine_canada.model_api import *


class taxable_dividend_income(Variable):
    value_type = float
    entity = Person
    label = "Total taxable dividends (eligible and other than eligible)"
    unit = CAD
    definition_period = YEAR
    reference = "https://pubsaskdev.blob.core.windows.net/pubsask-prod/806/I2-01.pdf#page=31"
