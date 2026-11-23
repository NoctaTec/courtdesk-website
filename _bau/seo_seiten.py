# Weitere Suchseiten für courtdesk.de (Stand 24.11.2026). Wird von seiten.py nach ratgeber.py ausgeführt (page() und ZURUECK kommen von dort).
# Grenzen wie in ratgeber.py: keine offizielle Playtomic-Verbindung, kein Check-in durch CourtDesk, keine Zahlungen,
# TAN/ID nur Formatprüfung, keine freien Plätze im Chat (nur Link zur Buchungsseite), Urban Sports Club noch nicht unterstützt.
# Zahlen immer als "bis zu" mit Rechenweg und genannter Basis. Kein Wort "Pilot", kein "Demo-Club".

WEITER = '<p><a href="/whatsapp-assistent-padelhalle/">WhatsApp-Assistent</a> · <a href="/spielerfragen-automatisch-beantworten/">Spielerfragen beantworten</a> · <a href="/zeitersparnis-firmenfitness-padelhalle/">Beispielrechnung Zeitersparnis</a> · <a href="/wellpass-hansefit-anmeldung-fehler/">Typische Fehler bei der Anmeldung</a></p>'

# ---------- WhatsApp-Assistent ----------
page(
    "whatsapp-assistent-padelhalle",
    "WhatsApp-Assistent für Padelhallen: Anmeldung und Fragen | CourtDesk",
    "Ein WhatsApp-Assistent für Padel-, Tennis- und Pickleballanlagen: nimmt Wellpass- und Hansefit-Anmeldungen entgegen, beantwortet Fragen rund um die Uhr und übergibt Sonderfälle an dein Team.",
    "WhatsApp-Assistent",
    """<p class="status">Produkt · WhatsApp</p>
<h1>Deine Halle antwortet immer. Auch nachts.</h1>
<p class="lead">Paola ist die KI-Assistentin von CourtDesk. Sie schreibt mit deinen Spielern auf WhatsApp, nimmt Firmenfitness-Anmeldungen entgegen, beantwortet die immer gleichen Fragen und holt dein Team nur dazu, wenn ein Mensch gebraucht wird.</p>

<h2>Was der Assistent übernimmt.</h2>
<div class="split">
  <div class="card on"><h3>Anmeldung</h3><ul>
    <li>Anbieter per Knopfdruck wählen, etwa Wellpass oder Hansefit/Epassi</li>
    <li>Name, E-Mail des Playtomic-Kontos und TAN oder ID abfragen</li>
    <li>Angaben vor dem Absenden bestätigen lassen</li>
    <li>Einmal am Tag eine fertige Importdatei per Mail</li>
  </ul></div>
  <div class="card on"><h3>Fragen</h3><ul>
    <li>Öffnungszeiten, Parken, Leihschläger, Duschen</li>
    <li>Antworten aus den Infos deiner Anlage</li>
    <li>Rund um die Uhr, auch am Wochenende</li>
    <li>In der Sprache des Spielers</li>
  </ul></div>
</div>

<h2>Warum WhatsApp.</h2>
<p>Deine Spieler schreiben dort, wo sie ohnehin sind. Es gibt keine App zum Installieren und kein Konto zum Anlegen. Ein QR-Code am Eingang oder ein Link auf deiner Website reicht, und der Chat ist offen. Für dich heißt das: ein fester Kanal statt Anrufen, Zetteln am Tresen und privaten Nachrichten, die sich über den Tag verteilen.</p>

<h2>Wenn ein Mensch gebraucht wird.</h2>
<p>Manches soll nicht automatisch laufen, etwa eine Gruppenanfrage oder eine Beschwerde. Schreibt ein Spieler „Mensch“ oder „Mitarbeiter“, fragt Paola nach dem Anliegen und der E-Mail-Adresse und legt ein Ticket mit eigener Nummer an. Bei dir kommt eine Mail an mit der Zusammenfassung, dem Kontakt und zwei Knöpfen zum Antworten, per E-Mail oder per WhatsApp, schon vorausgefüllt. So fragt dein Team nicht doppelt nach.</p>
<ol class="steps">
  <li><b>Der Spieler schreibt,</b> dass er einen Menschen sprechen möchte.</li>
  <li><b>Paola fragt nach</b> Anliegen und E-Mail-Adresse und bestätigt, dass sich jemand meldet.</li>
  <li><b>Dein Team bekommt ein Ticket</b> mit Nummer, Dringlichkeit, To-do und Kontaktdaten.</li>
</ol>

<h2>Offen mit der KI.</h2>
<p>Paola sagt von Beginn an, dass sie eine KI-Assistentin ist. Ihre Zusammenfassungen in den Tickets sind als KI-Zusammenfassung gekennzeichnet, der Verlauf steht darunter, damit dein Team alles prüfen kann. Hinweise zum Datenschutz stehen in der <a href="/datenschutz-whatsapp.html">Datenschutzerklärung zum WhatsApp-Chat</a>.</p>

<h2>Was der Assistent nicht tut.</h2>
<ul>
  <li>Er bucht keine Plätze und nimmt keine Zahlungen an. Gebucht wird weiter in Playtomic, er verlinkt auf die Buchungsseite deiner Anlage.</li>
  <li>Er checkt niemanden ein. Den Check-in macht der Spieler in der App seines Anbieters.</li>
  <li>Er prüft das Format von TAN oder ID, nicht ob sie gültig sind.</li>
</ul>
<p>Mehr zum Ablauf der Anmeldung steht im <a href="/firmenfitness-automatisierung/">Überblick zur Firmenfitness-Automatisierung</a>.</p>
""" + WEITER,
    [
        ("Brauchen meine Spieler eine App?",
         "Nein. Sie schreiben über WhatsApp, das fast jeder schon nutzt. Es gibt keine Installation und kein Login."),
        ("Merken Spieler, dass sie mit einer KI schreiben?",
         "Ja. Paola stellt sich von Anfang an als KI-Assistentin deiner Anlage vor."),
        ("Was passiert bei Sonderfällen wie Gruppen oder Beschwerden?",
         "Der Spieler kann jederzeit einen Menschen verlangen. Dann entsteht ein Ticket, und dein Team bekommt eine Mail mit Zusammenfassung, Kontakt und vorausgefüllter Antwort."),
        ("Funktioniert das auch für Tennis- und Pickleball-Anlagen?",
         "Ja. Der Assistent arbeitet mit den Infos deiner Anlage, egal ob Padel, Tennis oder Pickleball, und mit dem Import von Playtomic."),
        ("Kann der Assistent freie Plätze anzeigen?",
         "Aktuell nicht. Er verlinkt auf die Buchungsseite deiner Anlage in Playtomic."),
    ],
    parent=False,
)

