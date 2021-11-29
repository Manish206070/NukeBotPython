import discord
from discord.ext import commands
from discord.ext.commands import Cog

# Don't play with any of the code if you don't understand it

class errorsCog(Cog):
  def __init__(self, client):
    self.client = client 


  @Cog.listener("on_command_error") 
  async def ErrorHandlers(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        print(error)

    
def setup(client):
  client.add_cog(errorsCog(client))
