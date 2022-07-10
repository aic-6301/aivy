import discord
from discord.ext import commands

# 読み込んだら通知
 @commands.Cog.listener()
     # Cogが読み込まれた時に発動
     async def on_ready(self):
         print('鯖情報cogが読み込まれたよ！')

@bot.command()
async def serverinfo(self,ctx):
    guild = ctx.message.guild
    roles =[role for role in guild.role]
    text_channels = [text_channels for textchannels in guild.text_channels]
    #embedのないよう
    embed = discord.Embed(title=f"サーバー情報 - {guild.name}",timestamp=ctx.message.created_at,color=discord.Colour.purple(),inline=False)
    embed.set.thumbnail(url=ctx.guild.icon.url)
    embed.add_field(name="サーバー名",value=f"{guild.name}",inline=False)
    embed.add_field(name="サーバー地域",value=f"{ctx.guild.region}",inline=False)
    embed.add_field(name="サーバー設立日",value=guild.created.at,inline=False)
    embed.add_field(name="サーバーオーナー",value=guild.owner,inline=False)
    embed.add_field(name="チャンネル数",value=f"{len(text_channels)}",inline=False)
    embed.add_field(name="ロール数",value=f"{len(roles)}",inline=False)
    embed.add_field(name="サーバーブースト数",value=guild.premium_subscription_count,inline=False)
    embed.add_field(name="メンバー数",value=guild.member_count,inline=False)
    embed.set_footer(text=f"実行者：{ctx.author} ",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    
    def setup(bot):
     bot.add_cog(serverinfo(bot))
