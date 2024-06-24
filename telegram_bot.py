
#imports for Application
from telegram import Update
from telegram.ext import *
from dotenv import load_dotenv
import os
from gemini.text_response import *
from gemini.image_response import *
from gemini.video_response import *
from gemini.audio_response import *
from extension.file_extension import *

# load EVN api key
load_dotenv()

#get api key and bot name
TELEGRAM_API_KEY : str = os.getenv("BOT_TELE_KEY")
TELEGRAM_BOT_NAME : str = "@ai_gemini_bot"


#Commands for the bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with! me! I am a cat")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("l am a cat! pls type something so l can respond")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")


# main fun for program
async def telegram_bot(update : Update, context : ContextTypes.DEFAULT_TYPE):
     # message_type Get group type public, private or group chat Second line looks for new text messages in chat
     message_type: str = update.message.chat.type
     text : str = update.message.text
     print(f"User ({update.message.chat.id}) in {message_type}: {text}")
     
     # text response
     if update.message.text:
              message_type: str = update.message.chat.type
              text : str = update.message.text
              handle_response_text = asyncio.create_task(handle_response(text))
             # cheque if it is group or  private chat

              if message_type == "group":
                 if TELEGRAM_BOT_NAME in text:
                      new_text: str = text.replace(TELEGRAM_BOT_NAME, "").split()
                      response: str = await handle_response_text
                 else:
                     return
             
             #not group send message
              else:
                   response: str = await handle_response_text
              #send message and print(response)
              print(f"bot: {response}")
              await update.message.reply_text(response, parse_mode="Markdown")
     elif update.message.photo:
            #Get the image ID
            file = await context.bot.get_file(update.message.photo[-1].file_id)
            file_name = f"{update.message.chat.id}.jpg"
            download_folder = "image"
            #get caption of image

            caption = update.message.caption
            #Download the image
            if caption == None:
                 await update.message.reply_text("No captin")
            await file.download_to_drive(custom_path=os.path.join(download_folder, file_name))
            image_name = f"{update.message.chat.id}.jpg"
            
            #Send confirmation
            await update.message.reply_text(f"photo downloaded Successfully we are currently processing your image After proofing the image will be deleted {image_name}" , parse_mode="Markdown")
            print(f"{image_name}")
               
            image_response_task = asyncio.create_task(image_response(caption, image_name))   

            response_of_image = await image_response_task
            
            await update.message.reply_text(response_of_image, parse_mode="Markdown")

            # video response
     elif update.message.video:
               MAX_FILE_VIDEO_SIZE = 20000
               chat_id = update.message.chat.id
               download_folder_video = "video"
               file_name = update.message.video.file_name
               file_size = update.message.video.file_size
               file_size = file_size/1000
               
               
               if file_size > MAX_FILE_VIDEO_SIZE:
                      await update.message.reply_text("""Message form the Developer: Due to Telegram API limitations, bots and user in bot chat are only allowed to upload files up to 20MB source:https://core.telegram.org/bots/api#getfile .i apologize for any inconvenience this may cause.""")

     
               else:
                  file = await context.bot.get_file(update.message.video.file_id)
                  caption_video = update.message.caption 
                  await update.message.reply_text(file)
                  if file_name != None:
                                file_name_ex = update.message.video.file_name.split(".")[-1]
                                video_name = f"{chat_id}.{file_name_ex}"

                               
                                await file.download_to_drive(custom_path=os.path.join(download_folder_video, video_name))
                  else:
                               video_name = f"{chat_id}.mp4"
                               await file.download_to_drive(custom_path=os.path.join(download_folder_video, video_name)) 

                  video_response_task = asyncio.create_task(video_response(caption_video, video_name))
                  response_of_video = await video_response_task

                  await update.message.reply_text(response_of_video)
       # voice response        
     elif update.message.voice:

            chat_id = update.message.chat.id
            download_folder_audio = "audio"
            
            file = await context.bot.get_file(update.message.voice.file_id)
            await update.message.reply_text(f"mimi type {file}")
            audio_name = f"{chat_id}.ogg"
            await file.download_to_drive(custom_path=os.path.join(download_folder_audio, audio_name))

            voice_telegram = asyncio.create_task(voice(audio_name))

            response_audio = await voice_telegram
            os.chdir("audio")
            await update.message.reply_voice(response_audio)
            os.chdir("..")
            
       # pdf response  
     """
     elif update.message.document:
          chat_id = update.message.chat.id
          download_folder_doc : str = "document"
              
          file_doc = await context.bot.get_file(update.message.document.file_id)

          name = await name_ex(str(file_doc))
          if name.endswith(".pdf"):
           doc_name : str = f"{chat_id}.pdf"
           await file_doc.download_to_drive(custom_path=os.path.join(download_folder_doc, doc_name))

           await update.message.reply_text(f"all good {file_doc}")

           

              
              
            
     else:
          await update.message.reply_text("**oops**", parse_mode="Markdown")
     """  
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
     print(f"Update {"update"} casued error {context.error}")

if __name__ == "__main__":
    print("strarting....")
    app = ApplicationBuilder().token(TELEGRAM_API_KEY).build()
     
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    app.add_handler(MessageHandler(filters.ALL, telegram_bot))
    
    app.add_error_handler(error)
    print("polling...")
    app.run_polling(poll_interval=0) 