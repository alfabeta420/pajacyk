import requests

print("Ile chcesz klikniec?")
a = input()
a = int(a)
b = 0
while b < a:
    r = requests.post("https://www.pajacyk.pl/api/clicks")
    print(f"Wysłano kliknięcie nr {b}")
    b = b + 1
print("Zakonczono klikanie w przycisk :) milego dnia")
input()
