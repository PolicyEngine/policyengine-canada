from policyengine_canada.model_api import *


class ns_chargeable_rent_income(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Income Assistance rent received"
    unit = CAD
    definition_period = YEAR
    reference = "https://novascotia.ca/employmentnovascotia/programs/documents/Skills_Development_Guidelines.pdf"
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.income_assistance.eligibility.income.rent
        base = p.chargeable_rent_base
        boarders_living = person("boarders_living", period)
        roomers_living = person("roomers_living", period)
        rent_from_properties = person("rent_from_properties", period)
        rent_income = person("rent_income", period)
        # Define the conditions and corresponding values
        conditions = [
            boarders_living > 0,
            roomers_living > 0,
            rent_from_properties > 0
        ]

        values = [
            max_（base, (rent_income * p.live_with_boarders_rate)),  # for living with boarders
            max_（base, (rent_income * p.live_with_roomers_rate)),  # for living with roomers 
            (rent_income * p.rent_from_properties_rate)   # for rent from properties 
        ]

        # Calculate the chargeable rent income based on the conditions
        chargeable_rent_income = np.select(conditions, values, default=2)
    
        return chargeable_rent_income

