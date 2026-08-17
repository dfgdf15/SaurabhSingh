# -*- coding: utf-8 -*-
"""Hindi edition part 1: head + pages 1-3."""
import sys

P = "/app/saurabh-master-chart-hindi.html"
h = open(P).read()
miss = []

def rep(old, new, cnt=None):
    global h
    c = h.count(old)
    if c == 0:
        miss.append(old[:70]); return
    h = h.replace(old, new)

# ---------- head ----------
rep('<html lang="en">', '<html lang="hi">')
rep('<title>SAURABH — Master Astrological Chart</title>', '<title>सौरभ — मास्टर ज्योतिष कुंडली</title>')
rep("@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');",
    "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;600;700;800;900&display=swap');")
rep("font-family:'Inter',system-ui", "font-family:'Inter','Noto Sans Devanagari',system-ui")
rep("font-family: 'Inter', system-ui", "font-family:'Inter','Noto Sans Devanagari',system-ui")

# ---------- hero ----------
rep('Confidential · Natal Intelligence Dossier', 'गोपनीय · जन्म-कुंडली विवेचन दस्तावेज़ · हिंदी संस्करण')
rep('<h1>SAURABH</h1>', '<h1>सौरभ</h1>')
rep('Master Astrological Chart &amp; Planetary Architecture', 'मास्टर ज्योतिष कुंडली एवं ग्रह संरचना')
rep('<span class="k">Sun</span><span class="v">Cancer / 5H</span>', '<span class="k">सूर्य</span><span class="v">कर्क · पंचम भाव</span>')
rep('<span class="k">Moon</span><span class="v">Virgo / 7H</span>', '<span class="k">चंद्र</span><span class="v">कन्या · सप्तम भाव</span>')
rep('<span class="k">Ascendant</span><span class="v">Pisces 3°18′</span>', '<span class="k">लग्न</span><span class="v">मीन 3°18′</span>')
rep('<span class="k">Dominant Energy</span><span class="v">5H Innovation Stellium</span>', '<span class="k">प्रमुख ऊर्जा</span><span class="v">पंचम-भाव सृजन ग्रह-पुंज</span>')

# ---------- planetary table ----------
rep('<span class="txt">Planetary Positions</span>', '<span class="txt">ग्रह स्थिति</span>')
rep('<tr><th>Planet</th><th>Sign</th><th>House</th><th>Dignity / State</th><th>Core Strategic Effect</th></tr>',
    '<tr><th>ग्रह</th><th>राशि</th><th>भाव</th><th>स्थिति / बल</th><th>मुख्य रणनीतिक प्रभाव</th></tr>')
