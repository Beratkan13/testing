import discord
from discord.ext import commands
import psutil
import time

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command()
async def ping(ctx):
    # Bot ping
    bot_latency = round(bot.latency * 1000)  # MS cinsinden ping
    
    # RAM kullanımı
    ram = psutil.virtual_memory()
    ram_percent = ram.percent
    ram_used_gb = ram.used / (1024**3)  # GB cinsinden
    ram_total_gb = ram.total / (1024**3)  # GB cinsinden
    ram_used_mb = ram.used / (1024**2)  # MB cinsinden
    
    # CPU kullanımı
    cpu_percent = psutil.cpu_percent()
    
    # Disk kullanımı
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    disk_used_gb = disk.used / (1024**3)  # GB cinsinden
    disk_total_gb = disk.total / (1024**3)  # GB cinsinden
    
    embed = discord.Embed(title="🤖 Sistem Bilgileri", color=discord.Color.blue())
    
    # Ping bilgisi
    embed.add_field(
        name="📶 Ping",
        value=f"```{bot_latency}ms```",
        inline=False
    )
    
    # RAM bilgisi
    embed.add_field(
        name="💾 RAM Kullanımı",
        value=f"```Yüzde: %{ram_percent}\nKullanılan: {ram_used_gb:.2f}GB / {ram_total_gb:.2f}GB\nKullanılan (MB): {ram_used_mb:.2f}MB```",
        inline=False
    )
    
    # CPU bilgisi
    embed.add_field(
        name="💻 CPU Kullanımı",
        value=f"```Yüzde: %{cpu_percent}```",
        inline=False
    )
    
    # Disk bilgisi
    embed.add_field(
        name="💿 Disk Kullanımı",
        value=f"```Yüzde: %{disk_percent}\nKullanılan: {disk_used_gb:.2f}GB / {disk_total_gb:.2f}GB```",
        inline=False
    )
    
    await ctx.send(embed=embed)

# Botunuzun token'ını buraya ekleyin
bot.run('@me')
