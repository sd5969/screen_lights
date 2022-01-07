from mss import mss
import uuid
import time
import os

old_filename = ''

# The simplest use, save a screen shot of the 1st monitor
while True:
    with mss() as sct:

        # generate unique ID
        unique_str = uuid.uuid4()

        # create screenshot
        filename = sct.shot(output='./public/monitor-' + str(unique_str) + '.png')
        print('Screenshotted ' + filename)

        # write new file URL
        f = open("./public/image_url.html", "w")
        f.write('<span>http://10.0.0.91:1111/monitor-' + str(unique_str) + '.png</span>')
        f.close()

        # delete last screenshot
        if old_filename != '':
            os.remove(old_filename)
            print('Deleted ' + old_filename)

        # sleep 30s before loop repeats
        time.sleep(30)
        old_filename = filename
