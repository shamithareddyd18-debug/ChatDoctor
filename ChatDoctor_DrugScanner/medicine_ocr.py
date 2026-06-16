def extract_medicine_name(text):

    medicines = [
        "Paracetamol",
        "Ibuprofen",
        "Aspirin",
        "Amoxicillin"
    ]

    for medicine in medicines:

        if medicine.lower() in text.lower():
            return medicine

    return "Medicine Not Found"
