# OpenVino_sample

OpenVinoを利用したwebカメラから顔認識するサンプルを作成しました。
接続されたwebカメラの映像を表示し、その映像の中に人物の顔がある場合四角で囲みます。

## 環境構築

以下のページよりWindows用のOpenVinoをダウンロード
※個人情報の入力が必要
https://software.seek.intel.com/openvino-toolkit

ダウンロードしたexeを実行しOpenVinoをインストール

以下のページよりPython 3.8.12(x64)をダウンロード
https://www.python.org/downloads/windows/

ダウンロードしたexeを実行しPythonをインストール

以下のコマンドでpipを更新
python.exe -m pip install --upgrade pip

以下のコマンドでモデルオプティマイザー(ネットワークの中間表現(IR)を生成するツール)をインストール
C:\Program Files (x86)\Intel\openvino_2021\deployment_tools\model_optimizer\install_prerequisites\install_prerequisites.bat

以下のコマンドで顔認証用のモデルをダウンロード
C:\Program Files (x86)\Intel\openvino_2021.4.689\deployment_tools\tools\model_downloader>python downloader.py --name face-detection-adas-0001

以下のフォルダにモデルが保存される
C:\Program Files (x86)\Intel\openvino_2021.4.689\deployment_tools\open_model_zoo\tools\downloader\intel\face-detection-adas-0001\FP32

保存された以下のファイルをopenVinoWebCameraSample.pyと同じフォルダへコピー
face-detection-adas-0001.xml
face-detection-adas-0001.bin

# 実行方法

以下のコマンドで実行
"C:\Program Files (x86)\Intel\openvino_2021\bin\setupvars.bat"
python openVinoWebCameraSample.py