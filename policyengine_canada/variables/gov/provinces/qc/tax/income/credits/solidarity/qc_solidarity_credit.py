from policyengine_canada.model_api import *


class qc_solidarity_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec solidarity tax credit"
    definition_period = YEAR
    defined_for = "qc_solidarity_eligibility"

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.solidarity

        income = household("adjusted_family_net_income", period)

        housing_component = household(
            "qc_solidarity_housing_component_amount", period
        )
        qst_component = household("qc_solidarity_qst_component_amount", period)
        northern_village_amount = household(
            "qc_solidarity_northern_village_amount", period
        )

        # The solidarity tax credit has three components
        total_credit = (
            qst_component + housing_component + northern_village_amount
        )

        # The credit may be reduced on the basis of the family income and different component eligibility
        reduction_amount = where(
            (qst_component > 0)
            & (housing_component == 0)
            & (northern_village_amount == 0),
            p.reduction.qst_only.calc(income),
            p.reduction.others.calc(income),
        )

        return max_(total_credit - reduction_amount, 0)
