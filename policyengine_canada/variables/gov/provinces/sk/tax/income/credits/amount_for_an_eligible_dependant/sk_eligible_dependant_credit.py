from policyengine_canada.model_api import *


class sk_eligible_dependant_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan eligible dependant credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.amount_for_an_eligible_dependant

        dependant_income = person("dependant_income", period)
        live_with_dependant = person("joint_living", period)
        eligible = live_with_spouse
        reduction = where(
            dependant_income_income <= p.net_income_base_amount, 0, dependant_income
        )
        reduced_amount = p.maximum_amount - reduction
        return eligible * max_(0, reduced_amount)
        
        credit = (
            person("mb_head_eligibility", period)
            * person("mb_dependant_eligibility", period)
            * (p.max_amount - person("dependant_income", period))
        )

        return credit