rep('<span class="glyph">☉</span>Sun</td>', '<span class="glyph">☉</span>सूर्य</td>')
rep('<span class="glyph">☽</span>Moon</td>', '<span class="glyph">☽</span>चंद्र</td>')
rep('<span class="glyph">☿</span>Mercury</td>', '<span class="glyph">☿</span>बुध</td>')
rep('<span class="glyph">♀</span>Venus</td>', '<span class="glyph">♀</span>शुक्र</td>')
rep('<span class="glyph">♂</span>Mars</td>', '<span class="glyph">♂</span>मंगल</td>')
rep('<span class="glyph">♃</span>Jupiter</td>', '<span class="glyph">♃</span>बृहस्पति</td>')
rep('<span class="glyph">♄</span>Saturn</td>', '<span class="glyph">♄</span>शनि</td>')
rep('<span class="glyph">☊</span>Rahu</td>', '<span class="glyph">☊</span>राहु</td>')
rep('<span class="glyph">☋</span>Ketu</td>', '<span class="glyph">☋</span>केतु</td>')
rep('Cancer<span class="deg">', 'कर्क<span class="deg">')
rep('Virgo<span class="deg">', 'कन्या<span class="deg">')
rep('Leo<span class="deg">', 'सिंह<span class="deg">')
rep('Taurus<span class="deg">', 'वृषभ<span class="deg">')
rep('Capricorn<span class="deg">', 'मकर<span class="deg">')
rep('<td class="house">5H</td>', '<td class="house">पंचम</td>')
rep('<td class="house">7H</td>', '<td class="house">सप्तम</td>')
rep('<td class="house">6H</td>', '<td class="house">षष्ठ</td>')
rep('<td class="house">3H</td>', '<td class="house">तृतीय</td>')
rep('<td class="house">11H</td>', '<td class="house">एकादश</td>')
rep('<span class="tag blue">Radiant Core</span>', '<span class="tag blue">तेजस्वी केंद्र</span>')
rep('<span class="tag blue">Analytical Instinct</span>', '<span class="tag blue">विश्लेषक अंतर्ज्ञान</span>')
rep('<span class="tag blue">Creative Intellect</span>', '<span class="tag blue">सृजनशील बुद्धि</span>')
rep('<span class="tag blue">Bold Refinement</span>', '<span class="tag blue">साहसी परिष्कार</span>')
rep('<span class="tag">Neecha Bhanga · Raja Yoga</span>', '<span class="tag">नीच भंग · राज योग</span>')
rep('<span class="tag">Lord of 1st &amp; 10th</span>', '<span class="tag">लग्नेश एवं दशमेश</span>')
rep('<span class="tag blue">Iron Discipline</span>', '<span class="tag blue">लौह अनुशासन</span>')
rep('<span class="tag blue">Amplified Genius</span>', '<span class="tag blue">प्रवर्धित प्रतिभा</span>')
rep('<span class="tag blue">Detached Mastery</span>', '<span class="tag blue">निर्लिप्त प्रभुत्व</span>')
rep('<b>Leadership through creation.</b> Authority peaks in original work — products, ventures &amp; IP; visibility follows invention.',
    '<b>सृजन से नेतृत्व।</b> मौलिक कार्य — उत्पाद, उद्यम व बौद्धिक संपदा — में सत्ता शिखर पर; प्रतिष्ठा आविष्कार के पीछे चलती है।')
rep('<b>Emotional intelligence runs on data.</b> Reads counterparties instantly; deal-sense embedded at the gut level.',
    '<b>भावनात्मक बुद्धि आँकड़ों पर चलती है।</b> सामने वाले को क्षण में पढ़ लेते हैं; सौदे की समझ अंतर्मन में बसी है।')
rep('<b>Intuitive engineering mind.</b> Converts imagination into working systems — code, language &amp; product architecture.',
    '<b>अंतर्ज्ञानी अभियांत्रिक मन।</b> कल्पना को चालू प्रणालियों में बदलता है — कोड, भाषा व उत्पाद संरचना।')
rep('<b>Operations become brand theatre.</b> Premium taste applied to service, systems &amp; execution discipline.',
    '<b>कार्य-प्रणाली ही ब्रांड का मंच।</b> सेवा, प्रणाली और निष्पादन में प्रीमियम रुचि झलकती है।')
rep('<b>Debilitation reversed into rare power.</b> Raw drive matures into patient, strategic force — late-blooming, formidable.',
    '<b>नीचता दुर्लभ शक्ति में पलटी।</b> कच्चा जोश धैर्यपूर्ण रणनीतिक बल बनता है — देर से खिलता, पर प्रचंड।')
rep("<b>Career rises through self-built craft.</b> The chart's ruler invests in skills, content &amp; courage — a slow, compounding ascent.",
    '<b>स्व-निर्मित कौशल से करियर का उदय।</b> कुंडली का स्वामी कौशल, कंटेंट व साहस में निवेश करता है — धीमा पर चक्रवृद्धि आरोहण।')
rep('<b>The relentless craftsman.</b> Effort systematized — mastery of tools, hands &amp; code, built hour by hour.',
    '<b>अथक शिल्पकार।</b> परिश्रम को प्रणाली बनाया — औज़ार, हाथ व कोड पर घंटा-दर-घंटा अर्जित प्रभुत्व।')
rep('<b>Obsessive creative intelligence.</b> Unconventional bets in technology, speculation &amp; intellectual property.',
    '<b>जुनूनी सृजनात्मक बुद्धि।</b> तकनीक, संभावना व बौद्धिक संपदा में अपरंपरागत दाँव।')
