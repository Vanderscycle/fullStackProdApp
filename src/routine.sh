#!/bin/bash

#conda init
source ~/miniconda2/etc/profile.d/conda.sh
DESIRED_ENV=productivityApp
conda activate $DESIRED_ENV 
read -p 'runserver (rs), DB migration(mm), Postgres(ps), or  skip('')': ORDER
case $ORDER in 
    [rR][sS] | [runserver])
        echo 'starting Django server'
        python manage.py runserver
        ;; 
    [mM][mM] | [migrations])
        echo 'making migration'
        python manage.py makemigrations
        echo 'migrating'
        python manage.py migrate
        ;;
    [pP][sS] | [postgres])
        # we look for .env file with all the secrets
        ENV_FILE=$(find . -name .env)
        if test -f "$ENV_FILE"; 
        then
            # use the -e flag
            echo -e ".env file exists. \nfile located here$ENV_FILE"
        else
            echo ".env file not found"
        fi
        export $(sudo cat $(find . -name .env))
        USER=root
        cd ~/
        #./prodHealthApp/.env
        # read -p 'passworrd' ROOT_PASSWORD 
        echo 'Starting POSTGRES shell'
        psql --command='\conninfo' postgresql://$USER:$POSTGRES_ADMIN_SECRET@127.0.0.1:5432/productivityapp
        # https://stackoverflow.com/questions/18223665/postgresql-query-from-bash-script-as-database-user-postgres
        ;; 
    *)
        echo 'activating env' $DESIRED_ENV
esac
#conda env list

# ok so I don't really know why but to activate the environment you can't
# simply call the script ./routine.sh but you have to use the old source
# source ./routine.sh (correctly activates the environment)
# cd '/home/henri/Documents/Post Lighthouse-Lab work/localFilesWebsite/src'
# cat is used to read the content of a file
# find . {local folder system} -name <name file>
# https://www.tecmint.com/35-practical-examples-of-linux-find-command/