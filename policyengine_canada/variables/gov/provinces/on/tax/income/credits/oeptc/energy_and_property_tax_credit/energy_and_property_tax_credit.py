from policyengine_canada.model_api import *


class energy_and_property_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Energy and property tax credit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_net_family_income", period)
        senior_status = household("oeptc_senior_status", period)
        senior = senior_status == "SENIOR"
        non_senior = senior_status == "NON_SENIOR"
        household_status = household("oeptc_category", period)
        married = household_status == "MARRIED"
        single_no_children = household_status == "SINGLE_NO_CHILDREN"
        single_shared_custody = household_status == "SINGLE_SHARED_CUSTODY"
        single_sole_custody = household_status == "SINGLE_SOLE_CUSTODY"

        province = household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        p = parameters(period).gov.provinces.on.tax.income.credits.oeptc
        energy_component = household("energy_component", period)
        property_tax_component = household(
            "property_tax_component_senior", period
        )
        return select(
            [
                senior & married,
                senior & single_no_children,
                senior & single_shared_custody,
                senior & single_sole_custody,
                non_senior & married,
                non_senior & single_no_children,
                non_senior & single_shared_custody,
                non_senior & single_sole_custody,
            ],
            [],
        )