rep('<b>Immune to crowd validation.</b> Filters networks ruthlessly — few allies, all of them consequential.',
    '<b>भीड़ की स्वीकृति से निर्लिप्त।</b> संपर्कों की कठोर छँटाई — मित्र थोड़े, पर सब निर्णायक।')

# ---------- houses ----------
rep('<span class="txt">House Architecture</span>', '<span class="txt">भाव संरचना</span>')
rep('<div class="hh">The Vessel</div>', '<div class="hh">पात्र</div>')
rep('<div class="hsign">1st House · Pisces</div>', '<div class="hsign">प्रथम भाव · मीन</div>')
rep('<p><b>Identity &amp; Vision.</b> Ascendant at Pisces 3°18′ — an intuitive strategist who perceives whole systems before others see the parts.</p>',
    '<p><b>पहचान व दृष्टि।</b> मीन लग्न 3°18′ — ऐसा अंतर्ज्ञानी रणनीतिकार जो पूरे तंत्र को तब देख लेता है जब दूसरे टुकड़े भी नहीं देख पाते।</p>')
rep('<div class="hh">The Forge</div>', '<div class="hh">शिल्पशाला</div>')
rep('<div class="hsign">3rd House · Taurus</div>', '<div class="hsign">तृतीय भाव · वृषभ</div>')
rep('<p><b>Skills &amp; Discipline.</b> A Saturn–Jupiter conjunction: patient practice fused with expansive wisdom. Craft compounds into durable mastery.</p>',
    '<p><b>कौशल व अनुशासन।</b> शनि–गुरु युति: धैर्यपूर्ण अभ्यास और विस्तृत ज्ञान का संगम। शिल्प चक्रवृद्धि से स्थायी प्रभुत्व बनता है।</p>')
rep('<div class="hh">The Powerhouse</div>', '<div class="hh">ऊर्जा-गृह</div>')
rep('<div class="hsign">5th House · Cancer</div>', '<div class="hsign">पंचम भाव · कर्क</div>')
rep("<p><b>Innovation &amp; Intellect.</b> Four planets ignite the house of creation — Sun's authority, Mercury's engineering, Mars' force, Rahu's edge.</p>",
    '<p><b>नवाचार व बुद्धि।</b> सृजन के भाव में चार ग्रह प्रज्वलित — सूर्य की सत्ता, बुध की अभियांत्रिकी, मंगल का बल, राहु की धार।</p>')
rep('<div class="hh">The Arena</div>', '<div class="hh">रणक्षेत्र</div>')
rep('<div class="hsign">7th House · Virgo</div>', '<div class="hsign">सप्तम भाव · कन्या</div>')
rep('<p><b>Partnerships &amp; Markets.</b> The analytical Moon audits every alliance — logical, organized, consequential allies only.</p>',
    '<p><b>साझेदारी व बाज़ार।</b> विश्लेषक चंद्र हर गठजोड़ की परीक्षा लेता है — केवल तार्किक, व्यवस्थित और निर्णायक सहयोगी।</p>')

# ---------- executive summary ----------
rep('<span class="txt">Executive Summary &amp; Wealth Signature</span>', '<span class="txt">कार्यकारी सार एवं धन-हस्ताक्षर</span>')
rep('<div class="lbl">Archetype</div>', '<div class="lbl">मूल स्वरूप</div>')
rep('<div class="arch">THE INTUITIVE ARCHITECT</div>', '<div class="arch">अंतर्ज्ञानी वास्तुकार</div>')
rep('<p>A Pisces-ascendant visionary carrying a <b>four-planet Cancer stellium</b> in the 5th — the house of creation. Imagination is industrialized: a Saturn–Jupiter forge builds skill in the 3rd, the analytical Moon audits alliances in the 7th, and a <span class="au">Ketu-pruned 11th</span> keeps gains structural.</p>',
    '<p>मीन लग्न का दूरदर्शी, जिसके पंचम — सृजन के भाव — में <b>चार ग्रहों का कर्क ग्रह-पुंज</b> विराजमान है। कल्पना का औद्योगीकरण: तृतीय में शनि–गुरु की शिल्पशाला कौशल गढ़ती है, सप्तम में विश्लेषक चंद्र गठजोड़ परखता है, और <span class="au">केतु से छँटा एकादश</span> लाभ को संरचनात्मक रखता है।</p>')
