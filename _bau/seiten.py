"""Baut die drei Firmenfitness-Seiten für courtdesk.de aus einer gemeinsamen Vorlage."""
import json, html, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://www.courtdesk.de"
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, "base.css")).read()
ZAEHLER = open(os.path.join(HERE, "zaehler.html")).read().strip()
CSS += """
  .crumbs { margin: 0 0 1.4rem; font: 500 .74rem/1.4 var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--steel); }
  .crumbs a { color: var(--steel); text-decoration: none; }
  .crumbs a:hover { color: var(--white); }
  .crumbs span { margin-inline: .5rem; color: var(--signal); }
  ol.steps { list-style: none; counter-reset: s; padding: 0; margin: 1.2rem 0 1rem; }
  ol.steps li { counter-increment: s; position: relative; padding: 0 0 1.1rem 3.2rem; margin: 0; max-width: 64ch; }
  ol.steps li::before { content: counter(s, decimal-leading-zero); position: absolute; left: 0; top: .15rem; font: 500 .8rem/1 var(--mono); letter-spacing: .08em; color: var(--signal); }
  ol.steps b { color: var(--white); font-weight: 600; }
  .split { display: grid; gap: 1.4rem; margin: 1.2rem 0 1rem; }
  @media (min-width: 700px) { .split { grid-template-columns: 1fr 1fr; } }
  .card { border: 1px solid var(--rule); padding: 1.2rem 1.3rem .4rem; }
  .card h3 { margin-top: 0; font: 500 .78rem/1.3 var(--mono); letter-spacing: .1em; text-transform: uppercase; color: var(--steel); }
  .card.on h3 { color: var(--signal); }
  pre { margin: 1rem 0 1.2rem; padding: 1rem 1.1rem; border: 1px solid var(--rule); background: #0b0c0d; color: var(--ink); font: 400 .8rem/1.6 var(--mono); overflow-x: auto; white-space: pre; }
  .faq details { border-bottom: 1px solid var(--rule); }
  .faq details:first-of-type { border-top: 1px solid var(--rule); }
  .faq summary { list-style: none; cursor: pointer; display: flex; justify-content: space-between; gap: 1rem; padding: 1.05rem 0; font: 600 1rem/1.4 var(--sans); color: var(--white); }
  .faq summary::-webkit-details-marker { display: none; }
  .faq summary::after { content: "+"; font: 400 1.3rem/1 var(--mono); color: var(--signal); flex: none; }
  .faq details[open] summary::after { content: "\\2212"; }
  .faq details p { padding-bottom: .4rem; }
  .next { display: grid; gap: 1rem; margin: 1.2rem 0; }
  @media (min-width: 700px) { .next { grid-template-columns: 1fr 1fr; } }
  .next a { display: block; border: 1px solid var(--rule); padding: 1.2rem 1.3rem; text-decoration: none; transition: border-color .2s; }
  .next a:hover { border-color: var(--signal); }
  .next b { display: block; color: var(--white); font: 700 1.05rem/1.3 var(--head); letter-spacing: .04em; text-transform: uppercase; margin-bottom: .4rem; }
  .next span { color: var(--ink); font-size: .95rem; }
  .tm { margin-top: 2.4rem; }
"""

LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="8.5" y="3.5" width="15" height="25" fill="none" stroke="#f4f5f6" stroke-width="1.8"/><line x1="4" y1="16" x2="28" y2="16" stroke="#ff4d2e" stroke-width="2.2"/><circle cx="16" cy="16" r="2.6" fill="#ff4d2e"/></svg>'
TM = "NoctaTec und CourtDesk sind Marken der TF Vespasian Vermögensverwaltungs-GmbH. WhatsApp, EGYM Wellpass, Hansefit, Epassi und Playtomic sind Marken ihrer jeweiligen Inhaber. CourtDesk steht in keiner Verbindung zu diesen Unternehmen und wird nicht von ihnen gefördert."


