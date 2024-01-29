from policyengine_canada.model_api import *


class qc_designated_remote_area_travel_benefit(Variable):
    value_type = float
    entity = Person
    label = "Quebec deduction for residents of designated remote areas"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/201-to-260-net-income/line-236/"
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.deduction.designated_remote_areas.travel_benefit_amount

        living_in_northern_zone = person("qc_living_in_northern_zone", period)
        living_in_intermediate_zone = person(
            "qc_living_in_intermediate_zone", period
        )

        return select(
            # living areas
            [living_in_northern_zone, living_in_intermediate_zone],
            # benefits
            [p.northern_zone, p.intermediate_zone],
            default=0,
        )
