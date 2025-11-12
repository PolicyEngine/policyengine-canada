from policyengine_canada.model_api import *


class bc_sales_tax_credit_reduction(Variable):
    value_type = float
    entity = Person
    label = "British Columbia sales tax credit reduction"
    unit = CAD
    documentation = "Reduction to BC sales tax credit based on income"
    definition_period = YEAR
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        household = person.household
        is_married = household("is_married", period)

        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.sales_tax_credit

        # Income threshold differs for single vs couple
        threshold = where(is_married, p.threshold.couple, p.threshold.single)

        # Reduction is 2% of income over threshold
        excess_income = max_(0, income - threshold)
        return excess_income * p.reduction_rate
