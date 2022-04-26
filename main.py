import discord
import requests
from discord.ext import commands


# 추후 게임 업데이트 시 필요한 부분만 수정하도록 모듈화하기
class Data:
    prefix = "!"
    LANG = "ko"
    default_url = "https://www.bungie.net"
    season_info = [7, "SeasonOfTheRisen"]
    next_season_info = [7, "SeasonOfThe[ENCRYPTED]"]
    version = "4.0.1"
    next_version = "4.0.1.1"
    item_input = ""


client = commands.Bot(command_prefix=Data.prefix)
HEADERS = {"X-API_Key": ''}


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
    channel = client.get_channel(123456789101112131)
    await member.send(f'{client.user.name} 님, 환영합니다.')
    await channel.send('$help 또는 $h 명령어를 입력해 정보를 얻을 수 있습니다.')


# Sending the messages from BOT for members
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 서버 봇 대화체 기본 기능
    if message.content.startswith(Data.prefix + '도움') or message.content.startswith(Data.prefix + 'h'):
        embed = discord.Embed(title="Cerberus", description=Data.version, color=0xC0E6EB)
        embed.add_field(name="버전", value=Data.prefix + "버전", inline=True)
        embed.add_field(name="소식", value=Data.prefix + "소식", inline=True)
        embed.add_field(name="시즌", value=Data.prefix + "시즌, " + Data.prefix + "달력", inline=True)
        embed.add_field(name="레이드", value=Data.prefix + "모집, " + Data.prefix + "화력팀", inline=True)
        embed.add_field(name="아이템", value=Data.prefix + "아이템 {이름}", inline=True)
        embed.set_thumbnail(url="https://i.imgur.com/USmMni8.png")
        await message.channel.send(embed=embed)

    if message.content.startswith(Data.prefix + '클랜'):
        await message.channel.send('서버에 오신 것을 환영합니다.')

    if message.content.startswith(Data.prefix + '버전'):
        embed = discord.Embed(title="데스티니 가디언즈", description="최신 버전", color=0xC0E6EB)
        embed.set_footer(text=Data.version)
        await message.channel.Data(embed=embed)

    # 소식 기능
    if message.content.startswith(Data.prefix + '소식'):
        embed = discord.Embed(title="새 소식", description="번지넷 새 소식에 대한 정보를 불러옵니다.", color=0xC0E6EB)
        embed.add_field(name="test[0]", value="",
                        inline=False)
        await message.channel.send(embed=embed)
        # await message.channel.send('최신 소식은 번지넷 새 소식 탭에서 확인할 수 있습니다.\n' + data.default_url + "/News")

    # 시즌 기능
    if message.content.startswith(Data.prefix + '시즌'):
        embed = discord.Embed(title="데스티니 가디언즈", description=Data.version, color=0xC0E6EB)
        embed.add_field(name="되살아난 자", value="마녀 여왕이 빛을 훔쳤습니다. 그녀의 군체 군단이 전장을 가로질러 진격해 옵니다. "
                        + "화력팀의 힘으로 굴복시키기 전까지 그들은 분노를 멈추지 않을 것입니다. "
                        + "패배한 적의 고스트가 조용히 주위를 맴돕니다. 이 전쟁이 끝나지 않을 것 같은 불길한 예감이 듭니다. "
                        + "숨 돌릴 겨를도 없이, 눈앞에서 군단이 되살아나 다시 진격해 옵니다. "
                        + "조심하세요, 수호자.", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/EMyQKYf.png")
        embed.set_image(url="https://i.imgur.com/uzh0iAC.jpg")
        await message.channel.send(embed=embed)
    # https://www.bungie.net /7/ ko /Seasons/ SeasonOfTheRisen
    # New 17 Season: https://www.bungie.net /7/ ko /Seasons/ SeasonOfThe[ENCRYPTED]

    # 달력 기능
    if message.content.startswith(Data.prefix + '달력'):
        embed = discord.Embed(title="데스티니 가디언즈", description=Data.version, color=0xC0E6EB)
        embed.add_field(name="되살아난 자 시즌", value="2022년 2월 23일 ~ 2022년 5월 25일", inline=False)
        # embed.set_thumbnail(url="https://i.imgur.com/r7O87On.png")
        # embed.set_image(url="https://i.imgur.com/23gfNU0.jpg")
        await message.channel.send(embed=embed)

    # 현재 확장팩 (DLC) 구매 가격 조회
    if message.content.startswith(Data.prefix + '구매') or message.content.startswith(Data.prefix + 'currentDLC'):
        embed = discord.Embed(title="데스티니 가디언즈", description=Data.next_version, color=0xB6D7A8)
        embed.add_field(name="마녀 여왕", value="지금 구매" + "\n\n", inline=False)
        embed.add_field(name="스탠다드 에디션 (44,500원)", value="마녀 여왕 DLC, 왕좌 세계 경이 고스트 의체, 수수께끼 경이 감정 표현, 전설 문양",
                        inline=False)
        embed.add_field(name="디럭스 에디션 (89,000원)", value="스탠다드 에디션 + "
                                                        + "경이 기관단총, 촉매제, 장식, 16~19 시즌 패스, 5년차 던전 2종, 왕좌 세계 경이 참새",
                        inline=False)
        embed.add_field(name="디럭스 에디션 30주년 번들 (109,000원)", value="디럭스 에디션 + "
                        + "새로운 던전, 걀라르호른 경이 로켓 발사기, 촉매제, 장식, 과거 번지 세계에서 영감을 받아 제작된 새로운 무기, "
                        + "가시 방어구 세트, 번지 스트릿패션 장식 세트, 마라톤 테마 장식 세트, 특별한 헬멧 장식, "
                        + "경이 참새, 경이 우주선, 문양, 안료, 감정표현 등", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/USmMni8.png")
        embed.set_image(url="https://i.imgur.com/SATEVfl.jpg")
        await message.channel.send(embed=embed)

    # 레이드 기능
    if message.content.startswith(Data.prefix + '모집'):
        # 특정 채널에다가 모집 투표 글 업로드
        await message.channel.send()

    # 아이템 검색 기능
    if message.content.startswith(Data.prefix + '아이템' + Data.item_input):
        embed = discord.Embed(title="데스티니 가디언즈", description=Data.version, color=0xC0E6EB)
        embed.add_field(name=Data.item_input, value="", inline=False)

    # 암상인 줄 기능
    if message.content.startswith(Data.prefix + '줄'):
        xur_url = "https://www.bungie.net/Platform/Destiny/Advisors/Xur/"
        typehash = 6
        r = requests.get(xur_url, headers=HEADERS)

        print("\n\n\n번지넷에 연결 중입니다: " + xur_url + "\n")
        print("데이터를 불러오고 있습니다: 암상인 줄의 인벤토리")

        error_stat = r.json()['ErrorStatus']
        print("ErrorStatus: " + error_stat + "\n")

        r = requests.get(xur_url, headers=HEADERS)

        for saleItem in r.json()['Response']['data']['saleItemCategories']:
            my_sale_items = saleItem['saleItems']

            for my_item in my_sale_items:
                hash_id = str(my_item['item']['itemHash'])
                # [Working in progress]
                return hash_id

        base_url = Data.default_url + "/platform/Destiny/"

        for saleItem in r.json()['Response']['data']['saleItemCategories']:
            my_sale_items = saleItem['saleItems']

            for myItem in my_sale_items:
                hash_id = str(myItem['item']['itemHash'])
                hash_request_string = base_url + "Manifest/" + str(typehash) + "/" + hash_id
                res = requests.get(hash_request_string, headers=HEADERS)
                item_name = res.json()['Response']['data']['inventoryItem']['itemName']
                await message.channel.send(item_name)


# 디스코드 서버 봇 클라이언트 구동
client.run('..')
