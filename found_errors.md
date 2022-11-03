# AFL
## ASan
### stack-buffer-overflow

id:000000,sig:06,sync:main_small,src:000503
```log
=================================================================
==175343==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffe29c85a30 at pc 0x560334fc5563 bp 0x7ffe29c81880 sp 0x7ffe29c81878
WRITE of size 1 at 0x7ffe29c85a30 thread T0
    #0 0x560334fc5562 in build_huffman /src/stb_image.c:929:23
    #1 0x560334fc1303 in process_marker /src/stb_image.c:1427:21
    #2 0x560334f937e8 in decode_jpeg_header /src/stb_image.c:1558:12
    #3 0x560334f89c98 in decode_jpeg_image /src/stb_image.c:1574:9
    #4 0x560334f89c98 in load_jpeg_image /src/stb_image.c:1738:9
    #5 0x560334f84130 in stbi_jpeg_load_from_file /src/stb_image.c:1835:11
    #6 0x560334f84130 in stbi_load_from_file /src/stb_image.c:481:14
    #7 0x560334fbb43a in stbi_load /src/stb_image.c:472:13
    #8 0x560334fbb43a in main /src/jpg2tga.c:400:25
    #9 0x7f96fb2bed8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #10 0x7f96fb2bee3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #11 0x560334ea5494 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0x25494) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)

Address 0x7ffe29c85a30 is located in stack of thread T0 at offset 14800 in frame
    #0 0x560334f83e8f in stbi_load_from_file /src/stb_image.c:478

  This frame has 9 object(s):
    [32, 72) 's.i116' (line 3356)
    [112, 152) 's.i113' (line 3782)
    [192, 232) 's.i110' (line 3570)
    [272, 312) 's.i104' (line 3382)
    [352, 392) 's.i101' (line 3070)
    [432, 472) 's.i' (line 2805)
    [512, 576) 'p.i92' (line 2720)
    [608, 672) 'p.i' (line 2746)
    [704, 14800) 'j.i' (line 1833) <== Memory access at offset 14800 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /src/stb_image.c:929:23 in build_huffman
Shadow bytes around the buggy address:
  0x100045388af0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100045388b00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100045388b10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100045388b20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100045388b30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x100045388b40: 00 00 00 00 00 00[f3]f3 f3 f3 f3 f3 f3 f3 f3 f3
  0x100045388b50: f3 f3 f3 f3 f3 f3 f3 f3 f3 f3 f3 f3 f3 f3 f3 f3
  0x100045388b60: f3 f3 f3 f3 f3 f3 f3 f3 00 00 00 00 00 00 00 00
  0x100045388b70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x100045388b80: f1 f1 f1 f1 04 f2 04 f2 04 f2 04 f2 04 f2 04 f2
  0x100045388b90: 04 f2 f8 f8 f8 f8 f8 f3 f3 f3 f3 f3 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==175343==ABORTING
returned exit code 1
```

id:000001,sig:06,src:001210,time:602108,execs:48773,op:havoc,rep:4
```log
=================================================================
==30825==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffe1c0b98c4 at pc 0x561d4fb746ba bp 0x7ffe1c0b9890 sp 0x7ffe1c0b9060
WRITE of size 32 at 0x7ffe1c0b98c4 thread T0
    #0 0x561d4fb746b9 in __asan_memcpy (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa76b9) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)
    #1 0x561d4fbf4b2a in tga_load /src/stb_image.c:3239:18
    #2 0x561d4fbd17b4 in stbi_tga_load_from_file /src/stb_image.c:3358:11
    #3 0x561d4fbd17b4 in stbi_load_from_file /src/stb_image.c:499:14
    #4 0x561d4fc0843a in stbi_load /src/stb_image.c:472:13
    #5 0x561d4fc0843a in main /src/jpg2tga.c:400:25
    #6 0x7f4610c21d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #7 0x7f4610c21e3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #8 0x561d4faf2494 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0x25494) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)

Address 0x7ffe1c0b98c4 is located in stack of thread T0 at offset 36 in frame
    #0 0x561d4fbf308f in tga_load /src/stb_image.c:3126

  This frame has 1 object(s):
    [32, 36) 'raw_data' (line 3145) <== Memory access at offset 36 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa76b9) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e) in __asan_memcpy
Shadow bytes around the buggy address:
  0x10004380f2c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004380f2d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004380f2e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004380f2f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004380f300: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x10004380f310: 00 00 00 00 f1 f1 f1 f1[04]f3 f3 f3 00 00 00 00
  0x10004380f320: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004380f330: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10004380f340: 00 00 00 00 00 00 00 00 00 00 00 00 f1 f1 f1 f1
  0x10004380f350: 00 00 00 00 00 f2 f2 f2 f2 f2 f8 f8 f8 f8 f8 f2
  0x10004380f360: f2 f2 f2 f2 f8 f8 f8 f8 f8 f2 f2 f2 f2 f2 f8 f8
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==30825==ABORTING
returned exit code 1
```

