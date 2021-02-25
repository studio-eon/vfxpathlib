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
        path = r'C:\show\bee\work\s010\0010\comp\wip\nk\bee_s010_0010_comp_v01_w01.nk'
        sp = ShotPath(path)
        self.assertEqual(
            r'C:\show\bee\work\s010\0010\comp\wip\nk\bee_s010_0010_comp_v01_w01.nk',
            sp.format('{path}')
        )

    def test_format_3(self):
        path = '/show/cue/work/c010/mm/wip/ma/cue_c010_fx_v01_w01.ma'
        sp = ShotPath(path)
        self.assertEqual(
            'cue_c010_fx_v01',
            sp.format('{P}')
        )

if __name__ == '__main__':
    unittest.main()