import speech_recognition
#from pyuserinput import PyKeyboard
from pykeyboard import PyKeyboard
import time


def main() :
    recognizer = speech_recognition.Recognizer()
    while True :
        with speech_recognition.Microphone() as src:
            try:
                #audio = recognizer.adjust_for_ambient_noise(src)
                #print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
                print("Say \"Mario\" to begin:")
                audio = recognizer.listen(src, timeout=0.1, phrase_time_limit = 1)
                speech_to_txt = recognizer.recognize_google(audio).lower()
                print('\n' + speech_to_txt + '\n')
                if 'mario' in speech_to_txt :
                    print("Speak Command:")
                    audio_comm = recognizer.listen(src, phrase_time_limit = 1.5)
                    speech_to_comm = recognizer.recognize_google(audio_comm).lower()
                    print('\nCommand:\n' + speech_to_txt + '\n')
                    ASR_Keyboard(speech_to_comm)
                #release_all() 
            except Exception as ex:
                print("Sorry. Could not understand.")



def ASR_Keyboard(command) :
    k = PyKeyboard()
    

    
    command = command[command.lower().find('mario'):len(command)].split()
    for i in range(len(command)) : 
        if 'upright' in command[i].lower() :
            command[i] = 'up'
            command.insert(i + 1, 'right')

    for c in command :
        comm_list = c.lower()
        comm_list = write_right(comm_list)
        if comm_list == 'Mario' :
            break
        elif comm_list == 'up' or  comm_list == 'jump':
            k.press_key(k.up_key)
        elif comm_list == 'down' :
            k.press_key(k.down_key)
        elif comm_list == 'right' :
            k.press_key(k.right_key)
        elif comm_list == 'left' :
            k.press_key(k.left_key)
        elif 'stop' in command :
            release_all() 
        elif  command[len(command)-1] == 'hop' : 
            for i in range(20) :
                k.press_key(k.up_key)
                time.sleep(0.2)
                release_all()
        elif comm_list == 'fire' :
            k.press_key(k.control_key)
            time.sleep(0.05)
            release_all()
        elif comm_list == 'machine' :
            for i in range(10) :
                k.press_key(k.control_key)
                time.sleep(0.75)
                release_all()
            #ASR_Keyboard(command[0:len(command)-1])

    if command[len(command)-1] == 'long' :
       time.sleep(1)
       
    
    
    else :
       time.sleep(0.25)
        

    if 'hold' not in command :
        release_all()
    else :
        x = 0

    if 'stop' in command :
        release_all() 
        



def release_all() :
    k = PyKeyboard()
    k.release_key('A')
    k.release_key(k.up_key)
    k.release_key(k.down_key)
    k.release_key(k.right_key)
    k.release_key(k.left_key)
    k.release_key(k.control_key)


def write_right(command) :
    command = command.lower()
    if 'wright' in command  or 'rate' in command or 'rite' in command:
        command = 'right'
    elif command == 'lung' or command == 'along':
        command = 'long'
    elif command == 'hub':
        command = 'hop'
    else :
        command = command
    return command

def wait(time) :
    if time == 'long' :
       time.sleep(1)
       release_all() 
    
    
    else :
       time.sleep(0.25)
       release_all() 

if __name__ == '__main__':
    main()