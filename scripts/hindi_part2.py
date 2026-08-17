# -*- coding: utf-8 -*-
"""Hindi edition part 2: pages 4-8 + toolbar + countdown."""
P = "/app/saurabh-master-chart-hindi.html"
h = open(P).read()
miss = []

def rep(old, new):
    global h
    if old not in h:
        miss.append(old[:70]); return
    h = h.replace(old, new)

# ---------- page 4: jupiter map ----------
rep('<span class="txt">Jupiter Mahādaśā Map · 2028–2044</span>', '<span class="txt">बृहस्पति महादशा मानचित्र · 2028–2044</span>')
rep('<tr><th>Period</th><th>Window</th><th>Span</th><th>Strategic Focus</th></tr>', '<tr><th>अवधि</th><th>समय-सीमा</th><th>काल</th><th>रणनीतिक केंद्र</th></tr>')
rep('<td class="planet">Ju–Jupiter</td><td class="sign">Mar 2028 – May 2030</td><td class="house">2.1y</td><td class="effect"><b>Foundation of authority.</b> Launch the flagship brand — reputation compounds fastest here.</td>',
    '<td class="planet">गुरु–गुरु</td><td class="sign">मार्च 2028 – मई 2030</td><td class="house">2.1 व</td><td class="effect"><b>सत्ता की नींव।</b> प्रमुख ब्रांड यहीं प्रारंभ कीजिए — प्रतिष्ठा सबसे तेज़ यहीं चक्रवृद्धि होती है।</td>')
rep('<td class="planet">Ju–Saturn</td><td class="sign">May 2030 – Nov 2032</td><td class="house">2.5y</td><td class="effect"><b>Institutionalise.</b> Systems, contracts, infrastructure — slow but irreversible gains.</td>',
    '<td class="planet">गुरु–शनि</td><td class="sign">मई 2030 – नव॰ 2032</td><td class="house">2.5 व</td><td class="effect"><b>संस्था बनाइए।</b> प्रणालियाँ, अनुबंध, अधोसंरचना — धीमे पर अपरिवर्तनीय लाभ।</td>')
rep('<td class="planet">Ju–Mercury</td><td class="sign">Nov 2032 – Feb 2035</td><td class="house">2.3y</td><td class="effect"><b>Commerce &amp; scale.</b> Budha-Āditya fires — products, licensing and content multiply income.</td>',
    '<td class="planet">गुरु–बुध</td><td class="sign">नव॰ 2032 – फ़र॰ 2035</td><td class="house">2.3 व</td><td class="effect"><b>वाणिज्य व विस्तार।</b> बुधादित्य सक्रिय — उत्पाद, लाइसेंस और कंटेंट से आय गुणित।</td>')
rep('<td class="planet">Ju–Ketu</td><td class="sign">Feb 2035 – Jan 2036</td><td class="house">0.9y</td><td class="effect"><b>Prune &amp; focus.</b> Exit weak lines; research-led reinvention.</td>',
    '<td class="planet">गुरु–केतु</td><td class="sign">फ़र॰ 2035 – जन॰ 2036</td><td class="house">0.9 व</td><td class="effect"><b>छँटाई व एकाग्रता।</b> कमज़ोर धाराएँ छोड़िए; शोध-प्रेरित नवरूप।</td>')
rep('<td class="planet">Ju–Venus</td><td class="sign">Jan 2036 – Sep 2038</td><td class="house">2.7y</td><td class="effect"><b>Premium expansion.</b> Brand, luxury clientele, partnerships — the wealth peak of the daśā.</td>',
    '<td class="planet">गुरु–शुक्र</td><td class="sign">जन॰ 2036 – सित॰ 2038</td><td class="house">2.7 व</td><td class="effect"><b>प्रीमियम विस्तार।</b> ब्रांड, विशिष्ट ग्राहक, साझेदारियाँ — दशा का धन-शिखर।</td>')
