from flask import Flask,render_template,request,send_file,url_for
import numpy as np
import cv2
import time


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('generate_code.html')

@app.route('/generate_code',methods=['GET','POST'])
def generate_code():

    Qr = request.form.get('inputQr',None)
    Bar = request.form.get('inputBar',None)
    Dm = request.form.get('inputDm',None)
    Prop1 = request.form.get('inputProp1',None)
    Prop2 = request.form.get('inputProp2',None)
    Prop3 = request.form.get('inputProp3',None)
    size = request.form['size']
    Height,Width = map(int,size.split("X"))
    imgCanvas = np.zeros([Height, Width, 3], dtype=np.uint8)
    imgCanvas.fill(255)


    imgQr = cv2.imread(Qr)
    imgBar = cv2.imread(Bar)
    imgDm = cv2.imread(Dm)
    imgProp1 = cv2.imread(Prop1)
    imgProp2 = cv2.imread(Prop2)
    imgProp3 = cv2.imread(Prop3)

    time.sleep(1)

    # Rectangle for QR code
    # cv2.rectangle(imgCanvas,(int(0.2*Width),int(.2*Height)),(int(0.8*Width),int(0.8*Height)),(0,0,0),1)
    # Place image at these coordinates
    imgQrResize = cv2.resize(imgQr, (int(0.8 * Width) - int(0.2 * Width), int(0.8 * Height) - int(0.2 * Height)))
    imgCanvas[int(0.2 * Width):int(.8 * Width), int(0.2 * Height):int(0.8 * Height)] = imgQrResize

    # Rectangle for Bar code
    # cv2.rectangle(imgCanvas,(int(0.04*Width),int(.83*Height)),(int(0.74*Width),int(0.96*Height)),(0,0,0),1)
    # Place image at these coordinates
    imgBarResize = cv2.resize(imgBar, (int(0.74 * Width) - int(0.04 * Width), int(0.96 * Height) - int(0.83 * Height)))
    imgCanvas[int(0.83 * Height):int(0.96 * Height), int(0.04 * Width):int(0.74 * Width)] = imgBarResize

    # Rectangle for DataMatrix code
    # cv2.rectangle(imgCanvas,(int(0.76*Width),int(.83*Height)),(int(0.96*Width),int(0.96*Height)),(0,0,0),1)
    # Place image at these coordinates
    imgDmResize = cv2.resize(imgDm, (int(0.96 * Width) - int(0.76 * Width), int(0.96 * Height) - int(0.83 * Height)))
    imgCanvas[int(0.83 * Height):int(0.96 * Height), int(0.76 * Width):int(0.96 * Width)] = imgDmResize

    # Rectangle for proprietary code1
    # cv2.rectangle(imgCanvas,(int(0.2*Width),int(.04*Height)),(int(0.8*Width),int(0.17*Height)),(0,0,0),1)
    # Place image at these coordinates
    if Prop1 != "":
        if imgProp1.shape[0] > imgProp1.shape[1]:
            imgPropResize1 = cv2.rotate(imgProp1, cv2.ROTATE_90_CLOCKWISE)
            print("hi")
        else:
            imgPropResize1 = imgProp1
        imgPropResize1 = cv2.resize(imgProp1, (int(0.8 * Width) - int(0.2 * Width), int(0.17 * Height) - int(0.04 * Height)))
        imgCanvas[int(0.04 * Height):int(0.17 * Height), int(0.2 * Width):int(0.8 * Width)] = imgPropResize1
    else:
        pass
    # Rectangle for proprietary code2
    # cv2.rectangle(imgCanvas,(int(0.83*Width),int(.2*Height)),(int(0.96*Width),int(0.64*Height)),(0,0,0),1)
    # Place image at these coordinates
    if Prop2 != "":
        if imgProp2.shape[0] < imgProp2.shape[1]:
            imgPropResize2 = cv2.rotate(imgProp2, cv2.ROTATE_90_CLOCKWISE)
        else:
            imgPropResize2 = imgProp2
        imgPropResize2 = cv2.resize(imgPropResize2,
                                    (int(0.96 * Width) - int(0.83 * Width), int(0.64 * Height) - int(0.20 * Height)))
        imgCanvas[int(0.20 * Height):int(0.64 * Height), int(0.83 * Width):int(0.96 * Width)] = imgPropResize2
    else:
        pass
    # Rectangle for proprietry code3
    # cv2.rectangle(imgCanvas,(int(0.04*Width),int(.2*Height)),(int(0.17*Width),int(0.64*Height)),(0,0,0),1)
    # Place image at these coordinates

    if Prop3 != "":
        if imgProp3.shape[0] < imgProp3.shape[1]:
            imgPropResize3 = cv2.rotate(imgProp3, cv2.ROTATE_90_CLOCKWISE)
        else:
            imgPropResize3 = imgProp3
        imgPropResize3 = cv2.resize(imgPropResize3,
                                    (int(0.17 * Width) - int(0.04 * Width), int(0.64 * Height) - int(0.20 * Height)))
        imgCanvas[int(0.20 * Height):int(0.64 * Height), int(0.04 * Width):int(0.17 * Width)] = imgPropResize3
    else:
        pass
    # Rectangle for pivot1
    cv2.rectangle(imgCanvas, (int(0.83 * Width), int(0.04 * Height)), (int(0.96 * Width), int(0.17 * Height)),
                  (101, 190, 255), -1)
    # Rectangle for pivot2
    cv2.rectangle(imgCanvas, (int(0.04 * Width), int(0.04 * Height)), (int(0.17 * Width), int(0.17 * Height)),
                  (101, 190, 255), -1)
    # Rectangle for pivot3
    cv2.rectangle(imgCanvas, (int(0.83 * Width), int(0.67 * Height)), (int(0.96 * Width), int(0.8 * Height)),
                  (101, 190, 255), -1)
    # Rectangle for pivot4
    cv2.rectangle(imgCanvas, (int(0.04 * Width), int(0.67 * Height)), (int(0.17 * Width), int(0.8 * Height)),
                  (101, 190, 255), -1)
    filename = "composite_code"+str(size)+".png"
    cv2.imwrite("static/"+filename, imgCanvas)
    return render_template('response.html',image = url_for("static", filename=filename))

if __name__ == '__main__':
    app.run(debug=True)
