from fastapi import FastAPI


def create_app():
    app = FastAPI()
    app.state.my_state = False

    @app.get("/my_state/")
    def return_my_state():
        return {"state": app.state.my_state}

    @app.post("/my_state/")
    def set_my_state(content: dict):
        app.state.my_state = content["set"]

    return app


app = create_app()