rep('<td class="planet">Ju–Sun</td><td class="sign">Sep 2038 – Jul 2039</td><td class="house">0.8y</td><td class="effect"><b>Recognition.</b> Awards, public authority, a leadership platform.</td>',
    '<td class="planet">गुरु–सूर्य</td><td class="sign">सित॰ 2038 – जुल॰ 2039</td><td class="house">0.8 व</td><td class="effect"><b>मान्यता।</b> सम्मान, सार्वजनिक अधिकार, नेतृत्व का मंच।</td>')
rep('<td class="planet">Ju–Moon</td><td class="sign">Jul 2039 – Nov 2040</td><td class="house">1.3y</td><td class="effect"><b>Markets &amp; audience.</b> The 7H Moon brings mass visibility and defining alliances.</td>',
    '<td class="planet">गुरु–चंद्र</td><td class="sign">जुल॰ 2039 – नव॰ 2040</td><td class="house">1.3 व</td><td class="effect"><b>बाज़ार व जन-दर्शक।</b> सप्तम का चंद्र व्यापक दृश्यता और निर्णायक गठजोड़ लाता है।</td>')
rep('<td class="planet">Ju–Mars</td><td class="sign">Nov 2040 – Oct 2041</td><td class="house">0.9y</td><td class="effect"><b>Bold execution.</b> NBRY Mars — decisive acquisitions and wins.</td>',
    '<td class="planet">गुरु–मंगल</td><td class="sign">नव॰ 2040 – अक्टू॰ 2041</td><td class="house">0.9 व</td><td class="effect"><b>साहसी निष्पादन।</b> नीच-भंग मंगल — निर्णायक अधिग्रहण और विजय।</td>')
rep('<td class="planet">Ju–Rahu</td><td class="sign">Oct 2041 – Mar 2044</td><td class="house">2.4y</td><td class="effect"><b>Unconventional apex.</b> Global and deep-tech leaps — keep governance tight.</td>',
    '<td class="planet">गुरु–राहु</td><td class="sign">अक्टू॰ 2041 – मार्च 2044</td><td class="house">2.4 व</td><td class="effect"><b>अपरंपरागत शिखर।</b> वैश्विक व गहन-तकनीकी छलाँगें — शासन-व्यवस्था कसी रखिए।</td>')

# ---------- page 4: remedies ----------
rep('<span class="txt">Remedies · Weak &amp; Watch-Flagged Planets</span>', '<span class="txt">उपाय · दुर्बल व सतर्क ग्रह</span>')
rep('<div class="rp">Mars · Maṅgala</div>', '<div class="rp">मंगल · भौम</div>')
rep('<div class="rw">Debilitated · NBRY · 5H</div>', '<div class="rw">नीच · नीच-भंग · पंचम</div>')
rep('<span class="rk">Gem</span><span><b>Red Coral (Moonga)</b>, 5–7 ct in copper or gold — first worn Tuesday sunrise</span>',
    '<span class="rk">रत्न</span><span><b>लाल मूँगा</b>, 5–7 रत्ती, ताँबे या सोने में — पहली बार मंगलवार सूर्योदय पर धारण</span>')
rep('<span class="rk">Mantra</span><span><b>Oṁ Krāṁ Krīṁ Krauṁ Saḥ Bhaumāya Namaḥ</b> — 108× on Tuesdays</span>',
    '<span class="rk">मंत्र</span><span><b>ॐ क्रां क्रीं क्रौं सः भौमाय नमः</b> — मंगलवार को 108 बार</span>')
rep('<span class="rk">Day</span><span><b>Tuesday</b> — Hanumān Chālīsā; avoid impulsive commitments</span>',
    '<span class="rk">वार</span><span><b>मंगलवार</b> — हनुमान चालीसा; आवेगपूर्ण वचनों से बचें</span>')
