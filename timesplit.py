secondes = 25372001
annee, mois, jour, heure, minutes, sec = 31104000, 2592000, 86400, 3600, 60, secondes
annee = sec // annee
sec %= 31104000
mois = sec // mois
sec %= 2592000
jour = sec // jour
sec %= 86400
heure = sec // heure
sec %= 3600
minutes = sec // minutes
sec %= 60

print(secondes, "seconde(s) =", annee, "annee(s)", mois, "mois", jour, "jour(s)", heure, "heure(s)", minutes, "minute(s)", sec, "seconde(s)")