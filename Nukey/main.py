import discord, os
from discord.ext import commands

# Don't play with any of the code if you don't understand it

TOKEN = ''
PREFIX = ''
OWNER_ONLY = False # Set to True if you want the bot commands to be useable by users whom got their ID added to OWNER_IDS only
OWNERS_IDS = []
              # Append the IDs of the users that you'd like to be able to use the bot
              # used if OWNER_ONLY was set to True
DELETE_AFTER_EXECTUE = False # Set it to True if you'd like to delete the command after executing it.
NO_PREFIX = False # Set it to True if you'd like to not have a prefix
                  # [ Commands work by just typing them ]



if OWNER_ONLY and not OWNERS_IDS:
  print('Add at least 1 user ID to OWNER_IDS in order for the bot to work. | Press Enter to close this window.')
  input()
  exit()
elif not TOKEN:
  print('Set the bot token in the code in order for the bot to work. | Press Enter to close this window.')
  input()
  exit()
elif not PREFIX and not NO_PREFIX:
  print('Specify a prefix in PREFIX in order for the bot to work. | Press Enter to close this window.')
  input()
  exit()

def prefixes():
  prefixes_ = []
  if NO_PREFIX:
    return ''
  else:
    return PREFIX

client = commands.Bot(
intents = discord.Intents.all(),
command_prefix = commands.when_mentioned_or(prefixes()),
strip_after_prefix=True,
case_insensitive=True,
)
client.owners = OWNERS_IDS
client.delete = DELETE_AFTER_EXECTUE

@client.check
async def owner(ctx) -> bool:
  if OWNER_ONLY:
    if ctx.author.id in OWNERS_IDS:
      return True
    else:
      return False


@client.listen('on_ready')
async def on_ready():
  os.system('cls')
  print('Bot online.')

# Running the cogs (extensions)
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
client.run(TOKEN)
