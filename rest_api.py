from flask import Flask, jsonify, request, Response
from supabase import create_client, Client
from gevent.pywsgi import WSGIServer


app = Flask(__name__)
app.debug = False
app.config['FLASK_ENV'] = 'production'

url: str = "supabase address"
key: str = "supabase secret key"
supabase: Client = create_client(url, key)

@app.route('/')
def index():
    return "welcome to web3loc daily tasks api service"

@app.route('/top20')
def articles_list():
    data = supabase.table("articles").select("*").order("created_at",desc=True).limit(20).execute()
    return jsonify(data.data)

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

