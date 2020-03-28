import discord
import asyncio
import random
import openpyxl
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
from bs4 import BeautifulSoup
import os
import sys
import json
from selenium import webdriver
import time
import datetime
from urllib.request import urlopen

client = discord.Client()

@client.event
async def on_ready():
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
      if message.author==client.user:
                return          
      if message.content.startswith("/명령어 리스트"):
            embed = discord.Embed(title = "명령어 리스트")
            embed.add_field(name="안녕", value="인사", inline=False)
            embed.add_field(name="/링크", value="애국가", inline=False)
            embed.add_field(name="/소련", value="소오오오오오련", inline=False)
            embed.add_field(name="/크루유튜브", value="MrtyPlayerCrew`s Youtube", inline=False)
            await message.channel.send(embed=embed)
              
      if message.content.startswith("안녕"):
            await message.channel.send("안녕하세요.")

      if message.content.startswith("/링크"):
            await message.channel.send('https://www.youtube.com/watch?v=n6WaTObHRJM')

      if message.content.startswith("/뮤트"):
            author = message.guild.get_member(int(message.content[4:22]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.add_roles(role)
            await message.channel.purge(limit=1)
            await message.channel.send(str(author) + "의 채팅을 현시간부로 금지합니다.")
                 
      if message.content.startswith("/언뮤트"):
            author = message.guild.get_member(int(message.content[5:23]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.remove_roles(role)
            await message.channel.purge(limit=1)
            await message.channel.send(str(author) + "의 채팅을 현시간부로 허용합니다.")
            message.guild.kick()

      if message.content.startswith("/추방"):
            author = message.guild.get_member(int(message.content[4:22]))
            await message.guild.ban(author)
            await message.channel.purge(limit=1)
            await message.channel.send(str(author) + "가 숙청되었습니다.")

      if message.content.startswith("/소련"):
              embed = discord.Embed(title = "소련")
              embed.add_field(name = "소련 찬가", value = "https://www.youtube.com/watch?v=c_JjIQ_sJ1M", inline = False)
              embed.add_field(name = "위키피디아 - 소련", value = "https://ko.wikipedia.org/wiki/%EC%86%8C%EB%A0%A8", inline = False)
              await message.channel.send(embed = embed)
              
      if message.content.startswith("/크루유튜브"):
              await message.channel.send("https://www.youtube.com/channel/UCBUzHfE4UJ1RL9FzcpUBWCA")
              
      if message.content.startswith("/푸린"):
              await message.channel.send("https://www.youtube.com/channel/UC7bcRlidTERRb_MKRHPVSnw")

      if message.content.startswith("/페뇨"):
              await message.channel.send("https://www.youtube.com/channel/UC8FwEy3F0BHzyxYVNlrvzew")
              
      if message.content.startswith("/트박스"):
              await message.channel.send("https://www.youtube.com/channel/UCGNCf6ibX1HWndVRgiChpqw")

      if message.content.startswith("/탬탬버린"):
              await message.channel.send("https://www.youtube.com/channel/UCCA8UWUW80iHqK9ymdjRwPg")

      if message.content.startswith("/코시"):
              await message.channel.send("https://www.youtube.com/channel/UC7uEw7E1-NBpJwE5L2Amoyg")

      if message.content.startswith("/재니"):
              await message.channel.send("https://www.youtube.com/channel/UCZpYXHF--pvTjunD-JBarsQ")

      if message.content.startswith("/이초홍"):
              await message.channel.send("https://www.youtube.com/channel/UC-jHB5e-6LF-yz0kMCTZWdg")
              
      if message.content.startswith("/유준호"):
              await message.channel.send("https://www.youtube.com/channel/UCj0ElpMSiesbvyed1SZ-brw")

      if message.content.startswith("/오요"):
              await message.channel.send("https://www.youtube.com/channel/UCXhTIte6TjoItbiUVUnMIlA")
  
      if message.content.startswith("/에렌디라"):
              await message.channel.send("https://www.youtube.com/channel/UC6xWZn2suKPqAQkidOiMeHg")
              
      if message.content.startswith("/양아지"):
              await message.channel.send("https://www.youtube.com/channel/UCmMxEFwIOMGGoThkmtZZOvQ")  

      if message.content.startswith("/악동 김블루"):
              await message.channel.send("https://www.youtube.com/channel/UCNzcxCN_Hh_lu5RCSFXKgGQ")

      if message.content.startswith("/악녀"):
              await message.channel.send("https://www.youtube.com/channel/UCvXoedkUpd2frzLnZgpx1zw")  

      if message.content.startswith("/아구"):
              await message.channel.send("https://www.youtube.com/channel/UCAGUSx1hbPKDqzBZH7bTjiA")  

      if message.content.startswith("/스타크래프트"):
              await message.channel.send("https://www.youtube.com/channel/UClWPSY-fuGOIldrlUTqoEag")  

      if message.content.startswith("/샤를캣"):
              await message.channel.send("https://www.youtube.com/channel/UCta1OiMP2lG2gQvYHWfX-ww")    

      if message.content.startswith("/새우새우"):
              await message.channel.send("https://www.youtube.com/channel/UCHlQPZM_5xu_3BCa_3cVHVw")    

      if message.content.startswith("/모잉_"):
              await message.channel.send("https://www.youtube.com/channel/UCHzre37UF4o64HRhp-7CDzQ")    

      if message.content.startswith("/꽈뚜룹"):
              await message.channel.send("https://www.youtube.com/channel/UCkQCwnkQfgSuPTTnw_Y7v7w")  

      if message.content.startswith("/꽃핀"):
              await message.channel.send("https://www.youtube.com/channel/UC2MgNh831KCMuYkK7u8C2dg")  

      if message.content.startswith("/견자희"):
              await message.channel.send("https://www.youtube.com/channel/UCBvkQFBskQR9NeOoDYR8ckA")  

      if message.content.startswith("/강지"):
              await message.channel.send("https://www.youtube.com/channel/UCIVFv8AiQLqM9oLHTixrNYw")

      if message.content.startswith("/Life of Boris"):
              await message.channel.send("https://www.youtube.com/channel/UCS5tt2z_DFvG7-39J3aE-bQ")

      if message.content.startswith("/윤이샘"):
              await message.channel.send("https://www.youtube.com/channel/UCn5uvvTSxRZF56g70dpfiog")

      if message.content.startswith("ㅋ"):
              await message.channel.send("ㅋㅋㅋㅋㅋ")

      if message.content.startswith(""):
              file = openpyxl.load_workbook("level.xlsx")
              sheet = file.active
              exp = [10,20,30,40,50,60,70,80,90,100,150,200,300,400,500,750,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
              i = 1
              while True:
                      if sheet["A" + str(i)].value == str(message.author.id):
                              sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                              if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                                      sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                                      await message.channel.send(str(message.author) + "레벨이 올랐습니다.\n 현재 레벨 : " + str(sheet["C" + str(i)].value))
                              file.save("level.xlsx")
                              break

                      if sheet["A" + str(i)].value == None:
                              sheet["A" + str(i)].value = str(message.author.id)
                              sheet["B" + str(i)].value = 0
                              sheet["C" + str(i)].value = 1
                              file.save("level.xlsx")
                              break
                        
                      i = i + 1

      bad_words = ["나쁜 말","bad","word","자갈치","테사기","프사기","저사기","씨발","개","개새끼","병신"]

      for word in bad_words:
              if message.content.count(word) > 0:
                      print("A bad word was said")
                      await message.channel.purge(limit=1)
                      await message.channel.send("해당 금칙어를 삭제했습니다.")
                      file = openpyxl.load_workbook("level.xlsx")
                      sheet = file.active
                      i = 1
                      while True:
                              if sheet["A" + str(i)].value == str(message.author.id):
                                      sheet["B" + str(i)].value = 0
                                      sheet["C" + str(i)].value = 1
                                      file.save("level.xlsx")
                                      await message.channel.send(str(message.author) + "패널티로 레벨을 초기화했습니다.")
                                      break
                              i = i + 1
                              
client.run('NjkxMTc4OTQyMzc1Mzk1MzQ5.XncMmA.MI2NjAh-sdI09L_HW_WIz2Qt4r8')
