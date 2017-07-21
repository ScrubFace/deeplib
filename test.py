import neural
from numpy import random
from neural import Layers, NeuralNetwork

if __name__ == "__main__":
    random.seed(1)
    
    layer1 = Layers(1,3)
    
    network = NeuralNetwork()
    
    network.addLayer(layer1)
    
    print (network.printweights)
    
    train_in = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    train_out = array([[0, 1, 1, 0]]).T
    
    network.train(train_in, train_out, 70000)
    
    print(network.printweights)
    
    print "Stage 3) Considering a new situation [1, 1, 0] -> ?: "
    output = network.calc(array([1, 1, 0]))
    print output
    
    