__author__ = 'Basti'

import shutil, os
from html_renderer import HtmlRenderer

html_renderer = HtmlRenderer.HtmlRenderer()

html_renderer.add_step('D:\\Programme\\Programmierung\\Projekte\\OOSL_SEM\\test_files\\2.jpg', 'testTitel', 'TestText')
html_renderer.add_step('D:\\Programme\\Programmierung\\Projekte\\OOSL_SEM\\test_files\\14.jpg', 'testTitel2', 'TestText2')
html_renderer.render_html()