# ---------- Spielerfragen automatisch beantworten ----------
page(
    "spielerfragen-automatisch-beantworten",
    "Spielerfragen automatisch beantworten: Öffnungszeiten, Parken & mehr | CourtDesk",
    "Öffnungszeiten, Parken, Leihschläger, Duschen: so beantwortet ein WhatsApp-Assistent die immer gleichen Fragen deiner Spieler rund um die Uhr, mit den Infos deiner Padel- oder Tennisanlage.",
    "Spielerfragen beantworten",
    """<p class="status">Ratgeber · Kundenservice</p>
<h1>Die immer gleichen Fragen. Einmal beantwortet.</h1>
<p class="lead">„Habt ihr sonntags offen?“, „Wo kann ich parken?“, „Gibt es Leihschläger?“ Solche Fragen kommen täglich, oft abends oder am Wochenende, wenn niemand am Tresen steht. Ein Assistent auf WhatsApp antwortet sofort und mit den Angaben deiner Anlage.</p>

<h2>Welche Fragen sich eignen.</h2>
<div class="split">
  <div class="card on"><h3>Gut automatisierbar</h3><ul>
    <li>Öffnungszeiten und Feiertage</li>
    <li>Anfahrt und Parkplätze</li>
    <li>Leihschläger, Bälle, Preise für Zubehör</li>
    <li>Umkleiden, Duschen, Gastronomie</li>
    <li>Regeln zu Wellpass, Hansefit und Check-in</li>
  </ul></div>
  <div class="card"><h3>Besser beim Team</h3><ul>
    <li>Gruppen, Turniere, Events</li>
    <li>Beschwerden und Erstattungen</li>
    <li>Alles, was eine Einzelfallentscheidung braucht</li>
  </ul></div>
</div>

<h2>So entstehen die Antworten.</h2>
<ol class="steps">
  <li><b>Du sagst uns, was gilt.</b> Zeiten, Preise, Parken, Regeln und Besonderheiten deiner Anlage.</li>
  <li><b>Wir richten es ein.</b> Der Assistent stützt seine Antworten auf diese Angaben.</li>
  <li><b>Änderungen schickst du uns.</b> Neue Öffnungszeiten oder Preise sind danach im Chat aktuell.</li>
</ol>
<p>Wer eine Frage stellt, die nicht automatisch laufen soll, kann jederzeit einen Menschen verlangen. Dann bekommt dein Team ein <a href="/whatsapp-assistent-padelhalle/">Ticket mit allen Angaben</a>.</p>

<h2>Beispielrechnung.</h2>
<p>Angenommen, bei dir kommen 10 Fragen am Tag an, und jede kostet im Schnitt 2 Minuten mit Zuhören, Antworten und Nachschauen. Das sind 20 Minuten am Tag, über einen Monat mit 30 Tagen rund 10 Stunden. Beantwortet der Assistent davon bis zu 70 % allein, sind das bis zu 7 Stunden im Monat. Wie viel es bei dir ist, hängt von deinen Fragen ab. Die <a href="/zeitersparnis-firmenfitness-padelhalle/">komplette Beispielrechnung</a> steht auf einer eigenen Seite, und im <a href="/#rechner">Rechner auf der Startseite</a> setzt du deine eigenen Werte ein.</p>
""" + WEITER,
    [
        ("Erfindet der Assistent Antworten?",
         "Der Assistent stützt sich auf die Angaben, die du für deine Anlage hinterlegt hast. Als KI kann er trotzdem Fehler machen, deshalb kann jeder Spieler jederzeit einen Menschen verlangen. Dann bekommt dein Team ein Ticket."),
        ("Antwortet der Assistent auch auf Englisch?",
         "Ja, er antwortet in der Sprache, in der der Spieler schreibt."),
        ("Wie aktuell sind Öffnungszeiten und Preise?",
         "So aktuell, wie du sie uns mitteilst. Änderungen schickst du uns, wir passen sie an."),
        ("Kann ich festlegen, was der Assistent beantwortet?",
         "Ja. Bei der Einrichtung besprechen wir, welche Themen er übernimmt und welche beim Team bleiben."),
    ],
    parent=False,
)

