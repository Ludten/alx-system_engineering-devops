# Webstack monitoring
> Each file in this repository holds code that illustrates Webstack monitoring
> specific to the Bash Scripting & DevOps.

## Description of what each file shows:
* For this task head to https://www.datadoghq.com/ and sign up for a free `Datadog` account. When signing up, you’ll have the option of selecting statistics from your current stack that `Datadog` can monitor for you. Once you have an account set up, follow the instructions given on the website to install the `Datadog` agent.

	- Sign up for Datadog - **Please make sure you are using the US website of Datagog (.com)**
	- Install `datadog-agent` on `web-01`
	- Create an `application key`
	- Copy-paste in your Intranet user profile ([here](https://alx-intranet.hbtn.io/users/my_profile)) your DataDog `API key` and your DataDog application key.
	- Your server `web-01` should be visible in Datadog under the host name `XX-web-01`
		- You can validate it by using this [API](https://docs.datadoghq.com/api/latest/hosts/)
		- If needed, you will need to update the hostname of your server

* Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some `monitors` within the `Datadog` dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check](https://docs.datadoghq.com/integrations/system/).

	- Set up a monitor that checks the number of read requests issued to the device per second.
	- Set up a monitor that checks the number of write requests issued to the device per second.
