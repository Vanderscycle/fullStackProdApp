#!/bin/bash
source ~/miniconda2/etc/profile.d/conda.sh # Remove the following 3 lines if not needed
DESIRED_ENV=NNScraper
conda activate $DESIRED_ENV 
# add actions (later) because we are going the DevOps CI/CD route
function gitFiles(){

    if [ ! -f README.md ]
    then
        touch README.md
        echo 'README.md file created'

    if [ ! -f .gitignore ]
    then
        touch .gitignore
        echo '.gitignore file created'
        #EOL sometimes gives you errors if there is a space after
        cat >> .gitignore << EOL
.ipynb_checkpoints
.log
__pycache__
.vscode
.env
EOL
    fi

    if [ ! -f .env ]
    then
        touch .env
        echo 'empty .env file created'
    fi
    
}
# Dockerfile/.dockerignore/requirements.txt (requires pipreqs)
function dockerFiles(){

    if [ ! -f Dockerfile ]
    then
        touch Dockerfile
        echo 'empty Dockerfile file created'
        cat >> Dockerfile << EOL
FROM 
LABEL maintainer "Henri Vandersleyen <hvandersleyen@gmail.com>"
EOL
    fi

    if [ ! -f .dockerignore ]
    then
        touch .dockerignore
        echo '.dockerignore file created'
        cat >> .dockerignore << EOL
Dockerfile
.ipynb_checkpoints
.log
__pycache__
.vscode
.env
EOL
    fi
    
    echo 'creating the requirements.txt file'
    pipreqs . #pip install pipreqs # if not installed on your machine
    read -p 'Do you want to keep the python module version in requirements.txt? [y/n]': YSNOANS
    case $YSNOANS in
        [yY] | [yY][eE][sS])
        echo 'removing the python module version'
        # using sed to remove the version of each file -i flag updates the file name
        sed -i 's/==.*//' requirements.txt
        ;;
        [nN] | [nN][oO])
        echo 'NIL changes to requirements.txt'
        ;;
    esac
}
echo 'Welcome to the automatic Git and Docker files creation tool'
echo 'If you want to init a new git repo with an already populated .gitignore, partially populated README.md and empty .env file?: git'
echo 'If you want to init a new Docker with a partialy populated Dockerfile, populated .dockerignore file and a automatically generated requirements.txt?: docker'
echo 'If you want to create both Git and Docker file please senter: both'
read -p 'What do you want to create? (git/docker/both)': ANSWER

case $ANSWER in
    [gG] | [gG][iI][tT]) #g or git
        echo 'creating git files'
        gitFiles
        ;;
    [dD] | [dD][oO][cC][kK][eE][rR])
        echo 'creating docker files'
        dockerFiles
        ;;
    [bB] | [bB][oO][tT][hH])
        echo 'creating both git and docker files'
        gitFiles
        dockerFiles
        ;;
    *)
        echo 'Please enter g/git, d/docker or b/both'
esac