import tensorflow as tf
import numpy as np

import os


ROOT_DIR = "E:/PyCharm_Project/Tensorflow_Conda_TEST/"
def main():

    curPath=""
    #sess = tf.Session()
    #sess.run(tf.global_variables_initializer)
    validationGroup = np.empty(shape=[0,2])
    idx = 0
    for path,subdir,files in os.walk(ROOT_DIR+"optical"):

        if curPath != path:
            idx += idx
            curPath = path
        inputArray = np.array([[idx,path]])
        np.append(validationGroup,inputArray,axis=0)


        #print(files)
    print(validationGroup)

if __name__ == "__main__":
  main()