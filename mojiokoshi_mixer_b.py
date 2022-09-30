import speech_recognition as sr #音声認識用のライブラリ
import datetime as dt
import threading #Pythonでは基本は逐次処理なので、並列処理用の用のライブラリをimport
mic = sr.Microphone(device_index=2) #ステレオミキサー指定 ※print(sr.Microphone.list_microphone_names())でデバイス候補の確認/マイク入力はsr.Microphone()でOK

r = sr.Recognizer() #言葉を認識するオブジェクト
mic = sr.Microphone() #マイクオブジェクト
result_list = [] #データを格納するリスト
endFlag = False #記録終了フラグ
lock = threading.RLock() #ロックオブジェクトの生成

def speechToText(): #マイクから音声を取り込み続ける
    print("記録を開始しました。")
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source) #ノイズ対応
            audio  = r.listen(source) #オーディオファイルに変換
        threading.Thread(target=speechRecognize,args=(lock,audio)).start()
        if endFlag == True:
            break
    print("プログラム終了")

def speechRecognize(lock,audio): #音声を認識し文字列に変換する
    global endFlag
    if endFlag == True: #記録を終了と言われた場合は認識を行わない
        return
    with lock:
        try:
            print ("認識中",end="\r")
            result = r.recognize_google(audio, language='ja-JP')#音声を文字に変換
            now = dt.datetime.today()
            if result == "記録を終了": 
                endFlag = True
            else:
                print(str(now)+" "+result) #認識結果を表示
                result_list.append([now,result])#入力したデータをリスト形式で追加
        except:#例外処理（何もしない）
            pass

speechToText()#メイン処理