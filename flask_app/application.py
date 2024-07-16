from flask import Flask, request, redirect, render_template

import os
import cv2
from datetime import datetime
import numpy as np
import base64


#Flaskオブジェクトの生成
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 文字化け対策
app.debug = True

SAVE_DIR = "./data/upload_data/"

# urlにアクセスしたらindex.htmlを開く
@app.route('/')
def index():
    return render_template('index.html')


# アップロードファイルのデータ処理
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'image' in request.files:
        # 画像ファイルが送信された場合の処理
        image_file = request.files['image']
        if image_file.filename != '':
            # 画像として読み込み
            stream = image_file.stream
            img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
            img = cv2.imdecode(img_array, 1)

            # 画像をエンコードしてbase64に変換
            _, buffer = cv2.imencode('.png', img)
            img_base64 = base64.b64encode(buffer).decode('utf-8')

            # base64エンコードされた画像をテンプレートに渡す
            return render_template('index.html', img_data=img_base64)
        
    # GET リクエストやファイルが送信されていない場合の処理
    return "ファイルがアップロードされていません"

# port=****の部分でポート番号を変更できる。
if __name__ == '__main__':
    #'0.0.0.0'はどんな接続でも受け入れる状態
    app.run(debug=False, host='0.0.0.0', port=8880)