age = int(input("what's your age?"))
years = age
months = years * 12
weaks = months * 4
days = weaks * 7
houres = days * 24
minute = houres * 60
second = minute * 60

print(f"you lived for {years} year")
print(f"{months:,} month")
print(f"{weaks:,} weak")
print(f"{days:,} day")
print(f"{houres:,} houre")
print(f"{minute:,} minute")
print(f"{second:,} second")
