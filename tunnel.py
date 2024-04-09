# pip install ngrok

import ngrok

listener = ngrok.forward(7860, authtoken="27NU87uSwSxLsYLg5rOUJcDY2sx_2n28J7eez1fBtsDZkcnrG")

print(listener.url())

try:
    while True:
        pass
except KeyboardInterrupt:
    try:
        listener.close()
        print("Listener closed")
    except:
        pass