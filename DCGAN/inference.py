import matplotlib.pyplot as plt
import numpy
import torch

from DCGAN.model import Generator
from DCGAN.constants import CHANNELS_IMG, NOISE_DIM, FEATURES_GEN

def test():
    N = 1
    gen = Generator(NOISE_DIM, CHANNELS_IMG, FEATURES_GEN)
    gen.load_state_dict(torch.load("weights"))
    z = torch.randn((N, NOISE_DIM, 1, 1))
    image_output = gen(z)
    im_np = image_output.resize(64,64).detach().numpy()
    im_3d = numpy.stack([im_np,im_np,im_np]).swapaxes(0,1).swapaxes(1,2)
    plt.imshow(im_3d)
    plt.imsave("res", im_3d)
    plt.show()

test()