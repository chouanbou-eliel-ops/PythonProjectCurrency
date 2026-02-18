import yfinance as yf
from app.extensions import db
from app.models.conversion import Conversion

def get_rate(from_currency, to_currency):
    try:
        pair = f"{from_currency}{to_currency}=X"
        data = yf.Ticker(pair)
        rate = data.history(period="1d")["Close"].iloc[-1]
        return float(rate)
    except Exception as e:
        print("Erreur d'API",e)
        return None

def save_conversion(user_id, from_currency, to_currency, rate):
    conversion = Conversion(
        from_currency=from_currency,
        to_currency=to_currency,
        rate=rate,
        user_id=user_id,

    )
    db.session.add(conversion)
    db.session.commit()

def get_conversion(user_id, from_currency, to_currency, rate):
    conversion = Conversion(
        from_currency=from_currency,
        to_currency=to_currency,
        rate=rate,
        user_id=user_id
    )

def convert_currency(user_id, from_currency, to_currency):
    try:
        pair = f"{from_currency}{to_currency}=X"
        data = yf.Ticker(pair)
        rate = data.info['regularMarketPrice']
        conversion = Conversion(
            from_currency=from_currency,
            to_currency=to_currency,
            rate=rate,
            user_id=user_id,
            type = "cov"
        )
        if rate is None:
            return None
        return conversion
    except Exception as e:
        print("Erreur d'API",e)
        return None


#rate = data.history(period="1d", interval="1d")["Close"].iloc[-1]