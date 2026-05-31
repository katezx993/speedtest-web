from flask import Flask, render_template, Response
import speedtest
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run")
def run_test():
    def generate():
        try:
            yield f"data: {json.dumps({'phase': 'finding', 'msg': 'กำลังค้นหาเซิร์ฟเวอร์...'})}\n\n"
            st = speedtest.Speedtest(timeout=20)
            best = st.get_best_server()
            server = st.results.server
            client = st.results.client
            yield f"data: {json.dumps({'phase': 'server', 'msg': server.get('name','?'), 'isp': client.get('isp','?'), 'ip': client.get('ip','?')})}\n\n"
            ping = round(best.get("latency", st.results.ping))
            yield f"data: {json.dumps({'phase': 'ping', 'ping': ping})}\n\n"
            yield f"data: {json.dumps({'phase': 'downloading', 'msg': 'กำลังวัด Download...'})}\n\n"
            dl = st.download() / 1_000_000
            yield f"data: {json.dumps({'phase': 'download_done', 'download': round(dl, 2)})}\n\n"
            yield f"data: {json.dumps({'phase': 'uploading', 'msg': 'กำลังวัด Upload...'})}\n\n"
            ul = st.upload() / 1_000_000
            yield f"data: {json.dumps({'phase': 'done', 'download': round(dl,2), 'upload': round(ul,2), 'ping': ping, 'isp': client.get('isp','?'), 'ip': client.get('ip','?'), 'server': server.get('name','?')})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'phase': 'error', 'msg': str(e)})}\n\n"
    return Response(generate(), mimetype="text/event-stream", headers={"Cache-Control": "no-cache"})

if __name__ == "__main__":
    app.run(debug=True)
