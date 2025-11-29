from pathlib import Path

source_dir = Path('g:/')

def grab_files(file_extension):
	
	for i in source_dir.rglob(f"*.{file_extension}*"):
		if any(x.startswith('.') for x in i.parts):
			continue   		# Ignores any hidden folders (folders starting with an '.')
		print("*" * 20 )
		print(i)	# Outputs the grabbed files
		# print("\n")




def main():
	type_extension = input("Type the file extension: ")
	i = grab_files(type_extension)
	



if __name__== '__main__':

	main()
	