rep('<div class="lbl">Operational Directive</div>', '<div class="lbl">कार्य-निर्देश</div>')
rep("<p><b>Build original IP.</b> The <span class=\"pk\">5th house is the profit engine</span> — invent, code, ship. Jupiter, lord of the 1st &amp; 10th, converts self-built craft into career altitude; Mars' <span class=\"au\">Neecha Bhanga</span> turns raw drive into strategic force. Monetize creation, and let elite Capricorn networks distribute.</p>",
    '<p><b>मौलिक बौद्धिक संपदा बनाइए।</b> <span class="pk">पंचम भाव ही लाभ का इंजन है</span> — आविष्कार कीजिए, बनाइए, प्रस्तुत कीजिए। लग्नेश-दशमेश गुरु स्व-निर्मित कौशल को करियर की ऊँचाई देता है; मंगल का <span class="au">नीच भंग</span> कच्चे जोश को रणनीतिक बल बनाता है। सृजन से कमाइए, और वितरण मकर के चुनिंदा संपर्कों को सौंपिए।</p>')
rep('<span>Placements verified via Swiss Ephemeris — Sidereal · Lahiri · True Node · Whole-sign houses from Pisces 3°18′. Jupiter confirmed in Taurus · 3H (conjunct Saturn).</span>',
    '<span>ग्रह स्थितियाँ स्विस एफ़ेमेरिस से सत्यापित — नाक्षत्र (लाहिड़ी) · सत्य राहु · मीन 3°18′ से संपूर्ण-राशि भाव। गुरु वृषभ · तृतीय (शनि युत) में पुष्ट।</span>')
rep('<span style="white-space:nowrap">04.08.2000 · 21:00 IST · Pratapgarh, U.P.</span>', '<span style="white-space:nowrap">04.08.2000 · रात्रि 9:00 IST · प्रतापगढ़, उ.प्र.</span>')

# ---------- page 2 wheel + dedication ----------
rep('<span class="txt">Natal Wheel · Whole-Sign Houses</span>', '<span class="txt">जन्म-चक्र · संपूर्ण-राशि भाव</span>')
rep('letter-spacing="1" fill="#8B98A9">SUN</text>', 'letter-spacing="1" fill="#8B98A9">सूर्य</text>')
rep('letter-spacing="1" fill="#8B98A9">MOON</text>', 'letter-spacing="1" fill="#8B98A9">चंद्र</text>')
rep('letter-spacing="1" fill="#8B98A9">MERCURY</text>', 'letter-spacing="1" fill="#8B98A9">बुध</text>')
rep('letter-spacing="1" fill="#8B98A9">VENUS</text>', 'letter-spacing="1" fill="#8B98A9">शुक्र</text>')
rep('letter-spacing="1" fill="#8B98A9">MARS</text>', 'letter-spacing="1" fill="#8B98A9">मंगल</text>')
rep('letter-spacing="1" fill="#8B98A9">JUPITER</text>', 'letter-spacing="1" fill="#8B98A9">गुरु</text>')
rep('letter-spacing="1" fill="#8B98A9">SATURN</text>', 'letter-spacing="1" fill="#8B98A9">शनि</text>')
rep('letter-spacing="1" fill="#8B98A9">RAHU</text>', 'letter-spacing="1" fill="#8B98A9">राहु</text>')
rep('letter-spacing="1" fill="#8B98A9">KETU</text>', 'letter-spacing="1" fill="#8B98A9">केतु</text>')
rep('fill="#F59E0B">ASC</text>', 'fill="#F59E0B">लग्न</text>')
rep('fill="#FFFFFF" font-family="Inter, sans-serif">SAURABH</text>', 'fill="#FFFFFF" font-family="Noto Sans Devanagari, Inter, sans-serif">सौरभ</text>')
rep('fill="#3B82F6">PISCES RISING</text>', 'fill="#3B82F6">मीन लग्न</text>')
rep('fill="#8B98A9">PRATAPGARH · 25.9°N 81.9°E</text>', 'fill="#8B98A9">प्रतापगढ़ · 25.9°N 81.9°E</text>')
rep('<div class="wheelfoot">Sidereal · Lahiri Ayanāṁśa · True Node · Every planet plotted to the exact minute of arc</div>',
    '<div class="wheelfoot">नाक्षत्र · लाहिड़ी अयनांश · सत्य राहु · प्रत्येक ग्रह कला-मिनट तक अंकित</div>')
