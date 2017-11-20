# App architecture

The web app is developed using Flask and [SparqlWrapper](https://github.com/RDFLib/sparqlwrapper) library. It is deployed at https://utd-abhyas.appspot.com/. Depending on whether the sparql endpoint is working or not, you will be able to see the actual query visualization. We have used google charts APIs to generate the graphs and maps. Check the report on the about for more details.

The app is deployed on  google app engine.

### About GAE deployment

The details of the app are found in app.yaml. These are used by gae to deploy the app. All required libraries are available in requirements.txt.

Locally, to install libraries in the same directory as the app, do the following:

```
pip install -t lib -r requirements.txt
```
To run locally to test, do: 
```
dev_appserver.py app.yaml
```
To deploy: 
```
gcloud app deploy
```
To browse the deployed version:
```
gcloud app browse
```