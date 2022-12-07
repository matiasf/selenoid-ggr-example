# Selenoid ggr example

In this repository you will get a docker-compose.yml with selenoid, selenoid-ui, ggr, ggr-ui and a python execution example.

The pourpuse of this example it to check the architecture configuration to deploy a decouple Selenium cluster with the previews tools.

Also is needed to validate the posibilitiy to reconect to a previews existing session from outside script, this can be found on the script `outside-reconnect-session.py`

To run the example just run `docker-compuse up` on root directory.

### Reconnection example

Host requeriments:
* python3
* Install Selenium with `pip install selenium`


For the reconnection script you need to get the session previewsly created for the service `python-screaper-example.py`, when you run docker compuse you will see a log like this:

```shell
python-scraper-example_1  | 2022/12/07 15:58:23 - Creating connection to the hub
python-scraper-example_1  | 2022/12/07 15:58:24 - Print driver URL and session ID
python-scraper-example_1  | driver.command_executor._url: http://test:test-password@ggr:4444/wd/hub
python-scraper-example_1  | driver.session_id: 1f8ac2fbb819fa8bd83b9d15bf3796b81f03bae775fef77c639c3d314256e8da
python-scraper-example_1  | 2022/12/07 15:58:24 - Open page on session
python-scraper-example_1  | 2022/12/07 15:58:28 - Get element from page
python-scraper-example_1  | 2022/12/07 15:59:08 - The element capture show: HTML Tutorial
```

Get the session ID from `driver.session_id` and past it on `COPY_SESSION_RECONECT_HERE` in `outside-reconnect-session.py`

### This example is based on this articles

* [Selenium testing a new hope - Part I](https://hackernoon.com/selenium-testing-a-new-hope-7fa87a501ee9)
* [Selenium testing a new hope - Part II](https://hackernoon.com/selenium-testing-a-new-hope-a00649cdb100)
* [How to reconnect to the browser opened by webdriver with selenium](https://testup.io/how-to-reconnect-to-the-browser-opened-by-webdriver-with-selenium/)
