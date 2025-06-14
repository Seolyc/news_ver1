import requests
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Flask 앱 생성
app = Flask(__name__)
CORS(app) # 다른 도메인(프론트엔드)에서의 요청을 허용 (CORS 처리)

# NewsAPI 설정
NEWS_API_KEY = 'a3105a0a4528453da72b249eecca1324'  # 1단계에서 발급받은 본인의 API 키를 입력하세요.
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    """메인 HTML 페이지를 렌더링합니다."""
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    """NewsAPI로부터 최신 뉴스를 가져와 JSON 형태로 반환합니다."""
    params = {
        'country': 'kr',  # 대한민국 뉴스를 가져옵니다.
        'apiKey': NEWS_API_KEY
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status() # 오류가 발생하면 예외를 발생시킴
        news_data = response.json()
        return jsonify(news_data)
    except requests.exceptions.RequestException as e:
        # API 요청 중 에러 발생 시
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)