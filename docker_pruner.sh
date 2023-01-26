#!/bin/bash
# Docker pruner

# Nadaje właściciela na proces dockera
# Zanim ktoś to bezmyślnie odpali to jest to coś w stylu mikro ansible
# które czyści wszystkie nie używane kontenery i obrazy poboczne powstałe
# na skutek generowania obrazów, celem zwolnienia sporej ilości miejsca
# na dysku.
# Jeśli kopiujesz ten kod to zamień nazwę użytkownika na swoją

echo "Podaj hasło root aby przyznać uprawnienia do procesu docker"
sudo chown jakub:docker /var/run/docker.sock

# Usuwa wszystkie wyłączone kontenery
docker rm $(docker ps --filter status=exited -q);

# Usuwa obrazy przejściowe po robieniu główego obrazu
docker images -a | grep none | awk '{ print $3; }' | xargs docker rmi

echo "Czyszczenie dockera zakończone";
