Simple Flask App
================

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment

- Klonujemy repozytorium z github.com

  $ git clone https://github.com/canabis84/se_hello_printer_app

- Instalacja python virtualenv i virtualenvwrapper:

  $ sudo pip install virtualenv
  $ sudo pip install virtualenvwrapper

- Rozpocząnając pracę z projektem (wykorzystując virtualenv). Hermetyczne środowisko dla pojedyńczej aplikacji w python-ie:

    $ source /usr/local/bin/virtualenvwrapper.sh

    # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
    $ mkvirtualenv wsb-simple-flask-app

- Wchodzimy do katalogu:

    $ cd se_hello_printer_app
    $ make deps - alternatywa dla poniszych instalacji
    $ pip install -r requirements.txt
    $ pip install -r test_requirements.txt

  Sprawdź: `documentację virtualenvwrappera <https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html>`_ oraz `biblioteki flask <http://flask.pocoo.org>`_.

- Uruchamianie applikacji:

    # jako zwykły program (mozemy skorzystac z make run)
    $ python main.py

    # albo:
    $ PYTHONPATH=. FLASK_APP=hello_world flask run

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

    $ make test - alternatywa
    $ PYTHONPATH=. py.test
    $ PYTHONPATH=. py.test  --verbose -s

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:


    $ source /usr/local/bin/virtualenvwrapper.sh # nie trzeba, jeśli już w .bashrc
    $ workon wsb-simple-flask-app



    # deaktywacja virtualenv
    $ deactivate



Materiały
=========

- https://virtualenvwrapper.readthedocs.io/en/latest/
