from flask import Blueprint, render_template
from app.utils.news import get_news_data

news_routes = Blueprint('news_routes', __name__)

API_KEY = 'f9b1bae610174be08b5ed25cda2423ac'

@news_routes.route('/news')
def home():
    news_data = get_news_data(API_KEY)
    return render_template('news.html', news=news_data)
