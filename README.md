# hi there!

this is my portfolio project!

## usage:

remote

    dokku apps:create <appname>
    dokku postgres:create <dbname>
    dokku postgres:link <dbname> <appname>
    dokku config:set --no-restart <appname> SECRET_KEY="<secret_key>" #use keygen.py

local

    git remote add dokku dokku@<hostname>:<appname>
    git push dokku master

remote

    dokku config:set --no-restart <appname> DOKKU_LETSENCRYPT_EMAIL=<email>
    dokku letsencrypt <appname>
    dokku run <appname> python manage.py migrate
    dokku run <appname> python manage.py createsuperuser
