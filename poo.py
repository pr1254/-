import discord
import asyncio

client = discord.Client()

token = "ODAxOTk5NTc4OTc4NzEzNjAw.YAo2UA.uJoARLAlalT2glOcN5Q5UXx-D5Y"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('<도움말')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("안녕하세요")
    
    if message.content =="<도움말":
        embed = discord.Embed(title="푸른아이 도움말", color=0x00ff00)
        embed.add_field(name="청소 기능", value="<청소 (숫자) 입력",inline=True)
        embed.add_field(name="1", value="1",inline=True)
        embed.add_field(name="1", value="1",inline=True) 
        embed.add_field(name="1", value="1",inline=True)
        embed.set_footer(text="1")
        await message.channel.send(embed=embed)

    if message.content.startswith("<청소"):
        number =int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료!")

client.run(token)