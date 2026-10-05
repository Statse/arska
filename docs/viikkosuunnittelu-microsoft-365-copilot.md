# Viikkosuunnittelu käyttöön Microsoft 365 Copilotissa

Tämä ohje on **Microsoft 365 Copilot -sovellukselle**, jossa käytät esimerkiksi työtiliä ja Microsoft 365:n palveluita. Tavallisen Copilot-sovelluksen ohje on [täällä](viikkosuunnittelu-copilot.md).

## Luo oma apuri

Oma apuri eli agentti säilyttää ohjeensa tulevia keskusteluja varten. Sen luominen riippuu tilistä, lisenssistä ja työpaikan asetuksista. Jos **Uusi agentti / New agent** ei näy, käytä alempana olevaa keskusteluvaihtoehtoa.

1. Avaa [viikkosuunnittelutiedosto](../downloads/laari-viikkosuunnittelu.txt) ja paina oikean yläkulman latausnuolta (**Download raw file**). Tiedoston nimi on **laari-viikkosuunnittelu.txt**.
2. Avaa Microsoft 365 Copilot ja valitse **Uusi agentti / New agent**. Jos toimintoa ei löydy sovelluksesta, kokeile [Microsoft 365 Copilotin selainversiota](https://m365.cloud.microsoft).
3. Valitse **Skip to configure** tai avaa **Configure**-välilehti. Anna nimeksi **Laari – viikkosuunnittelu**.
4. Kopioi **Ohjeet / Instructions** -kenttään tämä teksti:

```text
Autat seuraavan viikon menojen, ruokien ja liikunnan suunnittelussa.
Keskustele suomeksi ja kysy puuttuvat tiedot vähän kerrallaan.
Käytä laari-viikkosuunnittelu.txt-tiedoston suunnitteluperiaatteita,
ruokien valintaohjeita ja kauppalistan laskentaohjeita.
Varmista viikon päivämäärät ja aikavyöhyke. Jos kalenteria ei ole
käytettävissä, pyydä sovitut menot käyttäjältä. Älä väitä lukeneesi sitä.
Huomioi työ, siirtymät, kotirutiinit, ruokarajoitteet ja palautuminen.
Älä oleta perhettä, lemmikkiä tai harjoitusohjelmaa. Jätä vapaa-aikaa.
Näytä luonnos päivä kerrallaan ja tarkista päällekkäisyydet ja kuormitus.
Erota sovitut menot ehdotuksista sekä tarkistetut reseptit arvioista.
Laske kauppalista ruokailijoiden ja valmistettavien erien mukaan;
älä laske tähdeateriaa uutena eränä. Älä keksi puuttuvia ainesmääriä.
Pyydä hyväksyntä ennen kalenterimuutoksia tai kutsujen lähettämistä.
Reseptien ja kauppalistan tallennus vaatii myös luvan. Tee muutoksia vain,
jos käytettävissä on siihen sopiva työkalu, ja tarkista onnistuminen.
Muuten anna suunnitelma kopioitavana äläkä väitä tallentaneesi sitä.
```

5. Lisää lataamasi **laari-viikkosuunnittelu.txt** kohtaan **Tietämys / Knowledge** tiedoston lataustoiminnolla. Odota, että lataus valmistuu. Tiedosto sisältää apurin tausta-aineiston; edellisen kohdan teksti ohjaa apurin toimintaa.
6. Kokeile apuria **Try it** -välilehdellä alla olevalla viestillä:

```text
Suunnitellaan ensi viikon menot, ruoat ja treenit.
Kysy tarvittavat tiedot vähän kerrallaan.
```

7. Tarkista vastaus ja viimeistele apurin luonti näkymän luonti- tai tallennuspainikkeella. Avaa jatkossa **Laari – viikkosuunnittelu** Microsoft 365 Copilotin agenttiluettelosta.

Kerro viikon sovitut menot itse, jos Copilot ei pääse kalenteriisi. Saat suunnitelman ja kauppalistan keskusteluun. Tämä käyttöönotto ei itsessään anna oikeutta lukea tai muuttaa kalenteria. Voit kopioida hyväksymäsi menot kalenteriin itse.

## Jos oman apurin luominen ei ole käytettävissä

Avaa ladattu **laari-viikkosuunnittelu.txt** Muistiossa ja kopioi sen koko sisältö uuteen Microsoft 365 Copilot -keskusteluun. Lähetä perään:

```text
Noudata edellä liittämäni Laari-ohjeen sisältöä tässä keskustelussa.
Suunnitellaan ensi viikon menot, ruoat ja treenit.
Kysy tarvittavat tiedot vähän kerrallaan.
```

Jatka samassa keskustelussa. Uudessa keskustelussa liitä ohje uudelleen. Tämä vaihtoehto ei luo pysyvää apuria.

[Microsoftin ohje oman agentin luomiseen](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) ja [tiedostojen lisäämiseen](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge). Painikkeiden nimet voivat vaihdella kielen ja version mukaan.
