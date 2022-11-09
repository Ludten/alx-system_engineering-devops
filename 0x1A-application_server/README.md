# Application server
> Each file in this repository holds code that illustrates Application server
> specific to the Bash Scripting & DevOps.

## Description of what each file shows:
* Let’s serve what you built for [AirBnB clone v2 - Web framework](https://alx-intranet.hbtn.io/projects/290) on `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

	Requirements:
	- Git clone your `AirBnB_clone_v2` on your `web-01` server.
	- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port `5000`.
	- Your Flask application object must be named `app` (This will allow us to run and check your code).

* Now that you have your development environment set up, let’s get your production application server set up with `Gunicorn` on web-01, port `5000`. You’ll need to install `Gunicorn` and any libraries required by your application. Your `Flask` application object will serve as a [WSGI](https://www.fullstackpython.com/wsgi-servers.html) entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

	Requirements:
	- Install `Gunicorn` and any other libraries required by your application.
	- The Flask application object should be called `app`. (This will allow us to run and check your code)
	- You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a `Gunicorn` instance to localhost listening on port `5000` with your application object as the entry point.

* 2-app_server-nginx_config: Building on your work in the previous tasks, configure `Nginx` to serve your page from the route `/airbnb-onepage/`

	Requirements:
	- `Nginx` must serve this page both locally and on its public IP on port 80.
	- `Nginx` should proxy requests to the process listening on port 5000.
	- Include your `Nginx` config file as `2-app_server-nginx_config`.

	Notes:
	- In order to test this you’ll have to spin up either your production or development application server (listening on port `5000`)
	- In an actual production environment the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.
	- You will probably need to `reboot` your server (by using the command `$ sudo reboot`) to have Nginx publicly accessible
