# nautobot-docker-sntzd
an example of a nautobot deployment on docker with docker compose with ldap support

## missing info and files

There are obviously things missing here. To start with, there are no certificates. You need to created your own. Here is a nice guide for you:

<https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu>

Also, this is for version 2.1.8 of Nautobot. You should test to find out if this setup is good for newer versions (I am currently facing some issues with 2.2.3).

The plugin requirements are good for 2.1.8. If you upgrade to newer Nautobot versions you should look up plugin compatibility.
The same goes for python modules compatibility, by the time you run into this repo, you may have issues with the latest modules version and may need to adjust they python pacakge versions.

As is obvious from the dockerfile, python version is 3.11.

## run it

While in the project folder run:

```bash
docker-compose build --no-cache
```

This will build the image. I have made the option to copy the nautobot_config.py file in the image to make sure file rights and ownership are as they should be.
Feel free to disagree, modify as you see fit.

Use this to start the containers up:

```bash
docker-compose up -d
```

And then look for logs to see everything goes as planned:

```bash
docker-compose logs --follow --tail 500
```

Good luck!!
