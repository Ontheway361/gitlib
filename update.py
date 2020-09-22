#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":

    with open('file2.log', 'w') as f:
        for i in range(100):
            f.write('%03d\n' % i)
    f.close()
    
