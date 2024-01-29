from policyengine_canada.model_api import *


class qc_designated_remote_area_travel_benefit_household(Variable):
    value_type = float
    entity = Household
    label = "Quebec deduction for household of designated remote areas"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/201-to-260-net-income/line-236/"
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        designated_remote_area_travel_benefit = add(
            household, period, ["qc_designated_remote_area_travel_benefit"]
        )
        household_size = household("household_size", period)

        return household_size * designated_remote_area_travel_benefit