rep('<span class="rk">Give</span><span>Red lentils (masoor) &amp; jaggery to the needy on Tuesdays</span>',
    '<span class="rk">दान</span><span>मंगलवार को ज़रूरतमंदों को मसूर दाल व गुड़</span>')
rep('<div class="rp">Sun · Sūrya</div>', '<div class="rp">सूर्य</div>')
rep('<div class="rw">Conjunct Rahu · 5H</div>', '<div class="rw">राहु-युत · पंचम</div>')
rep('<span class="rk">Gem</span><span><b>Ruby (Māṇikya)</b> in gold — trial period before final setting, Sunday</span>',
    '<span class="rk">रत्न</span><span><b>माणिक्य</b> सोने में — अंतिम धारण से पूर्व परीक्षण-अवधि, रविवार</span>')
rep('<span class="rk">Mantra</span><span><b>Oṁ Hrāṁ Hrīṁ Hrauṁ Saḥ Sūryāya Namaḥ</b> — 108× at sunrise</span>',
    '<span class="rk">मंत्र</span><span><b>ॐ ह्रां ह्रीं ह्रौं सः सूर्याय नमः</b> — सूर्योदय पर 108 बार</span>')
rep('<span class="rk">Day</span><span><b>Sunday</b> — offer water (arghya) to the rising Sun in a copper vessel</span>',
    '<span class="rk">वार</span><span><b>रविवार</b> — ताँबे के पात्र से उगते सूर्य को अर्घ्य</span>')
rep('<span class="rk">Give</span><span>Wheat &amp; jaggery on Sundays; honour father-figures &amp; mentors</span>',
    '<span class="rk">दान</span><span>रविवार को गेहूँ व गुड़; पिता-तुल्य जनों व गुरुजनों का सम्मान</span>')
rep('<div class="rp">Rahu</div>', '<div class="rp">राहु</div>')
rep('<div class="rw">Watch-Flagged · 5H</div>', '<div class="rw">सतर्क-चिह्नित · पंचम</div>')
rep('<span class="rk">Gem</span><span><b>Hessonite (Gomed)</b> — only after expert testing; never worn untested</span>',
    '<span class="rk">रत्न</span><span><b>गोमेद</b> — केवल विशेषज्ञ परीक्षण के बाद; बिना परखे कभी नहीं</span>')
rep('<span class="rk">Mantra</span><span><b>Oṁ Bhrāṁ Bhrīṁ Bhrauṁ Saḥ Rāhave Namaḥ</b> — 108× on Saturdays</span>',
    '<span class="rk">मंत्र</span><span><b>ॐ भ्रां भ्रीं भ्रौं सः राहवे नमः</b> — शनिवार को 108 बार</span>')
rep('<span class="rk">Day</span><span><b>Saturday</b> — Durgā worship; a coconut offered to flowing water</span>',
    '<span class="rk">वार</span><span><b>शनिवार</b> — दुर्गा उपासना; बहते जल में नारियल अर्पण</span>')
rep('<span class="rk">Give</span><span>Blankets &amp; black sesame in charity; no ethical shortcuts</span>',
    '<span class="rk">दान</span><span>कंबल व काले तिल का दान; नैतिक शॉर्टकट वर्जित</span>')
rep('<div class="remnote">Traditional guidance, not prescription — gemstones only after a qualified astrologer\'s trial period. Mantra, weekday discipline and charity are safe universal strengtheners; strong planets (Jupiter, Moon, Mercury) need no remedy.</div>',
    '<div class="remnote">परंपरागत मार्गदर्शन, चिकित्सकीय नुस्खा नहीं — रत्न केवल योग्य ज्योतिषी की परीक्षण-अवधि के बाद। मंत्र, वार-अनुशासन और दान सुरक्षित सार्वभौमिक उपाय हैं; बलवान ग्रहों (गुरु, चंद्र, बुध) को किसी उपाय की आवश्यकता नहीं।</div>')