def faq_html(faq):
    out = ['<div class="faq">']
    for q, a in faq:
        out.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    out.append("</div>")
    return "\n".join(out)


def strip(t):
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", t))


def page(slug, title, desc, crumb, body, faq, parent=True):
    url = f"{BASE}/{slug}/"
    crumbs = [("Start", f"{BASE}/")]
    if parent and slug != "firmenfitness-automatisierung":
        crumbs.append(("Firmenfitness", f"{BASE}/firmenfitness-automatisierung/"))
    crumbs.append((crumb, url))
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": url, "url": url, "name": title, "description": desc,
             "inLanguage": "de-DE", "isPartOf": {"@type": "WebSite", "url": f"{BASE}/", "name": "CourtDesk"},
             "publisher": {"@id": f"{BASE}/#org"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faq]},
        ],
    }
    crumb_html = '<p class="crumbs">' + "<span>/</span>".join(
        f'<a href="{u.replace(BASE, "")}">{n}</a>' if u != url else n for n, u in crumbs) + "</p>"
    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="CourtDesk">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/og.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="CourtDesk: Weniger Tipparbeit. Mehr Zeit für deine Anlage. Chat-Ansicht einer Wellpass-Anmeldung.">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}/og.png">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-48.png" type="image/png" sizes="48x48">
<link rel="icon" href="/favicon-96.png" type="image/png" sizes="96x96">
<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
<link rel="manifest" href="/site.webmanifest">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap"><a class="brand" href="/" aria-label="CourtDesk, zur Startseite">{LOGO}CourtDesk</a></div></header>
<main><div class="wrap">
{crumb_html}
{body}
<h2 id="fragen">Häufige Fragen.</h2>
{faq_html(faq)}
<div class="actions">
  <a class="btn" href="/#kontakt">15-Minuten-Gespräch</a>
  <a class="btn ghost" href="/#video">Demo auf WhatsApp testen</a>
</div>
<p class="muted tm">{TM}</p>
</div></main>
<footer><div class="wrap"><a href="/">courtdesk.de</a><a href="/firmenfitness-automatisierung/">Firmenfitness</a><a href="/egym-wellpass-playtomic/">Wellpass</a><a href="/hansefit-epassi-playtomic/">Hansefit</a><a href="/whatsapp-assistent-padelhalle/">WhatsApp-Assistent</a><a href="/ticketsystem-padelhalle/">Ticketsystem</a><a href="/roadmap/">Roadmap</a><a href="/firmenfitness-automatisierung/#ratgeber">Ratgeber</a><a href="/#impressum">Impressum</a><a href="/datenschutz.html">Datenschutz</a></div></footer>
{ZAEHLER}
</body>
</html>
"""
    os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
    open(os.path.join(ROOT, slug, "index.html"), "w").write(doc)


# ---------- Säulenseite ----------
page(
    "firmenfitness-automatisierung",
    "Firmenfitness auf der Padelanlage automatisieren | CourtDesk",
    "Wellpass- und Hansefit-Anmeldungen per WhatsApp, mit Formatprüfung und täglicher Importdatei für Playtomic. Was CourtDesk übernimmt und was bei der Anlage bleibt.",
    "Firmenfitness",
    """<p class="status">Ratgeber für Anlagen</p>
<h1>Firmenfitness ohne Abtippen.</h1>
<p class="lead">Mitglieder von EGYM Wellpass und Hansefit bringen Spieler auf deine Plätze. Am Empfang bringen sie vor allem Tipparbeit. CourtDesk nimmt ihre Anmeldungen per WhatsApp entgegen, prüft die Angaben auf das richtige Format und schickt dir einmal am Tag eine Importdatei für Playtomic.</p>
<ul class="toc"><li><a href="#heute">Heute</a></li><li><a href="#ablauf">Ablauf</a></li><li><a href="#aufteilung">Wer macht was</a></li><li><a href="#anbieter">Je Anbieter</a></li><li><a href="#ratgeber">Ratgeber</a></li><li><a href="#fragen">Fragen</a></li></ul>

