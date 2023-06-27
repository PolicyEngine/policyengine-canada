from policyengine_canada.model_api import *


class ab_disability_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta disability tax credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        disability = person("is_disabled", period)
        return (
            disability
            * parameters(
                period
            ).gov.provinces.ab.tax.income.credits.disability.base
        )
