from policyengine_canada.model_api import *


class on_health_premium(Variable):
    value_type = float
    entity = Person
    label = "Ontario health premium"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.ontario.ca/laws/statute/07t11#BK8"
    documentation = "The amount of the Ontario health premium"
    defined_for = ProvinceCode.ONT

    def formula(person, period, parameters):
        income = person("on_taxable_income", period)
        p = parameters(period).gov.provinces.on.tax.health_premium.rate
        return p.calc(income)
