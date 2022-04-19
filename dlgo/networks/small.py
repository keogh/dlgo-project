from __future__ import absolute_import

# tag::small_network[]
from tensorflow.keras import layers as ly


def layers(input_shape):
    return [
        ly.ZeroPadding2D(padding=3, input_shape=input_shape, data_format='channels_last'),  # <1>
        ly.Conv2D(48, (7, 7), data_format='channels_last'),
        ly.Activation('relu'),

        ly.ZeroPadding2D(padding=2, data_format='channels_last'),  # <2>
        ly.Conv2D(32, (5, 5), data_format='channels_last'),
        ly.Activation('relu'),

        ly.ZeroPadding2D(padding=2, data_format='channels_last'),
        ly.Conv2D(32, (5, 5), data_format='channels_last'),
        ly.Activation('relu'),

        ly.ZeroPadding2D(padding=2, data_format='channels_last'),
        ly.Conv2D(32, (5, 5), data_format='channels_last'),
        ly.Activation('relu'),

        ly.Flatten(),
        ly.Dense(512),
        ly.Activation('relu'),
    ]

# <1> We use zero padding layers to enlarge input images.
# <2> By using `channels_first` we specify that the input plane dimension for our features comes first.
# end::small_network[]
