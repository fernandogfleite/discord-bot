from discord.ext import commands

class Talks(commands.Cog):

    """" Conversas com o usuário """

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='oi')
    async def create_channel(self, context):
        response = f"Olá, {context.author.name}."

        await context.send(response)


def setup(bot):
    bot.add_cog(Talks(bot))