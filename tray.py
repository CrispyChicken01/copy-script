import pystray
from PIL import Image


image = Image.open('Barb_pic.jpg')


def do_stuff(icon, item):
	if str(item) == 'On':
		print('It is on')

	elif str(item) == 'Exit':
		print('-----Exiting-----')
		icon.stop()

	elif str(item) == 'Submenu 1':
		print('It is Submenu 1')

	elif str(item == 'Submenu 2'):
		print('It is Submenu 2')	

	else:
		print('It is off')

icon = pystray.Icon("copy-script", image, menu= pystray.Menu( 
	pystray.MenuItem('On', do_stuff),
	pystray.MenuItem('Off', do_stuff),
	pystray.MenuItem('Submenu', pystray.Menu(
		pystray.MenuItem('Submenu 1', do_stuff),
		pystray.MenuItem('Submenu 2', do_stuff)

		)

	),
	pystray.MenuItem('Exit', do_stuff)
))




icon.run()