from policyengine_canada.model_api import *

# No reduction in the Alberta Personal Income Tax Act

class ab_disability_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta disability tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = "ab_disability_tax_credit_eligible"

    def formula(person, period, parameters):
        return parameters(
            period
        ).gov.provinces.ab.tax.income.credits.disability.base
