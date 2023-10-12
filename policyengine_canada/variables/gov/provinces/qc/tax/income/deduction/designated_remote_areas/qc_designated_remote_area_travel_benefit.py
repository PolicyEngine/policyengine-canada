from policyengine_canada.model_api import *


class qc_designated_remote_area_travel_benefit(Variable):
    value_type = float
    entity = Household
    label = "Quebec deduction for residents of designated remote areas"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/201-to-260-net-income/line-236/"
    defined_for = ProvinceCode.QC

    def formula(hosuehold, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.deduction.designated_remote_area.travel_benefit_amount

        
