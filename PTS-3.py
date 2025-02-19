def suhu(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

hasil = suhu(30)
print(f"30°C sama dengan {hasil:.1f}°F")