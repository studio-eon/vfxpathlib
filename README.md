## API Examples
### episode-sequence-shot
```python
>>> import vfxpathlib as vp
>>> path = '/show/ark/work/e01/s010/c00100/ani/wip/ma/ark_e01_s010_c00100_ani_v01_w01.ma'
>>> sp = vp.ShotPath(path)
>>> print(sp.hierarchy)
episode-sequence-shot
>>> print(sp.project, sp.episode, sp.sequence, sp.shot, sp.task, sp.version, sp.wip)
ark e01 s010 c00100 ani v01 w01
>>> print(sp.format('{p}_{e}_{q}_{s}_{t}_{v}_{w}'))
ark_e01_s010_c00100_ani_v01_w01
```

### sequence-shot
```python
>>> import vfxpathlib as vp
>>> path = r'C:\show\bee\work\fl01\0010\fx\wip\hip\bee_fl01_0010_fx_v01_w01.hip'
>>> sp = vp.ShotPath(path)
>>> print(sp.hierarchy)
sequence-shot
>>> print(sp.project, sp.episode, sp.sequence, sp.shot, sp.task, sp.version, sp.wip)
bee None fl01 0010 fx v01 w01
>>> print(sp.format('{p}_{q}_{s}_{t}_{v}_{w}'))
bee_fl01_0010_fx_v01_w01
```

### shot
```python
>>> import vfxpathlib as vp
>>> path = '/show/cat/work/c001/comp/wip/nk/cat_c001_comp_v01_w01.nk'
>>> sp = vp.ShotPath(path)
>>> print(sp.hierarchy)
shot
>>> print(sp.project, sp.episode, sp.sequence, sp.shot, sp.task, sp.version, sp.wip)
cat None None c001 comp v01 w01
>>> print(sp.format('{p}_{s}_{t}_{v}_{w}'))
cat_c001_comp_v01_w01
```