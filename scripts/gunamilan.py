"""Guna Milan (Ashtakoota) — Saurabh x Kalpana. Swiss Ephemeris, Lahiri sidereal."""
import swisseph as swe

swe.set_sid_mode(swe.SIDM_LAHIRI)
FLG = swe.FLG_MOSEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED

SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
NAKS = ["Ashwini","Bharani","Krittika","Rohini","Mrigashira","Ardra","Punarvasu","Pushya","Ashlesha","Magha","Purva Phalguni","Uttara Phalguni","Hasta","Chitra","Swati","Vishakha","Anuradha","Jyeshtha","Mula","Purva Ashadha","Uttara Ashadha","Shravana","Dhanishta","Shatabhisha","Purva Bhadrapada","Uttara Bhadrapada","Revati"]

def dms(x):
    d = int(x); m = (x-d)*60
    return f"{d}\u00b0{int(m):02d}\u2032"

def chart(y,mo,d,hh,mm,lat,lon):
    jd = swe.julday(y,mo,d,(hh+mm/60.0)-5.5)  # IST -> UT
    out = {}
    for name,pl in [("Sun",swe.SUN),("Moon",swe.MOON),("Mars",swe.MARS),("Mercury",swe.MERCURY),
                    ("Jupiter",swe.JUPITER),("Venus",swe.VENUS),("Saturn",swe.SATURN),("Rahu",swe.TRUE_NODE)]:
        lo = swe.calc_ut(jd,pl,FLG)[0][0] % 360
        out[name] = lo
    out["Ketu"] = (out["Rahu"]+180)%360
    cusps, ascmc = swe.houses_ex(jd, lat, lon, b'W', swe.FLG_SIDEREAL)
    out["Asc"] = ascmc[0]%360
    return out

