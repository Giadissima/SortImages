# Contribuzione

Ciao! Segui i seguenti passaggi per contribuire alla mia repository. Inoltre, per qualsiasi evenienza, puoi contattarmi su [Telegram](https://t.me/Giadissima1234).

## Processo di Pull Request

### Come effettuare il setup della repository

1) Fai un *fork* della repository, cliccando [qui](https://github.com/Giadissima1/SortImages/fork).

2) Effettua un *clone* della repository digitando il seguente comando:

   ```bash
   git clone https://github.com/Giadissima/SortImages
   ```

3. Collega la mia repository alla tua:

   ```
   git remote add upstream https://github.com/Giadissima/SortImages
   ```

4. Digita il seguente comando per verificare il corretto collegamento con la mia repository:

   ```bash
   git remote -v
   ```

​	Dovresti avere sia "origin" (il tuo fork) che "upstream" (la repository originale).

5. (Facoltativo) Crea un nuovo branch. Assicurati di essere nel branch giusto (ad esempio, il branch principale) e crea un nuovo branch per le tue modifiche:

   ```bash
   git checkout -b nome-del-tuo-branch
   ```

6. Ora puoi eseguire il codice e modificarlo.

### Come eseguire il codice

Trovi le istruzioni nel file [README.md](README.md).

### Come effettuare una Pull Request 

Una Pull Request (**PR**), è una richiesta di push del tuo codice sulla mia repository. Una volta effettuata, avrai bisogno della mia approvazione perché io accetti la modifica sulla mia repository. Nel caso non te la dia e non hai capito il motivo, non esitare a contattarmi. Segui i seguenti passaggi per effettuarne una PR:

- **Aggiorna il README.md** con i dettagli delle modifiche che hai effettuato.

- **Aumenta i numeri di versione nel README.md** alla nuova versione che rappresenterà questa Pull Request. Lo schema di versionamento è [SemVer](https://semver.org) (Major.Minor.Patch).

- **Controlla di avere il mio codice aggiornato sulla tua repository**, in caso contrario, consulta i passaggi [sottostanti](CONTRIBUTE.md#Aggiornamento del mio codice sulla tua repository).

- **Effettua il push delle tue modifiche sul tuo fork su GitHub:**

  ```bash
  git push origin nome-del-tuo-branch
  ```

- **Crea la PR su GitHub:**

  - Vai sulla pagina principale della tua repository su GitHub.
  - Cambia il branch in quello che hai usato per modificare il codice.
  - Clicca sul pulsante "Pull Request" e segui le istruzioni per creare la PR.

- **Compila il modulo di Pull Request:** Fornisci una descrizione chiara delle tue modifiche nel modulo di Pull Request. Puoi anche menzionare eventuali problemi (issues) correlati.

- **Attendi la revisione.** Revisionerò il tuo codice appena possibile, grazie di aver contribuito ❤

### Aggiornamento del mio codice sulla tua repository

Nel caso io avessi fatto qualche modifica dopo che hai effettuato un *fork* del programma, non sarai in grado di fare una pull request. Ecco i passaggi per aggiornare il tuo codice:

1. Assicurati di avere l'ultima versione del mio codice, facendo un *pull*:

   ```bash
   git pull upstream
   ```

2. Cambia al tuo branch principale (solitamente `main`):

   ```bash
   git checkout main
   ```

3. Unisci le modifiche dalla mia repository al tuo *fork*:

   ```bash
   git merge upstream/main
   ```

   Assicurati di sostituire `main` con il nome del tuo branch principale, se è diverso.

4. Risolvi eventuali conflitti di merging, se presenti.

5. Aggiorna il tuo fork sulla tua repository su GitHub:

   ```bash
   git push origin main
   ```