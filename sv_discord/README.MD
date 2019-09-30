## SV_DISCORD

Working example of the usage of the "discord.py" library (game server c/python)

```
# -------------------------------------------------------------------------------------------------------
#          Name: sv_discord.py
#   Description: Communication between chat and discord channel
#        Author: IgorZ
#
#   SSL:
#   https://stackoverflow.com/questions/55012726/discord-py-unable-to-get-certificate
#
#   lib version: discord.py rewrite
#   docs: https://discordpy.readthedocs.io/en/rewrite/api.html
#
#   discord.Message:      author|content|channel|mention_everyone|mentions|id|attachments|raw_mentions
#   discord.Client:       guilds|activity|users|get_channel(id)|get_guild(id)|get_user(id)
#                         get_all_channels()|get_all_members()
#   discord.User:         name|id|discriminator|avatar|bot|mention ex: "<@358270891299307521>"
#   discord.TextChannel:  name|guild|id|category_id|topic|position
#   discord.Guild:        name|id|description|channels|members|get_member(user_id)|get_member_named(name)
#   discord.Member:       id|activity|nick|status|mobile_status|desktop_status|web_status|is_on_mobile()
#   discord.Embed:        title|type|description|url|colour|footer|set_footer()|image|set_image()|
#                         thumbnail|set_thumbnail
#
#   support.discordapp.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline)?page=6
#   Code Formatting:      *Italics* or _Italics_
#                         **bold**
#                         ***bold italics***
#                         __underline__
#                         __*underline italics*__
#                         __**underline bold**__
#                         __***underline bold italics***__
#                          ~~Strikethrough~~
#                         `one line code blocks`
#                         ```multiple
#                               line code blocks```
#                         ```css
#                            multiple line code blocks with stated language```
#                         [text with links](http://url)
#                         [links references][1]  [1]: http://url
#                         Block Quotes is > or >>> followed by a space
# -------------------------------------------------------------------------------------------------------
```