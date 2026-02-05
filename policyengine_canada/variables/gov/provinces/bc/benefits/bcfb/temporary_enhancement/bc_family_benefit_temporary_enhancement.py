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
        months = min_(p.cap_month, MONTHS_IN_YEAR)
        low_family_income = (
            family_net_income < p.phase_out.middle.thresholds[1]
        )
        middle_family_income = (
            p.phase_out.middle.thresholds[1]
            < family_net_income
            < p.phase_out.middle.thresholds[2]
        )
        high_family_income = (
            family_net_income > p.phase_out.middle.thresholds[2]
        )
        phase_out_amount_middle_income = p.phase_out.middle.calc(
            family_net_income
        )
        phase_out_amount_high_income = p.phase_out.high.calc(family_net_income)
        temporary_enhancement_low_family_income = p.amount * children * months
        temporary_enhancement_middle_family_income = (
            max_(
                p.amount * months - phase_out_amount_middle_income,
                p.income_threshold.income_threshold * months,
            )
            * children
        )
        temporary_enhancement_high_family_income = (
            max_(
                p.income_threshold.income_threshold * months
                - phase_out_amount_high_income,
                0,
            )
            * children
        )
        return select(
            [low_family_income, middle_family_income, high_family_income],
            [
                temporary_enhancement_low_family_income,
                temporary_enhancement_middle_family_income,
                temporary_enhancement_high_family_income,
            ],
        )
