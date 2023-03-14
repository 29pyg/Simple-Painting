import cv2 as cv

video_file = '/Users/tcp/Downloads/video.webm'

video = cv.VideoCapture(video_file)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)

    while True:
        valid, img = video.read()
        if not valid:
            break

        blr = cv.bilateralFilter(img, -1, 20, 6)
        canny = 255 - cv.Canny(img, 60, 100)
        canny = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
        
        dst = cv.bitwise_and(blr, canny)
        cv.imshow('My Video', dst)

        key = cv.waitKey(wait_msec)
        if key == 27: # ESC
            break

    cv.destroyAllWindows()