from playsound import playsound
import multitasking
import signal

signal.signal(signal.SIGINT, multitasking.killall)

@multitasking.task
def play_es():
	playsound('./mp3/lang_es.mp3')
	return True
@multitasking.task
def play_en():
	playsound('./mp3/lang_en.mp3')
	return True
@multitasking.task
def play_fr():
	playsound('./mp3/lang_fr.mp3')
	return True
@multitasking.task
def play_de():
	playsound('./mp3/lang_de.mp3')
	return True

if __name__ == '__main__':
	done = False
	count = 0
	opt = ''
	while not done:
		if count == 0:
			play_es()
			opt = input('Input: ')
		if count == 1:
			play_en()
			opt = input('Input: ')
		if count == 2:
			play_fr()
			opt = input('Input: ')
		if count == 3:
			play_de()
			opt = input('Input: ')
		if count >= 4:
			count = -1

		if opt != '0' and opt != '1' and opt != '2' and opt != '3':
			count += 1
			multitasking.wait_for_tasks()
			continue
		else:
			print('Done {}'.format(opt))
			break