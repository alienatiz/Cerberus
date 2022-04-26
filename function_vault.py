import discord
from discord import message

import main
import requests
from discord.ext import commands

# Declare the Data class from main.py
Data = main.Data()
client = commands.Bot(command_prefix=Data.prefix)
HEADERS = {"X-API_Key": ''}

# Debugging log
# print(url)
# html = urlopen(url)
# bsobject = BeautifulSoup(html, "html.parser")
# tempfile = bsobject.find_all()
# print(tempfile)

# 다음 확장팩 (DLC) 조회
if message.content.startswith(Data.prefix + 'DLC'):
    embed = discord.Embed(title="데스티니 가디언즈", description=Data.next_version, color=0xB6D7A8)
    embed.add_field(name="마녀 여왕", value="2022년 2월 23일 이용 가능" + "\n\n"
                    + "형체들의 자매, 검 파괴자, 마녀 여왕 – 그대들이 내 이야기를 엮으며 붙여준 나의 이름이다. "
                    + "내 안뜰에서 내가 선사한 빛을 숭배하는 자들 사이를 신중히 거닐어 보았음에도, "
                    + "아직도 이 힘의 가치를 부정하느냐?"
                    + "그들의 흔들리는 목소리를 들어라. 그리고 너의 심장에서 벼려낸 그 강철을 들고 스스로 물어라. "
                    + "널 휘두르는 것은 무엇인가?" + "\n\n" + "난 너를 기다린다, 수호자. "
                    + "\n" + "나의 왕좌 세계로 와서 진실을 마주하라.", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/USmMni8.png")
    embed.set_image(url="https://i.imgur.com/SATEVfl.jpg")
    await message.channel.send(embed=embed)

# 다음 확장팩 (DLC) 예약구매 가격 조회
if message.content.startswith(Data.prefix + '예약구매') or message.content.startswith(Data.prefix + 'preorderDLC'):
    embed = discord.Embed(title="데스티니 가디언즈", description=Data.next_version, color=0xB6D7A8)
    embed.add_field(name="마녀 여왕", value="2022년 2월 23일 이용 가능" + "\n\n", inline=False)
    embed.add_field(name="스탠다드 에디션 (44,500원)", value="마녀 여왕 DLC, 왕좌 세계 경이 고스트 의체, 수수께끼 경이 감정 표현, 전설 문양",
                    inline=False)
    embed.add_field(name="디럭스 에디션 (89,000원)", value="스탠다드 에디션 + "
                    + "경이 기관단총, 촉매제, 장식, 16~19 시즌 패스, 5년차 던전 2종, 왕좌 세계 경이 참새", inline=False)
    embed.add_field(name="디럭스 에디션 30주년 번들 (109,000원)", value="디럭스 에디션 + "
                    + "새로운 던전, 걀라르호른 경이 로켓 발사기, 촉매제, 장식, 과거 번지 세계에서 영감을 받아 제작된 새로운 무기, "
                    + "가시 방어구 세트, 번지 스트릿패션 장식 세트, 마라톤 테마 장식 세트, 특별한 헬멧 장식, "
                    + "경이 참새, 경이 우주선, 문양, 안료, 감정표현 등", inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/USmMni8.png")
    embed.set_image(url="https://i.imgur.com/SATEVfl.jpg")
    await message.channel.send(embed=embed)
