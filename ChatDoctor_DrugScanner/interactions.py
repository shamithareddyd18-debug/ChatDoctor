def check_interaction(
    medicine1,
    medicine2
):

    interactions = {

        (
            "Aspirin",
            "Ibuprofen"
        ):
        "May increase risk of bleeding",

        (
            "Warfarin",
            "Aspirin"
        ):
        "High risk of severe bleeding"
    }

    return interactions.get(
        (medicine1, medicine2),
        "No Known Interaction"
    )
