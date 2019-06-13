## GIT

```sh
git config --global user.name <name>
    git config --local user.email <email>
git config --system core.editor <editor>
```

<<    adding ssh keys    >>
1.ssh-keygen -t rsa 
2.
=>ssh-add "id_rsa"
=>ssh-agent -s
=>ssh-add ~/.ssh/id_rsa


1.existing project << download existing project >> 
git clone git@bitbucket.org:gowt1ham/ba_ranking.git
cd ba_ranking
echo "# My project's README" >> README.md
git add README.md
git commit -m "Initial commit"
git push -u origin masterzz

2. from scratch
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:thefr33radical/drive.git
git push -u origin master

3. Delete remote folder
rm -rf folder
git add .
git commit -a -m "removed folder"
git push origin master
--------------------------------------------------------------------------------------------------
# Grive

sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install grive
sudo apt-get install cmake build-essential libgcrypt11-dev libjson0-dev libcurl4-openssl-dev libexpat1-dev libboost-filesystem-dev libboost-program-options-dev binutils-dev
wget http://www.lbreda.com/grive/_media/packages/0.2.0/grive-0.2.0.tar.gz
tar xvfvz grive-0.2.0.tar.gz
cd grive-0.2.0
cmake .
make
sudo make install
mkdir ~/google_drive
cd ~/google_drive
grive -a

grive

# logout git

git config --global --unset user.name
git config --global --unset user.email

or 

git config --global --unset-all
