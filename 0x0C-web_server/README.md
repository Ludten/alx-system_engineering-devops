# Web server
> Each file in this repository holds code that illustrates Web server
> specific to the Bash Scripting & DevOps.

## Description of what each file shows:
* 0-transfer_file: A Bash script that transfers a file from our client to a server.

* 1-install_nginx_web_server: Web servers are the piece of software generating and serving HTML pages, let’s install one!

	Requirements:

	- Install `nginx` on your `web-01`
	- server
	- Nginx should be listening on port 80
	- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
	- As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
	- You can’t use `systemctl` for restarting `nginx`

* 2-setup_a_domain_name: Provide the domain name in your answer file.

	Requirement:

	- provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
	- configure your DNS records with an A entry so that your root domain points to your `web-01` IP address Warning: the propagation of your records can take time (~1-2 hours)
	- go to [your profile](https://alx-intranet.hbtn.io/rltoken/hH2hPj0jwETzZL-AvFJkwQ) and enter your domain in the `Project website url` field

* 3-redirection: Configure your Nginx server so that `/redirect_me` is redirecting to another page.

	Requirements:

	- The redirection must be a “301 Moved Permanently”
	- You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
	- Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

* 4-not_found_page_404: Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

	Requirements:

	- The page must return an HTTP 404 error code
	- The page must contain the string `Ceci n'est pas une page`
	- Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

* 7-puppet_install_nginx_web_server.pp: Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

	Requirements:

	- Nginx should be listening on port 80
	- When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
	- The redirection must be a “301 Moved Permanently”
	- Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