# ---------- Zeitersparnis, Beispielrechnung ----------
page(
    "zeitersparnis-firmenfitness-padelhalle",
    "Wie viel Zeit kostet Firmenfitness? Beispielrechnung für Padelhallen | CourtDesk",
    "Beispielrechnung: Wie viel Zeit Wellpass- und Hansefit-Anmeldungen sowie Spielerfragen in einer Padel- oder Tennisanlage kosten und wie viel davon eine Automatisierung per WhatsApp sparen kann.",
    "Beispielrechnung Zeitersparnis",
    """<p class="status">Rechenweg · Beispielrechnung</p>
<h1>Von 3 Minuten Handarbeit auf rund 20 Sekunden.</h1>
<p class="lead">Mit CourtDesk sparst du bis zu 90 % des Aufwands bei der Anmeldung neuer Firmenfitness-Mitglieder. Hier steht, woher die Zahl kommt, damit du sie mit deinen eigenen Werten nachrechnen kannst.</p>

<h2>Die Annahmen.</h2>
<ul>
  <li><b>Anmeldungen:</b> 15 neue Mitglieder pro Woche.</li>
  <li><b>Handarbeit je Anmeldung:</b> etwa 3 Minuten mit Zusammensuchen von Name, E-Mail und TAN, Rückfragen und Anlegen in Playtomic.</li>
  <li><b>Mit CourtDesk:</b> Die Spieler tippen ihre Daten selbst ein. Bei dir bleibt der Import der täglichen Datei, das sind etwa 20 Sekunden je Anmeldung.</li>
  <li><b>Fragen:</b> 10 Spielerfragen pro Tag, je 2 Minuten. Davon beantwortet der Assistent bis zu 70 % allein.</li>
  <li><b>Stundensatz:</b> 45 € für Inhaber oder Geschäftsführung, 18 € für das Team am Empfang.</li>
</ul>

<h2>Der Rechenweg.</h2>
<ol class="steps">
  <li><b>Aufwand je Anmeldung.</b> 3 Minuten sind 180 Sekunden. Bleiben 20 Sekunden, sind das rund 89 % weniger, also bis zu 90 %.</li>
  <li><b>Anmeldungen im Monat.</b> 15 pro Woche mal 4,33 Wochen sind rund 65 Anmeldungen. Mal 3 Minuten sind 195 Minuten, also gut 3 Stunden. Davon bis zu 90 % sind etwa 2,9 Stunden.</li>
  <li><b>Fragen im Monat.</b> 10 Fragen mal 2 Minuten mal 30 Tage sind 600 Minuten, also 10 Stunden. Davon bis zu 70 % sind 7 Stunden.</li>
  <li><b>Zusammen.</b> Rund 10 Stunden im Monat. Bei 45 € pro Stunde sind das rund 450 €, bei 18 € rund 180 €.</li>
</ol>
<pre>Anmeldungen   65 x 3 min = 195 min  -> bis zu 90 %  = 2,9 Std.
Fragen        300 x 2 min = 600 min -> bis zu 70 %  = 7,0 Std.
Zusammen      bis zu rund 10 Std. pro Monat</pre>

<h2>Was die Rechnung nicht zählt.</h2>
<ul>
  <li>Antworten nachts und am Wochenende, für die sonst niemand da ist.</li>
  <li>Anmeldungen, die nicht mehr liegen bleiben, weil sie sofort vollständig ankommen.</li>
  <li>Rückfragen, die entfallen, weil die E-Mail des Playtomic-Kontos im Chat bestätigt wird.</li>
</ul>
<p><b>Wichtig:</b> Das ist eine Modellrechnung mit Beispielwerten, keine Garantie. Bei dir können es mehr oder weniger Anmeldungen und Fragen sein. Der Stundensatz für die Geschäftsführung orientiert sich an einer Datev-Auswertung 2025 für Kleinstunternehmen, der Satz für den Empfang an Mindestlohn plus Abgaben für einen Minijob, gerundet. Setz deine Werte direkt im <a href="/#rechner">Rechner auf der Startseite</a> ein.</p>
""" + WEITER,
    [
        ("Woher kommt die Zahl „bis zu 90 %“?",
         "Aus einer Beispielrechnung: Von etwa 3 Minuten Handarbeit je Anmeldung bleiben rund 20 Sekunden für den Import der täglichen Datei. Das ist die Obergrenze, nicht die Zusage für jede Anlage."),
        ("Gilt das auch, wenn bei uns mehr Rückfragen anfallen?",
         "Dann ist die Handarbeit heute länger, und es gibt mehr zu sparen. Rechne mit deinen eigenen Minuten, der Rechenweg bleibt derselbe."),
        ("Spart CourtDesk Personal?",
         "CourtDesk nimmt Tipparbeit und Standardfragen ab. Was du mit der freien Zeit machst, entscheidest du."),
        ("Wo kann ich mit meinen eigenen Zahlen rechnen?",
         "Im Rechner auf der Startseite. Dort stellst du Anmeldungen, Minuten, Fragen und deinen Stundensatz selbst ein."),
    ],
)

