import os
import cv2
import numpy as np
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
def getimageAndid (path):
    imagepath = [os.path.join(path,f) for f in os.listdir(path)]
    if path + '.DS_Store' in imagepath:
            imagepath.remove(path + '.DS_Store')
    faces = []
    ids = []
    for imagepaths in imagepath:
        faceimg = Image.open(imagepaths).convert('L')
        facenp = np.array(faceimg , 'uint8')
        Id = int(os.path.split(imagepaths)[-1].split('.')[1])
        faces.append(facenp);
        print(Id)
        ids.append(Id)
        cv2.imshow("training",facenp)
        cv2.waitKey(10)
    return (ids),faces
ids , faces = getimageAndid(path)
recognizer.train(faces,np.array(ids))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyWindows()

