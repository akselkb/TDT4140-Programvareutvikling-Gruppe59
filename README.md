## Activate [![pipeline status](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/badges/master/pipeline.svg)](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/-/commits/master)

Activate er en webapplikasjon (på bestilling av Sit) som fasiliterer aktiviteter for brukerne. Applikasjonen er myntet på studenter, som kan segregeres i henholdsvis vanlige medlemmer og NTNUI-medlemmer. Som en bruker kan du enkelt både arrangere/opprette arrangementer, samt melde deg på eller av arrangementer. Med hensyn på personvern og brukerpsykologi er applikasjonen også tilrettelagt for stor grad av anonymitet.


## Motivasjon

Motivasjonen bak applikasjonen er at Sit har observert en stadig økende, og korrelerende, tendens av inaktivitet og ensomhet blant unge voksne i Norge. Derfor ønsker de å gjøre et motvirkende tiltak.


## Tech/rammeverk, code style og testing

Sjekk ut wikien: [Oversikt over kodekvalitet](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/-/wikis/Oversikt-over-kodekvalitet)


## Installasjon

### Med Docker
For å komme raskt i gang med å kjøre prosjektet lokalt, er det mulig å kjøre prosjektet i en Docker-container. For å gjøre dette:
1. Sørg for at du har installert Git ([guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
2. Klon prosjektet til din maskin med `git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59.git`
3. Sørg for at du har installert Docker ([guide](https://docs.docker.com/compose/install/))
4. Kjør deretter kommandoen `docker-compose up -d` fra prosjektets rotmappe `/59/activate/`
5. Du kan deretter besøke Activate-siden på URLen [http://127.0.0.1:8000](http://127.0.0.1:8000) – endringer du gjør i koden vil automatisk lastes inn ("hot reload")


### Uten Docker
Det er også enkelt å kjøre prosjektet lokalt uten Docker. For å gjøre dette:
1. Sørg for at Python 3.7 ([guide](https://www.python.org/downloads/)) og Git ([guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)) er installert på maskinen
2. Klon prosjektet til din maskin med `git clone https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59.git`
3. Lag og aktiver et virtual environment for prosjektet (to alternativer)
    - Sett opp prosjektet i din favoritt-IDE ([guide for PyCharm](https://www.dev2qa.com/how-to-import-existing-django-project-and-enable-django-support-in-pycharm/))
    - Opprett et virtual environment kalt f.eks. `sit-activate` i en mappe du velger (for eksempel `.virtualenvs` i hjemmemappen) ved å skrive `python -m venv sit-activate` ([guide for oppretting og aktivering](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments))
4. Naviger til prosjektets rotmappe, `/59/activate/`, og installer alle avhengigheter med `pip install -r requirements.txt`
5. For å oppdatere databasen kjør kommandoen `python manage.py migrate`
6. Til slutt kan du kjøre kommandoen `python manage.py runserver 8000` og besøke Activate-siden på URLen [http://127.0.0.1:8000](http://127.0.0.1:8000)


## Hvordan bruke applikasjonen

Sjekk ut wikien: [Brukermanual](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/-/wikis/Brukermanual)


## Medvirkning

Sjekk ut wikien: [Rutiner for evolusjon og endring](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/-/wikis/Rutiner-for-evolusjon-og-endring)


## Veien videre

Sjekk ut wikien: [Roadmap for produktet](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59/-/wikis/Roadmap)


## Credits

Underveis i prosjektet har gruppen brukt en rekke kilder som inspirasjon til hvordan man skal løse problemstillinger i koden. Under følger en liste med de mest vesentlige inspirasjonskildene vi har benyttet under produksjonen av produktet:

Oppsett av prosjektet:
- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)

Som generell støtte:
- [MDN web docs: Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

User management:
- [Corey Schafer: Python Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)


## Lisens

MIT License

Copyright (c) [2020] [TDT4140 - Gruppe 59](https://gitlab.stud.idi.ntnu.no/tdt4140-2020/59)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.