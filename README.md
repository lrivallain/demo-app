# demo-app
A simple Flask App to get informations about the local node running the app.

![Screnshot of the UI](/static/screenshot.png)

## Pre-requisites

Python3 installed with `pip` support.

## Installation

Clone the current repository, then:

```bash
cd demo-app/
pip install -r requirements.txt
flask run
```

Then you can join the UI from: http://127.0.0.1:5000

If you need to expose the informations on external IP address, use the following `run` command:

```bash
flask run --host=0.0.0.0
```

Then you can join the UI from: http://<ip address>:5000

## Features

The app provides 3 flask-based-routes:

* `/` is a simple redirect to `/ui`
* `/ui` provides a simple interface to display to result of API call
* `/api` is a endpoint to generate the JSON formated data about the system

In the `/ui` interface you can find:

* A `curl` command to get the data from a shell
* A *reload* button to refresh the data displayed on the UI
* A link to the `/api` endpoint
* A `<pre>` tag with the raw content of the API call result
* A `<ul>` list with formated data

In the data you will find the following information:

* **architecture**: Processor architecture
* **hostname**: Hostname of the system
* **ip-address**: IP address of the interface with default route
* **mac-address**: Mac address of the interface with default route
* **platform**: Type of OS
* **platform-release**: Kernel release
* **platform-version**: The OS version
* **processor**: Kind of processor
* **ram**: RAM capacity in GB
* **uptime**: System uptime in seconds

