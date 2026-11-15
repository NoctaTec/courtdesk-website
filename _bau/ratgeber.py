# Ratgeber-Seiten für courtdesk.de. Wird von seiten.py ausgeführt (page() kommt von dort).
# Inhaltliche Grenzen (Leon, 15.11.): keine direkte Playtomic-Verbindung, kein Check-in durch CourtDesk,
# keine Zahlungen, TAN/ID nur Formatprüfung, Urban Sports Club noch nicht unterstützt.

ZURUECK = '<p><a href="/firmenfitness-automatisierung/">Gesamtüberblick Firmenfitness</a> · <a href="/egym-wellpass-playtomic/">Ablauf für Wellpass</a> · <a href="/hansefit-epassi-playtomic/">Ablauf für Hansefit</a></p>'

# ---------- Playtomic-Kundenimport ----------
page(
    "playtomic-kundenimport",
    "Playtomic-Kundenimport per CSV: Spieler mit Kategorie anlegen | CourtDesk",
    "So importierst du Spieler per CSV in Playtomic Manager und ordnest sie einer Kategorie wie Wellpass oder Hansefit zu. Spalten, Datumsformat, typische Fehler.",
    "Playtomic-Kundenimport",
    """<p class="status">Ratgeber · Playtomic</p>
<h1>Spieler per CSV in Playtomic anlegen.</h1>
<p class="lead">Mit dem Kundenimport in Playtomic Manager legst du viele Spieler auf einmal an und gibst ihnen direkt eine Kategorie, etwa für Wellpass- oder Hansefit-Rabatte. Hier steht, worauf es bei der Datei ankommt.</p>

<h2>Wo der Import liegt.</h2>
<ol class="steps">
  <li><b>Kategorie zuerst anlegen.</b> Der Import ordnet nur Kategorien zu, die es in deiner Anlage schon gibt. Lege also zum Beispiel „Wellpass“ vorher an.</li>
  <li><b>Kunden, dann Importe, dann neue Kunden importieren.</b> Dort gibt es eine Beispieldatei. Lade sie einmal herunter und vergleiche die Spalten.</li>
  <li><b>Datei hochladen und prüfen.</b> Fehlerhafte Zeilen zeigt Playtomic an und bietet sie zum Herunterladen an, damit du sie gezielt korrigieren kannst.</li>
</ol>

<h2>Die Spalten.</h2>
<p>Pflicht sind Name und E-Mail. Alle anderen Spalten bleiben in der Datei stehen, auch wenn sie leer sind. Wer leere Spalten löscht, bekommt einen Fehler.</p>
<pre>name,email,phone_number,gender,birthdate,category_name,category_expires
Max Mustermann,max@mail.de,,,,Wellpass,</pre>
<ul>
  <li><b>email</b> muss die Adresse sein, mit der der Spieler sein Playtomic-Konto angelegt hat. Sonst landet der Rabatt nicht bei ihm.</li>
  <li><b>category_name</b> muss genau so geschrieben sein wie die Kategorie in deiner Anlage, inklusive Groß- und Kleinschreibung.</li>
  <li><b>category_expires</b> und <b>birthdate</b> stehen im Format JJJJ-MM-TT. Ein Ablaufdatum in der Vergangenheit lehnt Playtomic ab.</li>
  <li><b>phone_number</b> braucht die Vorwahl des Landes, in dem die Anlage liegt, in Deutschland also +49.</li>
</ul>
<p>Für Ketten mit mehreren Standorten gibt es eine eigene Beispieldatei mit Spalten je Anlage. Die Angaben hier beziehen sich auf den Import für eine einzelne Anlage. Maßgeblich ist immer die Beispieldatei in deinem Playtomic Manager.</p>

<h2>Die häufigsten Fehler.</h2>
<ul>
  <li>Die E-Mail gehört nicht zum Playtomic-Konto des Spielers, zum Beispiel die Firmenadresse statt der privaten.</li>
  <li>Die Kategorie heißt in der Datei „wellpass“, in Playtomic aber „Wellpass“.</li>
  <li>Die Datei wurde aus Excel mit Semikolon statt Komma gespeichert. Sicherer ist der Export als CSV mit Komma, etwa aus Google Tabellen.</li>
  <li>Eine Spalte fehlt, weil sie leer war und gelöscht wurde.</li>
</ul>

<h2>Wie CourtDesk dabei hilft.</h2>
<p>CourtDesk sammelt die Anmeldungen per WhatsApp und lässt den Spieler die E-Mail seines Playtomic-Kontos ausdrücklich bestätigen. Einmal am Tag bekommst du eine fertige Datei mit den richtigen Spalten und dem Kategorienamen deiner Anlage. Hochladen musst du sie selbst, eine direkte Verbindung zu Playtomic gibt es nicht.</p>
""" + ZURUECK,
    [
        ("Kann ich mit dem Import bestehende Spieler einer Kategorie zuordnen?",
         "Ja, über die E-Mail-Adresse. Entscheidend ist, dass sie genau zum Playtomic-Konto des Spielers passt."),
        ("Muss ich die Kategorie vorher anlegen?",
         "Ja. Der Import ordnet nur bestehende Kategorien zu. Der Name in der Datei muss genau dem Namen in Playtomic entsprechen."),
        ("Welches Datumsformat braucht Playtomic?",
         "JJJJ-MM-TT, also zum Beispiel 2026-12-31. Ein Ablaufdatum muss heute oder später liegen."),
        ("Was mache ich mit fehlerhaften Zeilen?",
         "Playtomic zeigt sie nach dem Hochladen an und bietet sie zum Herunterladen an. Korrigiere sie und lade nur diese Zeilen erneut hoch."),
    ],
)

