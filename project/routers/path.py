import argparse 
import pickle
import numpy as np
def pathes(data):
    parser = argparse.ArgumentParser(description ="This a demo for the argparse module!")
    parser.add_argument('--path',metavar = "String",type = str , nargs = "+",help = "The list of String")
    arguments = parser.parse_args()
    if arguments.path:
        #print(arguments.path)
        p=""
        for index in arguments.path:
            if index[0]=="C" or index[0]=="D" or index[0]=="E":
                p =index+":/"
                u=1
            else:
                p+=index+"/"
        print(p)
        loaded_model = pickle.load(open(p+'model.sav','rb'))
        data1 = data
        x = np.array(data).reshape(1,6)
        result = loaded_model.predict(x)
        if x.shape[0] == 1:
            result = result[0]
        return str(result)
    else:
        parser.print_help()    