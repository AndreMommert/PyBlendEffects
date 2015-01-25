__author__ = 'Basti'

import os
from html_renderer import HtmlRenderer

html_renderer = HtmlRenderer.HtmlRenderer()

html_renderer.set_text('Dies ist ein neuer Text.')
html_renderer.set_title('Ein neuer Titel.')
html_renderer.set_copy_path(os.path.dirname(__file__) + '\\das_gerenderte')

html_renderer.add_step(os.path.dirname(__file__) + '\\test_files\\2.jpg', 'testTitel', 'TestText')
html_renderer.add_step(os.path.dirname(__file__) + '\\test_files\\14.jpg', 'testTitel2', 'TestText2')
html_renderer.render_html()
