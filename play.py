await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)      
        await message.reply_photo(
            photo="final.png",
            caption="**ʏᴏᴜʀ sᴏɴɢ ɪᴢ ᴀᴅᴅᴇᴅ ɪɴ ᴛʜᴇ ǫᴜᴇᴜᴇ🥀💖 \n\nʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ: {} \nᴘᴏsɪᴛɪᴏɴ :- {}**".format(usrid, position),
            reply_markup=keyboard,
        )
        await message.delete()
    
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="ɴᴏᴡ ɪ ᴍ ᴘʟᴀʏɪɴɢ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢ 🌷️.\n\nᴘʟᴀʏɪɴɢ ᴀᴛ‍ 💫 :- {}...\nʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ: {}".format(
        message.chat.title, usrid
        ), )
        
    
    os.remove("final.png")
    return await lel.delete()