### requested allocation size exceeds maximum supported size

id:000001,sig:11,src:000660,time:583406,execs:825085,op:havoc,rep:8
```log
=================================================================
==178368==ERROR: AddressSanitizer: requested allocation size 0xfffffffffffe0001 (0xfffffffffffe1008 after adjustments for alignment, red zones etc.) exceeds maximum supported size of 0x10000000000 (thread T0)
    #0 0x55fb935482de in __interceptor_malloc (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa82de) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)
    #1 0x55fb935c752b in tga_load /src/stb_image.c:3189:29
    #2 0x55fb935a47b4 in stbi_tga_load_from_file /src/stb_image.c:3358:11
    #3 0x55fb935a47b4 in stbi_load_from_file /src/stb_image.c:499:14
    #4 0x55fb935db43a in stbi_load /src/stb_image.c:472:13
    #5 0x55fb935db43a in main /src/jpg2tga.c:400:25
    #6 0x7fc3403b4d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16

==178368==HINT: if you don't care about these errors you may set allocator_may_return_null=1
SUMMARY: AddressSanitizer: allocation-size-too-big (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa82de) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e) in __interceptor_malloc
==178368==ABORTING
returned exit code 1
```


### Global buffer overflow

id:000006,sig:06,src:001343+000521,time:909325,execs:114628,op:splice,rep:8
```log
=================================================================
==20743==ERROR: AddressSanitizer: global-buffer-overflow on address 0x55b5c816eabc at pc 0x55b5c8106bb0 bp 0x7ffff5deb1b0 sp 0x7ffff5deb1a8
READ of size 4 at 0x55b5c816eabc thread T0
    #0 0x55b5c8106baf in extend_receive /src/stb_image.c:1041:49
    #1 0x55b5c8106baf in decode_block /src/stb_image.c:1079:15
    #2 0x55b5c8106baf in parse_entropy_coded_data /src/stb_image.c:1352:27
    #3 0x55b5c8106baf in decode_jpeg_image /src/stb_image.c:1579:15
    #4 0x55b5c8106baf in load_jpeg_image /src/stb_image.c:1738:9
    #5 0x55b5c80f8130 in stbi_jpeg_load_from_file /src/stb_image.c:1835:11
    #6 0x55b5c80f8130 in stbi_load_from_file /src/stb_image.c:481:14
    #7 0x55b5c812f43a in stbi_load /src/stb_image.c:472:13
    #8 0x55b5c812f43a in main /src/jpg2tga.c:400:25
    #9 0x7fe556bf3d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #10 0x7fe556bf3e3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #11 0x55b5c8019494 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0x25494) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)

0x55b5c816eabc is located 36 bytes to the left of global variable '<string literal>' defined in '/src/stb_image.c:1494:91' (0x55b5c816eae0) of size 6
  '<string literal>' is ascii string 'bad H'
0x55b5c816eabc is located 11 bytes to the right of global variable '<string literal>' defined in '/src/stb_image.c:1492:20' (0x55b5c816eaa0) of size 17
  '<string literal>' is ascii string 'bad component ID'
SUMMARY: AddressSanitizer: global-buffer-overflow /src/stb_image.c:1041:49 in extend_receive
Shadow bytes around the buggy address:
  0x0ab739025d00: f9 f9 f9 f9 00 00 00 06 f9 f9 f9 f9 00 00 f9 f9
  0x0ab739025d10: 00 00 01 f9 f9 f9 f9 f9 00 04 f9 f9 00 05 f9 f9
  0x0ab739025d20: 00 06 f9 f9 00 07 f9 f9 00 00 01 f9 f9 f9 f9 f9
  0x0ab739025d30: 07 f9 f9 f9 07 f9 f9 f9 00 04 f9 f9 00 03 f9 f9
  0x0ab739025d40: 00 00 01 f9 f9 f9 f9 f9 00 f9 f9 f9 00 00 04 f9
=>0x0ab739025d50: f9 f9 f9 f9 00 00 01[f9]f9 f9 f9 f9 06 f9 f9 f9
  0x0ab739025d60: 06 f9 f9 f9 07 f9 f9 f9 00 02 f9 f9 00 00 f9 f9
  0x0ab739025d70: 00 07 f9 f9 00 00 f9 f9 00 00 00 00 05 f9 f9 f9
  0x0ab739025d80: f9 f9 f9 f9 00 00 07 f9 f9 f9 f9 f9 00 00 01 f9
  0x0ab739025d90: f9 f9 f9 f9 00 00 00 00 05 f9 f9 f9 f9 f9 f9 f9
  0x0ab739025da0: 00 05 f9 f9 00 00 01 f9 f9 f9 f9 f9 00 00 04 f9
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==20743==ABORTING
returned exit code 1
```