# ---------- Tennis und Pickleball ----------
page(
    "tennis-pickleball-firmenfitness",
    "Wellpass und Hansefit für Tennis- und Pickleball-Anlagen mit Playtomic | CourtDesk",
    "Firmenfitness-Anmeldungen per WhatsApp für Tennishallen, Pickleball-Anlagen und gemischte Racket-Anlagen, die über Playtomic buchen. Ablauf und Grenzen.",
    "Tennis und Pickleball",
    """<p class="status">Ratgeber · Tennis und Pickleball</p>
<h1>Firmenfitness auch für Tennis und Pickleball.</h1>
<p class="lead">Playtomic ist nicht nur für Padel da. Viele Tennishallen und Pickleball-Anlagen buchen darüber, und viele davon sind Partner von Wellpass oder Hansefit. Die Anmeldung neuer Mitglieder ist dort dieselbe Tipparbeit wie auf jeder Padelanlage.</p>

<h2>Für welche Anlagen CourtDesk passt.</h2>
<ul>
  <li><b>Tennishallen und Tennisclubs,</b> die Plätze über Playtomic vermieten und Firmenfitness-Mitglieder annehmen</li>
  <li><b>Pickleball-Anlagen,</b> oft neu und häufig ohne festen Empfang</li>
  <li><b>Gemischte Racket-Anlagen</b> mit Padel, Tennis und Pickleball unter einem Dach</li>
</ul>
<p>Entscheidend ist nicht die Sportart, sondern der Ablauf: Spieler buchen über Playtomic, Firmenfitness-Mitglieder bekommen über eine Kategorie ihren Rabatt, und jemand muss sie dafür anlegen.</p>

<h2>Was bei gemischten Anlagen wichtig ist.</h2>
<p>Gilt der Rabatt für alle Sportarten oder nur für einzelne? Gibt es Zeiten, in denen er nicht gilt? Diese Regeln legt deine Anlage bei der Einrichtung fest. Der Assistent beantwortet die Fragen danach so, wie sie für deine Anlage gelten, und gibt alles Unklare an dein Team weiter.</p>

<h2>Was gleich bleibt.</h2>
<p>Der Spieler meldet sich per WhatsApp an, bestätigt die E-Mail seines Playtomic-Kontos und schickt seine TAN oder ID. CourtDesk prüft das Format und schickt dir einmal am Tag die Importdatei. Den Check-in macht der Spieler in der App seines Anbieters, den Import startest du in Playtomic.</p>
""" + ZURUECK,
    [
        ("Funktioniert CourtDesk auch ohne Padelplätze?",
         "Ja. CourtDesk hängt nicht an der Sportart, sondern an Playtomic und den Firmenfitness-Anbietern. Eine reine Tennis- oder Pickleball-Anlage nutzt denselben Ablauf."),
        ("Können für Tennis und Padel unterschiedliche Rabatte gelten?",
         "Das regelt deine Anlage in Playtomic und mit dem Anbieter. Der Assistent erklärt Spielern die Regeln, die du bei der Einrichtung hinterlegst."),
        ("Unterstützt CourtDesk Urban Sports Club?",
         "Noch nicht. Unterstützt werden EGYM Wellpass und Hansefit/Epassi. Wenn du Urban Sports Club brauchst, schick uns einen Funktionswunsch."),
    ],
)