# ---------- Fehler bei der Anmeldung ----------
page(
    "wellpass-hansefit-anmeldung-fehler",
    "Wellpass- und Hansefit-Anmeldung: typische Fehler vermeiden | CourtDesk",
    "Die häufigsten Fehler bei der Registrierung und Anmeldung von Wellpass-, Hansefit- und Epassi-Mitgliedern in Padel- und Tennisanlagen und wie du sie mit Playtomic-Import und WhatsApp vermeidest.",
    "Typische Fehler bei der Anmeldung",
    """<p class="status">Ratgeber · Fehler vermeiden</p>
<h1>Wo die Registrierung von Firmenfitness-Mitgliedern hakt.</h1>
<p class="lead">Wellpass-, Hansefit- und Epassi-Mitglieder melden sich bei dir an, und fast jede Anlage kennt dieselben Stolpersteine. Hier sind die häufigsten, und was dagegen hilft.</p>

<h2>Die häufigsten Fehler.</h2>
<ol class="steps">
  <li><b>Die falsche E-Mail.</b> Der Spieler gibt die Firmenadresse an, sein Playtomic-Konto läuft aber über die private. Der Rabatt kommt dann nicht an. <i>Dagegen hilft:</i> immer ausdrücklich nach der E-Mail des Playtomic-Kontos fragen und sie bestätigen lassen.</li>
  <li><b>Ein Zahlendreher bei der TAN oder ID.</b> Beim Abgleich mit dem Anbieter fällt es erst später auf. <i>Dagegen hilft:</i> das Format sofort prüfen. Bei der Wellpass-TAN sind das 9 Ziffern. Ob sie gültig ist, siehst du beim Anbieter.</li>
  <li><b>Die Kategorie heißt anders.</b> In der Datei steht „wellpass“, in Playtomic aber „Wellpass“. <i>Dagegen hilft:</i> bei der Einrichtung den Namen deiner Kategorie übernehmen. Mehr im <a href="/playtomic-kundenimport/">Ratgeber zum Kundenimport</a>.</li>
  <li><b>Die Datei hat das falsche Format.</b> Semikolon statt Komma oder eine fehlende leere Spalte. <i>Dagegen hilft:</i> immer dieselbe, getestete Vorlage mit allen Spalten.</li>
  <li><b>Doppelte Anmeldungen.</b> Ein Spieler schreibt zweimal oder über zwei Kanäle. <i>Dagegen hilft:</i> ein fester Kanal für Anmeldungen.</li>
  <li><b>Kein Check-in.</b> Der Rabatt greift nur, wenn der Spieler vor dem Spiel in der App des Anbieters eincheckt. <i>Dagegen hilft:</i> ein Hinweis in der Bestätigung, jedes Mal.</li>
  <li><b>Liegen gebliebene Anmeldungen.</b> Am Wochenende kommen Nachrichten an, am Montag sind sie untergegangen. <i>Dagegen hilft:</i> ein Assistent, der rund um die Uhr antwortet, und eine tägliche Sammeldatei.</li>
</ol>

<h2>Was CourtDesk dabei übernimmt.</h2>
<p>CourtDesk fragt Anbieter, Name, die E-Mail des Playtomic-Kontos und die TAN oder ID per WhatsApp ab, lässt den Spieler alles bestätigen und prüft das Format. Einmal am Tag bekommst du die Importdatei mit den richtigen Spalten und dem Namen deiner Kategorie, dazu eine TAN-Liste für den Abgleich. Den Import in Playtomic startest du selbst.</p>

<h2>Was bei dir bleibt.</h2>
<ul>
  <li>Die Prüfung, ob eine TAN oder ID gültig ist, beim Anbieter.</li>
  <li>Der Import in Playtomic und die Abrechnung mit Wellpass, Hansefit oder Epassi.</li>
  <li>Sonderfälle, die ein Mensch klären soll. Sie kommen als <a href="/whatsapp-assistent-padelhalle/">Ticket</a> bei deinem Team an.</li>
</ul>
<p>Eine Liste zum Abhaken vor dem Start findest du in der <a href="/checkliste-firmenfitness/">Checkliste Firmenfitness</a>.</p>
""" + WEITER,
    [
        ("Prüft CourtDesk, ob eine Wellpass-TAN gültig ist?",
         "Nein, nur das Format. Die Gültigkeit siehst du beim Anbieter. Die TAN-Liste in der täglichen Mail macht den Abgleich einfacher."),
        ("Warum kommt der Rabatt bei manchen Spielern nicht an?",
         "Meist passt die E-Mail in der Importdatei nicht zum Playtomic-Konto, oder der Spieler hat nicht in der App des Anbieters eingecheckt."),
        ("Gilt das auch für Hansefit und Epassi?",
         "Ja. Hansefit gehört zur Epassi-Gruppe, im Ablauf ändert das nichts. Im Chat stehen beide Namen auf einem Knopf."),
        ("Was ist mit Urban Sports Club?",
         "Das unterstützt CourtDesk noch nicht. Schick uns gern einen Funktionswunsch."),
    ],
)
