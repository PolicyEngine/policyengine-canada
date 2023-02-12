from policyengine_canada.model_api import *


class bc_family_benefit_temporary_enhancement(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit temporary enhancement"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        children: household("bc_family_benefit_eligible_children", period)
        return (
            children
            * parameters(
                period
            ).gov.provinces.bc.benefits.bcfb.temporary_enhancement.amount
        )


# TODO: tie into first reduction (make first reduction cap parameter)
