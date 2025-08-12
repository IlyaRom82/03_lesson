from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79161234567"),
    Smartphone("Samsung", "Galaxy S23", "+79261234567"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79361234567"),
    Smartphone("Huawei", "Pura 70", "+79265173428"),
    Smartphone("Honor", "X8c", "+79561234567"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
