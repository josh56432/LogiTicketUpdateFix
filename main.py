@tasks.loop(seconds=120)          
async def buttonRefresh():
  db = pickledb.load('logiTicket.json', True)
  keys = str(db.getall()).replace("dict_keys([","").replace("]","").replace("'","").replace(")","").split(", ")
  for i in range(len(keys)):
    try:
      channel = client.get_channel(ticketChannel)
      messageId = int(db.get(str(keys[i])).split("//")[4])
      msg = await channel.fetch_message(messageId)
      if len(db.get(str(keys[i])).split("//")) == 6:
        await msg.edit(embed=msg.embeds[0], view=complete.completeButton())
      else:
        await msg.edit(embed=msg.embeds[0], view=reserve.reserveButton())
    except Exception as e:
      if keys[i] != "TicketNum" and keys[i] != "lb":
        print(e)


@client.event
async def on_ready():    
  print("Ready!")
  buttonRefresh.start()