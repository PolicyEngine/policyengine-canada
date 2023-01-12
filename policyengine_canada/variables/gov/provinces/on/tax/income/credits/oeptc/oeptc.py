from policyengine_canada.model_api import *


class oeptc(Variable):
    value_type = float
    entity = Household
    label = "Ontario energy and property tax credit"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        # A. Add the results of Step 2 and Step 3.
        energy_plus_property_tax_components = add(
            household,
            period,
            ["oeptc_energy_component", "oeptc_property_tax_component"],
        )
        # B. Subtract $x from your adjusted family net income for 2021 (if
        #    negative, the result is zero).
        # x varies by senior status and household category.
        afni = household("adjusted_family_net_income", period)
        senior_status = household("oeptc_senior_status", period)
        category = household("oeptc_category", period)
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.phase_out
        excess = max_(afni - p.start[senior_status][category], 0)
        # C. Multiply B by x%.
        # x is a constant.
        phase_out = excess * p.rate
        # D. Subtract C from A.
        phased_out = energy_plus_property_tax_components - phase_out
        # Apply second phase-out for singles with shared custody.
        # These lettered steps only apply to single people with shared custody.
        # This essentially repeats the first phase-out, and then returns the
        # average of the two phased-out amounts.
        # E. Divide D by 2.
        shared_custody_phased_out_divided = (
            phased_out / p.shared_custody.divisor
        )
        # F. Subtract $x from your adjusted family net income for 2021 (if
        #    negative, the result is zero).
        # x varies by senior status.
        shared_custody_excess = max_(
            afni - p.shared_custody.start[senior_status], 0
        )
        # G. Multiply F by x%.
        # x is the same constant as for the first phase-out.
        shared_custody_second_phase_out = shared_custody_excess * p.rate
        # H. Subtract G from A.
        shared_custody_second_phased_out = (
            energy_plus_property_tax_components
            - shared_custody_second_phase_out
        )
        # I. Divide H by 2.
        shared_custody_second_phased_out_divided = (
            shared_custody_second_phased_out / p.shared_custody.divisor
        )
        # J. Add E and I.
        shared_custody_result = (
            shared_custody_phased_out_divided
            + shared_custody_second_phased_out_divided
        )
        # Return result depending on shared custody.
        print(energy_plus_property_tax_components)
        print(phase_out)
        print(phased_out)
        return max_(
            0,
            where(
                category == category.possible_values.SINGLE_SHARED_CUSTODY,
                shared_custody_result,
                phased_out,
            ),
        )
