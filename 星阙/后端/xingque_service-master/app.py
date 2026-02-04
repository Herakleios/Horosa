import json
import time
from datetime import datetime

from flask import Flask, request
from kinqimen import kinqimen
from kinliuren import kinliuren
from ichingshifa import ichingshifa
from zh import conv
from calculator_liuren import lib

app = Flask(__name__)


@app.route('/qimen', methods=['POST'])  # 奇门起卦  时家奇门
def qimen():
    params = request.json
    year = params['gua_time']['year']
    month = params['gua_time']['month']
    day = params['gua_time']['day']
    hour = params['gua_time']['hour']
    minute = params['gua_time']['minute']

    dingju = params['gua_type']  # 1 拆补  2 置润

    # 转json
    tic = time.perf_counter()
    res = kinqimen.Qimen(year, month, day, hour, minute, dingju).pan()  # 1:拆補 2:置閏
    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")
    aa = res["神"]
    r = conv.traditional_to_simple(json.dumps(res, ensure_ascii=False))
    return r.replace("武", "玄").replace("禽", "芮").replace("勾","虎").replace("雀","玄").replace("陈", "勾")


@app.route('/liuren', methods=['POST'])  # 六壬起卦
def liuren():
    params = request.json
    year = params['gua_time']['year']
    month = params['gua_time']['month']
    day = params['gua_time']['day']
    hour = params['gua_time']['hour']
    minute = params['gua_time']['minute']

    res = lib.calculate_liuren(datetime(year, month, day, hour, minute))
    # todo 繁体字转简体字
    return conv.traditional_to_simple(json.dumps(lib.old_format(res), ensure_ascii=False))


@app.route('/liuyao', methods=['POST'])  # 六爻起卦
def liuyao():
    # return "success"
    params = request.json

    gua_type = params['gua_type']  # 起卦方式 1 给定值  2 时间起卦
    gua_value = params['lines']  # 手动起卦 需要给到value
    day_ganzhi = params['hseb']["day"]

    if gua_type == 1 or gua_type == 3:
        # 根据主卦变化 得到变化的挂
        change_gua = gua_value.replace("9", "8").replace("6", "7")
        if change_gua == gua_value:
            res = {"本卦": ichingshifa.Iching().decode_gua(gua_value, day_ganzhi, "")}
            res["本卦"]["value"] = gua_value
        else:
            res = ichingshifa.Iching().decode_two_gua(gua_value, change_gua, day_ganzhi)
            res["本卦"]["value"] = gua_value
            res["之卦"]["value"] = change_gua
            res["之卦"]["六親用神"] = ["孙" if x == "子" else x for x in res["之卦"]["六親用神"]]
    else:  # 时间起卦
        gua_time = params['gua_time']
        res = ichingshifa.Iching().qigua_time(gua_time['year'], gua_time['month'], gua_time['day'],
                                              gua_time['hour'], gua_time['minute'])
        res["本卦"]["value"] = res.get("大衍筮法")[0]
        if "之卦" in res:
            res["之卦"]["value"] = res.get("大衍筮法")[0].replace("9", "8").replace("6", "7")
            res["之卦"]["六親用神"] = ["孙" if x == "子" else x for x in res["之卦"]["六親用神"]]

    # todo 繁体字转简体字
    res["本卦"]["六親用神"] = ["孙" if x == "子" else x for x in res["本卦"]["六親用神"]]
    res_str = json.dumps(res, ensure_ascii=False)
    rsp = conv.traditional_to_simple(res_str)

    return rsp.replace("武", "玄").replace("陈", "勾").replace("妻", "财")


@app.route('/')
def hello_world():  # put application's code here
    # year, month, day, hour, minute = 2024, 1, 20, 22, 7
    # res = lib.calculate_liuren(datetime(year, month, day, hour, minute))
    # print(lib.old_format(res))
    # print(res.datetime)
    # print(res.lesson)
    # print(res.shishen)
    # print(json.dumps(res))
    return "res"


if __name__ == '__main__':

    # print(123312)
    # kinqimen.Qimen(2024, 6, 23,  22, 11).di(1)  # 1:拆補 2:置閏
    #
    # kinliuren.Liuren("驚蟄", "二", "己未", "甲午").result(0)
    #
    # kinqimen.Qimen(year, month, day, hour).gpan()(金函日家)
    # kinqimen.Qimen(year, month, day, hour).overall()(時家奇門 + 金函日家)
    app.run()
