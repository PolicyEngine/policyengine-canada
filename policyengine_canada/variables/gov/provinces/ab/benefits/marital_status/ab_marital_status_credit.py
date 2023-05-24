from policyengine_canada.model_api import *


class ab_marital_status_credit(Variable):
    value_type = float
    entity = Household
    label = "Alberta marital status credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        spouse_income = add(household, period, ["separated_spouse_income"])
        p = parameters(period).gov.provinces.ab.benefits.marital_status
        return max_(0, (p.base - spouse_income))
