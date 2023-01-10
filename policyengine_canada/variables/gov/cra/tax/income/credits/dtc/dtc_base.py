from policyengine_canada.model_api import *


class dtc_base(Variable):
    value_type = float
    entity = Person
    label = "Disability tax credit base"
    unit = CAD
    definition_period = YEAR
    defined_for = "dtc_eligible"

    def formula(person, period, parameters):
        return parameters(period).gov.cra.tax.income.credits.dtc.base
