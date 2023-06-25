from policyengine_canada.model_api import *


class qc_solidarity_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec solidarity tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.solidarity

        # claim eligibility
        eligibility = household("qc_solidarity_eligibility", period)

        # family situation
        married = household("is_married", period)
        children = household("count_children", period)
        income = household("adjusted_family_net_income", period)

        # Housing component
        housing_component_eligible = (
            add(household, period, ["property_tax"]) > 0
        ) | (add(household, period, ["rent"]) > 0)

        housing_family_amount = married * p.housing_component.family_amount
        housing_living_alone_amount = (
            ~married * p.housing_component.living_alone_amount
        )
        children_amount = children * p.housing_component.child_amount

        housing_component = housing_component_eligible * (
            housing_family_amount
            + housing_living_alone_amount
            + children_amount
        )

        # The QST component
        qst_component_eligible = add(household, period, ["qc_qst"]) > 0

        qst_spouse_amount = married * p.qst_component.spouse_amount
        qst_living_alone_amount = (
            ~married * p.qst_component.living_alone_amount
        )

        qst_component = qst_component_eligible * (
            p.qst_component.base_amount
            + qst_spouse_amount
            + qst_living_alone_amount
        )

        # total credit
        total_credit = qst_component + housing_component

        reduction_amount = select(
            [
                (qst_component_eligible == True)
                & (housing_component_eligible == True),
                (qst_component_eligible == True)
                & (housing_component_eligible == False),
            ],
            [
                p.qst_and_housing_reduction.calc(income),
                p.qst_only_reduction.calc(income),
            ],
        )

        return eligibility * max_(total_credit - reduction_amount, 0)
