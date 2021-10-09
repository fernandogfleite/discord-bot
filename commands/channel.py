from discord.ext import commands
import discord

class Channel(commands.Cog):

    """" Conversas com o usuário """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='criar-canal')
    @commands.has_role('Admin')
    async def create_channel(self, context, nome_canal='novo-canal'):
        guild = context.guild

        existent_channel = discord.utils.get(guild.channels, name=nome_canal)

        if not existent_channel:
            print(f'Criando novo canal: {nome_canal}')
            await guild.create_text_channel(nome_canal)


def setup(bot):
    bot.add_cog(Channel(bot))

