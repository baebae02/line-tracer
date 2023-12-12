__author__ = 'will'

import pickle
import numpy as np

data = pickle.load( open( "training_test.p", "rb" ), encoding="latin1" )
n_images = len(data)
test, training = data[0:int(n_images/3)], data[int(n_images/3):]

def get_training_data():
    print("length", n_images)
    trX = np.array([np.reshape(a[2],a[2].shape[0]**2) for a in training])
    trY = np.zeros((len(training)),dtype=float)
    for i, data in enumerate(training):
        trY[i] = float(data[0])

    # # 디버깅용 1
    # print("trX", trX, "trY", trY) # trX[i]는 학습 데이터, trY[i]는 학습 데이터 라벨
    # print()
    # for i in trX:
    # #     # 데이터를 16x16으로 재배열
    #      reshaped_data = np.array(i).reshape((16, 16))
    # print(trX.shape)

    # # 디버깅용 2
    # for i in range(0, len(trX)):
    #      print(np.array(trX[i]).reshape((16, 16)))
    #      print(trY[i])
    # return trX, trY

def get_test_data():
    teX = np.array([np.reshape(a[2],a[2].shape[0]**2) for a in test])
    teY = np.zeros((len(test)),dtype=float)
    for i, data in enumerate(test):
        teY[i] = float(data[0])
    return teX,teY

# 디버깅용
get_training_data()