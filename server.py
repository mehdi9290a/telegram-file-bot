from flask import Flask, send_from_directory
import os

app = Flask(__name__)

FILES_DIR = "files"
os.makedirs(FILES_DIR, exist_ok=True)

@app.route('/files/<path:filename>')
def download_file(filename):
    return send_from_directory(FILES_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