<h2 id="heute">Wo heute die Zeit hingeht.</h2>
<p>Bei jeder neuen Anmeldung wiederholt sich dasselbe. Name, E-Mail und TAN kommen über WhatsApp, Telefon oder am Tresen, oft in mehreren Nachrichten. Die E-Mail passt nicht zum Playtomic-Konto, also wird nachgefragt. Danach legt jemand den Spieler von Hand an und ordnet ihn der richtigen Kategorie zu. Aus der Praxis sind das rund drei Minuten pro Mitglied, bei unbemannten Anlagen landet die Arbeit abends beim Inhaber.</p>

<h2 id="ablauf">So läuft es mit CourtDesk.</h2>
<ol class="steps">
  <li><b>Der Spieler schreibt deiner Anlage auf WhatsApp</b> und wählt per Knopf seinen Anbieter.</li>
  <li><b>Er schickt Name und die E-Mail seines Playtomic-Kontos.</b> Der Assistent zeigt beides zur Kontrolle, der Spieler bestätigt oder korrigiert.</li>
  <li><b>Er schickt seine TAN oder ID.</b> Der Assistent prüft, ob sie das passende Format hat, und erinnert an den Check-in in der App des Anbieters.</li>
  <li><b>Einmal am Tag kommt die Importdatei per E-Mail,</b> mit allen neuen Anmeldungen und einer TAN-Liste.</li>
  <li><b>Du importierst die Datei in Playtomic.</b> Die Spieler landen in der Kategorie ihres Anbieters, für 15 Anmeldungen dauert das etwa eine Minute.</li>
</ol>

<h2 id="aufteilung">Was CourtDesk übernimmt und was bei dir bleibt.</h2>
<div class="split">
  <div class="card on"><h3>CourtDesk</h3><ul>
    <li>Anmeldung im Chat, rund um die Uhr</li>
    <li>Prüfung von Name, E-Mail und TAN-Format</li>
    <li>Tägliche Importdatei für Playtomic</li>
    <li>Antworten zu Rabatt und Check-in nach den Regeln deiner Anlage</li>
    <li>Übergabe an dein Team bei Sonderfällen</li>
  </ul></div>
  <div class="card"><h3>Anlage und Anbieter</h3><ul>
    <li>Prüfen, ob eine TAN gültig ist</li>
    <li>Den Import in Playtomic starten</li>
    <li>Check-in, den macht der Spieler in der App seines Anbieters</li>
    <li>Abrechnung mit Wellpass oder Hansefit, wie bisher</li>
  </ul></div>
</div>
<p>CourtDesk arbeitet neben Playtomic und ersetzt kein Buchungssystem. Es gibt keine offizielle Verbindung zu Playtomic, Wellpass oder Hansefit. Gerade deshalb bleibt die Kontrolle bei dir, denn in Playtomic landet nur, was du importierst.</p>

<h2 id="anbieter">Die Abläufe je Anbieter.</h2>
<div class="next">
  <a href="/egym-wellpass-playtomic/"><b>EGYM Wellpass</b><span>Anmeldung mit 9-stelliger TAN, Kategorie Wellpass in der Importdatei, Hinweis auf den Check-in in der Wellpass-App.</span></a>
  <a href="/hansefit-epassi-playtomic/"><b>Hansefit und Epassi</b><span>Anmeldung mit Mitglieds-ID, eigene Kategorie, und was gilt, wenn deine Anlage mehrere Anbieter hat.</span></a>
</div>

