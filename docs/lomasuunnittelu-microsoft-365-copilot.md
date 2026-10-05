# Lomasuunnittelu käyttöön Microsoft 365 Copilotissa

Tämä ohje on **Microsoft 365 Copilot -sovellukselle**, jossa käytät esimerkiksi työtiliä ja Microsoft 365:n palveluita. Tavallisen Copilot-sovelluksen ohje on [täällä](lomasuunnittelu-copilot.md).

## Luo oma apuri

Oma apuri eli agentti säilyttää ohjeensa tulevia keskusteluja varten. Sen luominen riippuu tilistä, lisenssistä ja työpaikan asetuksista. Jos **Uusi agentti / New agent** ei näy, käytä alempana olevaa keskusteluvaihtoehtoa.

1. Avaa [lomasuunnittelutiedosto](../downloads/laari-lomasuunnittelu.txt) ja paina oikean yläkulman latausnuolta (**Download raw file**). Tiedoston nimi on **laari-lomasuunnittelu.txt**.
2. Avaa Microsoft 365 Copilot ja valitse **Uusi agentti / New agent**. Jos toimintoa ei löydy sovelluksesta, kokeile [Microsoft 365 Copilotin selainversiota](https://m365.cloud.microsoft).
3. Valitse **Skip to configure** tai avaa **Configure**-välilehti. Anna nimeksi **Laari – lomasuunnittelu**.
4. Kopioi **Ohjeet / Instructions** -kenttään tämä teksti:

```text
Autat käyttäjää suunnittelemaan hänelle sopivan loman.
Keskustele suomeksi ja kysy vain puuttuvat tiedot, 2–3 kysymystä kerrallaan.
Käytä laari-lomasuunnittelu.txt-tiedoston lomatoiveiden, kohdetutkimuksen,
karttalinkkien ja päiväohjelman ohjeita. Lue tarvittavat kohdat suunnittelussa.
Selvitä kohde, ajankohta, kesto, matkaseurue ja majoitusalue.
Selvitä kiinnostukset, ruokailutyyli ja budjetti, päivärytmi, liikkuminen,
lepopäivien tarve ja päiväretkitoiveet. Käytä vahvistettuja aiempia toiveita.
Tutki ajantasaiset kohde-, ravintola- ja siirtymätiedot, jos verkko on käytettävissä.
Erota lähteistä tarkistetut tiedot arvioista ja vielä tarkistettavista asioista.
Ryhmittele kohteet alueittain. Varaa aikaa ruokailuun, siirtymiin ja lepoon.
Näytä päiväkohtainen suunnitelma, karttalinkit, kuluarvio ja varattavat asiat
suoraan keskustelussa. Älä rakenna verkkosivua. Tee PDF vain pyynnöstä,
jos tiedostonluonti on käytettävissä; muuten anna kopioitava teksti.
Ehdota vapaaehtoista toiveprofiilin tallennusta esimerkiksi Notioniin.
Varmista tallennuksen sisältö, kohde ja lupa. Jatkuva päivityslupa kattaa vain
sovitut pysyvät mieltymykset. Ilman yhteyttä anna kopioitava profiili.
Älä väitä tallentaneesi tietoja tai luoneesi karttaa ilman onnistunutta toteutusta.
Älä tee varauksia, ostoja, kalenterimuutoksia tai lähetä viestejä ilman erillistä lupaa.
```

5. Lisää lataamasi **laari-lomasuunnittelu.txt** kohtaan **Tietämys / Knowledge** tiedoston lataustoiminnolla. Odota, että lataus valmistuu. Tiedosto sisältää apurin tausta-aineiston; edellisen kohdan teksti ohjaa apurin toimintaa.
6. Kokeile apuria **Try it** -välilehdellä alla olevalla viestillä. Täytä hakasulkeisiin omat tietosi; voit jättää avoimet asiat pois:

```text
Suunnitellaan loma kohteeseen [kohde]. Matkan ajankohta on [ajankohta]
ja kesto [päivien määrä].
Kysy tarvittavat tiedot vähän kerrallaan.
```

7. Tarkista vastaus ja viimeistele apurin luonti näkymän luonti- tai tallennuspainikkeella. Avaa jatkossa **Laari – lomasuunnittelu** Microsoft 365 Copilotin agenttiluettelosta.

Saat päiväkohtaisen lomasuunnitelman suoraan keskusteluun: kiinnostavat kohteet, ruokailut, siirtymät, lepo ja karttalinkit. Kerro kohde, ajankohta ja matkan kesto tai aloita pelkällä kohteella. Apuri kysyy puuttuvat tiedot vähän kerrallaan.

Voit pyytää muutoksia suunnitelmaan. Toiveiden tallentaminen esimerkiksi Notioniin on vapaaehtoista ja edellyttää toimivaa yhteyttä sekä lupaasi. Ilman sitä saat kopioitavan toiveprofiilin seuraavaa matkaa varten. PDF:n voi pyytää erikseen, jos palvelu tukee tiedostojen luomista. Suunnitelma ei tee varauksia puolestasi.

## Jos oman apurin luominen ei ole käytettävissä

Avaa ladattu **laari-lomasuunnittelu.txt** Muistiossa ja kopioi sen koko sisältö uuteen Microsoft 365 Copilot -keskusteluun. Lähetä perään:

```text
Noudata edellä liittämäni Laari-ohjeen sisältöä tässä keskustelussa.
Suunnitellaan loma kohteeseen [kohde]. Matkan ajankohta on [ajankohta]
ja kesto [päivien määrä].
Kysy tarvittavat tiedot vähän kerrallaan.
```

Jatka samassa keskustelussa. Uudessa keskustelussa liitä ohje uudelleen. Tämä vaihtoehto ei luo pysyvää apuria.

[Microsoftin ohje oman agentin luomiseen](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) ja [tiedostojen lisäämiseen](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge). Painikkeiden nimet voivat vaihdella kielen ja version mukaan.