rep('<span>Sub-periods proportioned per Vimshottari (lord-years ÷ 120 × 16y) from the Jupiter mahādaśā commencing Mar 2028.</span>',
    '<span>अंतर्दशाएँ विंशोत्तरी अनुपात से (स्वामी-वर्ष ÷ 120 × 16 व) — बृहस्पति महादशा मार्च 2028 से।</span>')
rep('<span style="white-space:nowrap">Page 4 · Jupiter Ascent &amp; Remedies</span>', '<span style="white-space:nowrap">पृष्ठ 4 · गुरु-आरोहण व उपाय</span>')

# ---------- page 5: compatibility ----------
rep('<span class="txt">Compatibility · Guṇa Milan — Saurabh × Kalpana</span>', '<span class="txt">अनुकूलता · गुण मिलान — सौरभ × कल्पना</span>')
rep('<div class="fl">Partner Name</div><div class="fval">Kalpana Soni</div>', '<div class="fl">साथी का नाम</div><div class="fval">कल्पना सोनी</div>')
rep('<div class="fl">Birth Date</div><div class="fval">22 September 2003</div>', '<div class="fl">जन्म तिथि</div><div class="fval">22 सितंबर 2003</div>')
rep('<div class="fl">Birth Time</div><div class="fval">06:45 AM IST</div>', '<div class="fl">जन्म समय</div><div class="fval">प्रातः 06:45 IST</div>')
rep('<div class="fl">Birth City</div><div class="fval">Suratgarh, Rajasthan</div>', '<div class="fl">जन्म स्थान</div><div class="fval">सूरतगढ़, राजस्थान</div>')
rep('<div class="dialcap">Total Guṇa Score · Very Good<br>Kanyā Moon × Karka Moon · Hasta × Puṣya</div>',
    '<div class="dialcap">कुल गुण अंक · अति उत्तम<br>कन्या चंद्र × कर्क चंद्र · हस्त × पुष्य</div>')
