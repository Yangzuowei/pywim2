from __future__ import division, absolute_import, print_function

import unittest
import numpy as np
from numpy.testing import *

import pywim2
from pywim2 import channel



class TestChannelFilter(unittest.TestCase):
    def test_multipath(self):
        model = channel.Model()
        input = np.ones((1,10))

        coef = np.zeros((1,1,3,10))
        coef[0,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        delay = [0,1,2]
        output = model.filter(input, coef, delay)
        assert_array_equal(output,
                           np.array(((1,3,6,6,6,6,6,6,6,6),)))

        input = np.array(((1,1,1,1,1,1,1,1,1,1),
                          (2,2,2,2,2,2,2,2,2,2)))
        coef = np.zeros((2,1,3,10))
        coef[0,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        coef[1,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        output = model.filter(input, coef, delay)
        assert_array_equal(output,
                           np.array(((3,9,18,18,18,18,18,18,18,18),)))


        input = np.ones((1,10))
        coef = np.zeros((1,2,3,10))
        coef[0,0,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        coef[0,1,:,:] = np.array(
            ((1,1,1,1,1,1,1,1,1,1),
             (2,2,2,2,2,2,2,2,2,2),
             (3,3,3,3,3,3,3,3,3,3)))
        output = model.filter(input, coef, delay)
        assert_array_equal(output,
                           np.array(((1,3,6,6,6,6,6,6,6,6),
                                     (1,3,6,6,6,6,6,6,6,6))))
        
    def test_multiantenna(self):
        pass
        
if __name__ == '__main__':
    unittest.main()
    

