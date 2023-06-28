from policyengine_canada.model_api import *


class qc_living_in_northern_villages(Variable):
    value_type = bool
    entity = Person
    label = "If an individual living in northern villages of Quebec"
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/tax-credits/solidarity-tax-credit/components-of-the-solidarity-tax-credit/component-for-individuals-living-in-northern-villages/"
