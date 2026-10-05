# Reseptit käyttöön Microsoft 365 Copilotissa

Tämä ohje on **Microsoft 365 Copilot -sovellukselle**, jossa käytät esimerkiksi työtiliä ja Microsoft 365:n palveluita. Tavallisen Copilot-sovelluksen ohje on [täällä](reseptit-copilot.md).

## Luo oma apuri

Oma apuri eli agentti säilyttää ohjeensa tulevia keskusteluja varten. Sen luominen riippuu tilistä, lisenssistä ja työpaikan asetuksista. Jos **Uusi agentti / New agent** ei näy, käytä alempana olevaa keskusteluvaihtoehtoa.

1. Avaa [reseptitiedosto](../downloads/laari-reseptit.txt) ja paina oikean yläkulman latausnuolta (**Download raw file**). Tiedoston nimi on **laari-reseptit.txt**.
2. Avaa Microsoft 365 Copilot ja valitse **Uusi agentti / New agent**. Jos toimintoa ei löydy sovelluksesta, kokeile [Microsoft 365 Copilotin selainversiota](https://m365.cloud.microsoft).
3. Valitse **Skip to configure** tai avaa **Configure**-välilehti. Anna nimeksi **Laari – reseptit**.
4. Kopioi **Ohjeet / Instructions** -kenttään tämä teksti:

```text
Autat reseptien kääntämisessä suomeksi ja mittojen muuntamisessa.
Keskustele suomeksi. Käytä laari-reseptit.txt-tiedoston mittataulukoita
ja reseptipohjaa. Lue tarvittavat kohdat ennen muunnoksia.
Säilytä ainekset, annosmäärä ja työvaiheet. Suosi lähteen omia metrisiä
määriä. Muunna oletuksena tilavuudet dl/ml/l, painot g/kg ja lämpötilat
Celsius-asteiksi. Älä muunna tilavuutta painoksi ilman ainekohtaista tietoa.
Kerro muunnosten oletukset. Jos linkki ei aukea, pyydä reseptin teksti.
Älä keksi puuttuvia tietoja. Lisää alkuperäinen reseptilinkki loppuun.
Tallenna resepti muualle vain käyttäjän pyynnöstä ja käytettävissä olevalla
työkalulla. Kerro, jos tallentaminen ei onnistu.
```

5. Lisää lataamasi **laari-reseptit.txt** kohtaan **Tietämys / Knowledge** tiedoston lataustoiminnolla. Odota, että lataus valmistuu. Tiedosto sisältää apurin tausta-aineiston; edellisen kohdan teksti ohjaa apurin toimintaa.
6. Kokeile apuria **Try it** -välilehdellä alla olevalla viestillä ja korvaa hakasulkeet reseptin linkillä:

```text
Tuo tämä resepti suomeksi ja muuta mitat suomalaisiksi: [reseptin linkki]
```

7. Tarkista vastaus ja viimeistele apurin luonti näkymän luonti- tai tallennuspainikkeella. Avaa jatkossa **Laari – reseptit** Microsoft 365 Copilotin agenttiluettelosta.

Saat reseptin suomeksi, tutut mitat ja alkuperäisen linkin loppuun. Jos Copilot ei saa sivua auki, kopioi reseptin teksti keskusteluun.

## Jos oman apurin luominen ei ole käytettävissä

Avaa ladattu **laari-reseptit.txt** Muistiossa ja kopioi sen koko sisältö uuteen Microsoft 365 Copilot -keskusteluun. Lähetä perään:

```text
Noudata edellä liittämäni Laari-ohjeen sisältöä tässä keskustelussa.
Tuo tämä resepti suomeksi ja muuta mitat suomalaisiksi: [reseptin linkki]
```

Jatka samassa keskustelussa. Uudessa keskustelussa liitä ohje uudelleen. Tämä vaihtoehto ei luo pysyvää apuria.

[Microsoftin ohje oman agentin luomiseen](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents) ja [tiedostojen lisäämiseen](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge). Painikkeiden nimet voivat vaihdella kielen ja version mukaan.
