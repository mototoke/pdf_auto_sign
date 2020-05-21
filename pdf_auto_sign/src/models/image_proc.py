#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np


class ImageProc:
    def __init__(self):
        self.img = None
        self.is_show = False

    def __del__(self):
        cv2.destroyAllWindows()

    def set_image(self, img, is_show: bool):
        self.img = img
        self.is_show = is_show

    def get_large_blank_erea(self):
        # デバッグ
        # cv2.imshow('src', self.img)

        # 2値化
        # - cv2.findContours()は、黒と背景、白を物体として判定する為
        #   cv2.THRESH_BINARY_INV で 2値化し、ネガポジ反転
        # - cv2.THRESH_BINARY は単なる2値化
        # ret, tmp = cv2.threshold(
        #     self.img,
        #     250,  # 閾値
        #     256,  # 画素値の最大値
        #     cv2.THRESH_BINARY_INV)  # 2値化type
        # cv2.imshow('二値化', tmp)
        #
        # img_th = cv2.bitwise_not(tmp)
        # cv2.imshow('二値化：白黒反転', img_th)

        # contours, hierarchy = cv2.findContours(self.img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE )
        # # 輪郭を１つずつ書き込んで出力
        # for j in range(len(contours)):
        #     x, y, w, h = cv2.boundingRect(contours[j])
        #     cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), cv2.LINE_8)
        # cv2.namedWindow('aaa', cv2.WINDOW_NORMAL)
        # cv2.imshow('aaa', self.img)

        height, width = self.img.shape
        # 画像を4分割してリストで保持
        split_imgs = [
            self.img[0:height // 2, 0:width // 2],          # 左上
            self.img[0:height // 2, width // 2:width],      # 右上
            self.img[height // 2:height, width // 2:width], # 右下
            self.img[height // 2:height, 0:width // 2]      # 左下
        ]

        # 矩形の塗りつぶし
        th_split_imgs = []
        for i, split_img in enumerate(split_imgs):
            aa = split_img.copy()
            im = cv2.cvtColor(aa, cv2.COLOR_GRAY2BGR)
            im_con = im.copy()
            im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            retval, im_bw = cv2.threshold(im_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # 輪郭の検出
            contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            # external_contours = np.zeros(split_img.shape)
            # 輪郭を１つずつ書き込んで出力
            # for j in range(len(contours)):
            #     # x, y, w, h = cv2.boundingRect(contours[j])
            #     # cv2.rectangle(split_img, (x, y), (x + w, y + h), (0, 255, 0), cv2.LINE_4)
            #     if hierarchy[0][j][3] == -1:
            #         cv2.drawContours(im, contours, j, 0, -1)

            h, w, c = im_con.shape
            # 分割領域の4割より小さい矩形は塗りつぶす
            area = (h * w) * 0.4
            for j in range(len(contours)):
                retval = cv2.contourArea(contours[j])
                if area > retval:
                    cv2.drawContours(im_con, contours, j, (0, 0, 0), -1)

            # if self.is_show:
            #     cv2.namedWindow(f'clip_img:{i}', cv2.WINDOW_NORMAL)
            #     cv2.imshow(f'clip_img:{i}', im_con)

            im_con_gray = cv2.cvtColor(im_con, cv2.COLOR_BGR2GRAY)
            retval2, im_bw2 = cv2.threshold(im_con_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            th_split_imgs.append(im_bw2)

        # 白黒の面積計算
        white_pixels_list = []
        for i, th_split_img in enumerate(th_split_imgs):
            print(f'th_split_img.size:{i}, {th_split_img.size}')
            white_pixels = cv2.countNonZero(th_split_img)
            print(f'white_pixels:{i}, {white_pixels}')
            black_pixels = th_split_img.size - white_pixels
            print(f'blackPixels:{i}, {black_pixels}')
            white_pixels_list.append(white_pixels)
            # if self.is_show:
            #     cv2.namedWindow(f'white_pixels:{i}', cv2.WINDOW_NORMAL)
            #     cv2.imshow(f'white_pixels:{i}', th_split_img)

        # 白色ピクセルが一番大きい分割領域を取得
        max_white_pixels_index = np.argmax(white_pixels_list)
        print(f'max_white_pixels_index:{max_white_pixels_index}')
        white_max = th_split_imgs[max_white_pixels_index].copy()
        # デバッグ
        # cv2.namedWindow(f'white_max', cv2.WINDOW_NORMAL)
        # cv2.imshow(f'white_max', white_max)
        mu = cv2.moments(white_max, False)
        # 重心座標の取得
        x, y = int(mu["m10"] / mu["m00"]), int(mu["m01"] / mu["m00"])
        print(f'moment_x:{x}, moment_y:{y}')
        if self.is_show:
            cv2.circle(white_max, (x, y), 25, (0, 0, 0), -1)
            cv2.namedWindow(f'moment', cv2.WINDOW_NORMAL)
            cv2.imshow(f'moment', white_max)

        # 分割していない画像での重心位置を得る
        add_x, add_y = (0, 0)
        if max_white_pixels_index == 0:     # 左上
            add_x, add_y = (x, y)
        elif max_white_pixels_index == 1:   # 右上
            add_x, add_y = (width // 2 + x, y)
        elif max_white_pixels_index == 2:   # 右下
            add_x, add_y = (width // 2 + x, height // 2 + y)
        elif max_white_pixels_index == 3:   # 左下
            add_x, add_y = (x, height // 2 + y)
        if self.is_show:
            cv2.circle(self.img, (add_x, add_y), 25, (0, 0, 0), -1)
            cv2.namedWindow(f'image_proc', cv2.WINDOW_NORMAL)
            cv2.imshow(f'image_proc', self.img)

        return add_x, add_y
