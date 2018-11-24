
# Drugie zajęcia, pierwszy chat bot
name = input("Jak masz na imię?")
print("Witaj," + name)
year = input("W którym roku się urodziłeś/urodziłaś?")
year_as_int = int(year)
age = 2018 - year_as_int
age_as_string = str(age)
print("Masz kolego/koleżanko " + age_as_string + " lat.")
winner = input(name + " kto Twoim zdaniem wygra wybory w Warszawie?")
print("zatem " + winner + ", to ciekawy pogląd. Dzięki za Twój czas")
