# FREE GEOIP SERVICE

Get free geoip data for client requests.

This works thanks to some special headers added by Google App engine to each request that it serves.

For this reason, this **can only be deployed on App engine**.

App engine only returns some basic info like: **latitude, longitude, city, country** but if this is enough then you can get all this for free.

**Note:** This only works for requests that come directly from the client's device (no way to request for a specific IP).

## About

This is a simple Flask app that reads the special headers that Google App engine adds to each request and returns them as JSON.

App engine has a decent free tier so this service can be run for free.

Example response:

```json
{
    "city":"bucharest",
    "countryCode":"RO",
    "ipAddress":"xx.xxx.xxx.xx",
    "latitude":"44.426767",
    "longitude":"26.102538",
    "regionCode":"b"
}
```

## Demo

Try it for free at [https://free-geoip.ey.r.appspot.com/](https://free-geoip.ey.r.appspot.com/)

## How to deploy

1. Pull repo

```sh
git clone https://github.com/onel/freegeoip .
cd freegeoip
```

2. Create a new project in [Google cloud console](https://console.cloud.google.com) and an [App engine app](https://console.cloud.google.com/appengine).

3. Setup local configurations for this new project

```sh
gcloud config configurations create [project_id]
gcloud config set project [project_id]
gcloud auth login
gcloud app deploy . --version 1
```

4. Make requests to that endpoint to get getip info

```javascript
const url = '[your freegeoip endpoint]'
fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log('JSON data:', data);
    })
    .catch(error => {
        console.error('Fetch error:', error);
    })
```



## Stack

Python 3.9

Flask

## Licence

MIT
