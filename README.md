## Activate [![pipeline status](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/badges/master/pipeline.svg)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/-/commits/master)

Activate er en webapplikasjon (på bestilling av Sit) som fasiliterer aktiviteter for brukerne. Applikasjonen er myntet på studenter, som kan segregeres i henholdsvis vanlige medlemmer og NTNUI-medlemmer. Som en bruker kan du enkelt både arrangere/opprette arrangementer, samt melde deg på eller av arrangementer. Med hensyn på personvern og brukerpsykologi er applikasjonen også tilrettelagt for stor grad av anonymitet.

## Motivation

Motivasjonen bak applikasjonen er at Sit har observert en stadig økende, og korrelerende, tendens av inaktivitet og ensomhet blant unge voksne i Norge. Derfor ønsker de å gjøre et motvirkende tiltak.

## Tech/framework used

<b>Prosjektet ble bygd med:</b>
- [Python 3.7](https://www.python.org/)
- [Django 3.0.3](https://www.djangoproject.com/)
- [SQLite 3](https://www.sqlite.org/index.html)
- [Bootstrap 4](https://getbootstrap.com/)

## Code style

Sjekk ut (wiki om code style)


## Installasjon

### Med Docker
For å komme raskt i gang med å kjøre prosjektet lokalt, er det mulig å kjøre prosjektet i en Docker-container. For å gjøre dette:
1. Klon prosjektet til din maskin med `git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59.git`
2. Sørg for at du har installert Docker ([guide](https://docs.docker.com/compose/install/))
3. Kjør deretter kommandoen `docker-compose up -d` fra prosjektets rotmappe
4. Du kan deretter besøke Activate-siden på URLen 0.0.0.0:8000 – endringer du gjør i koden vil automatisk lastes inn ("hot reload")

### Uten Docker
Det er også enkelt å kjøre prosjektet lokalt uten Docker. For å gjøre dette:
1. Sørg for at Python 3.7 er installert på maskinen ([guide](https://www.python.org/downloads/)),
2. Klon prosjektet til din maskin med `git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59.git`
3. Lag og aktiver et virtual environment for prosjektet (to alternativer)
    - Sett opp prosjektet i din favoritt-IDE ([guide for PyCharm](https://www.dev2qa.com/how-to-import-existing-django-project-and-enable-django-support-in-pycharm/))
    - Opprett et virtual environment kalt f.eks. `sit-activate` i en mappe du velger (for eksempel `.virtualenvs` i hjemmemappen) ved å skrive `python -m venv sit-activate` ([guide for oppretting og aktivering](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments))
4. Installer alle avhengigheter med `pip install -r requirements.txt`
5. Du kan nå kjøre kommandoen `python manage.py runserver 8000` og besøke Activate-siden på URLen 127.0.0.1:8000


## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contribute

Sjekk ut (wiki om evolusjon/endring)

## Credits

Underveis i prosjektet har gruppen brukt en rekke kilder som inspirasjon til hvordan man skal løse problemstillinger i koden. Under følger en liste med de vesentlige inspirasjonskildene vi benyttet:
- Oppsett av prosjektet
  - [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- []()
- []()
- []()
- []()
- User management
  - [Corey Schafer: Python Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
## License

NTNU © [TDT4140 - Gruppe 59](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59)
