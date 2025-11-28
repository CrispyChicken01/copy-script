from pathlib import Path

source_dir = Path('g:/')

def grab_files():
	
	for i in source_dir.rglob(f"*.ppt*"):
		if any(x.startswith('.') for x in i.parts):
			continue
		print("*" * 20 )
		print(i)
		# print("\n")




def main():
	
	
	
	grab_files()




if __name__== '__main__':

	main()
	

