import pyscreenshot
# Capture the full screen
image = pyscreenshot.grab()

# Display the screenshot
image.show()
# Save the screenshot to a file
image.save("mahedi_123.png")

import pyscreenshot
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))
image.show()
image.save("mahedi_123.png")

