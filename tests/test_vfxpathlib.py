import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vfxpathlib import ShotPath
import vfxpathlib 

class ShotPathTestCase(unittest.TestCase):
    def test_format_1(self):
        path = '/show/ark/work/e01/s010/c00100/ani/wip/ma/ark_e01_s010_c00100_ani_v01_w01.ma'
        sp = ShotPath(path)
        self.assertEqual(
            'ark_e01_s010_c00100_ani_v01_w01',
            sp.format('{p}_{e}_{q}_{s}_{t}_{v}_{w}')
        )

    def test_format_2(self):
        path = r'C:\show\bee\work\fl01\0010\fx\wip\hip\bee_fl01_0010_fx_v01_w01.hip'
        sp = ShotPath(path)
        self.assertEqual(
            'bee_fl01_0010_fx_v01_w01',
            sp.format('{p}_{q}_{s}_{t}_{v}_{w}')
        )

    def test_format_3(self):
        path = '/show/cat/work/c001/comp/wip/nk/cat_c001_comp_v01_w01.nk'
        sp = ShotPath(path)
        self.assertEqual(
            'cat_c001_comp_v01_w01',
            sp.format('{p}_{s}_{t}_{v}_{w}')
        )

if __name__ == '__main__':
    unittest.main()