#im richtigen Ordner: 
sudo apt-get install git
git init
ls -a


git config --global user.name "Stefan Taubert-Apweiler"
git config --global user.email "stefan.taubert.apweiler@gmail.com"
git config --global core.editor nano


Anleitung: Generating a new SSH key and adding it to the ssh-agent(google)
pi: mkdir .ssh
pi: cd ~/.ssh
ssh-keygen -t ed25519 -C "stefan.taubert.apweiler@gmail.com" # neuen key generieren
eval "$(ssh-agent -s)"                                       # ssh agent starten
ssh-add ~/.ssh/id_ed25519                                    #key dem keyagent hinzufügen
nano id_ed25519.pub                                          #key kopieren und dann bei githaub hinzufügen
git remote add origin git@github.com:sraspi/USS.git
git fetch --set-upstream origin master
git pull git@github.com:sraspi/USS.git master
git pull --all


#new files need to be added to the Git repo and then committed
git add --all   #dauert eventuell lange!
git commit -am 'text'

git status
git log datei.txt

git checkout 5fd772a292c019a7cf3012b1156685280d4a7d2d datei.txt
git commit -am 'restore irgendwas'

git push -u origin master

#anschließend:
git pull --all  # holt Änderung aus github
git push --all  # upload zu github


