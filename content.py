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
    title="Anna Liman · Grafikdesignerin",   # <title> and og:title (already HTML-escaped)
    description="Anna Liman, staatlich geprüfte Grafikdesignerin aus Walldorf: Print, Web und Malerei. Arbeiten, Werdegang und Kontakt.",
    badge="Staatlich geprüfte Grafikdesignerin",   # small pill above the name; None hides it
    tagline="Grafikdesign für Print und Web. Und Malerei auf Leinwand.",
    lede="Ich gestalte Speisekarten, Websites und alles dazwischen, in InDesign, Illustrator und Photoshop. Ausgebildet an der Johannes-Gutenberg-Schule Heidelberg, dort auch Medienfachwirtin (Bachelor Professional).",
    meta=["Walldorf · Rhein-Neckar", "DE C2 · EN B2 · UA Muttersprache"],
    location="Walldorf",
    job_title="Grafikdesignerin",                   # schema.org jobTitle for search engines; optional
    # profile links: (label, url, icon name from src/icons.json or None). The first is the primary button.
    links=[("E-Mail schreiben", f"mailto:{EMAIL}", None), ("LinkedIn", LINKEDIN, "LinkedIn")],
    hero_cta=("Arbeiten ansehen", "#arbeiten"),     # third hero button; None hides it
)

# German interface strings for the chassis (see UI_DEFAULTS in build.py)
UI = dict(
    lang='de', locale='de_DE', contact='Kontakt', today='heute', back_to_top='Nach oben ↑',
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

HERO_PHOTOS = [('assets/hero/anna-2.jpg', 'Porträt von Anna Liman'), ('assets/hero/anna.jpg', 'Porträt von Anna Liman')]
STATS = []
MARQUEE = []

SECTIONS = [
    dict(id="arbeiten", type="gallery", nav="Design", label="Grafikdesign",
         heading="Grafikdesign",
         intro="Veg & Velvet, ein Café: Speisekarte und Startseite der Website. Zum Vergrößern ein Bild anklicken."),
    dict(id="malerei", type="gallery", nav="Malerei", label="Malerei",
         heading="Malerei",
         intro="Frühere freie Arbeiten auf Leinwand: Pop-Art, Landschaft und Porträt.",
         items=[
             dict(src="assets/work/malerei-popart-blond.jpg", caption="Pop-Art-Porträt in Gelb, auf Leinwand", tall=True),
             dict(src="assets/work/malerei-popart-traenen.jpg", caption="Pop-Art-Porträt mit Tränen, auf Leinwand", tall=True),
             dict(src="assets/work/malerei-bergsee.jpg", caption="Bergsee mit Spiegelung, auf Leinwand", tall=True),
             dict(src="assets/work/malerei-blau.jpg", caption="Porträt in Blau, freie Arbeit auf Leinwand", tall=True),
         ]),
    dict(id="ueber-mich", type="about", nav="Über mich", label="Über mich",
         heading="Gestaltung ist mein Handwerk.",
         paragraphs=[
             "Ich bin <strong>staatlich geprüfte Grafikdesignerin</strong> (Johannes-Gutenberg-Schule Heidelberg, 2023) und suche eine Stelle im Grafikdesign. Ich arbeite mit <strong>InDesign, Illustrator und Photoshop</strong>, zeichne digital in <strong>Procreate</strong> und habe Grundkenntnisse in Figma.",
             "Neben dem Grafikdesign male ich auf Leinwand: Pop-Art, Landschaften und freie Porträts. Einige dieser Arbeiten zeige ich weiter oben.",
             "Danach habe ich an derselben Schule die Weiterbildung zur <strong>Medienfachwirtin (Bachelor Professional)</strong> gemacht und kenne damit auch die Planung und Organisation von Medienprojekten. Was ich mitbringe: Kommunikationsstärke, eine schnelle Auffassungsgabe und eine strukturierte Arbeitsweise.",
         ],
         facts=[("Schwerpunkt", "Grafikdesign · Print · Web"), ("Außerdem", "Malerei · Illustration"), ("Ort", "Walldorf, Rhein-Neckar")]),
    dict(id="werdegang", type="experience", nav="Werdegang", label="Werdegang", heading="Werdegang",
         start_label="2020 · Beginn der Ausbildung"),
    dict(id="kenntnisse", type="skills", nav="Kenntnisse", label="Kenntnisse", heading="Kenntnisse &amp; Sprachen"),
    dict(id="kontakt", type="contact", nav=None, label="Kontakt",
         heading="Lassen Sie uns <span class=\"accent\">sprechen.</span>",
         text="Ich freue mich über Nachrichten zu Stellen im Grafikdesign. Am besten erreichen Sie mich per E-Mail oder über LinkedIn.",
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
    ("Design-Software", ["Adobe InDesign", "Adobe Illustrator", "Adobe Photoshop", "Procreate", "Figma (Grundkenntnisse)"]),
    ("Office", ["Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint"]),
    ("Stärken", ["Kommunikationskompetenz", "Schnelle Auffassungsgabe", "Strukturierte Arbeitsweise"]),
]
EDUCATION = []          # shown in the Werdegang timeline instead
CERTIFICATIONS = []
LANGS = [("Ukrainisch", "Muttersprache", 100), ("Deutsch", "C2 · annähernd muttersprachlich", 95), ("Englisch", "B2 · selbstständig", 70)]
CHIP_ICONS = "none"     # a designer's chips stay text
ICON_ALIAS = {}

IMPACT, PROJECTS, PUBLICATIONS = [], [], []
FOOTER = "© 2026 Anna Liman · Walldorf"
