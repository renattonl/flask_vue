from datetime import datetime, timedelta


def normalize_data(data):
    return {k: v for k, v in data.items() if v is not None}


def get_yesterday_date():
    return datetime.utcnow() - timedelta(1)


def get_today_date():
    return datetime.utcnow()


def get_formatted_date(date):
    return datetime.strftime(date, "%Y-%m-%d")
