import discord
import openpyxl as openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
      await message.channel.send("그랭")
    if message.content.startswith("씨발"):
      await message.channel.send("새끼야")
    if message.content.startswith("이현호병신"):
      await message.channel.send("씹인정")
    if message.content.startswith("히오스"):
      await message.channel.send("개씹갓겜")
      await message.channel.send("https://heroesofthestorm.com/ko-kr/")
    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("랭크"):
        file = openpyxl.load_workbook("랭크.xlsx")
        sheet = file.active
        exp = [10,20,30,40,50]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.channel.send("승급하였습니다.Wn현재 랭크 : " + str(sheet["C" + str(i)].value ) + "Wn포인트 : " + str(sheet["B" + str(i)].value))
                file.save("랭크.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                 sheet["A" + str(i)].value = str(message.author.id)
                 sheet["B" + str(i)].value = 0
                 sheet["C" + str(i)].value = 1
                 file.save("랭크.xlsx")
                 break

            i += 1



client.run("NTk2OTE1MDY0MTI5MzIzMDQz.XSAfEg.m-mbv-F9pw5AYRE0TRAslGHDk3k")