rep('<span class="txt">Dedication</span>', '<span class="txt">समर्पण</span>')
rep('<div class="lbl2">Dedication</div>', '<div class="lbl2">समर्पण</div>')
rep('<p class="dline">Prepared exclusively for <b>Saurabh</b> — engineer of systems, student of the hidden, sovereign of his own becoming. May every creation compound, every alliance be exact, and every season auspicious.</p>',
    '<p class="dline">विशेष रूप से <b>सौरभ</b> के लिए — प्रणालियों के अभियंता, गूढ़ के जिज्ञासु, अपने भविष्य के स्वयं शिल्पी। हर सृजन चक्रवृद्धि हो, हर गठजोड़ सटीक हो, और हर ऋतु शुभ हो।</p>')
rep('<div class="dmeta">Sealed · Natal Intelligence Dossier · MMXXVI</div>', '<div class="dmeta">मुद्रांकित · जन्म-कुंडली विवेचन दस्तावेज़ · २०२६</div>')
rep('<span>Wheel positions plotted from Swiss Ephemeris data — houses counted whole-sign from the Pisces ascendant.</span>',
    '<span>चक्र की स्थितियाँ स्विस एफ़ेमेरिस से अंकित — भाव मीन लग्न से संपूर्ण-राशि क्रम में।</span>')
rep('<span style="white-space:nowrap">Page 2 · Natal Wheel &amp; Dedication</span>', '<span style="white-space:nowrap">पृष्ठ 2 · जन्म-चक्र व समर्पण</span>')

# ---------- page 3 dasha ----------
rep('<span class="txt">Vimshottari Dasha Timeline</span>', '<span class="txt">विंशोत्तरी दशा समयरेखा</span>')
rep('<span class="dn">MARS</span><span class="dy">7y</span>', '<span class="dn">मंगल</span><span class="dy">7 वर्ष</span>')
rep('<span class="dn">RAHU</span><span class="dy">18y · current</span>', '<span class="dn">राहु</span><span class="dy">18 वर्ष · वर्तमान</span>')
rep('<span class="dn">JUPITER</span><span class="dy">16y · prime</span>', '<span class="dn">गुरु</span><span class="dy">16 वर्ष · स्वर्णिम</span>')
rep('<span class="dn">SATURN</span><span class="dy">19y</span>', '<span class="dn">शनि</span><span class="dy">19 वर्ष</span>')
rep('<i>NOW</i>', '<i>अभी</i>')
rep('<span>2063 → Mercury</span>', '<span>2063 → बुध</span>')
rep('>RA</div>', '>रा</div>'); rep('>JU</div>', '>गु</div>'); rep('>SA</div>', '>श</div>')
rep('>ME</div>', '>बु</div>'); rep('>KE</div>', '>के</div>'); rep('>VE</div>', '>शु</div>')
rep('>SU</div>', '>सू</div>'); rep('>MO</div>', '>चं</div>'); rep('>MA</div>', '>मं</div>')
rep('<div class="acap">Rahu mahādaśā sub-periods · Now: Rahu–Moon (Aug 2025 – Feb 2027) → Next: Rahu–Mars (Feb 2027 – Mar 2028)</div>',
    '<div class="acap">राहु महादशा की अंतर्दशाएँ · अभी: राहु–चंद्र (अग॰ 2025 – फ़र॰ 2027) → आगे: राहु–मंगल (फ़र॰ 2027 – मार्च 2028)</div>')
rep('<div class="wk">Now · Rahu–Moon → Feb 2027</div><p><b>Visibility &amp; alliance surge.</b> The 7H Moon activates partners, audiences and market instinct — negotiate, publish, be seen.</p>',
    '<div class="wk">अभी · राहु–चंद्र → फ़र॰ 2027</div><p><b>दृश्यता व गठजोड़ का ज्वार।</b> सप्तम का चंद्र साझेदार, दर्शक और बाज़ार-बोध जगाता है — वार्ता कीजिए, प्रकाशित कीजिए, दिखिए।</p>')