<h2 id="ratgeber">Ratgeber für den Alltag.</h2>
<div class="next">
  <a href="/playtomic-kundenimport/"><b>Playtomic-Kundenimport</b><span>Spieler per CSV-Datei anlegen und der richtigen Kategorie zuordnen. Spalten, Formate, typische Fehler.</span></a>
  <a href="/tennis-pickleball-firmenfitness/"><b>Tennis und Pickleball</b><span>Wellpass und Hansefit auf Tennis-, Pickleball- und gemischten Anlagen, die über Playtomic buchen.</span></a>
  <a href="/anlage-ohne-empfang/"><b>Anlage ohne Empfang</b><span>Wenn niemand am Tresen steht: wie Anmeldungen trotzdem vollständig ankommen.</span></a>
  <a href="/checkliste-firmenfitness/"><b>Checkliste Firmenfitness</b><span>Was in Playtomic, auf der Anlage und in der Kommunikation stehen sollte, bevor die ersten Mitglieder kommen.</span></a>
  <a href="/software-padelhalle/"><b>Software für Padelhallen</b><span>Buchung, Zutritt, Firmenfitness: welches Werkzeug welche Aufgabe übernimmt.</span></a>
  <a href="/whatsapp-assistent-padelhalle/"><b>WhatsApp-Assistent</b><span>Anmeldung, Fragen und Übergabe an dein Team: was Paola übernimmt und was nicht.</span></a>
  <a href="/spielerfragen-automatisch-beantworten/"><b>Spielerfragen beantworten</b><span>Öffnungszeiten, Parken, Leihschläger: die immer gleichen Fragen, rund um die Uhr beantwortet.</span></a>
  <a href="/zeitersparnis-firmenfitness-padelhalle/"><b>Beispielrechnung Zeitersparnis</b><span>Von 3 Minuten Handarbeit auf rund 20 Sekunden: der Rechenweg hinter „bis zu 90 %“.</span></a>
  <a href="/wellpass-hansefit-anmeldung-fehler/"><b>Typische Fehler bei der Anmeldung</b><span>Falsche E-Mail, Zahlendreher, falsche Kategorie: was bei der Registrierung hakt und was hilft.</span></a>
</div>""",
    [
        ("Brauchen wir dafür Personal am Empfang?",
         "Für Anmeldungen und Standardfragen nicht, beides läuft im Chat. Einmal am Tag lädt jemand die Importdatei in Playtomic hoch. Das geht auch vom Schreibtisch oder von zu Hause."),
        ("Ist CourtDesk direkt mit Playtomic verbunden?",
         "Nein. CourtDesk erstellt eine Datei für den Kundenimport von Playtomic. Gebucht wird weiter in Playtomic. Freie Plätze zeigt der Assistent nicht an. Er verlinkt auf die Buchungsseite deiner Anlage in Playtomic."),
        ("Wie läuft die Zuzahlung?",
         "CourtDesk wickelt keine Zahlungen ab. Der Rabatt hängt in Playtomic an der Kategorie, die mit dem Import gesetzt wird. Der Assistent erklärt Spielern vorab, welcher Rabatt für sie gilt und was sie dafür tun müssen."),
        ("Was passiert beim Check-in?",
         "Den Check-in macht der Spieler selbst in der App seines Anbieters. Der Assistent erinnert bei der Anmeldung daran und beantwortet Fragen dazu. In den Check-in greift CourtDesk nicht ein."),
        ("Prüft CourtDesk, ob eine TAN echt ist?",
         "Nein, nur das Format. Ob eine TAN gültig ist, siehst du wie bisher beim Anbieter. Die TAN-Liste in der täglichen Mail macht diesen Abgleich einfacher."),
        ("Was kostet das?",
         "Das klären wir in einem kurzen Gespräch, nachdem du die Demo gesehen hast. Für die ersten Anlagen gibt es Konditionen zum Start."),
    ],
)

# ---------- Wellpass ----------
page(
    "egym-wellpass-playtomic",
    "EGYM Wellpass und Playtomic | Anmeldung per WhatsApp | CourtDesk",
    "So melden sich Wellpass-Mitglieder auf deiner Padel- oder Tennisanlage per WhatsApp an. Mit TAN-Prüfung, Hinweis zum Check-in und Importdatei für Playtomic.",
    "EGYM Wellpass",
    """<p class="status">EGYM Wellpass</p>
