# Unit test for sekiro-corrupt-save-fix
# S0000.sl2 is part of Sekiro save file which contains only slot 0
# https://github.com/z0gSh1u/sekiro-corrupt-save-fix

import os.path as path
dirname__ = path.dirname(path.abspath(__file__))

import sys
sys.path.append(path.join(dirname__, '../'))

import unittest

from tool.fix import main as fix_main


class TestAll(unittest.TestCase):
    def test(self):
        fix_main(path.join(dirname__, './S0000.sl2'), 0)
        source = b''
        target = b''
        with open(path.join(dirname__, './S0000.sl2'), 'rb') as fp:
            source = fp.read()
        with open(path.join(dirname__, './S0000.sl2.good'), 'rb') as fp:
            target = fp.read()
        self.assertEqual(str(source), str(target))


if __name__ == '__main__':
    unittest.main()