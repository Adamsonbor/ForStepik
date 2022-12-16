class Layer:
    
    def __init__(self):
        self.name = 'layer'
        self.next_layer = None

    
    def __call__(self, layer):
        self.next_layer = layer
        return layer



class Input(Layer):

    def __init__(self, inputs):
        super().__init__()
        self.inputs = inputs
        self.name = 'Input'



class Dense(Layer):

    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation



class NetworkIterator:

    def __new__(self, network):
        obj = network
        while obj:
            yield obj
            obj = obj.next_layer



class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        self.it = self.network
        return self

    def __next__(self):
        if self.it is None:
            raise StopIteration
        out = self.it
        self.it = self.it.next_layer
        return out
        


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
a = NetworkIterator(network)
for i in NetworkIterator(network):
    print(i.name)