rep('<div class="wk">2027–28 · Rahu–Mars</div><p><b>Execution sprint.</b> NBRY Mars fires — ship aggressively and close positions before the daśā turns.</p>',
    '<div class="wk">2027–28 · राहु–मंगल</div><p><b>निष्पादन की दौड़।</b> नीच-भंग मंगल सक्रिय — आक्रामक गति से काम पूर्ण कीजिए, दशा बदलने से पहले स्थितियाँ सँभालिए।</p>')
rep('<div class="wk">2028–2044 · Jupiter Mahādaśā</div><p><b>The prime ascent.</b> Your 1st &amp; 10th lord opens a 16-year career &amp; wealth window. Build now, harvest then.</p>',
    '<div class="wk">2028–2044 · बृहस्पति महादशा</div><p><b>स्वर्णिम आरोहण।</b> लग्नेश-दशमेश 16 वर्षों का करियर व धन द्वार खोलता है। अभी निर्माण कीजिए, तब फल काटिए।</p>')

# ---------- page 3 yogas ----------
rep('<span class="txt">Yoga Panel · Strength Ratings</span>', '<span class="txt">योग पटल · बल मूल्यांकन</span>')
rep('Neecha Bhaṅga Rāja Yoga<span class="ysub">Mars · Cancer 5H</span>', 'नीच भंग राज योग<span class="ysub">मंगल · कर्क · पंचम</span>')
rep('<b>Setback engineered into strength.</b> Debilitated Mars is rescued by its dispositor Moon in a kendra — early friction matures into rare, patient power that peaks with age.',
    '<b>बाधा को बल में गढ़ा गया।</b> नीच मंगल को केंद्रस्थ राशि-स्वामी चंद्र का त्राण — आरंभिक संघर्ष आयु के साथ दुर्लभ, धैर्यवान शक्ति बनता है।')
rep('Budha-Āditya Yoga<span class="ysub">Sun + Mercury · Cancer 5H</span>', 'बुधादित्य योग<span class="ysub">सूर्य + बुध · कर्क · पंचम</span>')
rep('<b>Intellect fused with authority.</b> A clean, uncombust conjunction — administrative brilliance, sharp analysis, and a reputation built on intelligence.',
    '<b>बुद्धि और सत्ता का संगम।</b> शुद्ध, अस्त-रहित युति — प्रशासनिक प्रतिभा, तीक्ष्ण विश्लेषण और बुद्धि पर टिकी प्रतिष्ठा।')
rep('Dharma-Trikoṇa Rāja Yoga<span class="ysub">9th lord Mars in the 5th</span>', 'धर्म-त्रिकोण राज योग<span class="ysub">नवमेश मंगल पंचम में</span>')
rep("<b>Fortune through creation.</b> The luck-lord sits in the house of innovation — speculation, original work and ventures carry destiny's favour.",
    '<b>सृजन से सौभाग्य।</b> भाग्येश नवाचार के भाव में विराजमान — संभावनाएँ, मौलिक कार्य और उद्यम नियति की कृपा साथ लाते हैं।')
rep('Guru-Śani Saṅgama<span class="ysub">Jupiter + Saturn · Taurus 3H</span>', 'गुरु-शनि संगम<span class="ysub">गुरु + शनि · वृषभ · तृतीय</span>')
rep('<b>The great conjunction of 2000.</b> Discipline welded to wisdom in the skills house — craft compounds into institutions over decades.',
    '<b>सन् 2000 की महायुति।</b> कौशल-भाव में अनुशासन और ज्ञान का मेल — शिल्प दशकों में संस्थाओं का रूप लेता है।')
rep('Sūrya-Rāhu Sambandha<span class="ysub">Sun with Rahu · 5H · watch</span>', 'सूर्य-राहु संबंध<span class="ysub">सूर्य राहु संग · पंचम · सतर्क</span>')
rep('<b>Amplified ambition, shadowed ego.</b> Enormous unconventional drive; guard against overreach, shortcuts and authority clashes.',
    '<b>प्रवर्धित महत्वाकांक्षा, छायांकित अहं।</b> विराट अपरंपरागत ऊर्जा; अति, शॉर्टकट और सत्ता-टकराव से बचिए।')

