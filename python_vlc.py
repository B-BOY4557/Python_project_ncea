import vlc
import time

instance = vlc.Instance("--intf=newcurses")
player = instance.media_player_new()
media = instance.media_new(r"/src/videos/Test.mp4")
player.set_media(media)
player.play()