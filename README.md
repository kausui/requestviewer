# Request Viewer
Request Viewer is an web app that can the followings:
- View headers of HTTP request
- Test some HTTP request/response
 
# Requirement
See requirements.txt file.

# Installation
## Local
```bash
git clone https://github.com/kausui/requestviewer.git
cd requestviewer
pip install -r requirements.txt
python manage.py runserver
```
## Azure Web App
```bash
git clone https://github.com/kausui/requestviewer.git
cd requestviewer
az webapp up --resource-group "resource_group-name" --name "app-name" --location "eastus" --sku "P1V2"
```

# Usage
## URLs
All URL paths are handled as just a URL path request except the followings.

| Path           | Note                           |
|----------------|--------------------------------|
| /favicon.ico   | Response is always 404         |
| \*basicauth/\* | Basic authentication required. |

Default Basic Auth username and password:

USERNAME = user

PASSWORD = 12345678

## Parameters
Sample URL with parameters

https://your-fqdn.com/hoge/path?sleep=5&no-content-type=1&status=404

| Parameter       | Usage                                                    |
|-----------------|----------------------------------------------------------|
| sleep           | Delay for response(second).                              |
| no-content-type | No content type in response. Default value is text/html. |
| status | Status code of response. Default value is 200.           |

# License
"Request Viewer" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).