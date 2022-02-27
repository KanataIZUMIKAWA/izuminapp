from cgitb import reset
from sys import platlibdir
from turtle import title
from django.shortcuts import render
from izuminapp.forms import FirstviewForm
from izuminapp.model import Oldjson, Player, Firstview, Siteinfo
import requests
import datetime
import json

EMC_API_URL = "https://earthmc-api.herokuapp.com/api/v1"
UUID_API_URL = "https://api.mojang.com/users/profiles/minecraft/"
NUMBER_OF_FIRSTVIEWS = 5
ERROR_JSON = '{"population":"error","area":"error","king":"error","capitalName":"error","skin":"error"}'
primary = ["RyoK3", "KATA2000", "sakira1996", "raimu569", "hiroshi4872", "ramuate"]

def root(request):
    return render(request, 'izuminapp/root.html')

def inca(request):
    inca_info = {}


    # ファーストビューの処理
    firstviews = Firstview.objects.order_by('?')[:min(Firstview.objects.count(), NUMBER_OF_FIRSTVIEWS)]     # ランダムにNUMBER_OF_FIRSTVIEWS個取り出す
    firstviews = list(firstviews.values())
    inca_info["images"] = [d.get('image') for d in firstviews]
    inca_info["clTitle"] = [d.get('title') for d in firstviews]
    inca_info["clPlayers"] = [d.get('player') for d in firstviews]


    # APIの処理
    try :
        nations = requests.get(EMC_API_URL + "/nations/Inca_Empire")
    except Exception :      # ProxyErrorなら
        # jsonアーカイブからのアーカイブを読み込み
        inca_info["ableAPI"] = False
        newOldjson, _ = Oldjson.objects.get_or_create(pk = 0, defaults = {"nations" : ERROR_JSON})
        inca_info.update(dict(json.loads(newOldjson.nations)))      # 辞書型の結合

    else :      #正常にAPIを取得できたら
        inca_info["ableAPI"] = True
        if nations.status_code == 200 :
            # nationデータの取得
            nations_info = dict(nations.json())
            nations_info["population"] = len(nations_info["residents"])     # 人口の取得

            # スキンの取得
            king_uuid = requests.get(UUID_API_URL + nations_info["king"])
            if king_uuid.status_code == 200 :
                nations_info["skin"] = dict(king_uuid.json())["id"]
            
            inca_info.update(nations_info)      # 辞書型の結合

            # 国民の登録
            online = requests.get(EMC_API_URL + "/online")
            for player in nations_info["residents"] :
                newPlayer, _ = Player.objects.get_or_create(name = player, defaults = {"name" : player})
                if player in primary :      # 大臣なら
                    newPlayer.primary = True
                else :
                    newPlayer.primary = False
                
                # onlineカラムの切り替え
                if online.status_code == 200 :
                    online_info = online.json()
                    online_players = [d.get('name') for d in online_info]
                    if player in online_players :
                        newPlayer.online = True
                    else :
                        newPlayer.online = False
                newPlayer.save()

            # jsonのアーカイブ
            newOldjson, _ = Oldjson.objects.update_or_create(pk = 0, defaults = {"nations" : json.dumps(nations_info)})
            if newOldjson.nations == ERROR_JSON :
                newOldjson.nations = json.dumps(nations_info)
                newOldjson.save()

        # jsonアーカイブからのアーカイブを読み込み
        else :      # EMCサーバー側の問題なら
            inca_info["ableAPI"] = False
            newOldjson, _ = Oldjson.objects.get_or_create(pk = 0, defaults = {"nations" : ERROR_JSON})
            inca_info.update(dict(json.loads(newOldjson.nations)))

    return render(request, 'inca/inca.html', inca_info)

def applyimage(request) :
    result = {}
    if request.method == 'POST':
        newImage = request.FILES.get("image")
        newtitle = request.POST["title"]
        newPlayer = request.POST["player"]
        firstview = Firstview.objects.create(image = newImage, title = newtitle, player = newPlayer)
        firstview.save()
        result["title"] = newtitle
    else :
        result["title"] = "upload images..."

    form = FirstviewForm()
    result["form"] = form
    return render(request, 'inca/applyimage.html', result)