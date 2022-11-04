from math import remainder
from policyengine_canada.model_api import *


class training_credit(Variable):
    value_type = float
    entity = Person
    label = "Training credit"
    unit = CAD
    documentation = "Training credit available"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        income = tax_unit("training_credit_income", period)
        tuition = tax_unit("tuition_expenses", period)
        age = tax_unit("age", period)
        training = parameters(period).gov.credits.training
        lower_limit = training.age_eligibility.min
        upper_limit = training.age_eligibility.max
        aged = (age >= lower_limit) & (age <= upper_limit)
        existing_credits = tax_unit("existing_training_credits", period)
        cap = training.lifetime_cap
        remaining = max_(0, cap - existing_credits)
        threshold = training.amount
        credits = threshold.calc(income)
        student = tuition > 0
        eligible = min_(remaining, credits)
        if aged == True and student == True:
            return eligible
        else:
            return 0