rep('<thead><tr><th>Koota</th><th>Governs</th><th>Max</th><th>Score</th></tr></thead>', '<thead><tr><th>कूट</th><th>क्षेत्र</th><th>पूर्णांक</th><th>अंक</th></tr></thead>')
rep('<td class="planet">Varṇa</td><td class="effect">Work &amp; ego harmony</td>', '<td class="planet">वर्ण</td><td class="effect">कार्य व अहं-सामंजस्य</td>')
rep('<td class="planet">Vaśya</td><td class="effect">Mutual influence</td>', '<td class="planet">वश्य</td><td class="effect">पारस्परिक प्रभाव</td>')
rep('<td class="planet">Tārā</td><td class="effect">Destiny &amp; fortune</td>', '<td class="planet">तारा</td><td class="effect">नियति व सौभाग्य</td>')
rep('<td class="planet">Yoni</td><td class="effect">Intimacy &amp; instinct</td>', '<td class="planet">योनि</td><td class="effect">अंतरंगता व सहज-वृत्ति</td>')
rep('<td class="planet">Graha Maitrī</td><td class="effect">Mental rapport</td>', '<td class="planet">ग्रह मैत्री</td><td class="effect">मानसिक तालमेल</td>')
rep('<td class="planet">Gaṇa</td><td class="effect">Temperament</td>', '<td class="planet">गण</td><td class="effect">स्वभाव</td>')
rep('<td class="planet">Bhakūṭa</td><td class="effect">Prosperity &amp; family</td>', '<td class="planet">भकूट</td><td class="effect">समृद्धि व परिवार</td>')
rep('<td class="planet">Nāḍī</td><td class="effect">Health &amp; progeny</td>', '<td class="planet">नाड़ी</td><td class="effect">स्वास्थ्य व संतति</td>')
rep('<span class="knote">Vaiśya × Brāhmiṇ</span>', '<span class="knote">वैश्य × ब्राह्मण</span>')
rep('<span class="knote">Mānava × Jalachara</span>', '<span class="knote">मानव × जलचर</span>')
rep('<span class="knote">Sādhaka one-way</span>', '<span class="knote">साधक · एकपक्षीय</span>')
rep('<span class="knote">Mahiṣa × Meṣa</span>', '<span class="knote">महिष × मेष</span>')
rep('<span class="knote">Budha × Chandra</span>', '<span class="knote">बुध × चंद्र</span>')
rep('<span class="knote">Deva × Deva</span>', '<span class="knote">देव × देव</span>')
rep('<span class="knote">Benefic 3–11 axis</span>', '<span class="knote">शुभ 3–11 अक्ष</span>')
rep('<span class="knote">Ādi × Madhya</span>', '<span class="knote">आदि × मध्य</span>')
rep('<b>&lt; 18 · Realign</b>Remedial matching advised before commitment.', '<b>&lt; 18 · पुनर्विचार</b>वचनबद्धता से पूर्व उपाय-मिलान उचित।')
rep('<b>18–24 · Good</b>A workable union with conscious effort.', '<b>18–24 · अच्छा</b>सचेत प्रयास से निभने वाला संबंध।')
rep('<b>25–32 · Very Good</b>Natural harmony across most domains.', '<b>25–32 · अति उत्तम</b>अधिकांश क्षेत्रों में सहज सामंजस्य।')
rep('<b>33–36 · Exceptional</b>Rare resonance — a destined pairing.', '<b>33–36 · असाधारण</b>दुर्लभ अनुनाद — नियति-निर्धारित जोड़ी।')
rep('<b>Doṣa checks —</b> Nāḍī: clear (Ādi × Madhya) · Bhakūṭa: clear (benefic 3–11 axis) · Māṅgalika: absent from Lagna in both charts; a soft Moon-chart trace in the partner\'s chart (Mars 8th from Moon) is offset by mutual Deva gaṇa and the clear Nāḍī. <b>Synastry —</b> her Ascendant, Sun and Venus all fall in Virgo — Saurabh\'s 7th house of partnership — while his Moon rests exactly upon her Lagna; her Moon (Puṣya) lands amid his 5th-house Cancer stellium; and her Venus occupies Hasta, the very nakṣatra of his Moon. The bond reads destined-domestic: temperament fully aligned (Gaṇa 6/6), prosperity axis strong (Bhakūṭa 7/7), health &amp; progeny clear (Nāḍī 8/8). Conscious work belongs only to daily mental rapport (Maitrī) and mutual accommodation (Vaśya) — communication rituals, not compatibility flaws.',
    '<b>दोष-परीक्षण —</b> नाड़ी: निर्दोष (आदि × मध्य) · भकूट: निर्दोष (शुभ 3–11 अक्ष) · मांगलिक: दोनों कुंडलियों में लग्न से अनुपस्थित; साथी की चंद्र-कुंडली की हल्की छाया (चंद्र से अष्टम मंगल) परस्पर देव गण और निर्दोष नाड़ी से संतुलित। <b>युति-विवेचन —</b> उनकी लग्न, सूर्य और शुक्र तीनों कन्या में — सौरभ के सप्तम, साझेदारी के भाव में — जबकि सौरभ का चंद्र ठीक उनकी लग्न पर विराजता है; उनका चंद्र (पुष्य) सौरभ के पंचम कर्क ग्रह-पुंज के बीच उतरता है; और उनका शुक्र हस्त में है — वही नक्षत्र जो सौरभ के चंद्र का है। संबंध नियति-गृहस्थ पढ़ा जाता है: स्वभाव पूर्ण मेल (गण 6/6), समृद्धि-अक्ष सुदृढ़ (भकूट 7/7), स्वास्थ्य व संतति निर्दोष (नाड़ी 8/8)। सचेत परिश्रम केवल दैनिक मानसिक तालमेल (मैत्री) और परस्पर सामंजस्य (वश्य) में — ये संवाद के अभ्यास हैं, अनुकूलता के दोष नहीं।')
