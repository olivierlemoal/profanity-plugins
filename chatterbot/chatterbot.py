import prof
from chatterbotapi import ChatterBotFactory, ChatterBotType

factory = ChatterBotFactory()
bot = factory.create(ChatterBotType.CLEVERBOT)
# bot = factory.create(ChatterBotType.JABBERWACKY)
# bot = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot_session = {}
bot_state = False

def prof_post_chat_message_display(jid, message):
    if bot_state:
        if jid not in bot_session:
            bot_session[jid] = bot.create_session()
        response = bot_session[jid].think(message)
        prof.send_line("/msg " + jid + " " + response)

def _cmd_chatterbot(state):
    global bot_state

    if state == "enable":
        prof.cons_show("ChatterBot Activated")
        bot_state = True
    elif state == "disable":
        prof.cons_show("ChatterBot Stopped")
        bot_state = False
    else:
        if bot_state:
            prof.cons_show("ChatterBot is running - current sessions:")
            prof.cons_show(str(bot_session))
        else:
            prof.cons_show("ChatterBot is stopped - /chatterbot enable to activate.")
        
def prof_init(version, status):
    prof.register_command("/chatterbot", 0, 1, "/chatterbot [enable|disable]", "ChatterBot", "ChatterBot", _cmd_chatterbot)
