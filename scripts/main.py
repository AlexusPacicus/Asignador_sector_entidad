from graph.graph import app

tests = [
    "http://bbva-login.com",
    "http://login-seguro.com",
    "http://bbvaseguro.com",
    "http://correos-aviso.com",
    "",  # inválido
]

for url in tests:
    print("TEST:", url)
    state = {"url": url} if url else {}
    print(app.invoke(state))
    print("-" * 40)
