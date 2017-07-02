from numpy import exp, dot, array, random

class Layers:
    def __init__(self, number_of_output_neurons, number_of_input_neurons):
        self.synaptic_weights = 2 * random.random((number_of_input_neurons, number_of_output_neurons)) - 1

class NeuralNetwork:
    def __init__(self):
        self.numLayers = []
        self.num_layers = 0

    def addLayer(self, layer):
        self.numLayers.append(layer)
        self.num_layers += 1

    def logistic(self, x):
        return 1 / (1 + exp(-x))

    def derivative(self, x):
        return x * (1 - x)

    def backp(self, train_input, train_ouput, num_iterations):
        for iteration in xrange(num_iterations):
            for layer in xrange(len(numLayers)):

                if layer == 1:
                    output_from_layer_1 = self.calc(train_input)
                    layer1_error = layerx_delta.dot(self.numLayers[1].synaptic_weights.T)
                    layer1_delta = layer1_error * self.derivative(output_from_layer_1)
                    layer1_adjustment = training_input.T.dot(layer1_delta)
                    self.numLayers[0].synaptic_weights += layer1_adjustment
                else:
                    output_from_layer_x = self.calc(train_inputs)
                    layerx_error = training_set_outputs - output_from_layer_x
                    layerx_delta = layer2_error * self.derivative(output_from_layer_x)
                    layerx_adjustment = output_from_layer_1.T.dot(layerx_delta)
                    self.numLayers[layer].synaptic_weights += layerx_adjustment

    def calc(self, inputs):
        for layer in xrange(len(numLayers)):
            if layer == 1:
                output_from_layer1 = self.logistic(dot(inputs, self.numLayers[0].synaptic_weights))
                return output_from_layer1
            else:
                output_from_layerx = self.logistic(dot(output_from_layer1, self.numLayers[layer].synaptic_weights))
                return output_from_layerx

    def print_weights(self):
        for layer in xrange(len(numLayers)):
            print "Layer" + layer + ":"
            print self.numLayers[layer].synaptic_weights
