# General
My first FLASK crafted Website
## Requirements
+ Please read [Link](requirements.txt)
+ To freeze use: pip freeze requirements.txt
## Target
REST API which provides the AGS Key (Allgemeiner Gemeinde Schlüssel)
1. Get AGS Key by Village/City/District
2. Get Village/City/District by AGS-Key 
## Endpoints
+ /place/*args
+ /key/*args
## Apple
export FLASK_APP=app
## Windows
set FLASK_APP=app

flask run
>Run as fast as you can

## Docker
docker run -d -p 5000:5000 myflaskapp

### Sources 
[Short FLASK Introduction](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

[Flask Introduction Pargt 2](https://www.youtube.com/watch?v=xIgPMguqyws)

[Markup Basic Introduction](https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f)

#Test
1. pytest
2. bandit
3. Thunderclient  -> /APITests_Thunderclient/...