# ---------- Anlage ohne Empfang ----------
page(
    "anlage-ohne-empfang",
    "Padelhalle ohne Empfang: Wellpass- und Hansefit-Anmeldungen trotzdem vollständig | CourtDesk",
    "Unbemannte Padel-, Tennis- oder Pickleball-Anlage? So kommen Firmenfitness-Anmeldungen auch ohne Personal am Tresen vollständig und geprüft an.",
    "Anlage ohne Empfang",
    """<p class="status">Ratgeber · Unbemannte Anlagen</p>
<h1>Kein Empfang, trotzdem keine Lücken.</h1>
<p class="lead">Viele Anlagen laufen mit Zugangscode und ohne festes Personal. Buchen und Bezahlen klappt über Playtomic. Neue Wellpass- und Hansefit-Mitglieder bleiben aber oft an einer Stelle hängen: Irgendwer muss ihre Daten sammeln, nachfragen und sie anlegen.</p>

<h2>Wo es ohne Empfang hakt.</h2>
<ul>
  <li>Anfragen kommen abends und am Wochenende, beantwortet werden sie oft erst Tage später.</li>
  <li>Angaben kommen verteilt über mehrere Nachrichten und sind unvollständig.</li>
  <li>Die E-Mail passt nicht zum Playtomic-Konto, und der Rabatt greift nicht.</li>
  <li>Die Arbeit landet beim Inhaber, nach Feierabend und neben dem eigentlichen Job.</li>
</ul>

<h2>Was CourtDesk dort übernimmt.</h2>
<ol class="steps">
  <li><b>Erreichbar rund um die Uhr.</b> Der Assistent antwortet sofort, auch nachts.</li>
  <li><b>Vollständige Angaben.</b> Name, Playtomic-E-Mail und TAN oder ID werden abgefragt und vor dem Absenden bestätigt.</li>
  <li><b>Antworten auf Standardfragen,</b> etwa zu Rabatt, Check-in und Buchung, nach den Regeln deiner Anlage.</li>
  <li><b>Eine Datei pro Tag.</b> Statt vieler Einzelnachrichten bekommst du eine Importdatei und erledigst alles in etwa einer Minute.</li>
  <li><b>Übergabe bei Sonderfällen.</b> Was der Assistent nicht sicher weiß, gibt er an dich weiter.</li>
</ol>

<h2>Was bei dir bleibt.</h2>
<p>Den Import in Playtomic startest du selbst, einmal am Tag, auch von zu Hause. Ob eine TAN gültig ist, prüfst du wie bisher beim Anbieter. Zutritt, Licht und Zahlungen steuert CourtDesk nicht.</p>
""" + ZURUECK,
    [
        ("Ersetzt CourtDesk ein Zutrittssystem?",
         "Nein. CourtDesk kümmert sich um Firmenfitness-Anmeldungen und Fragen im Chat. Zutritt, Licht und Zahlungen laufen über deine bestehenden Systeme."),
        ("Wie viel Zeit bleibt für mich übrig?",
         "Einmal am Tag den Import in Playtomic, für 15 Anmeldungen etwa eine Minute. Dazu Sonderfälle, die der Assistent an dich weitergibt."),
        ("Was ist, wenn ein Spieler etwas fragt, das der Assistent nicht weiß?",
         "Dann sagt er das offen und gibt die Frage an dein Team weiter, statt zu raten."),
    ],
)

# ---------- Checkliste ----------
page(
    "checkliste-firmenfitness",
    "Checkliste: Wellpass und Hansefit auf der Padel- oder Tennisanlage einführen | CourtDesk",
    "Was in Playtomic, auf der Anlage und in der Kommunikation stehen sollte, bevor die ersten Wellpass- und Hansefit-Mitglieder kommen. Checkliste für Anlagenbetreiber.",
    "Checkliste",
    """<p class="status">Ratgeber · Checkliste</p>
<h1>Bevor die ersten Mitglieder kommen.</h1>
<p class="lead">Die Partnerschaft mit Wellpass oder Hansefit ist unterschrieben. Damit die ersten Anmeldungen nicht im Chaos enden, hilft diese Liste. Sie gilt mit und ohne CourtDesk.</p>

<h2>In Playtomic.</h2>
<ul>
  <li>Je Anbieter eine Kategorie anlegen, etwa „Wellpass“ und „Hansefit“, mit dem passenden Rabatt.</li>
  <li>Festlegen, ob die Kategorie ein Ablaufdatum bekommt.</li>
  <li>Die Beispieldatei für den Kundenimport herunterladen und ablegen. Mehr dazu im <a href="/playtomic-kundenimport/">Ratgeber zum Kundenimport</a>.</li>
</ul>

<h2>Regeln, die du vorher entscheidest.</h2>
<ul>
  <li>Für welche Sportarten, Plätze und Zeiten gilt der Rabatt?</li>
  <li>Wie oft pro Woche oder Monat kann ein Mitglied ihn nutzen?</li>
  <li>Was passiert, wenn ein Spieler nicht eincheckt?</li>
  <li>Bis wann wird ein neues Mitglied freigeschaltet, am selben Tag oder am nächsten?</li>
</ul>

<h2>Auf der Anlage und online.</h2>
<ul>
  <li>Ein Aushang oder QR-Code am Eingang: „Wellpass oder Hansefit? So meldest du dich an.“</li>
  <li>Derselbe Hinweis auf der Website und im Playtomic-Profil der Anlage.</li>
  <li>Ein klarer Hinweis auf den Check-in in der App des Anbieters, vor jedem Spiel.</li>
</ul>

<h2>Im Ablauf.</h2>
<ul>
  <li>Ein fester Kanal für Anmeldungen statt Telefon, Tresen und Privat-WhatsApp gemischt.</li>
  <li>Immer die E-Mail des Playtomic-Kontos abfragen, nicht irgendeine.</li>
  <li>Ein fester Zeitpunkt am Tag, an dem neue Mitglieder angelegt werden.</li>
  <li>Eine Person, die Sonderfälle klärt.</li>
</ul>
<p>CourtDesk deckt den Kanal, die Abfrage und die tägliche Datei ab. Die Regeln und den Import behältst du in der Hand.</p>
""" + ZURUECK,
    [
        ("Brauche ich für jeden Anbieter eine eigene Kategorie?",
         "Das ist sinnvoll, weil Rabatte und Regeln je Anbieter unterschiedlich sein können. CourtDesk ordnet jede Anmeldung automatisch der passenden Kategorie zu."),
        ("Wo sollte der Hinweis zur Anmeldung stehen?",
         "Dort, wo Spieler suchen: am Eingang, auf der Website und im Playtomic-Profil der Anlage. Ein QR-Code, der direkt in den WhatsApp-Chat führt, ist der kürzeste Weg."),
    ],
)

