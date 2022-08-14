# Secret app
The secret app is made to exchange secrets.

The repo contains code and test

To run the application, you need to install python v?

## Manual setup 
* Install python v?
* configure python path, ie: export __PYTHONPATH=~/source/YT-secrets/app__
* Create folder for secrets and give write access to __/storage/secrets/__

## Run using Docker
Or instead of the manual setup, build and run the docker image with the following commands
```sh
docker build -t yt-secrets .
docker run -v [absolute-path-to-app]:/App yt-secrets
```

### To start the app manually (From docker)
```sh
docker run -it -p 80:80 -v [absolute-path-to-app]:/App yt-secrets sh
flask --app SecretController  run -h 0.0.0.0 -p 80
```

## Configure automation
The following steps should be automated
* Testing the code on deploy
* Deploy the code to production (For missing critical application the code should first be deployed to a staging server and tested, I will not describe that)

### Manual Deployment to a server
Before doing any automation, I will test all the steps manually, the provisioning (start up) of the server will not be automated.
1) Configure a server where we can run the application, I will use Digital Ocean [![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg)](https://www.digitalocean.com/?refcode=dcd9cffbef59&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
   * Spin-up server✔
   * Create a certificate for secure access✔
   * Configure Firewall✔
   * Install docker✔ and docker-compose✔
2) Push the application to the server (using rsync)✔
3) Start the application using docker-compose✔
   * Create a docker-compose file that mounts the volumes✔
   * Start the application as a service
4) Update application to use a proper server✔ (notice the warning when starting using flask development server)

### Automatic deployment 
1) Setup github action to run test
2) Setup github action to deploy to production
   * Convert private key to not use a password
   * Install private key in github secrets
   * push using github (Stop the application before push and restart?)