# -*- coding: utf-8 -*-
"""Base class for Plugin classes."""

class BasePlugin(object):
    """Base class for APISpec plugin

    :param APISpec spec: APISpec object this plugin instance is attached to
    """
    def init_spec(self, spec):
        """Initialize plugin with APISpec object

        :param APISpec spec: APISpec object this plugin instance is attached to
        """
        self.spec = spec

    def definition_helper(self, name, definition, **kwargs):
        """Must return definition as a dict."""
        raise NotImplementedError

    def path_helper(self, path=None, operations=None, **kwargs):
        """Should return a Path instance. Any other return value type is ignored"""
        raise NotImplementedError

    def operation_helper(self, path=None, operations=None, **kwargs):
        """Should mutate operations. Return value ignored."""
        raise NotImplementedError

    def response_helper(self, method, status_code, **kwargs):
        """Should return a dict to update the response description.

        Returning None is equivalent to returning an empty dictionary.
        """
        raise NotImplementedError
