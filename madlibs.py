def main():
	# write your code here
	print("Mad libs where libs get mad.")
	print("Start bellow:\n")

	time = input("Enter number between 1 and 12: ")
	item = input("Enter a noun: ")
	name = input("Enter your name: ")
	scream = input("Enter any sentence: ")
	action = input("Enter your action: ")

	print("The story goes ...\n")
	print("It was %s oclock when I heard a knock at the door." % (time))
	print('I opened the door and there was a box full of %s with a note saying "From Mr. %s"' % (item,name.title()))
	print('Just as I closed the door I heard a scream "%s." ' % (scream.upper()))
	print("I froze in place and all I could do was %s." % (action))

if __name__ == '__main__':
	main()
