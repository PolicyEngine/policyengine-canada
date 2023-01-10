from policyengine_canada.model_api import *


class is_senior_for_oeptc(Variable):
    value_type = bool
    entity = Person
    label = "Is a senior for the oeptc"
    definition_period = YEAR

    def formula(person, period, parameters):
        return (
            person("age", period)
            >= parameters(
                period
            ).gov.provinces.on.tax.income.credits.oeptc.energy_and_property_tax_credit.oeptc
        )
