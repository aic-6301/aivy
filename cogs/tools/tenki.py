import discord
from discord.ext import commands

# 読み込んだら通知
 #@commands.Cog.listener()
     # Cogが読み込まれた時に発動
    # async def on_ready(self):
        # print('天気cogが読み込まれたよ！')
# 天気
# どこを取得するか
citycodes = {
    "北海道":"016010",
    "青森":"020010",
    "岩手":"030010",
    "宮城":"040010",
    "秋田":"050010",
    "山形":"060010",
    "福島":"070010",
    "茨城":"080010",
    "栃木":"090010",
    "群馬":"100010",
    "埼玉":"110010",
    "千葉":"120010",
    "東京":"130010",
    "神奈川":"140010",
    "新潟":"150010",
    "富山":"160010",
    "石川":"170010",
    "福井":"180010",
    "山形":"190010",
    "長野":"200010",
    "岐阜":"210010",
    "静岡":"220010",
    "愛知":"230010",
    "三重":"240010",
    "滋賀":"250010",
    "京都":"260010",
    "大阪":"270000",
    "兵庫":"280010",
    "奈良":"290010",
    "和歌山":"300010",
    "鳥取":"310010",
    "島根":"320010",
    "岡山":"330010",
    "広島":"340010",
    "山口":"350010",
    "徳島":"360010",
    "香川":"370000",
    "愛媛":"380010",
    "高知":"390010",
    "福島":"400010",
    "佐賀":"410010",
    "長崎":"420010",
    "熊本":"430010",
    "大分":"440010",
    "宮崎":"450010",
    "鹿児島":"460010",
    "沖縄":"471010",    
}

 # 取得
    
@bot.event
async def on_message(self,message):
  if message.author != client.user:

    reg_res = re.compile(u"(.+)の天気").search(message.content)
    if reg_res:

      if reg_res.group(1) in citycodes.keys():

        citycode = citycodes[reg_res.group(1)]
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
        resp = json.loads(resp.decode('utf-8'))
# メッセージにして送信
        msg = resp['location']['city']
        msg += "の天気は、\n"
        for f in resp['forecasts']:
          msg += f['dateLabel'] + "が" + f['telop'] + "\n"
        msg += "です。"

        await client.send_message(message.channel, message.author.mention + msg)

      else:
        await client.send_message(message.channel, message.content + "は対応していないか受信ができませんでした。")

        def setup(bot):
     bot.add_cog(tennki(bot)) # GreetingsCogにBotを渡してインスタンス化し、Botにコグとして登録する