<h1>Wellpass-Anmeldungen, fertig für Playtomic.</h1>
<p class="lead">Neue Wellpass-Mitglieder melden sich bei deiner Anlage per WhatsApp an, auch nachts und am Wochenende. Bei dir kommen die Daten geprüft und gesammelt an, bereit für den Import.</p>

<h2>Der Ablauf für Wellpass.</h2>
<ol class="steps">
  <li><b>Der Spieler tippt auf „Wellpass“.</b> Der Assistent fragt nach Vor- und Nachname und der E-Mail seines Playtomic-Kontos.</li>
  <li><b>Kontrolle vor dem Absenden.</b> Der Assistent zeigt Name, E-Mail und Anbieter, der Spieler bestätigt oder korrigiert.</li>
  <li><b>Die 9-stellige Wellpass-TAN.</b> Der Assistent nimmt nur Ziffern in der richtigen Länge an und fragt sonst freundlich nach.</li>
  <li><b>Bestätigung mit Hinweis.</b> Der Spieler erfährt, ab wann er mit Rabatt buchen kann, und dass er vor dem Spiel in der EGYM Wellpass App einchecken muss.</li>
  <li><b>Eintrag in der Importdatei.</b> Der Datensatz bekommt die Kategorie Wellpass und landet in der nächsten täglichen Mail.</li>
</ol>

<h2>So sieht der Eintrag aus.</h2>
<p>Die Spalten entsprechen dem Kundenimport von Playtomic. Bei der Einrichtung gleichen wir sie mit einer Beispieldatei deiner Anlage ab.</p>
<pre>name,email,phone_number,gender,birthdate,category_name,category_expires
Max Mustermann,max@mail.de,,,,Wellpass,</pre>

<h2>Was der Assistent Wellpass-Spielern beantwortet.</h2>
<ul>
  <li>Welcher Rabatt für sie gilt und wie oft</li>
  <li>Dass ohne Check-in in der Wellpass-App kein Rabatt möglich ist</li>
  <li>Ab wann die Freischaltung greift</li>
  <li>Wie sie ihr Playtomic-Konto anlegen, mit Links für iPhone und Android</li>
</ul>
<p>Die Antworten stammen aus den Regeln, die deine Anlage bei der Einrichtung festlegt. Was der Assistent nicht sicher weiß, gibt er an dein Team weiter.</p>

<h2>Was bei dir bleibt.</h2>
<p>Ob eine TAN gültig ist, prüfst du wie bisher bei Wellpass. Den Import startest du selbst in Playtomic. Die Abrechnung mit Wellpass ändert sich nicht.</p>
<p><a href="/firmenfitness-automatisierung/">Gesamtüberblick Firmenfitness</a> · <a href="/hansefit-epassi-playtomic/">Ablauf für Hansefit</a></p>""",
    [
        ("Was passiert, wenn die E-Mail nicht zum Playtomic-Konto passt?",
         "Der Assistent fragt ausdrücklich nach der E-Mail des Playtomic-Kontos und lässt sie vor dem Absenden bestätigen. Das fängt die häufigste Rückfrage am Empfang ab."),
        ("Der Spieler hat noch kein Playtomic-Konto. Was dann?",
         "Der Assistent schickt die Links zur Playtomic-App für iPhone und Android und erklärt, dass er sich mit derselben E-Mail anmelden soll."),
        ("Schreiben auch Spieler auf Englisch?",
         "Ja. Der Assistent antwortet in der Sprache der letzten Nachricht. Die Knöpfe und das Anmeldeformular bleiben deutsch."),
        ("Wie oft kommt die Importdatei?",
         "Einmal am Tag per E-Mail, mit allen neuen Anmeldungen und einer TAN-Liste für den Abgleich."),
    ],
)

# ---------- Hansefit / Epassi ----------
page(
    "hansefit-epassi-playtomic",
    "Hansefit und Epassi auf der Padelanlage | Anmeldung per WhatsApp | CourtDesk",
    "Hansefit-Mitglieder per WhatsApp anmelden, mit ID-Prüfung, eigener Kategorie und Importdatei für Playtomic. Auch für Anlagen mit Wellpass und Hansefit.",
    "Hansefit und Epassi",
    """<p class="status">Hansefit und Epassi</p>
