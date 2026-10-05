# Lomasuunnittelu käyttöön Claudessa

Tarvitset Claude-tilin. Tee käyttöönotto tietokoneen selaimessa.

1. [Lataa lomasuunnitteluskilli](https://github.com/Statse/laari/raw/refs/heads/master/downloads/lomasuunnittelu.zip). Säilytä ZIP-tiedosto sellaisenaan, älä pura sitä.
2. Avaa [Claude](https://claude.ai) ja kirjaudu sisään.
3. Valitse **Customize → Skills → + → Create skill → Upload a skill**.
4. Valitse lataamasi **lomasuunnittelu.zip** ja kytke lisätty skilli päälle.
5. Aloita uusi keskustelu ja lähetä tämä viesti. Täytä hakasulkeiden tilalle omat tietosi; voit jättää avoimet asiat pois:

```text
Käytä lomasuunnittelu-skilliä. Suunnitellaan loma kohteeseen [kohde].
Matkan ajankohta on [ajankohta] ja kesto [päivien määrä].
Kysy tarvittavat tiedot vähän kerrallaan.
```

Saat päiväkohtaisen lomasuunnitelman suoraan keskusteluun: kiinnostavat kohteet, ruokailut, siirtymät, lepo ja karttalinkit. Kerro kohde, ajankohta ja matkan kesto tai aloita pelkällä kohteella. Apuri kysyy puuttuvat tiedot vähän kerrallaan.

Voit pyytää muutoksia suunnitelmaan. Toiveiden tallentaminen esimerkiksi Notioniin on vapaaehtoista ja edellyttää toimivaa yhteyttä sekä lupaasi. Ilman sitä saat kopioitavan toiveprofiilin seuraavaa matkaa varten. PDF:n voi pyytää erikseen, jos palvelu tukee tiedostojen luomista. Suunnitelma ei tee varauksia puolestasi.

**Skills ei näy?** Ota **Settings → Capabilities → Code execution and file creation** käyttöön ja yritä uudelleen. [Clauden oma ohje](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
