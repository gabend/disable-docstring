import os

from nose.plugins import Plugin
from nose.case import FunctionTestCase

class DisableDocstring(Plugin):
    """Tells unittest not to use docstrings as test names."""

    name = 'disable-docstring'

    def options(self, parser, env=os.environ):
        super(DisableDocstring, self).options(parser, env=env)
        parser.add_option('--enable-docstring', action="store_true",
                          help=DisableDocstring.__doc__)

    def configure(self, options, conf):
        super(DisableDocstring, self).configure(options, conf)
        if options.enable_docstring:
            self.enabled = False
        else:
            self.enabled = True
        if not self.enabled:
            return

    def describeTest(self, test):
	module_str, python_str, test_str = test.address()
	return '%s:%s' % (module_str, test_str)
