## API Examples


```python
>>> import vfxpathlib as vp
>>> filepath = '/show/ark/work/e01/s010/c00100/ani/wip/ma/ark_e01_s010_c00100_ani_v01_w01.ma'
>>> sp = vp.ShotPath(filepath)
>>> print(sp.format('%p_%t_%v')) # {project}_{task}_{version}
ark_ani_v01
>>> print(sp.hierarchy)
episode-sequence-shot
```


```python
>>> import vfxpathlib as vp
>>> filepath = '/show/bee/work/s010/0010/mm/wip/ma/bee_s010_0010_mm_v01_w01.ma'
>>> sp = vp.ShotPath(filepath)
>>> print(sp.format('%q_%s')) # {sequence}_{shot}
as2_ani_v01
>>> print(sp.hierarchy)
sequence-shot
```


```python
>>> import vfxpathlib as vp
>>> filepath = '/show/cue/work/c010/mm/wip/ma/cue_c010_fx_v01_w01.ma'
>>> sp = vp.ShotPath(filepath)
>>> print(sp.format('%s_%w')) # {shot}_{wip}
as2_ani_v01
>>> print(sp.hierarchy)
shot
```