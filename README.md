# PIZZA PALVELU

Ideana olisi luoda online-pizzapalvelu, josta voi tilata pizzaa ja juomia.
 
Kun on luonut käyttäjän, on mahdollista tarkastella omia vanhoja tilauksia, nähdä kuinka paljon on käyttänyt yhteensä rahaa pizzapalveluun,
suosituimman pizzansa sekä suosituimman juomansa, ja jättää arvosteluja ja kommentteja.

Pizzapalvelun nettisivulta voi tilataamisen lisäksi nähdä annettuja arvosteluja, sekä kuinka monta tähteä palvelu on keskimäärin saanut.
Sivulla näkee myös, mikä on ollut suosituin pizza ja juoma.

Tilauksessa voi valita 0-5 kappaletta jokaista pizzaa ja juomaa. Tilaajan täytyy hänen ilmoittaa myös toimitusosoite ja antaa tarkat saapumisohjeet.


## Sovelluksen toiminnot

- Käyttäjä voi rekisteröidä uuden käyttäjätilin tai kirjautua sisään

- Jos käyttäjä on kirjautunut sisään, pystyy hän jättämään kommentteja tai arvosteluja

- Kuka tahansa pystyy tarkastelemaan arvosteluja ja kommentteja

- Käyttäjä pystyy tarkastelemaan omaa tilaushistoriaansa ja suosikkituotteitaan

- On mahdollista nähdä myös PizzaServicen suosituin pizza ja juoma


## Sovelluksen käynnistysohjeet

1. Kloonaa repositorio ja siirry sen juureen komennolla " cd pizzaservice"

2. Luo uusi ".env" -niminen tiedosto hakemiston juureen ja lisää sinne seuraavat tiedot:

    - DATABASE_URL= tietokannan-paikallinen-osoite
    - SECRET_KEY= salainen-avain


3. Aktivoi virtuaaliympäristö ja asenna sovellukseen riippuvuudet:

        $ python3 -m venv venv
        $ source venv/bin/activate

4. Lisää myös requirements tiedosto:
        
        venv $ pip install -r ./requirements.txt

4. Jos et ole vielä asentanut psql toimintoja koneellesi, tee se näiden ohjeiden mukaisesti:

[Ohjeet](https://github.com/hy-tsoha/local-pg)

5. Kun olet käynnistänyt tietokannan toisessa terminaali-ikkunassa komennolla:

        $ start-pg.sh

6. Voit määrittää tietokannan PizzaService repositorion juuressa komennolla:

        venv $ psql < schema.sql

5. Käynnistä sovellus komennolla

        venv $ flask run