### Heap buffer overflow

id:000008,sig:06,src:000895,time:664378,execs:913008,op:havoc,rep:8
```log
=================================================================
==190749==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000000031 at pc 0x55a1b6f5e607 bp 0x7ffd43f8a410 sp 0x7ffd43f89be0
READ of size 8 at 0x602000000031 thread T0
    #0 0x55a1b6f5e606 in __asan_memcpy (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa7606) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)
    #1 0x55a1b6fdeb2a in tga_load /src/stb_image.c:3239:18
    #2 0x55a1b6fbb7b4 in stbi_tga_load_from_file /src/stb_image.c:3358:11
    #3 0x55a1b6fbb7b4 in stbi_load_from_file /src/stb_image.c:499:14
    #4 0x55a1b6ff243a in stbi_load /src/stb_image.c:472:13
    #5 0x55a1b6ff243a in main /src/jpg2tga.c:400:25
    #6 0x7f66f3c10d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #7 0x7f66f3c10e3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #8 0x55a1b6edc494 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0x25494) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)

0x602000000031 is located 0 bytes to the right of 1-byte region [0x602000000030,0x602000000031)
allocated by thread T0 here:
    #0 0x55a1b6f5f2de in __interceptor_malloc (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa82de) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)
    #1 0x55a1b6fde6f3 in tga_load /src/stb_image.c:3199:33
    #2 0x55a1b6fbb7b4 in stbi_tga_load_from_file /src/stb_image.c:3358:11
    #3 0x55a1b6fbb7b4 in stbi_load_from_file /src/stb_image.c:499:14
    #4 0x55a1b6ff243a in stbi_load /src/stb_image.c:472:13
    #5 0x55a1b6ff243a in main /src/jpg2tga.c:400:25
    #6 0x7f66f3c10d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16

SUMMARY: AddressSanitizer: heap-buffer-overflow (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa7606) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa 01 fa fa fa[01]fa fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==190749==ABORTING
returned exit code 1
```

### SEGV

id:000071,sig:11,src:002265,time:6891949,execs:7678026,op:havoc,rep:4
```log
AddressSanitizer:DEADLYSIGNAL
=================================================================
==205916==ERROR: AddressSanitizer: SEGV on unknown address (pc 0x55f3dcfcb6f4 bp 0x000000000000 sp 0x7ffe1e74b1e0 T0)
==205916==The signal is caused by a READ memory access.
==205916==Hint: this fault was caused by a dereference of a high value address (see register values below).  Disassemble the provided pc to learn which register was used.
    #0 0x55f3dcfcb6f4 in __asan::Allocator::Deallocate(void*, unsigned long, unsigned long, __sanitizer::BufferedStackTrace*, __asan::AllocType) (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0x276f4) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)
    #1 0x55f3dd04c095 in free (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0xa8095) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)
    #2 0x55f3dd0b3bec in cleanup_jpeg /src/stb_image.c:1710:10
    #3 0x55f3dd0b3bec in load_jpeg_image /src/stb_image.c:1738:33
    #4 0x55f3dd0a8130 in stbi_jpeg_load_from_file /src/stb_image.c:1835:11
    #5 0x55f3dd0a8130 in stbi_load_from_file /src/stb_image.c:481:14
    #6 0x55f3dd0df43a in stbi_load /src/stb_image.c:472:13
    #7 0x55f3dd0df43a in main /src/jpg2tga.c:400:25
    #8 0x7fd5b90e2d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #9 0x7fd5b90e2e3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #10 0x55f3dcfc9494 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0x25494) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_ASan+0x276f4) (BuildId: 2326064a15111a4eeb9e3df0da94bdb1db4e802e) in __asan::Allocator::Deallocate(void*, unsigned long, unsigned long, __sanitizer::BufferedStackTrace*, __asan::AllocType)
==205916==ABORTING
returned exit code 1
```

## MSan
### SEGV

