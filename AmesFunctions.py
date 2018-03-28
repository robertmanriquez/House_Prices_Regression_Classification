import matplotlib.pyplot as plt

def PlotResiduals(y_train_predict,y_train):


    plt.figure(figsize = (10,8))
    plt.scatter(y_train_predict, y_train - y_train_predict,
                c='steelblue', marker = 'o', s = 60.0, edgecolor = 'white', label = 'Training data', alpha =0.5)
    plt.scatter(y_test_predict, y_test - y_test_predict,
               c='limegreen', marker = 's', s = 60.0, edgecolor = 'white', label = 'Test Data', alpha = 0.5)
    plt.xlabel('True Values', fontsize = 15)
    plt.ylabel('Residuals', fontsize = 15)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.legend(loc = 'upper left', fontsize = 15)
    plt.hlines(y=0, xmin = -100000, xmax =600000, color = 'black', lw=2)
    plt.show()
