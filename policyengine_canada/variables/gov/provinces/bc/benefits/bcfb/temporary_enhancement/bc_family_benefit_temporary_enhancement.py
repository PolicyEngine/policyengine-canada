from policyengine_canada.model_api import *


class bc_family_benefit_temporary_enhancement(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit temporary enhancement"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    reference = "https://www2.gov.bc.ca/gov/content/family-social-supports/affordability/family-benefit"

    def formula(household, period, parameters):
        children = household("bc_family_benefit_eligible_children", period)
        family_net_income = household("adjusted_family_net_income", period)
        p = parameters(
            period
        ).gov.provinces.bc.benefits.bcfb.temporary_enhancement
        phase_out_amount_middle_income = p.phase_out_rate_middle_income.calc(
            family_net_income
        )
        phase_out_amount_high_income = p.phase_out_rate_high_income.calc(
            family_net_income
        )
        return select(
            [
                family_net_income
                < p.phase_out_rate_middle_income.thresholds[1],
                p.phase_out_rate_middle_income.thresholds[1]
                < family_net_income
                < p.phase_out_rate_middle_income.thresholds[2],
                family_net_income
                > p.phase_out_rate_middle_income.thresholds[2],
            ],
            [
                p.max_amount * children,
                max_(
                    p.max_amount - phase_out_amount_middle_income,
                    p.minimum_amount_middle_family_income,
                )
                * children,
                max_(
                    p.minimum_amount_middle_family_income
                    - phase_out_amount_high_income,
                    0,
                )
                * children,
            ],
        )
