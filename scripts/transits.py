"""Transits Aug 2026 -> Mar 2028 + name numerology for Kaira/Kalpana Soni."""
import swisseph as swe
from datetime import date, timedelta

swe.set_sid_mode(swe.SIDM_LAHIRI)
FLG = swe.FLG_MOSEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
SIGNS = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]

def pos(d, pl):
    jd = swe.julday(d.year, d.month, d.day, 6.5)
    return swe.calc_ut(jd, pl, FLG)[0][0] % 360

# sign ingress tracking for Jupiter & Saturn
for name, pl in [("Jupiter", swe.JUPITER), ("Saturn", swe.SATURN)]:
    d = date(2026, 8, 17); prev = int(pos(d, pl) // 30)
    print(f"{name} on 17 Aug 2026: {SIGNS[prev]} {pos(d,pl)%30:.1f} deg")
    while d <= date(2028, 6, 30):
        d += timedelta(days=1)
        s = int(pos(d, pl) // 30)
        if s != prev:
            print(f"  {name} -> {SIGNS[s]} on {d.strftime('%d %b %Y')}")
            prev = s

# Jupiter crossing Kalpana's natal Moon (Cancer 12deg08 = 102.14) and Saurabh's natal Moon (Virgo 19.85 = 169.85)
targets = [("her natal Moon (Cancer 12.14)", 102.14), ("his 5H stellium Sun (Cancer 18.68)", 108.68)]
d = date(2026, 8, 17); prevlo = pos(d, swe.JUPITER)
hits = {t[0]: [] for t in targets}
while d <= date(2028, 6, 30):
    d += timedelta(days=1)
    lo = pos(d, swe.JUPITER)
    for label, tg in targets:
        a, b = sorted([prevlo, lo])
        if b - a < 20 and a <= tg <= b:
            hits[label].append(d.strftime("%d %b %Y"))
    prevlo = lo
for k, v in hits.items():
    print("Jupiter crosses", k, "->", v)

# Numerology (Pythagorean)
def pyth(s):
    vals = {c: (i % 9) + 1 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    t = sum(vals[c] for c in s.upper() if c.isalpha())
    return t

def reduce(n):
    while n > 9 and n not in (11, 22, 33):
        n = sum(int(x) for x in str(n))
    return n

for nm in ["KAIRA", "SONI", "KALPANA"]:
    t = pyth(nm); print(nm, "=", t, "->", reduce(t))
print("KALPANA SONI =", pyth("KALPANASONI"), "->", reduce(pyth("KALPANASONI")))
print("KAIRA SONI =", pyth("KAIRASONI"), "->", reduce(pyth("KAIRASONI")))
print("Her Moolank (22) ->", reduce(22), "| Bhagyank 22-09-2003 ->", reduce(2+2+0+9+2+0+0+3))
