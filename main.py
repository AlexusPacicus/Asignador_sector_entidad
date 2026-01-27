from graph.graph import app

state = {
    "url": "http://bbva-login.com"
}

print(app.invoke(state))
