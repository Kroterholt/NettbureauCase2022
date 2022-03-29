# README
Jeg har fokusert mest på backend delen, siden det er der jeg er sterkest. Er likevel fornøyd med all koden jeg har laget, selv om jeg får feilmelding etter at skjemaet submittes i frontend delen (mistenker at dette ikke er min skyld). Koden skal være godt dokumentert her og i form av komentarer i selve filene, men bare kontakt meg om dere har spørsmål.

## Backend:
Filen verifyData.py svarer på problemstillingen i backend delen av casen.
Emailen som blir sendt etter at skjemaet er validert blir sendt fra en mail jeg lagde spesifikt for denne casen (nettbureauTest@gmail.com), passordet er nettbureau123. Hvis dere vil teste med en annen email kan dette lett byttes øverst i sendEmail() (emailen må godta tilgang til mindre sikke apper i konto innstillinger).

Programmet kan testes ved å kjøre komandoen <./verifyData.py "navn;emaill;telefon;postnummer;kommentar"> i cmd. De forskjellige feltene må godkjennes av programmet før en varsel-email sendes (se kommentar i koden for nøyaktige krav for godkjenning).

### Libraries:
* Pandas - python


### Tanker om neste steg:
Har ikke lagt til noen metoder for å stoppe spam her, siden det avhenger litt av hva skjemaet blir brukt til. 
Feks; Hvis det ikke skal være mulig å lagre flere like Emailer på serveren, kunne programmet sjekket om Emailen er lagret fra før av i valideringsprosessen. Jeg kunne også lagt in en sleep() metode for å sette ett maks intervall på emailer, dette er nok beste måten å stoppe et evt. DDOS angrep. Men jeg tenker i utgangspunktet det er mest effektivt å beskytte mot spam på client siden (utenom DDOS angrep).

Hvis dette systemt skal brukes i stor skala burde hvertfall Emails sendes fra en annen node, da dette steget bruker en del kjøretid. Hvis man i det hele tatt vil motta mail for hvert eneste skjema i så stor skala. 


## Frontend:
Filene som er relevante for frontend delen er index.html og script.js.
I script.js ligger js koden for validere feltene.

Hver gang skjemaet submittes får jeg feilmelding; "{"status":false,"message":"The request must be made to the exact url https:\/\/case.nettbureau.no\/submit\/"}". Jeg har ikke gjort veldig mye javascript tidligere, så er usikker på om feilen er på min side.

For å teste koden er det bare å åpne index.html og fylle ut feltene. Feltene må tilfredstille validerings kravene for å gå videre. Sjekk komentarer i script.js for å se nøyaktige krav. Kravene er de samme som i backend delen.

Jeg fant aldri skjemaene som skulle ligge på nettsidene deres. Så får ikke komentert på dette.

## Kilder:
* Postnummerregister.csv er lastet ned fra https://www.bring.no/tjenester/adressetjenester/postnummer, og endret for å passe programmet mitt.
* Brukt nkom for å finne ut hva godkjente telefon nummer i Norge er. https://www.nkom.no/telefoni-og-telefonnummer/telefonnummer-og-den-norske-nummerplan/alle-nummerserier-for-norske-telefonnumre
* Har tatt utgangspunkt i index.html og css filene fra githuben jeg fikk tilsendt.
* Brukt en del kode herfra for å sende mail via python: https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development