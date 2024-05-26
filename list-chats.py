from pyrogram import Client, errors

app = Client("RepRec", api_id="13837945", api_hash="3fb3dae818a0dda632ae182ab83c8a50")

async def list_chats():
    async with app:
        async for dialog in app.get_dialogs():
            chat = dialog.chat
            print(f"Chat ID: {chat.id}, Type: {chat.type}, Name: {chat.title if chat.title else chat.first_name}")

async def send_message():
    group_chat_id = "-1002080755234"  # Ensure this is the correct group chat ID
    try:
        async with app:
            await app.send_message(group_chat_id, "Bot connected. Starting audio monitoring and sending...")
    except errors.PeerIdInvalid as e:
        print(f"Peer ID Invalid Error: {e}")
    except errors.Forbidden as e:
        print(f"Permissions Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

app.run(list_chats())
app.run(send_message())


