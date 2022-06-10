bot_token = '5524167802:AAEPvQ6-JvdwiaIKppweHTYsCXrym7vVHBM'  # Telegram bot token from @BotFather
admins_ids = [5455166957, 564796271]  # List of Telegram user identifiers (integers). Find via @myidbot

# `quick_access_cmds` represents the keyboard that will be displayed as Telegram keyboard (for quick
# access to frequently used commands).
#
# It is an array of arrays of strings. Second-level arrays represent lines of keyboard (top-to-bottom),
# strings in them are the commands for the keyboard.
#
# `quick_access_cmds` can be empty (or completely omitted in the config), but its subarrays and the strings
# in them must not be empty.
#
# After you update `quick_access_cmds` in the config, you should restart the bot (so that the config file
# is reread) and then send `/start` command in Telegram (so that the keyboard on your Telegram client
# is updated)
quick_access_cmds = [['/key space', '/type Hello, World!'], ['/type This will appear on second line']]
