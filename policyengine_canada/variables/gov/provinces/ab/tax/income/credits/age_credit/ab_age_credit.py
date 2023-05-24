from policyengine_canada.model_api import *


class ab_age_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta age benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(Person, period, parameters):
        income = Person("individual_net_income", period)
        eligibility = Person("ab_age_credit_eligible_count", period)
        p = parameters(period).gov.provinces.ab.tax.income.credits.age_credit
        prebenefit = max_((p.base - p.phase_out_rate.calc(income)), 0)

        benefit_amount = select(
            # Conditions.
            [eligibility == 0, eligibility > 0],
            # Results.
            [
                0,
                prebenefit * eligibility,
            ],
            default=0,
        )
        return benefit_amount
