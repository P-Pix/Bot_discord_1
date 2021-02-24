import discord
from discord.ext import commands
from discord.utils import get

#tamps video = 2:18:52

#creer un nouvelle instance du bot
#bot = discord.Client()
bot = commands.Bot(command_prefix = '//')

#detect bot ready
@bot.event
async def on_ready():
    print("Bot ready")
    await bot.change_presence(status = discord.Status.idle, activity = discord.Game('tuer des gens'))

#detecter l'ajout d'un emoji
@bot.event
async def on_raw_reaction_add(payload):
    user = payload.user_id #recuperer le mec
    emoji = payload.emoji.name #recuperer l'emoji
    canal = payload.channel_id #recuperer le canal
    message = payload.message_id #recuperer le numero du message
    server = payload.guild_id #recuperer l'id du serv
    membre = bot.get_guild(server).get_member(user)
    print("membre = ",membre)
    role = bot.get_guild(server).roles
    design_role = get(role, name = "weeb")
    print(design_role)

    #verirfier si l'emoji est le bon
    if emoji == "design" and canal == 797123727077802026 and message == 797124252955443250:
        print("acces role")
        #await membre.add_roles(design_role)
        #await membre.send("grade obtain")

#detecter l'ajout d'un emoji
@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name #recuperer l'emoji
    canal = payload.channel_id #recuperer le canal
    message = payload.message_id #recuperer le numero du message
    server = payload.guild_id #recuperer les server
    
    #verirfier si l'emoji est le bon
    if emoji == "design" and canal == 797123727077802026 and message == 797124252955443250:
        print("retrait role")

#commande //regles
@bot.command()
async def regles(ctx):
    await ctx.send("Regle n°1 pas de Spam\nRegle n°2 aimer les hentai est conseillé\nRegle n°3 regarder des manga de K LI T")

@bot.command()
async def aides(ctx):
    await ctx.send("les commandes sont :\n//regles\n//bienvenue")

@bot.command()
async def bienvenue(ctx, nouveau_member : discord.Member):
    pseudo = nouveau_member.mention
    await ctx.send(f"Bienvenue {pseudo} sur le serv discord pense à faire //aides")

#verifier l'erreur
@bienvenue.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("La commande est //bienvenue @pseudo")        

#donner le jeton d'autentification
token = "Nzk3MDk3OTA5OTU0MjgxNTAy.X_hhRw.ilt0ZPLKIREQQZ-uywJj3R6RH0c"

#connection au serv
print("lancement du bot...")
bot.run(token)


