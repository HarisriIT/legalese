from datetime import date

print("=" * 50)
print("       LEGALEASE - LEGAL DOCUMENT GENERATOR")
print("=" * 50)

print("\nEnter Rental Agreement Details\n")

landlord_name = input("Landlord Name: ")
tenant_name = input("Tenant Name: ")
property_address = input("Property Address: ")
monthly_rent = input("Monthly Rent: ")
agreement_duration = input("Agreement Duration (months): ")

agreement_date = date.today().strftime("%d-%m-%Y")

agreement = f"""
==================================================
              RENTAL AGREEMENT
==================================================

Agreement Date: {agreement_date}

Landlord Name: {landlord_name}

Tenant Name: {tenant_name}

Property Address: {property_address}

Monthly Rent: Rs. {monthly_rent}

Agreement Duration: {agreement_duration} months


TERMS AND CONDITIONS
--------------------------------------------------

1. The tenant agrees to pay the monthly rent on time.

2. The tenant shall keep the property clean and
   in good condition.

3. The tenant shall use the property only for
   lawful purposes.

4. Any damage caused to the property by the tenant
   shall be the tenant's responsibility.

5. Both parties agree to follow the terms mentioned
   in this rental agreement.


--------------------------------------------------
This is a computer-generated draft for reference.
Please have the document reviewed by a qualified
legal professional before signing or using it for
legal purposes.
==================================================
"""

print("\n" + agreement)

with open("generated_rental_agreement.txt", "w", encoding="utf-8") as file:
    file.write(agreement)

print("\nRental agreement generated successfully!")
print("Saved as: generated_rental_agreement.txt")