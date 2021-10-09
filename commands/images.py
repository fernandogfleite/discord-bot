from discord.ext import commands
import discord

ALLOWED_CHANNELS = [896189764892500038]

class Images(commands.Cog):

    """" Trabalha com imagens """

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='foto-aleatoria')
    async def get_random_image(self, context):
        if context.channel.id not in ALLOWED_CHANNELS:
            return

        url_image = "https://picsum.photos/1920/1080"

        embed = discord.Embed(
            title="Resultado da busca de imagem",
            description="A busca é totalmente aleatória",
            color=0x0000FF
        )

        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.avatar_url,
        )

        embed.set_footer(
            text=f"Feito por {self.bot.user.name}",
            icon_url=self.bot.user.avatar_url
        )

        embed.add_field(
            name="API",
            value="Usamos a API do https://picsum.photos"
        )

        embed.add_field(
            name="Parâmetros",
            value="<largura>/<altura>"
        )

        embed.add_field(
            name="Exemplo",
            value=url_image,
            inline=False
        )

        embed.set_image(
            url=url_image
        )

        await context.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Images(bot))