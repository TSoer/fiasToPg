#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
"""
Created on 20.08.2021

@author: TSoer
"""

import os
import lxml.etree as ET

dir_path = os.path.abspath(os.curdir)
# inputpath = os.path.join(dir_path, 'schemaXSD')
inputpath = '-s:C:\pythonproject\importFias\fiasdbfToPg-main\schemaXSD\AS_ACTSTAT_2_250_08_04_01_01.xsd'
xsltfile = os.path.join(dir_path, 'schemaXSLT', 'template.xsl')
outpath = dir_path

import subprocess

print(subprocess.call(["saxon", "-o:output.xml", inputpath, xsltfile]))



# for dirpath, dirnames, filenames in os.walk(inputpath):
#     for filename in filenames:
#         if filename.endswith(('.xml', '.xsd')):
#             print(os.path.join(inputpath, filename))
#             dom = ET.parse(os.path.join(inputpath, filename))
#             xslt = ET.parse(xsltfile)
#             transform = ET.XSLT(xslt)
#             print(transform)
#             newdom = transform(dom)
#             infile = (ET.tostring(newdom, pretty_print=True))
#             try:
#                 with open(os.path.join(outpath, filename + '.xml'), "a+") as file:
#                     file.write(infile)
#             except Exception as e:
#                 print(e)
#                 for error in transform.error_log:
#                     print(error.message, error.line)


# import win32com.client.dynamic
#
# xslt = win32com.client.dynamic.Dispatch("Msxml2.DOMDocument.4.0")
#
# xslt.load(xsltfile)
# xml = win32com.client.dynamic.Dispatch("Msxml2.DOMDocument.4.0")
#
# xml.load(inputpath)
# output = xml.transformNode(xslt)
# open(outpath + 'asdas.xml', 'wb').write(output)