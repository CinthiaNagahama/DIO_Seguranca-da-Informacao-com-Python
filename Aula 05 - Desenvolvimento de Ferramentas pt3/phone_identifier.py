from phonenumbers import geocoder
import phonenumbers

phone = input("Digite o telefone no formato +551112345678: ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, "pt"))