from address import Address
from mailing import Mailing

to_addr = Address("128405", "Москва", "Новослободская", "5", "17")
from_addr = Address("191014", "Санкт-Петербург", "Невский", "58", "42")

mail = Mailing(to_address=to_addr, from_address=from_addr, cost=350.50, track="AB123456789RU")

from_addr_str = (
    f"{mail.from_address.postal_code}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment}"
)
to_addr_str = (
    f"{mail.to_address.postal_code}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}"
)

print(
    f"Отправление {mail.track} из {from_addr_str} в {to_addr_str}. "
    f"Стоимость {mail.cost} рублей."
)
