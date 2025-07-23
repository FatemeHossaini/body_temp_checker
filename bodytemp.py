import csv

# get user's body temperature
temp = float(input("Enter your body temperature in Celsius: "))

# analyze temperature
if temp < 35:
    status = "Too Low (Possible Hypothermia)"
elif 35 <= temp <= 37.5:
    status = "Normal"
elif 37.5 < temp <= 38.5:
    status = "Mild Fever"
elif 38.5 < temp <= 40:
    status = "High Fever"
else:
    status = "Critical Fever"

# print result
print(f"Status: {status}")

# save data to CSV
with open("temperature_log.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([ temp, status])
print(" Data saved to temperature_log.csv")