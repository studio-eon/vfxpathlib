import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import vfxpathlib as vp


path1 = '/show/ark/work/e01/s010/c00100/ani/wip/ma/ark_e01_s010_c00100_ani_v01_w01.ma'
sp = vp.ShotPath(path1)
print(sp.hierarchy)
print(sp.project, sp.episode, sp.sequence, sp.shot, sp.task, sp.version, sp.wip)
print(sp.format('{p}_{e}_{q}_{s}_{t}_{v}_{w}'))


path2 = r'C:\show\bee\work\fl01\0010\fx\wip\hip\bee_fl01_0010_fx_v01_w01.hip'
sp = vp.ShotPath(path2)
print(sp.hierarchy)
print(sp.project, sp.episode, sp.sequence, sp.shot, sp.task, sp.version, sp.wip)
print(sp.format('{p}_{q}_{s}_{t}_{v}_{w}'))


path3 = '/show/cat/work/c001/comp/wip/nk/cat_c001_comp_v01_w01.nk'
sp = vp.ShotPath(path3)
print(sp.hierarchy)
print(sp.project, sp.episode, sp.sequence, sp.shot, sp.task, sp.version, sp.wip)
print(sp.format('{p}_{s}_{t}_{v}_{w}'))