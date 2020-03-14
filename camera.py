import cv2
from datetime import datetime
import pathlib

victims_dir = pathlib.Path('victims')


def save_victim_image():
    cam = cv2.VideoCapture(0)
    frame = None
    for i in range(3):  # Save third frame
        ret, frame = cam.read()
    else:
        str_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        img_name = 'victim_{0}.png'.format(str_date)
        save_path = victims_dir / img_name
        victims_dir.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(save_path), frame)
    print('{} written!'.format(img_name))

    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    save_victim_image()