<h1>Hansefit-Mitglieder anmelden, ohne abzutippen.</h1>
<p class="lead">Hansefit gehört zur Epassi-Gruppe, deshalb kennen Spieler beide Namen. Im Assistenten heißt der Knopf „Hansefit/Epassi“, damit jeder seinen Anbieter sofort findet.</p>

<h2>Der Ablauf für Hansefit.</h2>
<ol class="steps">
  <li><b>Der Spieler tippt auf „Hansefit/Epassi“</b> und schickt Name und die E-Mail seines Playtomic-Kontos.</li>
  <li><b>Kontrolle vor dem Absenden.</b> Der Assistent zeigt die Angaben, der Spieler bestätigt oder korrigiert.</li>
  <li><b>Die Mitglieds-ID.</b> Der Assistent prüft das Format und fragt bei Tippfehlern nach.</li>
  <li><b>Bestätigung mit den Regeln deiner Anlage,</b> etwa ab wann die Freischaltung greift und wie der Check-in läuft.</li>
  <li><b>Eintrag in der Importdatei</b> mit der Kategorie, die deine Anlage in Playtomic für Hansefit nutzt.</li>
</ol>

<h2>Wenn deine Anlage mehrere Anbieter hat.</h2>
<p>Viele Anlagen sind Partner von Wellpass und Hansefit, manche nur an einzelnen Standorten. Bei der Einrichtung legen wir fest, welche Anbieter deine Anlage annimmt. Der Spieler sieht nur diese Knöpfe, und jeder Datensatz bekommt automatisch die passende Kategorie. In der täglichen Mail stehen alle Anmeldungen zusammen.</p>

<h2>Was bei dir bleibt.</h2>
<p>Die Prüfung der ID beim Anbieter, der Import in Playtomic und die Abrechnung mit Hansefit laufen wie bisher. CourtDesk nimmt dir das Sammeln, Nachfragen und Abtippen ab.</p>
<p><a href="/firmenfitness-automatisierung/">Gesamtüberblick Firmenfitness</a> · <a href="/egym-wellpass-playtomic/">Ablauf für Wellpass</a></p>""",
    [
        ("Heißt es jetzt Hansefit oder Epassi?",
         "Hansefit gehört zur Epassi-Gruppe. Für deine Anlage ändert das am Ablauf nichts. Im Assistenten stehen beide Namen auf einem Knopf, damit Spieler nicht suchen müssen."),
        ("Wir sind nur Partner von Hansefit. Geht das trotzdem?",
         "Ja. Der Assistent zeigt nur die Anbieter, die deine Anlage annimmt."),
        ("Was ist mit Urban Sports Club?",
         "Das unterstützt CourtDesk noch nicht. Wenn du es brauchst, schick uns einen Funktionswunsch. Die nächsten Funktionen richten sich nach den Anlagen, die CourtDesk nutzen."),
        ("Kann ich die Kategorie in Playtomic selbst benennen?",
         "Ja. Wir übernehmen bei der Einrichtung den Namen, den deine Anlage in Playtomic schon nutzt, damit der Import ohne Nacharbeit klappt."),
    ],
)
exec(open(os.path.join(HERE, "ratgeber.py")).read())
exec(open(os.path.join(HERE, "seo_seiten.py")).read())
# SEO-Pflege: lastmod in sitemap.xml, llms.txt, robots.txt (Regel im Hub, seit 27.11.2026)
import subprocess
subprocess.run([sys.executable, os.path.join(HERE, "seo_pflege.py")], cwd=ROOT, check=False)
print("gebaut")
