# importujemy bibliotekę odpowiedzialną za wyrażenia regularne
import re

# przykładowy teskt
text = "My name is Loren and my email is loren@gmail.com"
# wyrażenie regularne opisujące struktrę maila
mail_regex = re.compile(r'\w+@\w+.\w+')
# znajdź w danym tekscie pierwsze wyrażenie, które spełnia moje wymagania
# operacja zwraca nieczytelny obiekt typu:
# <_sre.SRE_Match object; span=(42, 56), match='loren@gmail.com'>
search_object = mail_regex.search(text)
# pokaż czytelny obiekt
email_address = search_object.group()

print(email_address)
# loren@gmail.com

# a co jeśli kilka?
rubbish = "asdfas@wp.pl asdfadsf adsfas a loren@gmail.com, sadfasdfiohiuj @pw.pl jan@wp.pl"
# wtedy używamy metody findall()
emails = mail_regex.findall(rubbish)
# zwróci nam listę
print(emails)
# ['asdfas@wp.pl', 'loren@gmail.com', 'jan@wp.pl']

# ściąga z zasadmi regexów:
# https://www.rexegg.com/regex-quickstart.html
