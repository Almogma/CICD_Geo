# CICD_Geo

This project is for developers who want to write applications that can query IP-API,
We shows the data in format via a simple URL-based interface over HTTP, which enables us to use our data directly from a user's browser or from your server.

### Prerequisites

The files we need to install are -
* Python interpreter (version 3.7)
* requests
* pylint

```
* To install requests you have to write that line on your terminal - pipenv install requests.
* To install pylint you have to write that line on your terminal - pip install pylint.
```
### How to install the project - 
1. Clone this repository to your computer by using the command "git clone : https://github.com/Almogma/CICD_Geo.git" 
2. Open the project in your preferred workspace
3. Run Main

Choose feature number 1 -

### Feature num 1 - IP Geolocation - JSON endpoint 

To search with query IP-API you have to write by this format : 
```
The API base path is
http://ip-api.com/json/{query}
```
{query} can be a single IPv4/IPv6 address or a domain name. If you don't supply a query the current IP address will be used.


```
Example - 
Query : 24.48.0.1
response : 
{
  "query": "24.48.0.1",
  "status": "success",
  "country": "Canada",
  "countryCode": "CA",
  "region": "QC",
  "regionName": "Quebec",
  "city": "Montreal",
  "zip": "H1S",
  "lat": 45.5808,
  "lon": -73.5825,
  "timezone": "America/Toronto",
  "isp": "Le Groupe Videotron Ltee",
  "org": "Videotron Ltee",
  "as": "AS5769 Videotron Telecom Ltee"
}
```

Choose feature number 2 -

### Feature num 2 - Client Subnet and DNS server API -  

Call the API by sending HTTP GET requests to
```
http://[32 random alphanumeric characters].edns.ip-api.com/json
```
[32 random alphanumeric characters] - you cant pass the limit of 32 characters.

you can run automatic redirection by this HTTP requests 

```
http://edns.ip-api.com/json
```

```
Example - 
HTTP GET requests - http://edns.ip-api.com/json

response : 
{
    "dns": {
        "ip": "74.125.73.83",
        "geo": "United States - Google"
    },
    "edns": {
        "ip": "91.198.174.0",
        "geo": "Netherlands - Wikimedia Foundation"
    }
}
```

* dns contains the IP address and Geolocation (country, ISP) of the DNS server the client used.

* edns contains the IP address and Geolocation (country, ISP) of the client. If the DNS server did not send the client subnet, the edns field will be be absent.

## information source

* https://ip-api.com/docs/dns
* https://ip-api.com/docs/api:json

## Authors

**[Almog Mahluf](https://github.com/Almogma)** 

**[Alon Gabay](https://github.com/AlonGabbay)** 

* **Almog Mahluf** - *Initial work* - [PurpleBooth]
