### 
This is the first working version of T.O.A.S.T.
Please note that you may have to install CustomTkinter for it to run.
You should also get familiar with py2app and the code used for this before trying it out yourself since I am uncertain how it will affect 
other computers. All I can tell is that it works fine on my mac.

Due to uncertainty I have removed the .app file from this repository. If you want to try it for yourself simply copy the code of toast_v2.0.2.py and transform it into a .app application by using py2app.

Afterwards you will have to drag a file called 'store.txt' into the the Resources folder (~/Contents/Resources) for it to work properly.

For information about py2app visit: https://py2app.readthedocs.io/en/latest/

For information about CustomTkinter visit: https://customtkinter.tomschimansky.com

I'm unable to create a stable and universal application for x86_64 and arm64 via universal2. Hence there won't be another way for anyone to use it except from running it through the terminal or creating the app by oneself using either py2app or pyinstaller. There's no other stable option to distribute this program.

I'm currently working on v2.1 for a better data management with an actual sql database and the buttons being summed up in one class. The .db file won't have to be included into the Resources folder manually by yourselves as well as the .txt file, unless I find a way to properly convey this thing as a whole. Funny enough, the core problem was a missing opener.

sort_dict.py will soon be relocated.
