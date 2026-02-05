from policyengine_canada.model_api import *


class gis_topup_net(Variable):
    value_type = float
    entity = Person
    label = "Net Guaranteed Income Supplement Top-Up"
    unit = CAD
    documentation = (
        "Highest GIS Topup a person is eligible for, minus their reduction. "
    )
    definition_period = YEAR

    def formula(person, period, parameters):
        gis_topup_cap = person("gis_topup_cap", period)
        gis_topup_reduction = person("gis_topup_reduction", period)

        return max_(gis_topup_cap - gis_topup_reduction, 0)