# ---------- Software für Padelhallen ----------
page(
    "software-padelhalle",
    "Software für Padelhallen: Buchung, Zutritt und Firmenfitness im Überblick | CourtDesk",
    "Welche Software in einer Padelhalle welche Aufgabe übernimmt: Buchung mit Playtomic, Zutritt und Licht, Firmenfitness-Anmeldungen per WhatsApp mit CourtDesk.",
    "Software für Padelhallen",
    """<p class="status">Ratgeber · Software</p>
<h1>Welche Software was übernimmt.</h1>
<p class="lead">In einer Padelhalle arbeiten meist mehrere Systeme nebeneinander. Hier steht, wofür sie da sind und wo CourtDesk dazwischen passt. CourtDesk ist ein Dienst für Sportanlagen und ersetzt keines der anderen Systeme.</p>

<div class="split">
  <div class="card"><h3>Buchung und Bezahlung</h3><ul>
    <li>Plätze, Preise, Zahlungen, Kundenkonten</li>
    <li>In Deutschland oft Playtomic</li>
    <li>Kategorien für Rabatte, etwa für Firmenfitness</li>
  </ul></div>
  <div class="card"><h3>Zutritt und Technik</h3><ul>
    <li>Türcodes, Schlösser, Licht</li>
    <li>Wichtig für Anlagen ohne Personal</li>
    <li>Teils mit Playtomic gekoppelt, je nach Anbieter</li>
  </ul></div>
  <div class="card on"><h3>Firmenfitness-Anmeldung</h3><ul>
    <li>Wellpass- und Hansefit-Mitglieder per WhatsApp anmelden</li>
    <li>Name, Playtomic-E-Mail und TAN-Format prüfen</li>
    <li>Tägliche Importdatei für Playtomic</li>
  </ul></div>
  <div class="card"><h3>Abrechnung mit dem Anbieter</h3><ul>
    <li>Läuft direkt zwischen Anlage und Wellpass oder Hansefit</li>
    <li>Der Check-in passiert in der App des Anbieters</li>
  </ul></div>
</div>

<h2>Warum eine eigene Lösung für Firmenfitness.</h2>
<p>Buchungssysteme sind dafür gebaut, dass Spieler Plätze buchen. Die Anmeldung von Firmenfitness-Mitgliedern liegt dazwischen: Daten sammeln, nachfragen, abgleichen, anlegen. Genau diese Lücke füllt CourtDesk, ohne dass du dein Buchungssystem wechseln musst.</p>
""" + ZURUECK,
    [
        ("Muss ich Playtomic für CourtDesk ersetzen?",
         "Nein. CourtDesk arbeitet neben Playtomic. Gebucht wird weiter dort, CourtDesk liefert nur die Importdatei für neue Firmenfitness-Mitglieder."),
        ("Gibt es eine Schnittstelle zu Playtomic?",
         "Nein, keine offizielle. CourtDesk nutzt den Kundenimport, den Playtomic jeder Anlage anbietet. So bleibt die Kontrolle bei dir."),
        ("Für welche Sportarten eignet sich CourtDesk?",
         "Für alle Anlagen, die über Playtomic buchen und Firmenfitness-Mitglieder annehmen, vor allem Padel, Tennis und Pickleball."),
    ],
    parent=False,
)
