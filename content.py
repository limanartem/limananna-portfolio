"""Everything about the person. build.py renders it; nothing here is HTML.

Sections appear in the order of SECTIONS and only when listed, so a profile without
side projects or without an outcomes section simply leaves those entries out.
Each section entry: dict(id=..., type=<renderer>, nav=<nav label or None>, label=<numbered label>, **options).
Types: about, impact, experience, projects, gallery, publications, skills, contact.
"""
EMAIL = "limananna2004@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/anna-liman-a863981b3/"

PERSON = dict(
    name="Anna Liman", first="Anna", last="Liman", initials="AL",
    title="Anna Liman · Grafikdesignerin &amp; Medienfachwirtin",   # <title> and og:title (already HTML-escaped)
    description="Anna Liman, staatlich geprüfte Grafikdesignerin und Medienfachwirtin (Bachelor Professional) aus Walldorf. Arbeiten, Werdegang und Kontakt.",
    badge="Grafikdesignerin · Medienfachwirtin",   # small pill above the name; None hides it
    tagline="Gestaltung und Medienwirtschaft aus einer Hand.",
    lede="Staatlich geprüfte Grafikdesignerin mit Weiterbildung zur Medienfachwirtin (Bachelor Professional), beides an der Johannes-Gutenberg-Schule in Heidelberg.",
    meta=["Walldorf · Rhein-Neckar", "DE C2 · EN B2 · UA Muttersprache"],
    location="Walldorf",
    # profile links: (label, url, icon name from src/icons.json or None). The first is the primary button.
    links=[("E-Mail schreiben", f"mailto:{EMAIL}", None), ("LinkedIn", LINKEDIN, "LinkedIn")],
    hero_cta=("Arbeiten ansehen", "#arbeiten"),     # third hero button; None hides it
)

# German interface strings for the chassis (see UI_DEFAULTS in build.py)
UI = dict(
    lang='de', contact='Kontakt', today='heute', back_to_top='Nach oben ↑',
    education='Ausbildung', certifications='Zertifikate &amp; Weiterbildung', languages='Sprachen',
    view_full='Vergrößern', view_repo='Auf GitHub ansehen', private_repo='Privates Repository',
    prev_slide='Vorheriges Bild', next_slide='Nächstes Bild', go_slide='Zu Bild', screenshots='Bilder', photo='Foto',
    prev_image='Vorheriges Bild', next_image='Nächstes Bild', close='Schließen', image_viewer='Bildansicht',
    open_menu='Menü öffnen', close_menu='Menü schließen', main_nav='Hauptnavigation', technologies='Werkzeuge',
    theme='Farbschema', theme_system='Systemeinstellung', theme_light='Hell', theme_dark='Dunkel',
)

THEME = dict(
    scheme="light",           # "dark" | "light" | "system": what a first-time visitor gets
    accent_dark="#C9A6E0", accent_light="#6B3F8C",   # the lilac and aubergine of her CV
    display_font="Newsreader", body_font="Manrope", mono_font="DM Mono",
    google_fonts="family=Newsreader:opsz,wght@6..72,500;6..72,600;6..72,700&family=Manrope:wght@400;500;600&family=DM+Mono:wght@400;500",
)

HERO_PHOTOS = [('assets/hero/anna.webp', 'Porträt von Anna Liman')]
STATS = []
MARQUEE = []

