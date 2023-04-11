from policyengine_canada.model_api import *


class ntltc_low_base(Variable):
    value_type = float
    entity = Household
    label = "Low income for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit.threshold_low
         
        income = Household("income", period)
    
        return (
            p.low.low_rate * income
        )