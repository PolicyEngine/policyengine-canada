class nb_disability_amount_for_self(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick disability amount for self"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nb.tax.income.credits.low_income_tax_reduction
        married = household("is_married", period)
        dependant = person("is_dependant", period)
        return min_(
            p.base.max_amount,
            p.base.head
            + married * p.base.spouse
            + dependant * p.base.dependant,
        )