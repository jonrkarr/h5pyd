##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of H5Serv (HDF5 REST Server) Service, Libraries and      #
# Utilities.  The full HDF5 REST Server copyright notice, including          #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################

import config

if config.get("use_h5py"):
    import h5py
else:
    import h5pyd as h5py
    
from common import ut, TestCase

        
class TestAttribute(TestCase):
    
        
    def test_create(self):
        filename = self.getFileName("create_attribute")
        print("filename:", filename)
         
        f = h5py.File(filename, 'w')
        
        #f.attrs['a1'] = 42  #  to-dofix

        g1 = f.create_group('g1')
 
        g1.attrs['a1'] = 42 
        #g1.attrs['a2'] = [b'hello', b'goodbye']
        n = g1.attrs['a1']
        self.assertEqual(n, 42)
        #words = g1.attrs['a2']
        #self.assertEqual(words[0], b'hello')
        #self.assertEqual(words[1], b'goodbye')     
         
        
if __name__ == '__main__':
    ut.main()


     
    
