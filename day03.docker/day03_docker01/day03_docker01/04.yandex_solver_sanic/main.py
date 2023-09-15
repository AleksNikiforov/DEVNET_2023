from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)


def calculate_sum(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError
    return a + b


@app.route("/")
async def hello(request):
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        result = calculate_sum(int(a), int(b))
    except:
        return json({"status": False, "result": "wrong request"})
    else:
        return json({"status": True, "result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, motd=False, access_log=False)
