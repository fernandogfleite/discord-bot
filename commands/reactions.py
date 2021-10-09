from discord.ext import commands

class Reactions(commands.Cog):

    """" Trabalha com reações do usuário """

    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👍":
            role = user.guild.get_role(896222205371908126)
        
        elif reaction.emoji == "🦄":
            role = user.guild.get_role(896221983862296626)
        
        elif reaction.emoji == "🐂":
            role = user.guild.get_role(896222062962675742)
        
        else:
            role = user.guild.get_role(896222896458981427)

        await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))