# Obsługa Wyjątków // Handling Exceptions

# Często podczas działania naszego programu mogą pojawić się błędy. Podczas pracy nad aplikacją są wręcz 
# pożądane, bo pozwalają nam uniknąc błędów na produkcji. Wiele z nich możemy łatwo naprawić (błędy składniowe,
# związane z nieodpowiednią ilością wcięć itp.), jednak niektóre pojawią się mimo naszych najlepszych chęci.
# W prawdzimy życiu używa się obsługi błędów często do właściwej reakcji względem świata zewnętrznego. 
# Np. przy wysyłce maila możemy stracić połączenie, wtedy funckja odpowiedzialna za wysyłkę wysypie błąd, 
# ale nie chcemy, żeby skutkowało to zatrzymaniem całej naszej aplikacji, a jedynie wyświetleniem komunikatu.

# przykład składni obsługi błedu:

try: # 1
	number = int(input("Podaj liczbę"))  # 2
except ValueError:  # 3
	print("To nie jest liczba ziomek!")  # 4

# Na obsługę wyjątku składa się:
# 1. słowo kluczowe 'try' i dwukropek po nim
# 2. kod który ma się wykonać w ramach "próby", czyli to co po wcięciu
# 3. słowo kluczowe 'except' i określenie błedu (opcjonalne) i dwukropek
# 4. kod który ma się wykonać jeśli wystąpi błąd

# Nazwa błędu jest opcjonalna. Jeśli jej nie podamy, obsłużony zostanie każdy wyjątek.
try:
	value = my_crazy_function() # 2
except:  # 3
	print("I can't handle you, man!")
# W ten sposób niezależnie jaki błąd wywoła nasza funckja, jeśli pojawi się jakikolwiek, wykona się kod
# pod except.
# Nie jest to jednak dobra praktyka. Zasada właściwa całemu programowaniu głosi: Catch What You Can Handle.
# Idzie o to, że jeśli oczekujemy, że nasza aplikacja może się wywalić, to chcemy mieć kontrolę nad charakterm
# tego upadku. Na przykładzie: jeśli uczymy dziecko jeżdzić na rowerze, to uwzględniamy, że się wywróci, ok,
# nic się nie stało. Ale jeśli dostanie drgawek i zacznie wymiotować to powinniśmy jak najszybciej zaregować.
# Tu jest podobnie. Miejsca w aplikacji, które są gotowe na przyjęcie jakiekolwiek błędu utrudnią nam w 
# przyszłości debugowanie aka odrobaczanie kodu. Więc po prostu tego nie rób.

# Ok, teraz zrób proszę zadanie nr 1