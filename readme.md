# Secret app
The secret app is made to exchange secrets.

Contains code and test for the secrets

To run the application, you need to install python v?

Manual setup 
* Install python v?
* configure python path, ie: export __PYTHONPATH=~/source/YT-secrets/app__
* Create folder for secrets and give write access to __/storage/secrets/__

Or instead of the manual setup, build and run the docker image with the following commands
```sh
docker build -t yt-secrets .
docker run -v ~/source/YT-secrets/app:/App yt-secrets
```