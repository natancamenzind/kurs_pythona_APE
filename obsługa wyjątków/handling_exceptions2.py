"""
Ok, znasz już podstawy obsługi wyjątków. Teraz zajmiemy się bardziej zaawansowanym wykorzystaniem tej 
funkcjonalności.

1. Wykorzysatnie treści błędu
2. Rozszerzona składnia obsługi wyjątków
3. Samodzielne wywołanie błędu
4. Definiowanie własnych błędów
"""

# 1. Wykorzystanie treści błędu

# Może być tak, że automatyczna treść błędu, jego argument przyda nam się do czegoś. Możemy się do niej dostać
# w natępujący sposób:

try:
	1/0
except ZeroDivisionError as error:
	print('Nie dziel cholero przez zero!')
	print(error)
# Wykonianie tego kodu wyprintuje następujące kominukaty:
# Nie dziel cholero przez zero!
# division by zero

# Argument błedu to zwykle oficjalny komunikat Pythona związany z danym błędem.
# Użyte tu słowo kluczowe 'as' jest powszechne i można go używać na przykład tak:
from random import randint as twoj_stary_myje_gary
random_intiger = twoj_stary_myje_gary(1, 100)
# idzie o to, żeby stworzyć skrót, alias, który pozwoli nam się odnieść do danej rzeczy


# 2. Rozszerzona składnia obsługi wyjątków
# Jak możę zauważyłaś_eś jest coś podobnego w składni obsługi wyjątkow do warunków. Podobieńtwa będą jeszcze
# bardziej widoczne, kiedy obczaimy bardziej rozbudowaną składnię. Ano błędy można obługiwać także tak:
try:
	print('Do my thing')
except MyStrangeError:
	print('An error occured!')
else:
	print('Error did not occured!')

# To co pod else wykona się jeśli wyjątek nie wystąpi.

# Ale możmemy pójść krok dalej:

try:
	print('Do my thing')
except MyStrangeError:
	print('An error occured!')
else:
	print('Error did not occured!')
finally:
	print('This will apear if the error occures as well as if it wont. This will just be printed')

# Kod po finally zostanie wykonany na końcu naszegej obsługi wyjątku, niezależnie do tego, czy błąd się
# pojawi czy nie. Metafora z życia: to co finally to jak "kurtyna!" po spektaklu - opada niezależnie od tego,
# czy aktorzy_orki się pomylą czy nie.

# 3. Samodzielne wywołanie błędu
# Zazwyczaj błąd pojawia się przy wykonywaniu jakiejś funkcji, której definicja znjaduje się gdzie indziej.
# Czasem chcemy, żeby wewnątrz funkcji, pod jakimś warunkiem wystąpił błąd. Samodzielnie możemy wywołać błąd
# używając słow kluczowego 'raise'
# Przykład:
def send_nice_email(msg):
	if 'kurwa' in msg:
		raise NotBeeingNiceException  # o tutaj
	send_mail(msg)

try:
	send_nice_email(my_very_nice_msg)
except NotBeeingNiceException:
	print('This is not nice!')

# Z czego błąd o nazwie NotBeeingNiceException nie istnieje. Jeszcze!

# 4. Definiowanie własnych błędów
# Wszystkie błędy/wyjątki to obieky definiowane przez klasy. Wszyskie dziedziczą po najogólniejszym błędzie,
# który nazywa się po protsu Exception i implementuje całą podstawową logikę "rzucania błędu".
# Nic nie stoi na przeszkodzie, żebyśmy stworzyli nasz własny błąd. Przydaje się to m.in. w sytuacjach, gdy
# tworzymy osobne moduły, które będą używane w wielu miejscach i jeśli pojawi się błąd - niech bedzie wiadomo,
# że to od nas.

# Jak to robimy?
class NotBeeingNiceException(Exception):
	pass

# I już!
# W konsoli będzie to wyglądać tak:

# In [18]: raise NotBeeingNiceException                                                                                                
# ---------------------------------------------------------------------------
# NotBeeingNiceException                    Traceback (most recent call last)
# <ipython-input-18-b83736003ea7> in <module>
# ----> 1 raise NotBeeingNiceException
#
# NotBeeingNiceException: 

# Z czego czasem chcemy, żeby nasz błąd zawiera jakąś dodatkową wiadomość. 
# Na przykład jeśli wpiszesz w konsoli 1/0 i wykonasz, otrzymasz:
# ZeroDivisionError: division by zero

# Jeśli chcemy, żeby nasz błąd jednorazowo zawierał jakąś wiadomość, tj. tylko w danym fragmencie kodu, to:
raise NotBeeingNiceException('Ty chuju!')
# dostniemy:
# NotBeeingNiceException: Ty chuju!

# Ale jeśli chcemy mieć stałą wiadomość, to musi zmienić kosntruktor klasy błędu
class NotBeeingNiceException(Exception):
	
	def __init__(self, *args, **kwargs):
		super().__init__('Chuj Ci w cyce!', *args, **kwargs) 

# O co chodzi?
# W funckji __init__ podajemy argument specjalne *args i **kwargs (co to znaczy - innym razem)
# i przekazujemy je do funkcji super, czyli mówimy "rób to, co robią Twoje klasy nadrzędne", z tą różnicą,
# że dodajemy pierwszy argumetn, którym w przypadku konstruktora Exception jest message, wiadomość, która
# wyświetla się z nazwą błędu.

# Nawet jeśli teraz ta konstrukcja nie jest do końca jasna, to niebawem będzie chleb powszedni, spoko ;)

# Zrób proszę zadanie 2.
# Najlepszym źródłem wiedzy jest zawsze w pierwszej kolejności dokumentacja 
# https://docs.python.org/3.7/tutorial/errors.html
# a potem stack overflow



