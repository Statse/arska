# Arskan käyttöönotto ChatGPT:ssä ja Claudessa

Arska on ohjeista koostuva skill-kokoelma. Tämä ohje koskee viikkosuunnittelua. Yhden reseptin tuontiin, suomentamiseen ja mittamuunnoksiin on [oma reseptiskillin ohje](reseptit.md). Ohjeet sopivat molemmille palveluille, mutta käyttöönoton tapa eroaa. Näitä polkuja ei ole testattu kirjautuneilla ChatGPT- ja Claude-tileillä; palvelukohtaiset vaiheet on tarkistettu virallisista ohjeista 4.10.2026.

## ChatGPT: käyttö projektissa

ChatGPT-projekti kokoaa tiedostot ja projektiohjeet yhteen ja käyttää niitä projektin keskusteluissa. Tässä käyttötavassa skilli on projektin ohjeaineistoa. [Virallinen projektiohje](https://learn.chatgpt.com/docs/projects).

1. Lataa GitHubissa repo valitsemalla **Code → Download ZIP** ja pura se.
2. Luo ChatGPT:ssä uusi projekti nimeltä **Arska**.
3. Lisää projektin tiedostoihin/lähteisiin nämä kolme tiedostoa:
   - `viikkosuunnittelu/SKILL.md`
   - `viikkosuunnittelu/references/asetukset.md`
   - `viikkosuunnittelu/references/ruoat.md`
4. Lisää projektin ohjeisiin seuraava teksti:

```text
Olet Arska, arjen suunnitteluassistenttini. Kun pyydän viikkosuunnittelua,
lue projektin SKILL.md ja noudata sen työnkulkua. Lue myös asetukset.md
ja ruokien suunnittelussa ruoat.md. SKILL.md:n references/-viittaukset
tarkoittavat näitä projektin tiedostoja.

Keskustele suomeksi ja kysy puuttuvat tiedot vähän kerrallaan.
Käytä tässä projektissa antamiani henkilökohtaisia asetuksia.
Kerro, jos jokin tiedosto, kalenteri tai reseptilähde ei ole saatavilla.
Älä luo tai muuta kalenteritapahtumia tai lähetä kutsuja ennen kuin
olen hyväksynyt konkreettisen suunnitelman ja kutsujen vastaanottajat.
```

5. Aloita uusi keskustelu projektin sisällä. Anna alla olevat aloitustiedot ja kirjoita **“Suunnitellaan ensi viikko.”**

Kokeilua varten voit myös liittää samat tiedostot yksittäiseen keskusteluun ja pyytää käyttämään niitä viikkosuunnitteluun. Projekti helpottaa toistuvaa käyttöä.

### ChatGPT:n varsinainen skill-käyttö

OpenAI tukee myös Agent Skills -muotoa. Itsenäisiä skillejä voi käyttää työpöytäsovelluksessa ja Codexissa; webissä ja mobiilissa skillejä jaetaan myös pluginien kautta. ChatGPT:ssä käytössä olevan skillin voi valita `@`-maininnalla. [Virallinen skill-ohje](https://learn.chatgpt.com/docs/build-skills).

Tämä repo sisältää skillin tiedostot ja Claudeen sopivan ZIPin. Se ei vielä sisällä julkaistua ChatGPT-pluginia. Yllä oleva projektipolku ei edellytä Arskan plugin-julkaisua.

## Claude: tuo varsinainen skilli

1. Lataa [viikkosuunnittelu.zip](../downloads/viikkosuunnittelu.zip). GitHubissa avaa tiedosto ja valitse latauspainike / **Download raw file**.
2. Ota tarvittaessa **Settings → Capabilities → Code execution and file creation** käyttöön. Organisaatiotilillä myös ylläpitäjän asetukset voivat vaikuttaa saatavuuteen.
3. Avaa **Customize → Skills → + → Create skill → Upload a skill**.
4. Lataa ZIP ja kytke skilli päälle.
5. Aloita keskustelu: **“Käytä viikkosuunnittelu-skilliä. Suunnitellaan ensi viikko.”** Anna henkilökohtaiset aloitustiedot keskustelussa.

Vaiheet perustuvat [Clauden viralliseen skill-ohjeeseen](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Valikkojen nimet voivat muuttua.

ZIPissä on yksi skill-kansio ja sen tarvitsemat viitetiedostot. Koko GitHub-repon ZIP ei ole sama asia kuin yhden skillin tuontipaketti. [Clauden pakkausohje](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

```text
viikkosuunnittelu.zip
└── viikkosuunnittelu/
    ├── SKILL.md
    └── references/
        ├── asetukset.md
        └── ruoat.md
```

## Kalenteri ja reseptit: erillinen käyttöönotto

Skill ei sisällä kirjautumistietoja eikä anna itsestään pääsyä palveluihin.

Voit aloittaa ilman yhteyksiä ja antaa tiedot keskustelussa. Kalenteriyhteyden avulla tekoäly voi lukea sovitut menot. Notion-yhteyttä voi käyttää omien reseptien hakemiseen. Sähköpostia ei tarvita tämän taidon käyttöön.

- **ChatGPT:** yhdistä käyttämäsi kalenteripalvelu sovelluksen Plugins-näkymässä, jos integraatio on tililläsi saatavilla. Saatavuus riippuu tilistä ja työtilan asetuksista. [Virallinen ChatGPT-ohje](https://learn.chatgpt.com/docs/use-chatgpt).
- **Claude:** yhdistä Google Calendar connector-asetuksissa. Clauden Google Workspace -yhteys tukee tapahtumien lukemista, luontia, muokkausta ja toistuvia tapahtumia. [Virallinen integraatio-ohje](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors).
- **Reseptit:** yhdistä oma reseptilähteesi, kuten Notion, tai lataa reseptit tiedostoina. Anna linkki tai tunniste yksityisessä keskustelussa.

Varmista käytössä olevat toiminnot ennen ensimmäistä kalenteriin vientiä. Voit pyytää:

```text
Tarkista, pääsetkö lukemaan ensi viikon tapahtumat kalenteristani.
Kerro myös, onko käytössäsi tapahtumien luonti, kutsut ja toistuvuus.
Älä vielä luo tai muuta mitään.
```

Jos yhteyttä tai kirjoitusoikeuksia ei ole, Arska voi tehdä suunnitelman antamiesi tietojen pohjalta. Lisää tapahtumat silloin itse kalenteriin. Skill ei voi ottaa käyttöön puuttuvia kirjoitustoimintoja.

### Notion omaksi muistiksi ja muistioksi

Voit tehdä Notioniin oman Arska-sivun ja sen alle esimerkiksi reseptikokoelman, arjen asetukset sekä hyväksytyt suunnitelmat ja kauppalistat. Tämä on ehdotus omaan käyttöösi; repo ei vielä sisällä valmista Notion-pohjaa.

Anna assistentille linkit sivuihin, joita haluat sen käyttävän, ja varmista pääsy niihin. Kerro esimerkiksi:

```text
Reseptini ovat tällä Notion-sivulla: [oma linkki].
Käytä sitä ruokien suunnittelussa.
Kysy erikseen ennen uusien reseptien tai kauppalistan tallentamista.
```

Notionin sivuja voi käyttää tavallisina muistiinpanoina ilman Notion AI:ta. Tallennus ei tapahdu automaattisesti: pyydä sitä erikseen ja varmista, että assistentilla on siihen tarvittava toiminto.

## Aloitustiedot ensimmäiselle viikolle

Kopioi ja täydennä tarpeelliset kohdat yksityisessä keskustelussa:

```text
Suunnitellaan ensi viikko.

Aikavyöhykkeeni:
Kalenterit, joita käytetään, ja uusien tapahtumien kohdekalenteri:
Työpäivät ja työajat:
Etäpäivät ja työmatkan kesto:
Yhteiset tapahtumat ja niihin kutsuttavat:
Mahdolliset hoitorutiinit ja niiden ajat:
Liikunta- ja harrastustavoitteet:
Ruokailijoiden määrä, ruokarajoitteet ja reseptilähde:
Tälle viikolle jo sovitut menot, jotka eivät näy kalenterissa:
Toive vapaille illoille:
```

Kaikkea ei tarvitse täyttää: Arska kysyy olennaiset puuttuvat tiedot. Pidä omat osoitteet ja tunnisteet poissa julkisesta GitHub-reposta.

## Päivittäminen

Kun skill muuttuu, korvaa ChatGPT-projektin vanhat tiedostot uusilla. Claudessa tuo päivitetty skill-paketti palvelun käyttöliittymän kautta ja varmista, että oikea versio on käytössä. GitHubiin tehty muutos ei automaattisesti päivitä kopioituja tiedostoja.

Ylläpitäjälle: rakenna latauspaketti uudelleen skill-tiedostojen muutosten jälkeen. Repon juuressa PowerShellillä:

```powershell
Compress-Archive -Path ./viikkosuunnittelu -DestinationPath ./downloads/viikkosuunnittelu.zip -Force
```
