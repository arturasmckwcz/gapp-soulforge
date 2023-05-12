import os
from flask import Flask, render_template

from console import log
from graphql.get_graphql_data import get_graphql_data
from manager.manager import run_timepulse


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return {"message": "The SoulForge is up and running"}

    @app.route("/start_timepulse", methods=["GET"])
    def start_timepulse():
        if run_timepulse.is_running():
            return {"message": "The SoulForge is already listening to the Timepulse"}

        run_timepulse.start()
        return {"message": "The SoulForge has started listening to the Timepulse"}

    @app.route("/stop_timepulse", methods=["GET"])
    def stop_timepulse():
        if not run_timepulse.is_running():
            return {
                "message": "The SoulForge has already stopped listening to the Timepulse"
            }

        run_timepulse.start()
        return {"message": "The The SoulForge has stopped listening to the Timepulse"}

    @app.route("/test_graphql", methods=["GET"])
    def test_graphql():
        query = """
        {
            persons {
                id
                name
                place {
                    address
                }
                placeOfBirth {
                    address
                }
            }
        }
        """
        data = get_graphql_data(query)
        log("data is of type:", type(data))
        return render_template("graphql_test.html", data=data)

    return app


if __name__ == "__main__":
    port = os.environ.get("PORT") or 3000
    create_app().run(host="0.0.0.0", port=port)
