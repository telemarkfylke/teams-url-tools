import requests
import os
 
antallLenker = 0

# Globale variabler for å holde styr diverse info
path = "./General"
filnavn = [] # Liste med alle filnavn i hele mappestrukturen
good_files = [] # Liste med filnavn som er slutter på .url
bad_files = [] # Liste med filnavn som ikke slutter på .url
bad_urls = [] # Liste med url'er som ikke fungerer
 
# Traverserer alle mapper og henter ut alle filnavn i hele mappestrukturen
for root,d_names,f_names in os.walk(path):
   for f in f_names:
      filnavn.append(os.path.join(root, f))
 
# Henter ut alle url-filer
for i in range(len(filnavn)): # Sett in len(filnavn) for å kjøre på alle filer
    try:
        if filnavn[i].split(".")[-1] == "url":
            good_files.append(filnavn[i])
    except:
        print("Feil filformat:", filnavn[i])
        bad_files.append(filnavn[i])

for i in range(len(good_files)):
    url_file = open(good_files[i], "r")
    url = url_file.read().split("URL=")[-1].split("\n")[0]
    try:
        response = requests.get(url)
        if response.status_code == 403:
            bad_urls.append({"msg": "Krever autentisering - Må sjekkes manuelt", "status_code": response.status_code ,  "url": url, "url-fil": good_files[i]})
        elif response.status_code == 400:
            bad_urls.append({"msg": "Bad request", "status_code": response.status_code ,  "url": url})
        elif response.status_code == 200:
            bad_urls.append({"msg": "Jøss, hva skjedde her da?", "status_code": response.status_code ,  "url": url})
        else:
            bad_urls.append({"msg": "Udefinert", "status_code": response.status_code ,  "url": url})
    except requests.exceptions.RequestException as e:
        print("Blæ, noe gikk skikkelig galt")
        bad_urls.append({"msg": "Her gikk det skikkelig galt", "status_code": "ERROR",  "url": url})
    print("Ferdig med fil:", good_files[i])
    antallLenker += 1

print("Antall lenker:", antallLenker)

# Write bad urls to file
with open("url_info.json", 'w') as new_file:
    new_file.write(str(bad_urls))


 