"""
This file defines the entities needed by our legislation.

Taxes and benefits can be calculated for different entities: persons, household, companies, etc.

See https://openfisca.org/doc/key-concepts/person,_entities,_role.html
"""

from policyengine_core.entities import build_entity

Household = build_entity(
    key="household",
    plural="households",
    label="Household",
    doc="A group of people sharing a living space",
    roles=[
        {
            "key": "member",
            "plural": "members",
            "label": "Member",
            "doc": "A member of the household.",
        },
    ],
)

Person = build_entity(
    key="person",
    plural="people",
    label="Person",
    doc="A single person",
    is_person=True,
)


entities = [Household, Person]
