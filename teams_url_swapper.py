# Programmet bytter ut en gammel lenke med en ny lenke i alle url-filer i en mappestruktur

import os

# Globale variabler for å holde styr diverse info
path = "./General" # Stien til mappen som inneholder alle url-filene
gammel_lenke = "<Sett inn uttrykket som man ønsker å bytte ut>" # Strengen som man ønsker å bytte ut
ny_lenke = "<Sett in ny streng som skal erstatte den gamle>" # Strengen som erstatter det man ønsker å bytte ut
filnavn = [] # Liste med alle filnavn i hele mappestrukturen
good_files = [] # Liste med filnavn som er slutter på .url
bad_files = [] # Liste med filnavn som ikke slutter på .url
 
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
 
# Skriver ut alle filnavn som slutter på .url og lenken som finnes i filen
# Lager en ny mappe som heter "General_replaced" med nye oppdaterte url'er
print("\nFiler som slutter på .url:")
for i in range(len(good_files)):
    url_file = open(good_files[i], "r")
    url = url_file.read().split("URL=")[-1]
    ny_url = url.replace(gammel_lenke, ny_lenke)
    url_file = "[InternetShortcut]\nURL=" + ny_url
    print("Filnavn:", good_files[i], "\nLenke:", url)
    print(url_file)
    # Erstattet gammel url-fil med ny
    with open(good_files[i], 'w') as new_file:
        new_file.write(url_file)