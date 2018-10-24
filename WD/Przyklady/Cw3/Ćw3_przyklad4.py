#Słowniki i zamiana klucza z wartością

skroty={"PZU": "Państwowy zakład Ubezpieczeń",
          "ZUS": "Zakład Ubezpieczeń Społecznych",
          "PKO": "Powszechna Kasa Oszczędności"}

odwrocone={value: key for key, value in skroty.items()}
print("Oryginalny słownik")
print(skroty)
print("Słownik odwrócony")
print(odwrocone)