id:000000,sig:11,sync:main_small,src:001524
```log
MemorySanitizer:DEADLYSIGNAL
==129904==ERROR: MemorySanitizer: SEGV on unknown address (pc 0x564956b6e6fe bp 0x7fffab59d3b0 sp 0x7fffab599c00 T129904)
==129904==The signal is caused by a READ memory access.
==129904==Hint: this fault was caused by a dereference of a high value address (see register values below).  Disassemble the provided pc to learn which register was used.
    #0 0x564956b6e6fe in stbi_tga_load_from_file /src/stb_image.c:3359:1
    #1 0x564956b6e6fe in stbi_load_from_file /src/stb_image.c:499:14
    #2 0x564956ba3dc8 in stbi_load /src/stb_image.c:472:13
    #3 0x564956ba3dc8 in main /src/jpg2tga.c:400:25
    #4 0x7f02c3ba1d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #5 0x7f02c3ba1e3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #6 0x564956abd404 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_MSan+0x1f404) (BuildId: 11adcc2b7f7665b2648e76ab20e45a5c2eee8a52)

MemorySanitizer can not provide additional info.
SUMMARY: MemorySanitizer: SEGV /src/stb_image.c:3359:1 in stbi_tga_load_from_file
==129904==ABORTING
returned exit code 1
```

id:000012,sig:11,src:002369+002018,time:21866864,execs:608999,op:splice,rep:4
```log
MemorySanitizer:DEADLYSIGNAL
==126705==ERROR: MemorySanitizer: SEGV on unknown address (pc 0x563a63f76756 bp 0xa0a0a0a0a0a0a0a sp 0x7ffe7d802958 T126705)
==126705==The signal is caused by a READ memory access.
==126705==Hint: this fault was caused by a dereference of a high value address (see register values below).  Disassemble the provided pc to learn which register was used.
MemorySanitizer:DEADLYSIGNAL
MemorySanitizer: nested bug in the same thread, aborting.
returned exit code 1
```

### Use of uninitialized-value

id:000001,sig:06,src:001929,time:1536579,execs:25126,op:havoc,rep:8
```log
==124248==WARNING: MemorySanitizer: use-of-uninitialized-value
    #0 0x55ca36f6b137 in decode /src/stb_image.c:996:8
    #1 0x55ca36f6b137 in decode_block /src/stb_image.c:1073:12
    #2 0x55ca36f6b137 in parse_entropy_coded_data /src/stb_image.c:1352:27
    #3 0x55ca36f6b137 in decode_jpeg_image /src/stb_image.c:1579:15
    #4 0x55ca36f6b137 in load_jpeg_image /src/stb_image.c:1738:9
    #5 0x55ca36f5dd14 in stbi_jpeg_load_from_file /src/stb_image.c:1835:11
    #6 0x55ca36f5dd14 in stbi_load_from_file /src/stb_image.c:481:14
    #7 0x55ca36f93dc8 in stbi_load /src/stb_image.c:472:13
    #8 0x55ca36f93dc8 in main /src/jpg2tga.c:400:25
    #9 0x7f8e96483d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #10 0x7f8e96483e3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #11 0x55ca36ead404 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_MSan+0x1f404) (BuildId: 11adcc2b7f7665b2648e76ab20e45a5c2eee8a52)

SUMMARY: MemorySanitizer: use-of-uninitialized-value /src/stb_image.c:996:8 in decode
Exiting
returned exit code 1
```

id:000007,sig:06,src:001599,time:8968758,execs:350254,op:havoc,rep:2
```log
==105330==WARNING: MemorySanitizer: use-of-uninitialized-value
    #0 0x561bc9b7921b in main /src/jpg2tga.c:401:11
    #1 0x7fdb27e73d8f in __libc_start_call_main csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #2 0x7fdb27e73e3f in __libc_start_main csu/../csu/libc-start.c:392:3
    #3 0x561bc9a92404 in _start (/home/pohlm01/Documents/Uni/Software_Security/picojpeg/fuzzing_group_02_MSan+0x1f404) (BuildId: 11adcc2b7f7665b2648e76ab20e45a5c2eee8a52)

SUMMARY: MemorySanitizer: use-of-uninitialized-value /src/jpg2tga.c:401:11 in main
Exiting
returned exit code 1
```

### Requested allocation size exceeds maximum supported size

id:000005,sig:11,src:001164+001871,time:8492596,execs:279209,op:splice,rep:2
```log
==128891==ERROR: MemorySanitizer: requested allocation size 0xffffffff9e9ad6ef exceeds maximum supported size of 0x200000000
    <empty stack>

==128891==HINT: if you don't care about these errors you may set allocator_may_return_null=1
SUMMARY: MemorySanitizer: allocation-size-too-big
returned exit code 1
```


## Hangs

A few examples. I cannot distinguish yet, if they have different root causes.
```log
id:000006,src:001876,time:11878351,execs:24325324,op:havoc,rep:2
id:000006,src:001994+002559,time:4541357,execs:4131612,op:splice,rep:8
id:000003,src:002480,time:9437455,execs:368407,op:havoc,rep:4
id:000005,src:002639,time:18459241,execs:482900,op:havoc,rep:2
id:000004,src:000847,time:655217,execs:902193,op:havoc,rep:4

```