import discord
from discord.ext import commands
import requests


# 추후 게임 업데이트 시 필요한 부분만 수정하도록 모듈화하기
class data:
    prefix = "!"
    LANG = "ko"
    default_url = "https://www.bungie.net"
    season_info = [7, "SeasonOfTheLost"]
    version = "3.4.0.2"
    next_version = "4.0.0"
    item_input = ""


client = commands.Bot(command_prefix=data.prefix)
HEADERS = {"X-API_Key": ''}


# Debugging log
# print(url)
# html = urlopen(url)
# bsobject = BeautifulSoup(html, "html.parser")
# tempfile = bsobject.find_all()
# print(tempfile)


# Running Destiny Guardians
@client.event
async def on_ready():
    # 서버 봇을 서버로 입장시키면 아래 메시지가 출력됩니다
    print(f'{client.user} has connected to Discord!')
    print(client.user.name)
    print(client.user.id)


# Coming the new members in the server
@client.event
async def on_member_join(member):
    # 새로운 멤버가 입장하면 아래 내용을 출력합니다.
    channel = client.get_channel(746781653002616863)
    await member.send(f'{client.user.name} 님, 환영합니다.')
    await channel.send('$help 또는 $h 명령어를 입력해 정보를 얻을 수 있습니다.')


# Sending the messages from BOT for members
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 서버 봇 대화체 기본 기능
    if message.content.startswith(data.prefix + '도움') or message.content.startswith(data.prefix + 'h'):
        embed = discord.Embed(title="Cerberus", description=data.version, color=0xC0E6EB)
        embed.add_field(name="버전", value=data.prefix + "버전", inline=True)
        embed.add_field(name="소식", value=data.prefix + "소식", inline=True)
        embed.add_field(name="시즌", value=data.prefix + "시즌, " + data.prefix + "달력", inline=True)
        embed.add_field(name="레이드", value=data.prefix + "모집, " + data.prefix + "화력팀", inline=True)
        embed.add_field(name="아이템", value=data.prefix + "아이템 {이름}", inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/gUg8zIm.png")
        await message.channel.send(embed=embed)

    if message.content.startswith(data.prefix + '클랜'):
        await message.channel.send('서버에 오신 것을 환영합니다.')

    if message.content.startswith(data.prefix + '버전'):
        embed = discord.Embed(title="데스티니 가디언즈", description="최신 버전", color=0xC0E6EB)
        embed.set_footer(text=data.version)
        await message.channel.send(embed=embed)

    # 소식 기능
    if message.content.startswith(data.prefix + '소식'):
        embed = discord.Embed(title="새 소식", description="번지넷 새 소식에 대한 정보를 불러옵니다.", color=0xC0E6EB)
        embed.add_field(name="test[0]", value="",
                        inline=False)
        await message.channel.send(embed=embed)
        # await message.channel.send('최신 소식은 번지넷 새 소식 탭에서 확인할 수 있습니다.\n' + data.default_url + "/News")

    # 시즌 기능
    if message.content.startswith(data.prefix + '시즌'):
        embed = discord.Embed(title="데스티니 가디언즈", description=data.version, color=0xC0E6EB)
        embed.add_field(name="귀환", value="각성자의 여왕 마라 소프. 그녀가 없는 동안 상상할 수 없을 만큼 많은 일들이 일어났습니다. "
                        + "영원히 잠들었던 그녀의 남동생은 이제 수호자들 사이에서 새로운 이름으로 불리고 있고, "
                        + "시부 아라스의 병력은 검은 함대 아래 집결했으며, 끝없는 밤의 배후에 있던 사바툰이 모습을 드러냈습니다."
                        + "그리고 이제, 오랫동안 기다려온 태양 빛 아래, 마라 소프가 꿈의 도시로 돌아옵니다. "
                        + "그리고 마녀 여왕과의 대면을 고대하고 있습니다.", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/EMyQKYf.png")
        embed.set_image(url="https://i.imgur.com/uzh0iAC.jpg")
        await message.channel.send(embed=embed)
    # https://www.bungie.net /7/ ko /Seasons/ SeasonOfTheLost

    # 달력 기능
    if message.content.startswith(data.prefix + '달력'):
        embed = discord.Embed(title="데스티니 가디언즈", description=data.version, color=0xC0E6EB)
        embed.add_field(name="잃어버린 자 시즌", value="2021년 8월 25일 ~ 2022년 2월 23일", inline=False)
        # embed.set_thumbnail(url="https://i.imgur.com/r7O87On.png")
        # embed.set_image(url="https://i.imgur.com/23gfNU0.jpg")
        await message.channel.send(embed=embed)

    # 다음 확장팩 (DLC) 조회
    if message.content.startswith(data.prefix + 'DLC'):
        embed = discord.Embed(title="데스티니 가디언즈", description=data.next_version, color=0xB6D7A8)
        embed.add_field(name="마녀 여왕", value="2022년 2월 23일 이용 가능" + "\n\n"
                        + "형체들의 자매, 검 파괴자, 마녀 여왕 – 그대들이 내 이야기를 엮으며 붙여준 나의 이름이다. "
                        + "내 안뜰에서 내가 선사한 빛을 숭배하는 자들 사이를 신중히 거닐어 보았음에도, "
                        + "아직도 이 힘의 가치를 부정하느냐?"
                        + "그들의 흔들리는 목소리를 들어라. 그리고 너의 심장에서 벼려낸 그 강철을 들고 스스로 물어라. "
                        + "널 휘두르는 것은 무엇인가?" + "\n\n" + "난 너를 기다린다, 수호자. "
                        + "\n" + "나의 왕좌 세계로 와서 진실을 마주하라.", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/gUg8zIm.png")
        embed.set_image(url="https://i.imgur.com/EmzlFGB.jpg")
        await message.channel.send(embed=embed)

    # 다음 확장팩 (DLC) 예약구매 가격 조회
    if message.content.startswith(data.prefix + '예약구매') or message.content.startswith(data.prefix + '예구'):
        embed = discord.Embed(title="데스티니 가디언즈", description=data.next_version, color=0xB6D7A8)
        embed.add_field(name="마녀 여왕", value="2022년 2월 23일 이용 가능" + "\n\n", inline=False)
        embed.add_field(name="스탠다드 에디션 (44,500원)", value="마녀 여왕 DLC, 왕좌 세계 경이 고스트 의체, 수수께끼 경이 감정 표현, 전설 문양",
                        inline=False)
        embed.add_field(name="디럭스 에디션 (89,000원)", value="스탠다드 에디션 + "
                        + "경이 기관단총, 촉매제, 장식, 16~19 시즌 패스, 5년차 던전 2종, 왕좌 세계 경이 참새", inline=False)
        embed.add_field(name="디럭스 에디션 30주년 번들 (109,000원)", value="디럭스 에디션 + "
                        + "새로운 던전, 걀라르호른 경이 로켓 발사기, 촉매제, 장식, 과거 번지 세계에서 영감을 받아 제작된 새로운 무기, "
                        + "가시 방어구 세트, 번지 스트릿패션 장식 세트, 마라톤 테마 장식 세트, 특별한 헬멧 장식, "
                        + "경이 참새, 경이 우주선, 문양, 안료, 감정표현 등", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/gUg8zIm.png")
        embed.set_image(url="https://i.imgur.com/EmzlFGB.jpg")
        await message.channel.send(embed=embed)

    # 레이드 기능
    if message.content.startswith(data.prefix + '모집'):
        # 특정 채널에다가 모집 투표 글 업로드
        await message.channel.send()

    # 아이템 검색 기능
    if message.content.startswith(data.prefix + '아이템' + data.item_input):
        embed = discord.Embed(title="데스티니 가디언즈", description=data.version, color=0xC0E6EB)
        embed.add_field(name=data.item_input, value="", inline=False)

    # 암상인 줄 기능
    if message.content.startswith(data.prefix + '줄'):
        xur_url = "https://www.bungie.net/Platform/Destiny/Advisors/Xur/"
        hashType = 6
        r = requests.get(xur_url, headers=HEADERS)

        print("\n\n\n번지넷에 연결 중입니다: " + xur_url + "\n")
        print("데이터를 불러오고 있습니다: 암상인 줄의 인벤토리")

        error_stat = r.json()['ErrorStatus']
        print("ErrorStatus: " + error_stat + "\n")

        r = requests.get(xur_url, headers=HEADERS)

        for saleItem in r.json()['Response']['data']['saleItemCategories']:
            mysaleItems = saleItem['saleItems']

            for myItem in mysaleItems:
                hashID = str(myItem['item']['itemHash'])

        base_url = data.default_url + "/platform/Destiny/"

        for saleItem in r.json()['Response']['data']['saleItemCategories']:
            mysaleItems = saleItem['saleItems']

            for myItem in mysaleItems:
                hashID = str(myItem['item']['itemHash'])
                hashReqString = base_url + "Manifest/" + hashType + "/" + hashID
                res = requests.get(hashReqString, headers=HEADERS)
                item_name = res.json()['Response']['data']['inventoryItem']['itemName']
                await message.channel.send(item_name)

# 디스코드 서버 봇 클라이언트 구동
client.run('..')