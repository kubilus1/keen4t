# Keen4T  
Commander keen4 for Tandy 16 color hack/patch.

Based on the Keen 4 composite CGA patch.  See:
[https://int10h.org/blog/2016/05/dopefish-goes-ntsc-commander-keen-4/](https://int10h.org/blog/2016/05/dopefish-goes-ntsc-commander-keen-4/)

## Usage

1.  Get a copy of Keen 4 CGA.  You should see a checksum like: 
```
$ md5sum KEEN4C.EXE
ebf2e480fb1c44904ccd3b22677d6625  KEEN4C.EXE
```

2.  Extract your keen4 CGA zip.

3.  Copy KEEN4T.BAT, KEEN4T.PAT, CK4PATCH.EXE, c16graph.ck4, and cgahead.ck4
    to the same location.

4. Run in dosbox, or on your Tandy 1000:

```
> KEEN4T.BAT
```

## NOTES:

This is a kind of quick-n-nasty reworking of the 16 color composite work noted
above to Tandy 160x200 mode.  This won't look as good as a nice 320x200 TGA
mode version.

While it _ought_ to technically possible to create a 320x200 TGA
mode version, one would probably want to leverage the EGA graphics.  EGA and
TGA work very differently, however, so it would take quite a lot more work.
