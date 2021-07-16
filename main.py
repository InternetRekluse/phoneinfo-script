# Program by: internetrekluse

import phonenumbers
import datetime
from test import number
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

now = datetime.datetime.now()
print("Current date and time is:")
print(now.strftime("%y-%m-%d %H:%M:%S"))
print()

# Parsing String to Phone number
# Phone number format: (+Countrycode)xxxxxxxxxx
phoneNumber = phonenumbers.parse(number)
print("phone_information: ")
print(phoneNumber)
print()

# Test to see if phone number is possible.
possible = phonenumbers.is_possible_number(phoneNumber)  # too few digits for USA
print("Is possible: ")
print(possible)
print()

# Formats testing
national_format = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.NATIONAL)
international_format = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
other_format = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.E164)
print("Phone number formats: ")
print(national_format)
print(international_format)
print(other_format)
print()


# Test to see if phone number is validate.
validate = phonenumbers.is_valid_number(phoneNumber)
print("Is validate: ")
print(validate)
print()

# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(phoneNumber)

# It print the timezone of a phonenumber
print("timezones: ")
print(timeZone)
print()

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print("location_id: ")
print(geocoder.description_for_number(ch_number, "en"))
print()

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("Carrier: ")
print(carrier.name_for_number(service_number, "en"))
print()