def desc(lo):
    s = int(lo//30); n = int(lo//(360/27)); pada = int((lo%(360/27))//(360/108))+1
    return f"{SIGNS[s]} {dms(lo%30)} | {NAKS[n]} pada {pada}"

# ---- charts ----
saurabh = chart(2000,8,4,21,0, 25.90, 81.95)      # Pratapgarh UP
kalpana = chart(2003,9,22,6,45, 29.3211, 73.8993) # Suratgarh, Rajasthan

for nm,ch in [("SAURABH",saurabh),("KALPANA",kalpana)]:
    print(f"--- {nm} ---")
    for k in ["Asc","Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Rahu","Ketu"]:
        print(f"  {k:8s} {desc(ch[k])}")

def moon_info(ch):
    lo = ch["Moon"]; return int(lo//30), int(lo//(360/27))

b_sign, b_nak = moon_info(saurabh)   # boy
g_sign, g_nak = moon_info(kalpana)   # girl
print(f"\nBoy Moon: {SIGNS[b_sign]} / {NAKS[b_nak]} | Girl Moon: {SIGNS[g_sign]} / {NAKS[g_nak]}")

# ---- 1 VARNA ----
VARNA = {0:3,4:3,8:3, 1:2,5:2,9:2, 2:1,6:1,10:1, 3:4,7:4,11:4}  # 4 Brahmin 3 Kshatriya 2 Vaishya 1 Shudra
VNAME = {4:"Brahmin",3:"Kshatriya",2:"Vaishya",1:"Shudra"}
varna = 1.0 if VARNA[b_sign] >= VARNA[g_sign] else 0.0
print(f"1 Varna: boy {VNAME[VARNA[b_sign]]}, girl {VNAME[VARNA[g_sign]]} -> {varna}/1")

# ---- 2 VASHYA ---- groups: C=Chatushpada M=Manava J=Jalachara V=Vanachara K=Keeta
def vashya_grp(sign, lon_in_sign):
    m = {0:"C",1:"C",2:"M",3:"J",4:"V",5:"M",6:"M",7:"K",10:"M",11:"J"}
    if sign==8: return "M" if lon_in_sign<15 else "C"   # Sagittarius
    if sign==9: return "C" if lon_in_sign<15 else "J"   # Capricorn
    return m[sign]
VMAT = {  # boy -> girl
 "C":{"C":2,"M":1,"J":1,"V":0,"K":1},
 "M":{"C":1,"M":2,"J":0.5,"V":0,"K":1},
 "J":{"C":1,"M":0.5,"J":2,"V":1,"K":1},
 "V":{"C":1,"M":0,"J":1,"V":2,"K":0},
 "K":{"C":1,"M":1,"J":1,"V":0,"K":2}}
bg = vashya_grp(b_sign, saurabh["Moon"]%30); gg = vashya_grp(g_sign, kalpana["Moon"]%30)
vashya = VMAT[bg][gg]
print(f"2 Vashya: boy {bg}, girl {gg} -> {vashya}/2")

# ---- 3 TARA ----
def tara_ok(frm,to):
    cnt = ((to-frm)%27)+1; r = cnt%9
    return r not in (3,5,7,0) or r==0 and cnt%9==0  # remainder 0 => 9th (Ati-Mitra, good)
def tara_good(frm,to):
    r = (((to-frm)%27)+1)%9
    if r==0: r=9
    return r not in (3,5,7)
t1 = tara_good(g_nak,b_nak); t2 = tara_good(b_nak,g_nak)
tara = (1.5 if t1 else 0)+(1.5 if t2 else 0)
print(f"3 Tara: girl->boy good={t1}, boy->girl good={t2} -> {tara}/3")

# ---- 4 YONI ----
YONI_OF = ["Horse","Elephant","Sheep","Serpent","Serpent","Dog","Cat","Sheep","Cat","Rat","Rat","Cow","Buffalo","Tiger","Buffalo","Tiger","Deer","Deer","Dog","Monkey","Mongoose","Monkey","Lion","Horse","Lion","Cow","Elephant"]
YORD = ["Horse","Elephant","Sheep","Serpent","Dog","Cat","Rat","Cow","Buffalo","Tiger","Deer","Monkey","Mongoose","Lion"]
YM = [
 [4,2,2,3,2,2,2,1,0,1,3,3,2,1],
 [2,4,3,3,2,2,2,2,3,1,2,3,2,0],
 [2,3,4,2,1,2,1,3,3,1,2,0,3,1],
 [3,3,2,4,2,1,1,1,1,2,2,2,0,2],
 [2,2,1,2,4,2,1,2,2,1,0,2,1,1],
 [2,2,2,1,2,4,0,2,2,1,3,3,2,1],
 [2,2,1,1,1,0,4,2,2,2,2,2,1,2],
 [1,2,3,1,2,2,2,4,3,0,3,2,2,1],
 [0,3,3,1,2,2,2,3,4,1,2,2,2,1],
 [1,1,1,2,1,1,2,0,1,4,1,1,2,1],
 [3,2,2,2,0,3,2,3,2,1,4,2,2,1],
 [3,3,0,2,2,3,2,2,2,1,2,4,3,2],
 [2,2,3,0,1,2,1,2,2,2,2,3,4,2],
 [1,0,1,2,1,1,2,1,1,1,1,2,2,4]]
by, gy = YONI_OF[b_nak], YONI_OF[g_nak]
yoni = YM[YORD.index(by)][YORD.index(gy)]
print(f"4 Yoni: boy {by}, girl {gy} -> {yoni}/4")

# ---- 5 GRAHA MAITRI ----
LORD = {0:"Mars",1:"Venus",2:"Mercury",3:"Moon",4:"Sun",5:"Mercury",6:"Venus",7:"Mars",8:"Jupiter",9:"Saturn",10:"Saturn",11:"Jupiter"}
FR = {"Sun":{"f":{"Moon","Mars","Jupiter"},"e":{"Venus","Saturn"}},
      "Moon":{"f":{"Sun","Mercury"},"e":set()},
      "Mars":{"f":{"Sun","Moon","Jupiter"},"e":{"Mercury"}},
      "Mercury":{"f":{"Sun","Venus"},"e":{"Moon"}},
      "Jupiter":{"f":{"Sun","Moon","Mars"},"e":{"Mercury","Venus"}},
      "Venus":{"f":{"Mercury","Saturn"},"e":{"Sun","Moon"}},
      "Saturn":{"f":{"Mercury","Venus"},"e":{"Sun","Moon","Mars"}}}
def rel(a,b):
    if a==b: return "f"
    if b in FR[a]["f"]: return "f"
    if b in FR[a]["e"]: return "e"
    return "n"
bl, gl = LORD[b_sign], LORD[g_sign]
r1, r2 = rel(bl,gl), rel(gl,bl)
pair = tuple(sorted([r1,r2]))
GM = {("f","f"):5,("f","n"):4,("n","n"):3,("e","f"):1,("e","n"):0.5,("e","e"):0}
maitri = GM[pair]
print(f"5 Graha Maitri: boy lord {bl} ({r1} of girl's), girl lord {gl} ({r2} of boy's) -> {maitri}/5")

# ---- 6 GANA ----
GANA_OF = ["D","M","R","M","D","M","D","D","R","R","M","M","D","R","D","R","D","R","R","M","M","D","R","R","M","M","D"]
GNAME={"D":"Deva","M":"Manushya","R":"Rakshasa"}
GMAT = {("D","D"):6,("D","M"):6,("D","R"):0,("M","D"):5,("M","M"):6,("M","R"):0,("R","D"):1,("R","M"):0,("R","R"):6}
bgn, ggn = GANA_OF[b_nak], GANA_OF[g_nak]
gana = GMAT[(bgn,ggn)]
print(f"6 Gana: boy {GNAME[bgn]}, girl {GNAME[ggn]} -> {gana}/6")

# ---- 7 BHAKOOT ----
d1 = ((g_sign-b_sign)%12)+1; d2 = ((b_sign-g_sign)%12)+1
bad = {frozenset({2,12}),frozenset({5,9}),frozenset({6,8})}
bhakoot = 0 if frozenset({d1,d2}) in bad else 7
print(f"7 Bhakoot: {d1}/{d2} -> {bhakoot}/7")

# ---- 8 NADI ----
NADI_OF = ["A","M","T","T","M","A","A","M","T","T","M","A","A","M","T","T","M","A","A","M","T","T","M","A","A","M","T"]
NNAME={"A":"Adi","M":"Madhya","T":"Antya"}
bn, gn = NADI_OF[b_nak], NADI_OF[g_nak]
nadi = 8 if bn!=gn else 0
print(f"8 Nadi: boy {NNAME[bn]}, girl {NNAME[gn]} -> {nadi}/8")

total = varna+vashya+tara+yoni+maitri+gana+bhakoot+nadi
print(f"\nTOTAL: {total}/36")

# ---- Mangal dosha ----
def mangal(ch,label):
    asc_s = int(ch["Asc"]//30); moon_s = int(ch["Moon"]//30); mars_s = int(ch["Mars"]//30)
    ha = ((mars_s-asc_s)%12)+1; hm = ((mars_s-moon_s)%12)+1
    da = ha in (1,2,4,7,8,12); dm = hm in (1,2,4,7,8,12)
    print(f"Mangal {label}: Mars {ha}H from Asc (dosha={da}), {hm}H from Moon (dosha={dm})")
    return da,dm
mangal(saurabh,"SAURABH"); mangal(kalpana,"KALPANA")
