"""Muhurta finder for Saurabh (natal Moon Virgo / Hasta) — scan Sep 2026 -> Mar 2028.
Filters: weekday Mon/Wed/Thu · Chandra bala (no 4/8/12 from Virgo: Sag/Aries/Leo) ·
Tarabala from Hasta (good taras 2,4,6,8,9) · Shukla tithis {2,3,5,7,10,11,13} ·
nakshatra sets for Launch vs Signing. Also: Guru-Pushya detection + Mercury retro windows."""
import swisseph as swe
from datetime import date, timedelta

swe.set_sid_mode(swe.SIDM_LAHIRI)
FLG = swe.FLG_MOSEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED

NAKS = ["Ashwini","Bharani","Krittika","Rohini","Mrigashira","Ardra","Punarvasu","Pushya","Ashlesha","Magha","Purva Phalguni","Uttara Phalguni","Hasta","Chitra","Swati","Vishakha","Anuradha","Jyeshtha","Mula","Purva Ashadha","Uttara Ashadha","Shravana","Dhanishta","Shatabhisha","Purva Bhadrapada","Uttara Bhadrapada","Revati"]
SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
TITHI_N = {1:"Pratipadā",2:"Dvitīyā",3:"Tṛtīyā",5:"Pañchamī",7:"Saptamī",10:"Daśamī",11:"Ekādaśī",13:"Trayodaśī"}

HASTA = 12  # 0-based natal nakshatra
BAD_MOON_SIGNS = {8, 0, 4}  # Sagittarius(4th from Virgo), Aries(8th), Leo(12th)
GOOD_TARAS = {2,4,6,8,0}    # remainder mod 9 (0 == 9 Param Mitra)
LAUNCH_NAKS = {"Ashwini","Mrigashira","Pushya","Hasta","Chitra","Swati","Shravana","Dhanishta","Revati"}
SIGN_NAKS   = {"Rohini","Uttara Phalguni","Uttara Ashadha","Uttara Bhadrapada","Anuradha","Pushya"}
DAYS = {0:"Monday",2:"Wednesday",3:"Thursday"}

def calc(jd, pl):
    return swe.calc_ut(jd, pl, FLG)[0]

launch, signing, golden = [], [], []
d = date(2026, 9, 1)
end = date(2028, 3, 31)
while d <= end:
    jd = swe.julday(d.year, d.month, d.day, 9.0 - 5.5)  # 09:00 IST
    wd = d.weekday()
    mo = calc(jd, swe.MOON)[0] % 360
    su = calc(jd, swe.SUN)[0] % 360
    nak = int(mo // (360/27)); sign = int(mo // 30)
    tithi = int(((mo - su) % 360) // 12) + 1  # 1..30
    nakname = NAKS[nak]
    # Guru-Pushya: Thursday + Pushya (report regardless of tithi, still respect chandra bala)
    if wd == 3 and nakname == "Pushya" and sign not in BAD_MOON_SIGNS:
        golden.append((d, tithi))
    if wd not in DAYS: d += timedelta(days=1); continue
    if sign in BAD_MOON_SIGNS: d += timedelta(days=1); continue
    tara = ((nak - HASTA) % 27 + 1) % 9
    if tara not in GOOD_TARAS: d += timedelta(days=1); continue
    if not (1 <= tithi <= 15 and tithi in TITHI_N): d += timedelta(days=1); continue
    rec = (d, DAYS[wd], nakname, TITHI_N[tithi], SIGNS[sign])
    if nakname in LAUNCH_NAKS: launch.append(rec)
    if nakname in SIGN_NAKS: signing.append(rec)
    d += timedelta(days=1)

print(f"LAUNCH candidates: {len(launch)}")
for r in launch: print("  ", r[0].strftime("%d %b %Y"), r[1][:3], "·", r[2], "·", r[3], "· Moon", r[4])
print(f"\nSIGNING candidates: {len(signing)}")
for r in signing: print("  ", r[0].strftime("%d %b %Y"), r[1][:3], "·", r[2], "·", r[3], "· Moon", r[4])
print("\nGURU-PUSHYA (Thu+Pushya):", [(g[0].strftime("%d %b %Y"), "tithi %d"%g[1]) for g in golden])

# Mercury retrograde windows
print("\nMERCURY RETROGRADE:")
d = date(2026, 9, 1); prev = calc(swe.julday(2026,8,31,3.5), swe.MERCURY)[3] < 0
start = None
while d <= date(2028, 3, 31):
    jd = swe.julday(d.year, d.month, d.day, 3.5)
    retro = calc(jd, swe.MERCURY)[3] < 0
    if retro and not prev: start = d
    if not retro and prev and start: print("  ", start.strftime("%d %b %Y"), "->", (d-timedelta(days=1)).strftime("%d %b %Y")); start=None
    prev = retro
    d += timedelta(days=1)
if start: print("  ", start.strftime("%d %b %Y"), "-> ongoing")
