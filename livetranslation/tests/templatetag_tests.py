from django.test import TestCase

from django.template import Template, Context


class Trans_Tests(TestCase):
    """Tests for the {% trans %} template tag"""

    def test_marks_up_translations(self):
        """The {% trans %} tag marks up translations"""
        template = ('{% load livetranslation_tags %}'
                    '{% trans "Text" %} '
                    '{% blocktrans with myvar as value %}'
                    'A "dangerous" </script> {{ value }}'
                    '{% endblocktrans %}')
        rendered = Template(template).render(Context({'myvar': 'value'}))
        self.assertEqual(rendered,
                         u'[livetranslation-id 0/] [livetranslation-id 1/]')

        # todo: move this to middleware tests
        """
        u'<span id="livetranslate-0">Text</span>'
            u'<script type="text/javascript">'
            u'jQuery("#livetranslate-0").livetranslate("Text", "");'
            u'</script> '
            u'<span id="livetranslate-1">A "dangerous" '
            u'</script> value</span>'
            u'<script type="text/javascript">'
            u'jQuery("#livetranslate-1").livetranslate('
            u'"A "dangerous" </script> %(value)s", ""'
            u');</script>')
            """
