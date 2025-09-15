from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Backend worker servers
backends = [
    "http://app1:5000",
    "http://app2:5000",
    "http://app3:5000"
]

index = 0  # for round robin

@app.route("/", methods=["GET", "POST"])
def proxy():
    global index
    backend = backends[index]  # choose backend
    index = (index + 1) % len(backends)  # round robin

    # Forward the request
    resp = requests.request(
        method=request.method,
        url=backend + request.full_path,
        headers={key: value for (key, value) in request.headers if key != "Host"},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    # Send response back
    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
