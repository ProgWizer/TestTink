from flask import Flask, request, render_template
from tinkoff_portfolio_bot.tinkoff_client import get_portfolio_info

app = Flask(__name__)

@app.route("/portfolio")
def portfolio_page():
    return render_template("portfolio.html")

@app.route("/api/portfolio")
def api_portfolio():
    user_id = request.args.get("user_id", type=int)
    if not user_id:
        return "Не передан Telegram ID", 400
    return get_portfolio_info(user_id)
