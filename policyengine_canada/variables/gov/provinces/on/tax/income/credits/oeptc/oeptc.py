from policyengine_canada.model_api import *


class oeptc(Variable):
    value_type = float
    entity = Household
    label = "Ontario energy and property tax credit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        energy_plus_property_tax_components = add(
            household,
            period,
            ["oeptc_energy_component", "oeptc_property_tax_component"],
        )
        afni = household("adjusted_family_net_income", period)
        senior_status = household("oeptc_senior_status", period)
        category = household("oeptc_category", period)
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.phase_out
        excess = max_(afni - p.start[senior_status][category], 0)
        phase_out = excess * p.rate
        phased_out = energy_plus_property_tax_components - phase_out
        shared_custody_phased_out_divided = (
            phased_out / p.shared_custody.divisor
        )
        shared_custody_excess = max_(
            afni - p.shared_custody.start[senior_status], 0
        )
        shared_custody_second_phase_out = shared_custody_excess * p.rate
        shared_custody_second_phased_out = (
            energy_plus_property_tax_components
            - shared_custody_second_phase_out
        )
        shared_custody_second_phased_out_divided = (
            shared_custody_second_phased_out / p.shared_custody.divisor
        )
        shared_custody_result = (
            shared_custody_phased_out_divided
            + shared_custody_second_phased_out_divided
        )
        return max_(
            0,
            where(
                category == category.possible_values.SINGLE_SHARED_CUSTODY,
                shared_custody_result,
                phased_out,
            ),
        )
