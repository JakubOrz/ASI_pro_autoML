#!/bin/bash
# Docker pruner

# Nadaje właściciela na proces dockera
# Zanim ktoś to bezmyślnie odpali to jest to coś w stylu mikro ansible
# które czyści wszystkie nie używane kontenery i obrazy poboczne powstałe
# na skutek generowania obrazów, celem zwolnienia sporej ilości miejsca
# na dysku.

echo "Podaj hasło root aby przyznać uprawnienia do procesu docker"

# Usuwa wszystkie wyłączone kontenery
sudo docker rm $(docker ps --filter status=exited -q);

# Usuwa obrazy przejściowe po robieniu główego obrazu
sudo docker images -a | grep none | awk '{ print $3; }' | xargs docker rmi

echo "Czyszczenie dockera zakończone";
