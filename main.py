from graph.graph import app

state = {
    "url": "http://bbva-login.com",
    "is_spanish": True,
    "entity_id": None
}

print(app.invoke(state))
