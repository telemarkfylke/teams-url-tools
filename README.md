# Teams URL-tools

URL-objekter i filarkivet på teams er en liten tekstfil som inneholder en lenke. I dette repoet finner du script for å hente ut og bearbeide disse lenkene.

## Bruksanvisning

1. Last ned mappestruktur fra teams. Dette gjøres ved å gå til filarkivet i teams, velge "last ned" og deretter "mappestruktur". Dette vil laste ned en zip-fil som inneholder alle filene i filarkivet.
2. Pakk ut zip-filen.
3. Kjør scriptet `get_urls.py` med mappen som inneholder filene som argument. Scriptet vil skrive ut alle lenkene som finnes i filene i mappen. Skriptet kan kjøres flere ganger hvis man ønsker å bytte ut flere strenger i lenkene.
4. Når man er fornøyd med resultatet kan skriptet `url-validator.py` kjøres. Dette scriptet vil så langt det er mulig sjekke om lenkene er gyldige. Resultatet skrives til en fil som heter url_info.json slik at man kan verifisere lenkene manuelt.

Lykke til! 🤩