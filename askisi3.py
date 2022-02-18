# H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς. 
# Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να βρείτε ποιος 
# είναι ο τελευταίος γύρος και στην συνέχεια πάρτε τις τελευταίες 100 τιμές (πεδίο randomness) μέσα από 
# το https://drand.cloudflare.com/public/{round}. Μετατρέψτε αυτές τις τιμές σε δυαδικό και εμφανίστε 
# το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά και το μήκος της μεγαλύτερης ακολουθίας με 
# συνεχόμενες μονάδες.

import requests
Url = "https://drand.cloudflare.com/public/latest"

with requests.Session() as session:
    response1 = session.get(Url)
    if response: 
        Url2 ="https://drand.cloudflare.com/public/{loads(response1.text)['round']}"
        response2 = session.get(Url2)
        if response2:
            randomness = loads(response2.text)['randomness']
            rBin = bin(int(randomness, base=16))[2:]
            maxZeroCount = len(max(rBin.split('0')))
            maxOneCount = len(max(rBin.split('1')))
            print {maxZeroCount}
            print {maxOneCount}