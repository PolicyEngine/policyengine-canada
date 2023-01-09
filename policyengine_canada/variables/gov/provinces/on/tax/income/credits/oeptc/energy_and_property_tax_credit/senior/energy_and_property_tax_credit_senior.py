from policyengine_canada.model_api import *


class energy_and_property_tax_credit_senior(Variable):
    value_type = float
    entity = Household
    label = "Energy and property tax credit senior"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        province = person.household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.energy_and_property_tax_credit
        energy_component = household("energy_component", period)
        property_tax_component = household(
            "property_tax_component_senior", period
        )
        income = household("adjusted_net_family_income", period)
