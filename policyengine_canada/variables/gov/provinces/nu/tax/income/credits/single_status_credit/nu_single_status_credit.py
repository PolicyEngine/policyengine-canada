from policyengine_canada.model_api import *


class nu_single_status_credit(Variable):
    value_type = float
    entity = Person
    label = "Nunavut single status credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        eligible = person("nu_single_status_credit_eligible", period)
        amount = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.single_status_credit.amount
        return amount * eligible
