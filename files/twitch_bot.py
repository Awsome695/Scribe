from twitchio.ext import commands
import re
import random
from cider_apis import return_name, return_artistName, return_songLink

bot = commands.Bot(token="05d3ipi63wix1propykisiu0cc2ykr", prefix="!", initial_channels=["Awsome695"])
username_pattern = re.compile(r'^[a-zA-Z0-9_]{4,25}$')
initial_channels = ["Awsome695"]


# Function to verify if a string is a valid Twitch username
async def is_valid_username(username: str) -> bool:
    return bool(username_pattern.match(username))


@bot.event()
async def event_ready():
    if initial_channels:
        await (bot.get_channel(initial_channels[0])
               .send("Hello! I am now online! use '!' to summon me! use '!help' for more info!"))
        print(f'Logged into Twitch | {bot.nick}')




@bot.command()
async def cookie(ctx: commands.Context) -> None:
    await ctx.send(f"{ctx.author.name} gets a cookie!")


@bot.command()
async def song(ctx: commands.Context) -> None:
    await ctx.send(f"{ctx.author.name} the current song is: '" + str(return_name()) + "' by: '"
                   + str(return_artistName()) + "'")


@bot.command()
async def songlink(ctx: commands.Context) -> None:
    await ctx.send(f"{ctx.author.name} Here is Song.Link for the current song: " + str(return_songLink()))


@bot.command()
async def give_cookie(ctx, username: str):
    if username.startswith('@'):
        truncated_username = username.lstrip('@')
        # Check if the provided username is valid
        if await is_valid_username(truncated_username):
            # Get the sender's username
            # sender_username = ctx.author.name

            # Send a message mentioning both the sender and the mentioned username
            await ctx.send(f'{ctx.author.name} Gave a cookie to: {username}!')
        else:
            # Send an error message if the provided username is invalid
            await ctx.send("I can't seem to find that person, sorry!")
    else:
        # Send an error message if the provided username is invalid
        await ctx.send("Please use @ when mentioning someone!")


@bot.command()
async def unalive(ctx, username: str):

    if username.startswith('@'):
        truncated_username = username.lstrip('@')
        # Check if the provided username is valid
        if await is_valid_username(truncated_username):
            # Get the sender's username
            # sender_username = ctx.author.name

            phrases = [
                f"{username} you have been unalived at the hands of {ctx.author.name}",
                f"Breaking News! {username} has been found buried under {ctx.author.name}'s Backyard!",
                f"{username} has fallen into the Lego city river!"
            ]

            rand = random.randint(0, len(phrases) - 1)
            print(rand)

            # Send a message mentioning both the sender and the mentioned username
            await ctx.send(phrases[rand])

        else:
            # Send an error message if the provided username is invalid
            await ctx.send("It seems the person you have mentioned has evaded you...")
    else:
        # Send an error message if the provided username is invalid
        await ctx.send("Please use @ when mentioning someone!")


@bot.command()
async def help(ctx, *args) -> None:
    if args:
        # If arguments were provided, handle them accordingly
        # For example, you can have different help messages for different commands
        command = args[0].lower()  # Convert to lowercase for case-insensitive matching

        if command == "!help" or command == "help":
            await ctx.send("!help - Help and Info command!")

        elif command == "!cookie" or command == "cookie":
            await ctx.send("!cookie - Get a cookie!")

        elif command == "!give_cookie" or command == "give_cookie":
            await ctx.send("!give_cookie - give someone a cookie! mention them with '@'")

        elif command == "!song" or command == "song":
            await ctx.send("!song - gives song name and artist")

        elif command == "!songlink" or command == "songlink":
            await ctx.send("!songlink - gives Song.Link for the current Song")

        elif command == "!unalive" or command == "unalive":
            await ctx.send("!unalive - funny little command to do with people, mention them with '@' !")
        else:
            await ctx.send("I'm not sure what that is...")

    else:
        await ctx.send("Current commands are: "
                       "!cookie "
                       "!give_cookie "
                       "!song "
                       "!songlink "
                       "!unalive"
                       )
        await ctx.send("!help [command name] - for more info!")


bot.run()
