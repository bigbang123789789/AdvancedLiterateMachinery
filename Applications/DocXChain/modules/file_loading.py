#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import numpy as np
import cv2

import pdfplumber

def load_image(image_path):

    # initialization
    image = None

    # read image (only JPEG and PNG formats are supported currently) (20230815)
    name = image_path.lower()
    if name.endswith('.jpg') or name.endswith('.png'):
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    return image

def load_pdf(pdf_path):

    # initialization
    image = None

    # read PDF file
    name = pdf_path.lower()
    if name.endswith('.pdf'):
        with pdfplumber.open(pdf_path) as pdf:
            first_page = pdf.pages[0]
            page_image = first_page.to_image(resolution=150) # convert the first page to image by default (20230815)
            image = cv2.cvtColor(np.array(page_image.original), cv2.COLOR_RGB2BGR)

            pdf.close()

    return image

def load_document(document_path):

    # initialization
    image = None

    # load file
    name = document_path.lower()
    if name.endswith('.pdf'):
        image = load_pdf(document_path)
    else:
        image = load_image(document_path)

    return image