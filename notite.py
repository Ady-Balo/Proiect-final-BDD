"""
Folder features:
    - fisiere cu extensie feature - contin pasi de executie a testelor in limbaj Gherkin
    : Feature, Scenario, Given, When, Then, And
    - avem un fisier pentru fiecare pagina
    - scenariile dintr'un fisier au aceleasi preconditii( givens)
    - pasii in features au implementare python in fisiere steps

Folder steps:
    - fisiere cu extensie py. cod Python
    - identificarea metodelor se face cu decoratori
    ex.: @given("pasul cum se afla el in feature")
    - metodele intotdeauna sunt: def step_impl()
    - aceste metode step_impl primesc parametru context pentru
        context.login_page.navigate_to_home()
environment.py - fisier python in care setam toate resursele necesare pentru context
    - metoda before all
    - metoda after all - eliberam driverul

browser.py - clasa Driver/Browser selenium pentru interactionarea cu elementele web din pagina.

Folder pages:
    - un fisier python pentru fiecare pagina, pentru fiecare feature (POM - page object model)
    - contine o clasa Python: LoginPage().
        - constantele selectorilor cu tuple (By.ID, "username")
        - metodele de interactionare cu elementele paginii
    - fiecare clasa page va mostenii clasa BasePage, care la randul ei va mosteni Driverul(browser.py/driver.py)

Rularea in contextul 800 cu behave:
1.Din terminal rulam
    - behave (parseaza toate fisierele .feature din folderul feature, cauta pasii in steps pentru fiecare -> metodele din
     paginile din folderul pages)
     - behave --tags=shoppingChart (specificam tagul scenariilor care dorim sa fie executate)
     - behave -t=shoppingChart
     - behave
        -f behave_html_formatter: HTMLFormatter (putem configura un formatter)
        -o behave-report.html                  (putem specifica fisierul in care se gerereaza raportul)

    # behave -f behave_html_formatter: HTMLFormatter -o behave-report.html

Running from Terminal:
    behave -f html -o behave-report.html
    SAU
    behave -f html -o behave-ini-report.html

"""



