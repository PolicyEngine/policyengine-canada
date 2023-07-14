from policyengine_canada.model_api import *


class qc_solidarity_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec solidarity tax credit"
    definition_period = YEAR
    defined_for = "qc_solidarity_eligibility"

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.solidarity

        # claim eligibility
        eligibility = household("qc_solidarity_eligibility", period)

        # family situation
        married = household("is_married", period)
        children = household("count_children", period)
        income = household("adjusted_family_net_income", period)

        # Housing component
        pays_property_tax = add(household, period, ["property_tax"]) > 0
        pays_rent = add(household, period, ["rent"]) > 0
        housing_eligible = pays_property_tax | pays_rent

        housing_family_amount = married * p.amount.housing.family
        housing_living_alone_amount = ~married * p.amount.housing.living_alone
        housing_children_amount = children * p.amount.housing.child

        housing = housing_eligible * (
            housing_family_amount
            + housing_living_alone_amount
            + housing_children_amount
        )

        # QST component
        # Requires having paid some Quebec sales tax
        qst_eligible = add(household, period, ["qc_sales_tax"]) > 0

        qst_spouse_amount = married * p.amount.qst.spouse
        qst_living_alone_amount = ~married * p.amount.qst.living_alone

        qst = qst_eligible * (
            p.amount.qst.base + qst_spouse_amount + qst_living_alone_amount
        )

        # Components for individuals living in a northern village
        northern_village_eligible = household(
            "qc_living_in_northern_villages", period
        )

        northern_village_children_amount = (
            children * p.amount.northern_village.child
        )
        northern_village_spouse_amount = (
            married * p.amount.northern_village.base
        )

        northern_village_amount = northern_village_eligible * (
            p.amount.northern_village.base
            + northern_village_spouse_amount
            + northern_village_children_amount
        )

        # total credit
        total_credit = qst + housing + northern_village_amount

        reduction_amount = select(
            [
                qst_eligible & housing_eligible,
                qst_eligible & ~housing_eligible,
            ],
            [
                p.reduction.qst_and_housing.calc(income),
                p.reduction.qst_only.calc(income),
            ],
            default=0,
        )

        return eligibility * max_(total_credit - reduction_amount, 0)
