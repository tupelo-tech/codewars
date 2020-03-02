#!/usr/bin/env python
import sys
import time
import array
from soco import SoCo

def printSkull():

 art = '''\
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
 '''
 return art

def askForCode():
       guess = raw_input("Enter Secret Code: ")
       result = checkCode( guess )

       if result == "GAMEOVER":
                endGame()
       elif result == False:
                attackSelf()
       else:
                attackEnemy()

def attackSelf():
       print "This is not a valid enemy attack code. The enemy has intercepted your attack and will now be able to attack you! Take cover for 3 minutes!"
       mp3 = "https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/failme.mp3" # FAIL MP3
       playTrack(mp3, 'self')
       time.sleep( 4 )
       mp3 = "https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/blasters.mp3" # BLASTERS MP3
       playTrack(mp3, 'self')

def attackEnemy():
       print "Congratulations! This is a valid enemy attack code! You have broken their defenses and they will be attacked momentarily!"
       mp3 = "https://fairlawnhackathon.s3.eu-west-2.amazonaws.com/yourfather.mp3" # FAIL MP3
       playTrack(mp3, 'self')

       mp3 = "https://fairlawnhackathon.s3.eu-west-2.amazonaws.com/yourfather.mp3" # FAIL MP3
       playTrack(mp3, 'enemy')

       time.sleep( 4 )
       mp3 = "https://fairlawnhackathon.s3.eu-west-2.amazonaws.com/blasters.mp3" # Success MP3
       playTrack(mp3, 'enemy')

def endGame():
       print "CONGRATULATIONS! YOU HAVE WON THE GAME AND DEFEATED YOUR ENEMY"

       winners = "https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/winners.mp3" # THEME TUNE
       losers  = "https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/losers.mp3" # THEME TUNE

       mp3 = "https://s3.eu-west-2.amazonaws.com/fairlawnhackathon/withtheforce.mp3" # Success MP3
       playTrack(mp3, 'self')

       time.sleep( 4 )
       playTrack( winners, 'self')
       playTrack( losers, 'enemy' )

def checkCode( code ):
        print "Code entered: ", code

        if code == "WVXLWVSRTHSRXXNJGSFZWRGKPQYXRWOGFMRONNDJXAOANPRIRERLRXHQQERRSHJXZVHVIHSRUGOVUGULFI":
               result = True
        elif code == "HIGSHICCMQTHUADITPKJBCIDLTUNILMMWQCZLZMKIRIVIOICSJJVIIHSQ":
               result = True
        elif code == "YYIMPDQWZEPLGFXYEZHPQJEHIISMYVH":
               result = True
        elif code == "THEIMPERIALISTSHAVEBEENDEFEATED":
               result = "GAMEOVER"
        else:
                result = False;

        return result

def playTrack( mp3, location ):


        my_sonos     = ['192.168.0.135']
        enemy_sonos  = ['192.168.0.144','192.168.0.135'] #testing with 2 sonos only
        #enemy_sonos  = ['192.168.0.12','192.168.0.15'] #multiple enemies
       # enemy_sonos  = '192.168.0.15' #single enemy

        ips = []
        if location == "self":
               ips = my_sonos
        else:
               ips = enemy_sonos

        for ip in ips:
            sonos = SoCo( ip ) # Sonos
            sonos.play_uri( mp3 )
            track = sonos.get_current_track_info()
            print track['title']
            sonos.pause()
            sonos.play()

if __name__ == '__main__':

 print printSkull()

 askForCode()
