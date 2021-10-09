from discord.ext import commands


class Manager(commands.Cog):

    """" Manager do bot """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} se conectou ao Discord')


    @commands.Cog.listener()
    async def on_message(self, message):
        return

    
    @commands.Cog.listener() 
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Olá {member.name}, você entrou no meu servidor'
        )
        print(f'Olá {member.name}, você entrou no meu servidor')


    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        with open('errors.log', 'a', encoding="utf-8") as file:
            file.write(f'Erro não tratado no {event}: {args[0]}\n')


    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        if isinstance(error, commands.errors.CheckFailure):
            await context.send('Você não tem permissão para usar esse comando.')


def setup(bot):
    bot.add_cog(Manager(bot))