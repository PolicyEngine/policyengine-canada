from policyengine_canada.model_api import *


class training_credit(Variable):
    value_type = float
    entity = Person
    label = "Training credit"
    unit = CAD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        income = tax_unit("training_credit_income", period)
        tuition = tax_unit("tuition_expenses", period)
        age = tax_unit("age", period)
        training = parameters(period).gov.cra.tax.income.credits.training
        lower_limit = training.age_eligibility.min
        upper_limit = training.age_eligibility.max
        meets_age_requirement = (age >= lower_limit) & (age <= upper_limit)
        existing_credits = tax_unit("prior_training_credits", period)
        cap = training.lifetime_cap
        remaining = max_(0, cap - existing_credits)
        threshold = training.amount
        credits = threshold.calc(income)
        student = tuition > 0
        amount_if_eligible = min_(remaining, credits)
        eligible = meets_age_requirement & student
        return eligible * amount_if_eligible
