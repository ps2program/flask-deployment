from flask import Flask

app = Fask("MyFlaskApp")

@app.route('/', mehtods=["GET"])
def welcome():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run