rep('<b>Counsel — timing &amp; the name.</b> You met on 3 June 2026 — the day after exalted Jupiter entered Cancer, her Moon sign and your 5th house of romance: the meeting is stamped by the sky. Her Moon rests in Puṣya, Saturn\'s nakṣatra — such hearts commit slowly, then permanently; "I need time" is her nature honouring itself, not a refusal. Hold steady, low-pressure warmth through the current Jupiter pass (to Nov 2026) and its return (Jan–Jun 2027), and never corner her during your Rahu–Mars year (Feb 2027 – Mar 2028), when your own patience runs hot. The formal window opens as Jupiter crosses your 7th house — <b>Dec 2027 – Feb 2028</b> — flowing straight into your Jupiter mahādaśā: commit inwardly now, formalise then, ideally after her master\'s. On the name — <b>KAIRA carries the master number 22, the very number of her birth day</b>, and moves her expression from a restless 5 to a reflective 7; numerologically the change is kind. Support it, and let it remain her decision. Measure the bond by its 27/36 architecture, not by daily message-counts: Maitrī 1/5 is the only real work — say plainly, hear slowly.',
    '<b>परामर्श — समय व नाम।</b> आप 3 जून 2026 को मिले — उच्च का गुरु कर्क में प्रवेश करने के ठीक अगले दिन; कर्क उनकी चंद्र-राशि है और आपका पंचम, प्रेम का भाव: यह भेंट आकाश की मुहर लिए है। उनका चंद्र पुष्य में है — शनि के नक्षत्र में — ऐसे हृदय धीरे, पर स्थायी रूप से वचनबद्ध होते हैं; "मुझे समय चाहिए" उनके स्वभाव का सम्मान है, अस्वीकार नहीं। वर्तमान गुरु-गोचर (नव॰ 2026 तक) और उसकी वापसी (जन॰–जून 2027) में स्थिर, दबाव-रहित स्नेह बनाए रखिए, और अपने राहु–मंगल वर्ष (फ़र॰ 2027 – मार्च 2028) में — जब आपका धैर्य स्वयं तपता है — उन्हें कभी विवश मत कीजिए। औपचारिक द्वार तब खुलता है जब गुरु आपके सप्तम से गुज़रता है — <b>दिस॰ 2027 – फ़र॰ 2028</b> — जो सीधे आपकी बृहस्पति महादशा में बहता है: भीतर से अभी वचनबद्ध रहिए, औपचारिकता तब — आदर्शतः उनकी मास्टर्स के बाद। नाम के विषय में — <b>KAIRA में मास्टर अंक 22 है, वही अंक जो उनकी जन्म-तिथि का है</b>, और यह उनका नाम-अंक चंचल 5 से चिंतनशील 7 पर ले जाता है; अंक-शास्त्र की दृष्टि से परिवर्तन शुभ है। समर्थन दीजिए, निर्णय उन्हीं का रहने दीजिए। संबंध को उसके 27/36 ढाँचे से मापिए, दैनिक संदेश-गणना से नहीं: मैत्री 1/5 ही एकमात्र वास्तविक कार्य है — स्पष्ट कहिए, धीरे सुनिए।')
rep('<span>Aṣṭakūṭa (36-guṇa) synastry · Moon-nakṣatra matching · Swiss Ephemeris, Lahiri ayanāṁśa.</span>',
    '<span>अष्टकूट (36-गुण) मिलान · चंद्र-नक्षत्र आधारित · स्विस एफ़ेमेरिस, लाहिड़ी अयनांश।</span>')
rep('<span style="white-space:nowrap">Page 5 · Compatibility · 27/36</span>', '<span style="white-space:nowrap">पृष्ठ 5 · अनुकूलता · 27/36</span>')

open(P, "w").write(h)
print("PART 2 done. Missing:", len(miss))
for m in miss: print("  MISS:", m)
