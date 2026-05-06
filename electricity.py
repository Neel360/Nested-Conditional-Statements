energy_used = input("Enter the amount of energy used: ").lower().strip()
energy_used = int(energy_used)

if energy_used < 50:
    amount = energy_used * 2.60
    surcharge = 25
elif energy_used <= 100:
    amount = 130 + (energy_used - 50) * 3.25
    surcharge = 35
elif energy_used <= 200:
    amount = 130 + 162.5 + (energy_used - 100) * 5.26
    surcharge = 45
else:
    amount = 130 + 162.5 + 526 + (energy_used - 200) * 8.45
    surcharge = 75

total_amount = amount + surcharge
print("The total amount due is: %.2f" % total_amount)