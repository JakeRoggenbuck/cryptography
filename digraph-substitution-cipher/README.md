### Digraph substitution cipher

Similar to the [monoalphabetic table-substitution-cipher](https://github.com/thondascully/cryptography/edit/master/table-substitution-cipher), this is another substitution cipher. Unlike the monoalphabetic table cipher, instead of replacing every plaintext letter with its corresponding ciphertext letter,
this cipher replaces every plaintext digraph with its corresponding ciphertext digraph.

### What does the digraph substitution cipher do?

Think of a standard 10x10 multiplication table. If I want to multiply `5` by `6`, I first find the `5` column label, and then I move down to the corresponding `6` row label. At this point, both the column and row will intersect at the `30` value. 

For a digraph substitution cipher, the row and column labels are alphabet letters instead of 1..10, and the values are the corresponding ciphertext digraphs.

_For simplicity's sake, this will only handle lowercase alphabets._

### Disclaimer: do NOT implement this as a security tool. A single key shift results in a bad [substitution box](https://en.wikipedia.org/wiki/S-box). Truly random sbox choices should provide the 26*26 possible choices per digraph ciphertext, but this sbox is not random (since it remains in an ordered alphabetic permutation).

More information on how to break this cipher is below

-----------------------

### Implementation

Instead of each row/column label expressing `abcdef..`, we can add disorder by shifting the labels, making the table less predictable. Ex: `abcdef..` -> `fghijk..`

```python 'ignore
shift_row = 4
shift_column = 17

alpha = "abcdefghijklmnopqrstuvwxyz"

# Shifts the alphabet over by `shift` amount. Loops overflow values to start.
def shift_alpha(alpha, shift) -> str:
    return alpha[shift:len(alpha)] + alpha[:shift]
```
```python 'ignore
sbox = [[shift_alpha(alpha, shift_column)[i] + (shift_alpha(alpha, shift_row)[j])
         for j in range(len(alpha))] for i in range(len(alpha))]
```

`sbox` is displayed below (generated with [print_table.py](https://github.com/thondascully/cryptography/blob/master/digraph-substitution-cipher/python/print_table.py))

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
| 1 | `re` | `rf` | `rg` | `rh` | `ri` | `rj` | `rk` | `rl` | `rm` | `rn` | `ro` | `rp` | `rq` | `rr` | `rs` | `rt` | `ru` | `rv` | `rw` | `rx` | `ry` | `rz` | `ra` | `rb` | `rc` | `rd` |
| 2 | `se` | `sf` | `sg` | `sh` | `si` | `sj` | `sk` | `sl` | `sm` | `sn` | `so` | `sp` | `sq` | `sr` | `ss` | `st` | `su` | `sv` | `sw` | `sx` | `sy` | `sz` | `sa` | `sb` | `sc` | `sd` |
| 3 | `te` | `tf` | `tg` | `th` | `ti` | `tj` | `tk` | `tl` | `tm` | `tn` | `to` | `tp` | `tq` | `tr` | `ts` | `tt` | `tu` | `tv` | `tw` | `tx` | `ty` | `tz` | `ta` | `tb` | `tc` | `td` |
| 4 | `ue` | `uf` | `ug` | `uh` | `ui` | `uj` | `uk` | `ul` | `um` | `un` | `uo` | `up` | `uq` | `ur` | `us` | `ut` | `uu` | `uv` | `uw` | `ux` | `uy` | `uz` | `ua` | `ub` | `uc` | `ud` |
| 5 | `ve` | `vf` | `vg` | `vh` | `vi` | `vj` | `vk` | `vl` | `vm` | `vn` | `vo` | `vp` | `vq` | `vr` | `vs` | `vt` | `vu` | `vv` | `vw` | `vx` | `vy` | `vz` | `va` | `vb` | `vc` | `vd` |
| 6 | `we` | `wf` | `wg` | `wh` | `wi` | `wj` | `wk` | `wl` | `wm` | `wn` | `wo` | `wp` | `wq` | `wr` | `ws` | `wt` | `wu` | `wv` | `ww` | `wx` | `wy` | `wz` | `wa` | `wb` | `wc` | `wd` |
| 7 | `xe` | `xf` | `xg` | `xh` | `xi` | `xj` | `xk` | `xl` | `xm` | `xn` | `xo` | `xp` | `xq` | `xr` | `xs` | `xt` | `xu` | `xv` | `xw` | `xx` | `xy` | `xz` | `xa` | `xb` | `xc` | `xd` |
| 8 | `ye` | `yf` | `yg` | `yh` | `yi` | `yj` | `yk` | `yl` | `ym` | `yn` | `yo` | `yp` | `yq` | `yr` | `ys` | `yt` | `yu` | `yv` | `yw` | `yx` | `yy` | `yz` | `ya` | `yb` | `yc` | `yd` |
| 9 | `ze` | `zf` | `zg` | `zh` | `zi` | `zj` | `zk` | `zl` | `zm` | `zn` | `zo` | `zp` | `zq` | `zr` | `zs` | `zt` | `zu` | `zv` | `zw` | `zx` | `zy` | `zz` | `za` | `zb` | `zc` | `zd` |
| 10 | `ae` | `af` | `ag` | `ah` | `ai` | `aj` | `ak` | `al` | `am` | `an` | `ao` | `ap` | `aq` | `ar` | `as` | `at` | `au` | `av` | `aw` | `ax` | `ay` | `az` | `aa` | `ab` | `ac` | `ad` |
| 11 | `be` | `bf` | `bg` | `bh` | `bi` | `bj` | `bk` | `bl` | `bm` | `bn` | `bo` | `bp` | `bq` | `br` | `bs` | `bt` | `bu` | `bv` | `bw` | `bx` | `by` | `bz` | `ba` | `bb` | `bc` | `bd` |
| 12 | `ce` | `cf` | `cg` | `ch` | `ci` | `cj` | `ck` | `cl` | `cm` | `cn` | `co` | `cp` | `cq` | `cr` | `cs` | `ct` | `cu` | `cv` | `cw` | `cx` | `cy` | `cz` | `ca` | `cb` | `cc` | `cd` |
| 13 | `de` | `df` | `dg` | `dh` | `di` | `dj` | `dk` | `dl` | `dm` | `dn` | `do` | `dp` | `dq` | `dr` | `ds` | `dt` | `du` | `dv` | `dw` | `dx` | `dy` | `dz` | `da` | `db` | `dc` | `dd` |
| 14 | `ee` | `ef` | `eg` | `eh` | `ei` | `ej` | `ek` | `el` | `em` | `en` | `eo` | `ep` | `eq` | `er` | `es` | `et` | `eu` | `ev` | `ew` | `ex` | `ey` | `ez` | `ea` | `eb` | `ec` | `ed` |
| 15 | `fe` | `ff` | `fg` | `fh` | `fi` | `fj` | `fk` | `fl` | `fm` | `fn` | `fo` | `fp` | `fq` | `fr` | `fs` | `ft` | `fu` | `fv` | `fw` | `fx` | `fy` | `fz` | `fa` | `fb` | `fc` | `fd` |
| 16 | `ge` | `gf` | `gg` | `gh` | `gi` | `gj` | `gk` | `gl` | `gm` | `gn` | `go` | `gp` | `gq` | `gr` | `gs` | `gt` | `gu` | `gv` | `gw` | `gx` | `gy` | `gz` | `ga` | `gb` | `gc` | `gd` |
| 17 | `he` | `hf` | `hg` | `hh` | `hi` | `hj` | `hk` | `hl` | `hm` | `hn` | `ho` | `hp` | `hq` | `hr` | `hs` | `ht` | `hu` | `hv` | `hw` | `hx` | `hy` | `hz` | `ha` | `hb` | `hc` | `hd` |
| 18 | `ie` | `if` | `ig` | `ih` | `ii` | `ij` | `ik` | `il` | `im` | `in` | `io` | `ip` | `iq` | `ir` | `is` | `it` | `iu` | `iv` | `iw` | `ix` | `iy` | `iz` | `ia` | `ib` | `ic` | `id` |
| 19 | `je` | `jf` | `jg` | `jh` | `ji` | `jj` | `jk` | `jl` | `jm` | `jn` | `jo` | `jp` | `jq` | `jr` | `js` | `jt` | `ju` | `jv` | `jw` | `jx` | `jy` | `jz` | `ja` | `jb` | `jc` | `jd` |
| 20 | `ke` | `kf` | `kg` | `kh` | `ki` | `kj` | `kk` | `kl` | `km` | `kn` | `ko` | `kp` | `kq` | `kr` | `ks` | `kt` | `ku` | `kv` | `kw` | `kx` | `ky` | `kz` | `ka` | `kb` | `kc` | `kd` |
| 21 | `le` | `lf` | `lg` | `lh` | `li` | `lj` | `lk` | `ll` | `lm` | `ln` | `lo` | `lp` | `lq` | `lr` | `ls` | `lt` | `lu` | `lv` | `lw` | `lx` | `ly` | `lz` | `la` | `lb` | `lc` | `ld` |
| 22 | `me` | `mf` | `mg` | `mh` | `mi` | `mj` | `mk` | `ml` | `mm` | `mn` | `mo` | `mp` | `mq` | `mr` | `ms` | `mt` | `mu` | `mv` | `mw` | `mx` | `my` | `mz` | `ma` | `mb` | `mc` | `md` |
| 23 | `ne` | `nf` | `ng` | `nh` | `ni` | `nj` | `nk` | `nl` | `nm` | `nn` | `no` | `np` | `nq` | `nr` | `ns` | `nt` | `nu` | `nv` | `nw` | `nx` | `ny` | `nz` | `na` | `nb` | `nc` | `nd` |
| 24 | `oe` | `of` | `og` | `oh` | `oi` | `oj` | `ok` | `ol` | `om` | `on` | `oo` | `op` | `oq` | `or` | `os` | `ot` | `ou` | `ov` | `ow` | `ox` | `oy` | `oz` | `oa` | `ob` | `oc` | `od` |
| 25 | `pe` | `pf` | `pg` | `ph` | `pi` | `pj` | `pk` | `pl` | `pm` | `pn` | `po` | `pp` | `pq` | `pr` | `ps` | `pt` | `pu` | `pv` | `pw` | `px` | `py` | `pz` | `pa` | `pb` | `pc` | `pd` |
| 26 | `qe` | `qf` | `qg` | `qh` | `qi` | `qj` | `qk` | `ql` | `qm` | `qn` | `qo` | `qp` | `qq` | `qr` | `qs` | `qt` | `qu` | `qv` | `qw` | `qx` | `qy` | `qz` | `qa` | `qb` | `qc` | `qd` |

### Verification

If we look at the table, we see that the `h` character is denoted by `8`. Likewise, the `e` character is denoted by `5`. By finding the intersection point at `(8, 5)`, we see that the resulting ciphertext digraph is `vl`, which matches our program's output.

```python 'ignore
string = "he"
print("Encrypting string %s... %s" % (string, encrypt(string)))
print("Decrypting string %s... %s" % (encrypt(string), decrypt(encrypt(string))))
```

Result: 

<img width="899" alt="Screen Shot 2022-12-21 at 9 55 11 PM" src="https://user-images.githubusercontent.com/114739901/209066874-0e9da925-fdb9-4759-ad6f-043d9740d600.png">

### Breaking an ordered alphabetic permutation digraph substitution cipher:

Cracking a digraph table substitution cipher whose sbox generator is not random boils down to finding a cipher text digraph that has two repeating letters. 

For example, `(C, P)` returns `GG` . Since each row and column is an ordered alphabetic permutation (shifted), the user now knows the row is shifted by `G-C` = `17` letters. Likewise, the column is shifted `G-P` = `4` letters. Those are the shift keys...

In reality, an sbox design should choose each digraph result uniformly at random without replacement, but there other are ways to design it to be even more resistant to [differential cryptanaylsis](https://en.wikipedia.org/wiki/Differential_cryptanalysis)

### Immediate ways to strengthen the digraph substitution cipher:

Instead of using a `row shift` and a `column shift`, one can create the row and column labels from two separate mixed alphabets created from two different keys. In this case, the mixed alphabet is created by writing out the key word and then filling in the rest of the alphabet using the unused letters. The [playfair cipher](https://github.com/thondascully/cryptography/tree/master/playfair-cipher)'s matrix is created using this mixed alphabet method, so visit that directory for more information.

Example:

```python 'ignore
key = "shadow"
mixed_alphabet_for_label = "shadowbcefgijklmnpqrtuvxyz"
```

Additionally, one can randomize the alphabet completely to make an sbox with 26^26 plaintext options for every ciphertext digraph position.

# Test cases

```python 'ignore
string = "hello world"
```

<img width="635" alt="Screen Shot 2022-12-21 at 9 11 40 PM" src="https://user-images.githubusercontent.com/114739901/209061878-59d91b5a-2566-4485-9895-f6be3e7cc34b.png">

```python 'ignore
string = "a"
```

<img width="635" alt="Screen Shot 2022-12-21 at 9 12 00 PM" src="https://user-images.githubusercontent.com/114739901/209061884-df74de7d-ee86-497d-80b4-7bb509cc80ae.png">

```python 'ignore
string = "b"
```

<img width="635" alt="Screen Shot 2022-12-21 at 9 12 27 PM" src="https://user-images.githubusercontent.com/114739901/209061888-986d603c-a7bf-4de5-bd9c-046270db4a74.png">

```python 'ignore
string = "from teo"
```

<img width="635" alt="Screen Shot 2022-12-21 at 9 13 06 PM" src="https://user-images.githubusercontent.com/114739901/209061894-f2ac3d57-634d-4197-ab9f-c794ef1ade76.png">

```python 'ignore
string = "From TEO"
```

<img width="631" alt="Screen Shot 2022-12-21 at 9 15 11 PM" src="https://user-images.githubusercontent.com/114739901/209062119-cc8c969e-3f3e-4ec1-94f7-ca0b8b2a975c.png">
