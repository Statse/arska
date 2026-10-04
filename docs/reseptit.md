# Tuo resepti Arskalle

Anna reseptilinkki ja kerro, miten haluat mitat. Arska lukee reseptin, tekee siitä suomenkielisen version ja lisää alkuperäisen linkin loppuun.

```text
Tuo tämä resepti suomeksi ja muuta cupit desilitroiksi: [reseptilinkki]
```

Oletuksena saat Suomessa tavalliset mitat: dl, ml, l, g, kg, tl, rkl ja °C. Voit myös pyytää esimerkiksi kaikki nestemäärät millilitroina. Valmiiksi suomenkielinen resepti ja sen sopivat mitat säilytetään sellaisinaan.

## Käyttöönotto

**Claude:** lataa [reseptit.zip](../downloads/reseptit.zip), tuo se kohdassa Customize → Skills → + → Create skill → Upload a skill ja ota käyttöön. Tarvittaessa ota Code execution and file creation käyttöön asetuksista. [Virallinen ohje](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

**ChatGPT:** luo projekti nimeltä **Arska – reseptit** ja lisää sen lähteisiin `reseptit/SKILL.md` sekä `reseptit/references/mitat.md`. Lisää projektiohjeeksi:

```text
Kun annan reseptilinkin tai reseptin tekstinä, käytä projektin SKILL.md:n
reseptiohjeita. Sen references/mitat.md tarkoittaa projektin mitat.md-tiedostoa.
Kirjoita resepti suomeksi ja käytä oletuksena suomalaisia mittoja.
Säilytä alkuperäinen linkki aina reseptin lopussa.
Älä tallenna reseptiä ulkoiseen palveluun ilman pyyntöäni tai aiempaa lupaani.
Jos et saa linkin sisältöä luettua, pyydä minulta reseptin teksti.
```

Tämä käyttää skilliä projektin ohjeaineistona. Oma reseptiprojekti erottaa sen viikkosuunnittelun samannimisestä `SKILL.md`-tiedostosta. [Virallinen projektiohje](https://learn.chatgpt.com/docs/projects).

Linkistä tuonti tarvitsee verkkosivun lukemiseen sopivan työkalun. Jos sitä ei ole tai sivu ei aukea, voit liittää reseptin tekstinä ja antaa lähdelinkin erikseen. Skillin tuontia ei ole testattu kirjautuneilla Claude- ja ChatGPT-tileillä.

## Esimerkkipyyntöjä

- “Tuo tämä resepti: [linkki].”
- “Käännä suomeksi ja muuta nesteet millilitroiksi: [linkki].”
- “Muunna tämä resepti suomalaisiin mittoihin kuudelle hengelle: [linkki].”
- “Tämä on jo suomeksi. Säilytä resepti sellaisenaan ja lisää lähdelinkki loppuun: [linkki].”
- “Tuo tämä resepti ja tallenna se omaan Notion-reseptikokoelmaani: [linkki].”

Cupista saa desilitroja suoraan, kun cupin koko tunnetaan. Grammoiksi muuntaminen vaatii myös raaka-ainekohtaisen tiedon: jauhot ja öljy painavat eri määrän. Arska käyttää reseptin omia grammoja ensisijaisesti ja kertoo tarvittavat oletukset. Muunnosperiaatteet ja lähteet ovat [mittaohjeessa](../reseptit/references/mitat.md).

## Tallennus ja käyttö viikkosuunnittelussa

Ilman tallennuspyyntöä resepti tulee keskusteluun kopioitavaksi. Jos pyydät tallennusta, tarvitset yhteyden esimerkiksi Notioniin ja oman reseptikokoelman kohteen. Arska säilyttää lähdelinkin sekä reseptin lopussa että kokoelman lähdekentässä, jos sellainen on olemassa. Ilman toimivaa yhteyttä se kertoo, ettei tallennusta tehty.

Kun resepti on omassa kokoelmassasi, voit käyttää sitä myös viikkosuunnittelun ruokaehdotuksissa. Reseptiskilli toimii itsenäisesti eikä tarvitse viikkosuunnitteluskilliä, kalenteria tai sähköpostia.

## Paketin päivittäminen

Reseptiskillin tiedostojen muutosten jälkeen rakenna ZIP uudelleen repon juuressa PowerShellillä:

```powershell
Compress-Archive -Path ./reseptit -DestinationPath ./downloads/reseptit.zip -Force
```
