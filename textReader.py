import discord
from discord.ext import commands

import subprocess
import ffmpeg
from vcTalk import creat_WAV

bot = commands.Bot(command_prefix="$")
token = "自分のトークン"

#起動確認
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#VC接続
@bot.command(aliases=["connect","hi"])
async def join(ctx):

    #チャンネル取得
    vc = ctx.author.voice.channel

    #接続
    await ctx.send("ボイスチャンネルに接続しました。")
    await discord.VoiceChannel.connect(vc)

#VC切断
@bot.command(aliases=["disconnect","bye"])
async def leave(ctx):

    voice_client = ctx.message.guild.voice_client

    #接続していない時
    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    #切断
    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")

#メッセージ読み上げ
@bot.event
async def on_message(message):
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            #実行出力
            print(message.content)

            #読み上げ用ファイル作成
            creat_WAV(message.content)

            #読み上げ
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass
        await bot.process_commands(message)


bot.run(token)