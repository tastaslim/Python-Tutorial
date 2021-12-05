import falcon
import json
import requests
baseUrl = "https://rickandmortyapi.com/api"


class FalconTest:
    @staticmethod
    def on_get_bar(req, resp):
        response = requests.get(
            f"{baseUrl}/character/2", headers={"Content-Type": "application/json"}).json()
        resp.data = response
        resp.status = falcon.HTTP_200

    @staticmethod
    def on_get_demo(req, resp):
        resp.text = json.dumps(
            {"author": "Jack", "name": "Pirates"})
        resp.status = falcon.HTTP_200


app = application = falcon.App()
app.add_route("/demo", FalconTest(), suffix="demo")
app.add_route("/bar", FalconTest(), suffix="bar")
