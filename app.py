import config.app as config_app


app = config_app.create_app()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host=config_app.HOST, port=config_app.PORT)
    app.run(debug=True)