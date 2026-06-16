def scan_barcode(barcode):

    medicines = {
        "8901234567890": "Paracetamol",
        "8909876543210": "Ibuprofen"
    }

    return medicines.get(
        barcode,
        "Medicine Not Found"
    )
