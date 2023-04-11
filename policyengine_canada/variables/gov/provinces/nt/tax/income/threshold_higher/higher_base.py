from policyengine_canada.model_api import *


class ntltc_higher_base(Variable):
    value_type = float
    entity = Household
    label = "Higher income for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):

        return (
            942
        )