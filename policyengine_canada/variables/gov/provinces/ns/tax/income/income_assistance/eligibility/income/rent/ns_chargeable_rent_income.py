from policyengine_canada.model_api import *


class ns_chargeable_rent_income(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Income Assistance chargeable rent income"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/employmentnovascotia/programs/documents/Skills_Development_Guidelines.pdf"
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.income.rent
        base = p.chargeable_rent_base
        boarder_rent = person("rent_from_boarders", period)
        boarder_rent_rate = boarder_rent * p.live_with_boarders_rate
        roomers_rent = person("rent_from_roomers", period)
        roomers_rent_rate = roomers_rent * p.live_with_roomers_rate
        properties_rent = person("rent_from_properties", period)
        
        amount_with_boarders = where(
            boarder_rent > 0,
            max_(base, boarder_rent_rate),
            0,
        )
        amount_with_roomers = where(
            roomers_rent > 0,
            max_(base, roomers_rent_rate),
            0,
        )
        amount_with_properties = where(
            properties_rent > 0,
            properties_rent * p.rent_from_properties_rate,
            0,
        )

        return (
            amount_with_boarders + amount_with_roomers + amount_with_properties
        )
