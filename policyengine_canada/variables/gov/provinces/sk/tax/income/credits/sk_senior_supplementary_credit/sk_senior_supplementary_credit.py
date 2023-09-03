from policyengine_canada.model_api import *


class sk_senior_supplementary_credit(Variable):
    value_type = float
    unit = CAD
    entity = Person
    label = "Sasktachewan senior supplementary tax credit"
    definition_period = YEAR
    defined_for = "sk_senior_supplementary_credit_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.sk_senior_supplementary
        eligibility = person("sk_senior_supplementary_credit_eligible", period)
        return eligibility * p.amount
