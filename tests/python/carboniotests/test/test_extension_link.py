"""The Linux static libuv package exports libuv::uv_a, not libuv::uv.

_ssl used to name libuv::uv directly, so configure failed before this module
existed. Importing it is the runtime check that the selected target linked.
"""

import importlib
import unittest


class ExtensionLinkTest(unittest.TestCase):
    def test_static_libuv_modules_import(self):
        for name in ("_carbonsocket", "carbonselect", "_carbonssl"):
            module = importlib.import_module(name)
            self.assertTrue(module.__file__)


if __name__ == "__main__":
    unittest.main()
