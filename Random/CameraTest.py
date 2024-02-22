# import required modules
import cv2

def main():
	# 1. Get the required webcam feed
	cap = cv2.VideoCapture(1)

	# 2. Create a window to display the feed
	cv2.namedWindow("preview")

	# 3. Display the feed in the window
	if cap.isOpened():  # try to get the first frame
		rval, frame = cap.read()
	else:
		rval = False

	while rval:
		cv2.imshow("preview", frame)
		rval, frame = cap.read()
		key = cv2.waitKey(20)

		# exit on ESC
		if key == 27:
			cv2.destroyWindow("preview")
			break

		# exit loop if the window is closed
		if cv2.getWindowProperty("preview", 0) < 0:
			break

if __name__ == "__main__":
	main()
