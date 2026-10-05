# Reseptit käyttöön Claudessa

Tarvitset Claude-tilin. Tee käyttöönotto tietokoneen selaimessa.

1. [Lataa reseptiskilli](https://github.com/Statse/laari/raw/refs/heads/master/downloads/reseptit.zip). Säilytä ZIP-tiedosto sellaisenaan, älä pura sitä.
2. Avaa [Claude](https://claude.ai) ja kirjaudu sisään.
3. Valitse **Customize → Skills → + → Create skill → Upload a skill**.
4. Valitse lataamasi **reseptit.zip** ja kytke lisätty skilli päälle.
5. Aloita uusi keskustelu. Kopioi alla oleva viesti, vaihda hakasulkeiden tilalle reseptin linkki ja lähetä:

```text
Käytä reseptit-skilliä. Tuo tämä resepti suomeksi ja muuta mitat
suomalaisiksi: [reseptin linkki]
```

Saat reseptin suomeksi, mitat esimerkiksi desilitroina ja grammoina sekä alkuperäisen linkin reseptin loppuun. Jos Claude ei saa sivua auki, kopioi reseptin teksti keskusteluun.

**Skills ei näy?** Ota **Settings → Capabilities → Code execution and file creation** käyttöön ja yritä uudelleen. [Clauden oma ohje](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
