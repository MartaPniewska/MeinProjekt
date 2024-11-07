1 Anmeldung bei GitHub (www.github.com) 

2. Erstellung eines neuen leeres Repository mit dem Namen "MeinProjekt".

3. URL des erstellten Repositories, notiert. 
	git@github.com:MartaPniewska/MeinProjekt.git

4.-7. SSH-Schlüssel mit dem folgenden Befehl: ls ~/.ssh/ überprüft und vorhanden.

velpTEC edutainment@PC-63V92W MINGW64 / (main)
$ ls ~/.ssh/
'agent pid.txt'   id_rsa.pub    known_hosts.old  'ssh rsa.txt'
 id_rsa           known_hosts  'ssh befehl.txt'   ssh.txt


8. Erstellung des lokalen Git-Repository im Terminal 

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP (main)
$ cd MeinProjekt

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt (main)


9. "MeinProjekt" im GitHub-Repository geklont.
git clone git@github.com:MartaPniewska/MeinProjekt.git

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt
$ git clone git@github.com:MartaPniewska/MeinProjekt.git
Cloning into 'MeinProjekt'...
Enter passphrase for key '/c/Users/velpTEC edutainment/.ssh/id_rsa':
warning: You appear to have cloned an empty repository.

10. Das geklonte Verzeichnis "MeinProjekt" geöffnet.

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP (main)
$ cd MeinProjekt

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt (main)

11. Konfiguration von Git mit meinem Namen und E-Mail:

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git config user.name "MartaPniewska"
velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git config user.email "kmpniewska@hotmail.com"

12. Initial-Commit mit main.py:

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git add main.py

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git commit -m "Initialer Commit"
[main (root-commit) e3a8923] Initialer Commit
 1 file changed, 15 insertions(+)
 create mode 100644 main.py

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git init
Reinitialized existing Git repository in C:/Users/velpTEC edutainment/GitHub/TP/MeinProjekt/MeinProjekt/.git/


13. Erstellung einer neuen Branch mit dem Namen "feature":

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git checkout -b feature
Switched to a new branch 'feature'

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (feature)


14. Eine weitere Datei "utils/database.py") hinzufügen inkl. einem Commit auf dem "feature"-Branch:

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (feature)
$ git add utils/database.py

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (feature)
$ git commit -m "Neue Funktion hinzugefügt"
[feature 742e75e] Neue Funktion hinzugefügt
 1 file changed, 1 insertion(+)
 create mode 100644 utils/database.py

15. Speicherung der Änderungen in der Datei "main.py" inkl. einem Commit auf dem "feature"-Branch durch:

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (feature)
$ git add main.py

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (feature)
$ git commit -m "Hauptdatei aktualisiert"
[feature 288b63d] Hauptdatei aktualisiert
 1 file changed, 1 insertion(+), 1 deletion(-)


16. Wechsel zurück zum "master"-Branch:

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (feature)
$ git checkout main
Switched to branch 'main'

17. Erneutes Commit der Änderungen in der Datei "main.py" auf dem "main"-Branch durch und Push ins Repository:

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git add main.py

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git commit -m "Hauptdatei aktualisiert"

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git push
Enter passphrase for key '/c/Users/velpTEC edutainment/.ssh/id_rsa':
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 660 bytes | 16.00 KiB/s, done.
Total 7 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:MartaPniewska/MeinProjekt.git
   e3a8923..288b63d  main -> main

18. Merge von "feature"-Branch in den "main"-Branch:

velpTEC edutainment@PC-63V92W MINGW64 ~/GitHub/TP/MeinProjekt/MeinProjekt (main)
$ git merge feature
Updating e3a8923..288b63d
Fast-forward
 main.py           | 2 +-
 utils/database.py | 1 +
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 utils/database.py

