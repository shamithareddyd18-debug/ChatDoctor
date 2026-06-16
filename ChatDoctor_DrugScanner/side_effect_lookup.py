def get_side_effects(medicine):

    database = {

        "Paracetamol": [
            "Nausea",
            "Rash",
            "Liver Damage (Overdose)"
        ],

        "Ibuprofen": [
            "Stomach Pain",
            "Dizziness",
            "Nausea"
        ],

        "Aspirin": [
            "Bleeding",
            "Stomach Irritation"
        ]
    }

    return database.get(
        medicine,
        ["No Data Available"]
    )
