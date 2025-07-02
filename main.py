from proton import App, html

app = App()

@app.route("/")
def home():
    return html("Hello, World from Proton on EC2!")

app.run()
