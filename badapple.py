import cv2 as cv


def gray_to_ascii(img):
    '''convert grayscale image into ascii formated image'''
    ascii_format = ['.', ',', '*', '+', '^', ';', '?', '%', '$', "#", '@']
    ascii_draw = ''

    i=0
    for x in img.flatten():
        i+=1
        ascii_draw+= ascii_format[x//25]        
        if i%img.shape[1]==0:
            ascii_draw+='\n'    
    print(ascii_draw)


def video_display(filepath):
    """converts a video to ascii and display both cmd text and original video"""
    cap = cv.VideoCapture(filepath)
    
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)

    aspect_ratio = 3 if width//height<=1 else width//height
    new_height = 50
    new_width = new_height*aspect_ratio

    while cap.isOpened:
        ret, frame = cap.read()
        
        if not ret:
            print("thanks for watching")
            break

        cv.imshow('display',frame)

        frame = cv.resize(cv.cvtColor(frame, cv.COLOR_BGR2GRAY),(new_width, new_height))
        gray_to_ascii(frame)
        
        if cv.waitKey(1) == ord('q'):
            break
            
    cap.release()
    cv.destroyAllWindows()


def main():
    video_display('assets//badapple.mp4')


if __name__ == "__main__":
    main()