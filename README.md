# YTDL
#im richtigen Ordner: 
echo "# YTDL" >> README.md
git init
ls -a


git config --global user.name "Stefan Taubert-Apweiler"
git config --global user.email "stefan.taubert.apweiler@gmail.com"
git config --global core.editor nano




#new files need to be added to the Git repo and then committed
git add --all   #dauert eventuell lange!
git commit -am 'text'

git status
git log datei.txt

git checkout 5fd772a292c019a7cf3012b1156685280d4a7d2d datei.txt
git commit -am 'restore irgendwas'

#github upload bei 1.upload:
pi mkdir .ssh
pi: cd ~/.ssh

profile/settungs/SSH and GPG keys:new key


git remote add origin git@github.com:sraspi/ACC.git
git push -u origin master

#anschlieÃŸend:
git pull --all  # holt Ã„nderung aus github
git push --all  # upload zu github

