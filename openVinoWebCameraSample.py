# coding: utf-8
import sys
import cv2
from openvino.inference_engine import IECore

model_xml='face-detection-adas-0001.xml'
model_bin='face-detection-adas-0001.bin'
device='CPU' #CPU or GPU or MYRIAD
camera_no=0 #1番目に接続されたカメラ
accuracy=0.7

# モデル、処理デバイス設定し、推論エンジンを初期化
core = IECore()
net = core.read_network(model=model_xml, weights=model_bin)
exec_net = core.load_network(network=net, num_requests=1, device_name=device) 

# 映像分析への入出力部分設定
input_blob = next(iter(net.input_info))
out_blob   = next(iter(net.outputs))

# model_xmlからバッチサイズ、色数、画像サイズを取得
model_batch_size, model_channel, model_hight, model_width = net.inputs[input_blob].shape

# カメラから映像を1フレームずつ取得し分析し続ける
cap = cv2.VideoCapture(camera_no)
while cap.isOpened():

    # カメラから画像取得できなければ終了
    ret, frame = cap.read()
    if not ret:
        break

    cap_hight = cap.get(4)
    cap_width = cap.get(3)
    
    # 画像をHWC(縦、横、色(チャネル))からCHW(色(チャネル)、横、縦）に変換
    # モデルの色数、サイズに合わせる
    input_frame = cv2.resize(frame, (model_width, model_hight))
    input_frame = input_frame.transpose((2, 0, 1))  
    input_frame = input_frame.reshape((model_batch_size, model_channel, model_hight, model_width))

    exec_net.start_async(request_id=0, inputs={input_blob: input_frame})

    if exec_net.requests[0].wait(-1) == 0:
        result = exec_net.requests[0].outputs[out_blob]

        for face in result[0][0]:
            if face[2] > accuracy:
                x_min = int(face[3] * cap_width)
                y_min = int(face[4] * cap_hight)
                x_max = int(face[5] * cap_width)
                y_max = int(face[6] * cap_hight)
                class_id = int(face[1])

                # 顔に枠を追加
                color = (255, 0, 0)
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)


    cv2.imshow("face detect", frame)

    # ESCボタンで終了
    key = cv2.waitKey(1)
    if key == 27:
        break
