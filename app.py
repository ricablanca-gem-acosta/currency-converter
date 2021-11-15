from datetime import datetime, timedelta
from flask import Flask, render_template, request
from model import currencies, rate

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    currencyDict=currencies()
    max_date = datetime.today().strftime("%Y-%m-%d")
    select_date = request.form.get("date") or (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")
    from_currency = request.form.get("from") or "eur"
    to_currency = request.form.get("to") or "eur"
    try:
        ratio = rate(select_date, from_currency, to_currency)
        conversion = "1 {fro} = {rate} {to}".format(fro=currencyDict[from_currency], rate=ratio, to=currencyDict[to_currency])
    except:
        conversion = "Conversion not available at this time"
    return render_template(
        "home.html",
        currencies=currencyDict,
        min_date="2020-11-22",
        max_date=max_date,
        select_date=select_date,
        from_currency=from_currency,
        to_currency=to_currency,
        conversion=conversion
    )
