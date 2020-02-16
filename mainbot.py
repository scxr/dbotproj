import discord, re, os
from dbreader import read
from dbwriter import inserter
from dbdel import delete
from jsonparser import parsejson
from tohaste import hasteme
from apiclient import fromapi
from updatedb import updater
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('claim'):
        code = message.content.split()[1]
        resp = read('Claimables',str(code),'CODE')
        try:
            val = int(resp[0][2])
            author_id = message.author.id
            inserter(author_id, val)
            await message.channel.send("Congratulations you have claimed "+str(val)+" requests")
            delete(code)
        except IndexError:
            await message.channel.send("Code could not be found")

    if message.content.startswith('srchuser'):
        try:
            r = read('Users','userid',message.author.id)
            print(int(r[0][2]) - 1)
            if int(r[0][2]) > 0: 
                newval = int(r[0][2]) -1
                await message.channel.send('Please allow up to 60 seconds for your response, we have a lot of data to process. You have ' + str(newval)+' requests left')
                
                tmp = message.content.split()
                myresp = str(fromapi(tmp[1]))
                newresp = '['+myresp[myresp.find('[')+1:myresp.find('],"')]+']' 
                filename = str(message.id) + '.txt'
                tst = re.split('(,{)', newresp)
            
                with open(filename,"w") as f:
                    f.write(newresp)
                    f.close()
                

                if len(tst) < 20:
                    await message.channel.send('No Results Returned')

                else:
                    mytup = (tst[0][1::], '{'+tst[2], '{'+tst[4],'{'+tst[6],'{'+tst[8],'{'+tst[10],'{'+tst[12],'{'+tst[14],'{'+tst[16],'{'+tst[18],'{'+tst[20])
                    embed = discord.Embed(title="Top 10 **censored** results", description="Here are the top ten results")
                    embed2 = discord.Embed(title="Top 10 **uncensored** results", description="Here are the top ten results")
                    for i in mytup:
                        val = eval(i.replace('null','""'))
                        print(val['id'])
                        embed.add_field(name="ID : " + str(val['id']), value="Username  : "+val['username'] + "\n"+"email: "+val['email'] + "\n"+" password: " + 'x' * len(val['password']) + "\n" + "Found in : " + val['obtained_from'], inline=False)
                        embed2.add_field(name="ID : " + str(val['id']), value="Username  : "+val['username'] + "\n"+"email: "+val['email'] + "\n"+" password: " + val['password'] + "\n" + "Found in : " + val['obtained_from'], inline=False)
     
                    await message.channel.send(embed=embed)
                    await message.channel.send('We are sending your uncensored details in private')
                    await message.author.send(embed=embed2)
                    await message.author.send('Here is everything we found', file=discord.File(filename))
                    os.remove(filename)

                    
                    updater(message.author.id,int(newval))
            else:
                await message.channel.send('Please purchase some credits to use this function, you are currently empty')
            
        except IndexError:
            await message.channel.send('We can not find your account in our databases please purchase a code to use ')

client.run('')
