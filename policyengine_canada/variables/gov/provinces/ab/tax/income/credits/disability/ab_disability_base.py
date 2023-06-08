from policyengine_canada.model_api import *


class ab_disability_base(Variable):
    value_type = float
    entity = Person
    label = "Alberta disability tax credit base"
    unit = CAD
    definition_period = YEAR
    defined_for = "ab_disability_eligible"

    def formula(person, period, parameters):
        return parameters(period).gov.provinces.ab.tax.income.credits.disability.base
    

