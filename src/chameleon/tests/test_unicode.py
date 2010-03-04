# -*- encoding: utf-8 -*-
import unittest

class TestUnicodeMisc(unittest.TestCase):
    def test_utf8_in_page_text_template_file(self):
        import os
        path = os.path.join(os.path.dirname(__file__), "templates")
        from chameleon.zpt.template import PageTextTemplateFile
        t = PageTextTemplateFile(os.path.join(path, 'helloworld.txt'))
        result = t().decode('utf-8')
        self.assertEqual(result,
                         u'Hello World!\nTesting utf-8: \xe4\xf6\xfc\xdf\n')

    def test_utf8_values_in_page_text_template_file(self):
        import os
        path = os.path.join(os.path.dirname(__file__), "templates")
        from chameleon.zpt.template import PageTextTemplateFile
        t = PageTextTemplateFile(os.path.join(path, 'uglyworld.txt'))
        value = u'ä'.encode("utf-8")
        result = t(value=value).decode('utf-8')
        self.assertEqual(result,
                u'Inserting a value: ä\n')

    def test_unicode_values_in_page_text_template_file(self):
        import os
        path = os.path.join(os.path.dirname(__file__), "templates")
        from chameleon.zpt.template import PageTextTemplateFile
        t = PageTextTemplateFile(os.path.join(path, 'uglyworld.txt'))
        value = u'ä'
        result = t(value=value).decode('utf-8')
        self.assertEqual(result,
                u'Inserting a value: ä\n')
