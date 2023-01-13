# ASI_pro_autoML
 Repozytorium dla projektu ASI

### Lista kontrybutorów
#### Szefowa zespołu: Janina Jegorowa
#### Architekt systemowy: Jakub Orzyłowski
#### Data scientist: Błażej Bartkiewicz, Jakub Windak
#### Inżynier ML: Błażej Bartkiewicz
#### Programista #1 Paweł Sołtys


## Change log

### 07.01.2023 docker-compose

Dodałem docker-compose

Jakub Windak

### 09.01.2023 Czyszczenie zbędnych bibliotek

Po tym jak obraz Dockera nagle zaczął wynosić ponad 4GB decydowałem się na totalne 
wyczyszczenie bibliotek, celem optymalizacji budowy Dockera

Usunąłem / zakomentowałem pliki związane z wandb, optuna, jupter
Z racji tego, ze nie sa używane w ostatecznym pipeline.

Nasz pipeline będzie używał pycareta do trenowania modelu, polecam reset virtual enva.

### 05.01.2023 Dockerfile

Dodałem dockerfile za pomocą kedro docker

Jakub Orzyłowski

### 18.12.2022 Czyszczenie repozyorium z plików i ludzi które powinny być w .gitignore

Który fan VS Code zapomniał o dodaniu folderu .vs do .gitignore?

Jakub Orzyłowski

### 4.12.2022 hotfix

Na dvc remote wrzuciłem wytrenowane modele, aby było wam łatwiej
potraktować je wandb

Aby pobrać te modele (bez odpalania kedro)

``dvc pull -r server``

Jakub Orzyłowski


### 4.12.2022

Implementacja trenowania i wybierania najlepszego modelu za pomocą
pycaret oraz optuna, zawarte w pipeline

- optuna_model_training
- pycret_pipeline

``kedro run -p pyceret_pipeline``

``kedro run -p optuna_model_training``

Pamiętajcie o zaktualizowaniu wymagań

Jakub Orzyłowski, Błażej Bartkiewicz

### 04.12.2022
Dodałem pierwszą wersję notebooka z pycarretem.

Działa utworzenie data frame z naszymi danymi, ustawienie modelu, porównanie modeli i wybranie najlepszego.

Ewaluacje oraz zapisanie modelu dodam w ciągu dnia.

Błażej Bartkiewicz

### 02.12.2022

Dodałem notatki z careta i optuny dla data Scientists

Jakub Orzyłowski

### 14.11.2022

Dodałem notebooka, żeby spełnić wymagania. Nie byłem pewny, co w nim powinno siedzieć, więc po prostu pobiera dane i trenuje model.
Dodałem podzieloną na sensowne node'y funkcjonalność modelu w miejsce poprzedniego, testowego pipeline'a.

Reszty nie tykałem, co złego to nie ja.



Pozdrawiam,
Paweł Sołtys

PS
Używam VSCode'a, bo nie będziesz mi mówił, jak mam żyć

### 13.11.2022

Usunąłem te pakiety które teraz zostały włączone jako kedro, celem oczyszcznia 
kodu.
Należy zaktualizować pakiety

`pip install -r requirements.txt` 

Usunąłem puste katalogi które były automatycznie generowane przez kedro.

Skonfigurowałem dvc remote na serverze ssh. Można już śmiało używać 

`dvc push -r server -v`

`dvc pull -r server -v`

Komenda -v sprawia że wyświetli się więcej informacji 

Jakub O.
### 12.11.2022
Zaimplementowałem projekt Kedro, aby odpalić kedro należy wejsć do katalogu
autocarml.<br>
W tej chwili mamy jeden pipeline, o nazwie również autocarml tam póki co to co się wykonuje to
odczytanie head pliku csv, i pozbycie się wadliwych wierzszy. 
Na chwilę 12.11 20:21 jeszcze nie podłączyłem dvc remote, zrobię to w następnym
patchu<br>
Aby odpalić kedro należy być w katalogu autocarml <br>
Pamiętajcie o ponownym użyciu<br>
`pip install -r requirements.txt` <br>
Doszły nowe biblioteki (kedro)

`kedro run`

Dla tych co uzywają PyCharma<br>
- Project, openfrom VCS
- Wybrać to repozytorium
- Commitować jak coś zmieniacie

Dla tych co używają VS Code
- Zainstalujcie PyCharma

Instalowanie własnej paczki przykładowa treedrawer<br>
``pip install -e <scieżka do folderu gdzie jest setup.py>``

Odapalanie venva (dla opornych)<br>
``python -m venv env``

Instalowanie bibliotek (dla opornych)<br>
``pip instal -r requirements.txt``<p>
Instalowanie lokalnych paczek (mamy dwie)<br>
``pip install -e ./data_package1``<br>
``pip install -e ./hearts_package``<br>

Uwaga, dla tych co używają windowsa potrzebna 
jest dodatkowa paczka<br>
``pip install -r win_extra_requirements.txt``

Zanim zaczniecie edytować kod pamiętajcie o<br>
``git pull``<br>W PyCharmie ta niebieska strzałeczka,
nie chce mi się potem naprawiać za was rozjechanych branchów <br>