SECTIONS = [
    dict(id="arbeiten", type="gallery", nav="Arbeiten", label="Arbeiten",
         heading="Ausgewählte Arbeiten",
         intro="Veg & Velvet, ein Café: Speisekarte und Startseite der Website. Zum Vergrößern ein Bild anklicken."),
    dict(id="ueber-mich", type="about", nav="Über mich", label="Über mich",
         heading="Gestalten und planen.",
         paragraphs=[
             "Ich bin <strong>staatlich geprüfte Grafikdesignerin</strong> (Johannes-Gutenberg-Schule Heidelberg, 2023) und habe an derselben Schule die Weiterbildung zur <strong>Medienfachwirtin (Bachelor Professional)</strong> gemacht. Ich bringe damit beides mit: das gestalterische Handwerk und den Blick dafür, wie Medienprojekte geplant und umgesetzt werden.",
             "Daneben habe ich anderthalb Jahre in einer Praxis für Gastroenterologie in Wiesloch gearbeitet, am Empfang und in der Betreuung von Patienten. Was ich mitbringe: Kommunikationsstärke, eine schnelle Auffassungsgabe und eine strukturierte Arbeitsweise.",
         ],
         facts=[("Abschlüsse", "Grafikdesignerin · Medienfachwirtin"), ("Sprachen", "Deutsch C2 · Englisch B2 · Ukrainisch"), ("Ort", "Walldorf, Rhein-Neckar")]),
    dict(id="werdegang", type="experience", nav="Werdegang", label="Werdegang", heading="Werdegang",
         start_label="2020 · Beginn der Ausbildung"),
    dict(id="kenntnisse", type="skills", nav="Kenntnisse", label="Kenntnisse", heading="Kenntnisse &amp; Sprachen"),
    dict(id="kontakt", type="contact", nav=None, label="Kontakt",
         heading="Lassen Sie uns <span class=\"accent\">sprechen.</span>",
         text="Ich freue mich über Nachrichten zu Stellen in Grafikdesign und Medien. Am besten erreichen Sie mich per E-Mail oder über LinkedIn.",
         buttons=[(EMAIL, f"mailto:{EMAIL}", None), ("LinkedIn", LINKEDIN, "LinkedIn")]),
]

GALLERY = [
    dict(src="assets/work/veg-velvet-menu.jpg", caption="Veg & Velvet: Speisekarte mit Getränken, Kuchen und Snacks", wide=True, tall=True),
    dict(src="assets/work/veg-velvet-website.jpg", caption="Veg & Velvet: Startseite der Website mit dem Sommer-Menü", wide=True, tall=True),
]

JOBS = [
 dict(logo='jgs', period='09/2025 – 07/2026', company='Johannes-Gutenberg-Schule', place='Heidelberg', current=False,
      role='Bachelor Professional: Medienfachwirtin',
      scope='Weiterbildung zur Medienfachwirtin.'),
 dict(logo='praxis', period='02/2024 – 08/2025', company='Praxis für Gastroenterologie', place='Wiesloch',
      role='Minijob: Empfang und Patientenbetreuung',
      scope='Anderthalb Jahre neben der Ausbildung.',
      points=['Aufnahme der Patienten an der Rezeption.',
              'Betreuung von Patienten und Überwachung während der Endoskopie.',
              'Aufbereitung medizinischer Geräte.']),
 dict(logo='jgs', period='09/2020 – 07/2023', company='Johannes-Gutenberg-Schule', place='Heidelberg',
      role='Staatlich geprüfte Grafikdesignerin',
      scope='Schulische Ausbildung zur Grafikdesignerin mit staatlicher Prüfung.'),
]
EARLIER = []
MONOGRAM = {'jgs': 'JGS', 'praxis': 'GE'}

SKILLS = [
    ("Stärken", ["Kommunikationskompetenz", "Schnelle Auffassungsgabe", "Strukturierte Arbeitsweise"]),
    ("Gestaltung", ["Adobe InDesign", "Adobe Illustrator", "Adobe Photoshop", "Procreate", "Figma (Grundkenntnisse)"]),
    ("Office", ["Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint"]),
]
EDUCATION = []          # shown in the Werdegang timeline instead
CERTIFICATIONS = []
LANGS = [("Ukrainisch", "Muttersprache", 100), ("Deutsch", "C2 · annähernd muttersprachlich", 95), ("Englisch", "B2 · selbstständig", 70)]
CHIP_ICONS = "none"     # a designer's chips stay text
ICON_ALIAS = {}

IMPACT, PROJECTS, PUBLICATIONS = [], [], []
FOOTER = "© 2026 Anna Liman · Walldorf"