# ---------- page 3 numerology ----------
rep('<span class="txt">Numerology Signature</span>', '<span class="txt">अंक-ज्योतिष हस्ताक्षर</span>')
rep('<div class="nlab">Moolānk · Root</div><div class="ntxt">The Builder — structure, method, unconventional systems. Rahu\'s number, echoing your 5H Rahu.</div>',
    '<div class="nlab">मूलांक</div><div class="ntxt">निर्माता — संरचना, विधि, अपरंपरागत प्रणालियाँ। राहु का अंक, जो पंचम के राहु से गूँजता है।</div>')
rep('<div class="nlab">Bhāgyānk · Destiny</div><div class="ntxt">The Versatile — commerce, communication, motion. Mercury\'s number mirrors your 5H Mercury.</div>',
    '<div class="nlab">भाग्यांक</div><div class="ntxt">बहुमुखी — वाणिज्य, संवाद, गति। बुध का अंक, जो पंचम के बुध का दर्पण है।</div>')
rep('<div class="nlab">Expression · Saurabh</div><div class="ntxt">The Seeker — analysis, hidden knowledge, deep tech. Ketu\'s number; the researcher\'s signature.</div>',
    '<div class="nlab">नाम अंक · सौरभ</div><div class="ntxt">खोजी — विश्लेषण, गूढ़ ज्ञान, गहन तकनीक। केतु का अंक; शोधकर्ता का हस्ताक्षर।</div>')
rep('<div class="nlab">Soul Urge</div><div class="ntxt">Inner engine: autonomy and change — thrives on movement, starves on routine.</div>',
    '<div class="nlab">अंतरात्मा अंक</div><div class="ntxt">भीतरी इंजन: स्वायत्तता व परिवर्तन — गति पर पनपता है, ढर्रे में मुरझाता है।</div>')
rep('<div class="nlab">Personality</div><div class="ntxt">Outer read: measured, diplomatic — Moon-calm at the negotiating table.</div>',
    '<div class="nlab">व्यक्तित्व अंक</div><div class="ntxt">बाहरी छवि: संयत, कूटनीतिक — वार्ता की मेज़ पर चंद्र-सी शीतलता।</div>')
rep('<div class="nlab">Personal Year 2026</div><div class="ntxt">Master Builder vibration — lay foundations this year that outlive the decade.</div>',
    '<div class="nlab">व्यक्तिगत वर्ष 2026</div><div class="ntxt">मास्टर बिल्डर स्पंदन — इस वर्ष ऐसी नींव रखिए जो दशक से आगे टिके।</div>')
rep("<div class=\"numsyn\"><b>The 4–5–7 triad.</b> A disciplined builder (4) with a merchant's adaptability (5) and a mystic-analyst's depth (7) — the numbers and the natal chart tell one story: engineered creativity, monetized through original systems.</div>",
    '<div class="numsyn"><b>4–5–7 की त्रयी।</b> अनुशासित निर्माता (4), व्यापारी की लचक (5) और रहस्य-विश्लेषक की गहराई (7) — अंक और कुंडली एक ही कथा कहते हैं: अभियांत्रिक सृजनशीलता, मौलिक प्रणालियों से अर्थ में परिणत।</div>')
rep('<span>Daśā computed from Moon in Hasta nakṣatra (lord Moon, balance 2.61y at birth) · 365.25-day years · Numerology: Pythagorean name values, Vedic moolānk/bhāgyānk.</span>',
    '<span>दशा हस्त नक्षत्र के चंद्र से गणित (जन्म पर शेष 2.61 वर्ष) · 365.25-दिवसीय वर्ष · अंक-ज्योतिष: पाइथागोरियन नाम-मान, वैदिक मूलांक/भाग्यांक।</span>')
rep('<span style="white-space:nowrap">Page 3 · Timing, Yogas &amp; Numbers</span>', '<span style="white-space:nowrap">पृष्ठ 3 · काल, योग व अंक</span>')

open(P, "w").write(h)
print("PART 1 done. Missing:", len(miss))
for m in miss: print("  MISS:", m)
