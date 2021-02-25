import discord
import asyncio
import random

#client = discord.Client()

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	#await client.get_channel(channel_id).send("bot is online")
	#channel = discord.Object(channel_id)

@client.event
async def on_message(message):
	c_channel = discord.utils.get(message.guild.text_channels, name='general')

	messages = await c_channel.history(limit=1).flatten()
	msg = messages[0].content
	msg_user = message.author.name

	with open('dashboard/data/msg.txt','w') as f:
		f.write( ' '+ msg_user + ':: ' + msg)

	with open('dashboard/data/test.txt','r') as file:
		lines = file.readlines()
		idx = random.randint(1,len(lines))

		bot_msg = lines[idx]

		if bot_msg.strip():
			await asyncio.sleep(4)
			await message.channel.send(bot_msg)
		else:
			return



client.run('') ##YOUR TOKEN HERE
