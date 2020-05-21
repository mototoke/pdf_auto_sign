#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy


def find_homography(src, dst):
    """
    各座標系の対応する4点以上の位置から
    射影変換行列を作成します
    :param src:
    :param dst:
    :return:
    """
    # X = (x*h0 +y*h1 + h2) / (x*h6 + y*h7 + 1)
    # Y = (x*h3 +y*h4 + h5) / (x*h6 + y*h7 + 1)
    #
    # X = (x*h0 +y*h1 + h2) - x*h6*X - y*h7*X
    # Y = (x*h3 +y*h4 + h5) - x*h6*Y - y*h7*Y
    
    x1, y1 = src[0]
    x2, y2 = src[1]
    x3, y3 = src[2]
    x4, y4 = src[3]
    
    u1, v1 = dst[0]
    u2, v2 = dst[1]
    u3, v3 = dst[2]
    u4, v4 = dst[3]
    
    A = numpy.matrix([
            [x1, y1, 1, 0, 0, 0, -x1*u1, -y1*u1, 0],
            [0, 0, 0, x1, y1, 1, -x1*v1, -y1*v1, 0],
            [x2, y2, 1, 0, 0, 0, -x2*u2, -y2*u2, 0],
            [0, 0, 0, x2, y2, 1, -x2*v2, -y2*v2, 0],
            [x3, y3, 1, 0, 0, 0, -x3*u3, -y3*u3, 0],
            [0, 0, 0, x3, y3, 1, -x3*v3, -y3*v3, 0],
            [x4, y4, 1, 0, 0, 0, -x4*u4, -y4*u4, 0],
            [0, 0, 0, x4, y4, 1, -x4*v4, -y4*v4, 0],
            [0, 0, 0,  0,  0, 0,      0,      0, 1],
            ])
    B = numpy.matrix([
            [u1],
            [v1],
            [u2],
            [v2],
            [u3],
            [v3],
            [u4],
            [v4],
            [1],
            ])
    
    X = A.I * B
    X.shape = (3, 3)
    x_mat = numpy.matrix(X)
    return x_mat


if __name__ == '__main__':
    src_ = [[0, 0], [100, 0], [100, 100], [0, 100]]
    dst_ = [[20, 20], [120, 20], [120, 120], [20, 120]]
    
    homography = find_homography(src_, dst_)
    
    print(homography)
    
    target = numpy.array([100, 0, 1])
    Y = numpy.dot(homography, target)
    print(Y)

    # 逆変換
    Y_ = numpy.squeeze(numpy.asarray(Y))
    homography_inverse = numpy.linalg.inv(homography)
    Y_inverse = numpy.dot(homography_inverse, Y_)
    print(Y_inverse)

