#!/bin/bash

eval $(ssh-agent) # Create agent and environment variables
ssh-add ~/.ssh/secrets
rsync -az --progress --stats --chown=www-data:www-data . root@142.93.137.143:/var/www/secret_app