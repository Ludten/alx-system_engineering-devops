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

* 3-app_server-nginx_config: Building on what you did in the previous tasks, let’s expand our web application by adding another service for `Gunicorn` to handle. In `AirBnB_clone_v2/web_flask/6-number_odd_or_even`, the route `/number_odd_or_even/<int:n>` should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure `Nginx` to proxy HTTP requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a `Gunicorn` instance listening on port 5001. The key to this exercise is getting `Nginx` configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of `Gunicorn` without having multiple terminals open, see tips below.

	Requirements:
	- `Nginx` must serve this page both locally and on its public IP on port `80`.
	- `Nginx` should proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` the process listening on port `5001`.
	- Include your `Nginx` config file as `3-app_server-nginx_config`.

	Tips:
	- Check out these articles/docs for clues on how to configure `Nginx`: [Understanding Nginx Server and Location Block Selection Algorithms](https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms#matching-location-blocks), [Understanding Nginx Location Blocks Rewrite Rules](http://blog.pixelastic.com/2013/09/27/understanding-nginx-location-blocks-rewrite-rules/), [Nginx Reverse Proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/#).
	- In order to spin up a `Gunicorn` instance as a detached process you can use the terminal multiplexer utility `tmux`. Enter the command `tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'` and if successful you should see no output to the screen. You can verify that the process has been created by running `pgrep gunicorn` to see its PID. Once you’re ready to end the process you can either run `tmux a` to reattach to the processes, or you can run `kill <PID>` to terminate the background process by ID.

* 4-app_server-nginx_config: Let’s serve what you built for [AirBnB clone v3 - RESTful API]() on `web-01`.

	Requirements:
	- Git clone your `AirBnB_clone_v3`
	- Setup `Nginx` so that the route `/api/` points to a `Gunicorn` instance listening on port `5002`
	- `Nginx` must serve this page both locally and on its public IP on port `80`
	- To test your setup you should bind `Gunicorn` to `api/v1/app.py`
	- Upload your `Nginx` config file as `4-app_server-nginx_config`
