# Apvienot datnes 'admin.txt' un 'viesis.txt'
combined_data = []

# Nolasa 'admin.txt'
with open("admin.txt", "r") as admin_file:
    combined_data.extend(admin_file.readlines())

# Nolasa 'viesis.txt'
with open("viesis.txt", "r") as guest_file:
    combined_data.extend(guest_file.readlines())

# Izdrukā apvienotos datus
print("Apvienotie dati:")
for line in combined_data:
    print(line.strip())
    
with open("combined_data.txt", "w") as combined_file:
    for line in combined_data:
        combined_file.write(line)

# Aprēķina statistiku par administratoriem
def calculate_admin_statistics(data):
    total_age = 0
    min_age = float('inf')
    max_age = 0
    admin_count = 0

    for line in data:
        parts = line.strip().split()
        if len(parts) == 4 and "Admin" in line:
            age = int(parts[3])
            total_age += age
            if age < min_age:
                min_age = age
            if age > max_age:
                max_age = age
            admin_count += 1

    average_age = total_age / admin_count if admin_count > 0 else 0
    return average_age, min_age, max_age, admin_count

# Aprēķina statistiku par administratoriem
average_admin_age, youngest_admin_age, oldest_admin_age, admin_count = calculate_admin_statistics(combined_data)

# Izdrukā administratoru statistiku
print("\nAdministratoru statistika:")
print(f"Vidējais vecums: {average_admin_age:.2f}")
print(f"Jaunākais administrators: {youngest_admin_age}")
print(f"Vecākais administrators: {oldest_admin_age}")
#print(f"Administratoru skaits: {admin_count}")

# Aprēķina administratoru un viesu skaitu
def count_admins_and_guests(data):
    admin_count = sum(1 for line in data if "Admin" in line)
    guest_count = sum(1 for line in data if "Guest" in line)
    return admin_count, guest_count

# Aprēķina administratoru un viesu skaitu
admins_count, guests_count = count_admins_and_guests(combined_data)

# Izdrukā administratoru un viesu skaitu
print("\nAdministratoru un viesu skaits:")
print(f"Administratoru skaits: {admins_count}")
print(f"Viesu skaits: {guests_count}")
