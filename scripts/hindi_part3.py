# -*- coding: utf-8 -*-
"""Hindi edition part 3: pages 6-8 + toolbar + countdown JS."""
P = "/app/saurabh-master-chart-hindi.html"
h = open(P).read()
miss = []

def rep(old, new):
    global h
    if old not in h:
        miss.append(old[:70]); return
    h = h.replace(old, new)

# ---------- page 6: roadmap ----------
rep('<span class="txt">Strategic Roadmap · ReadyUP · Daśā-Aligned</span>', '<span class="txt">रणनीतिक रोडमैप · ReadyUP · दशा-संरेखित</span>')
rep('<div class="ck">Company</div><div class="cv"><b>ReadyUP</b> · ready2up.com</div>', '<div class="ck">कंपनी</div><div class="cv"><b>ReadyUP</b> · ready2up.com</div>')
rep('<div class="ck">Founded</div><div class="cv">3 Nov 2023 → <b>№ 3</b></div>', '<div class="ck">स्थापना</div><div class="cv">3 नव॰ 2023 → <b>अंक 3</b></div>')
rep('<div class="ck">Track Record</div><div class="cv">Online since <b>2017</b></div>', '<div class="ck">अनुभव</div><div class="cv"><b>2017</b> से ऑनलाइन</div>')
rep('<div class="ck">Service Lines</div><div class="cv">Web · Apps · Games · Extensions</div>', '<div class="ck">सेवाएँ</div><div class="cv">वेब · ऐप · गेम · एक्सटेंशन</div>')
rep('<div class="ck">War Chest</div><div class="cv"><b>₹1–5L</b> deployable</div>', '<div class="ck">निवेश-कोष</div><div class="cv"><b>₹1–5 लाख</b> उपलब्ध</div>')
rep('<div class="lv">₹1L / mo</div><div class="lk">Month 3 · Proof</div>', '<div class="lv">₹1 लाख / माह</div><div class="lk">माह 3 · प्रमाण</div>')
rep('<div class="lv">₹5L / mo</div><div class="lk">Month 9 · Engine</div>', '<div class="lv">₹5 लाख / माह</div><div class="lk">माह 9 · इंजन</div>')
rep('<div class="lv">₹15L / mo</div><div class="lk">Month 18 · Scale</div>', '<div class="lv">₹15 लाख / माह</div><div class="lk">माह 18 · विस्तार</div>')
rep('<div class="lv">₹2–5 Cr</div><div class="lk">Cumulative · Year 2</div>', '<div class="lv">₹2–5 करोड़</div><div class="lk">संचयी · वर्ष 2</div>')
rep('<span class="txt">Offer Architecture</span>', '<span class="txt">ऑफ़र संरचना</span>')
rep('<div class="wk">Local Packages · ₹25K / ₹45K / ₹65K</div><p><b>Anchored to your proven ₹66K ceiling.</b> Three fixed tiers, never below ₹25K — the ₹5–10K market is a treadmill, not a business. Every build bundles hosting setup: +₹5–7K affiliate margin per project.</p>',
    '<div class="wk">स्थानीय पैकेज · ₹25/45/65 हज़ार</div><p><b>आपकी सिद्ध ₹66 हज़ार की ऊँचाई पर आधारित।</b> तीन निश्चित स्तर, ₹25 हज़ार से नीचे कभी नहीं — ₹5–10 हज़ार का बाज़ार चक्की है, व्यवसाय नहीं। हर प्रोजेक्ट में होस्टिंग सेटअप: +₹5–7 हज़ार एफ़िलिएट मार्जिन।</p>')
rep('<div class="wk">Growth Retainer · ₹8–25K/mo</div><p><b>The compounding layer.</b> Maintenance + SEO + content, priced for this market. Thirty retainers is a ₹4.5L/month recurring floor before any new sale.</p>',
    '<div class="wk">ग्रोथ रिटेनर · ₹8–25 हज़ार/माह</div><p><b>चक्रवृद्धि की परत।</b> रखरखाव + SEO + कंटेंट, इसी बाज़ार के अनुसार। तीस रिटेनर यानी हर नई बिक्री से पहले ₹4.5 लाख/माह का स्थायी आधार।</p>')
rep('<div class="wk">International Premium · $2–6K</div><p><b>USD changes the economics 3–5×.</b> US/UK/UAE via LinkedIn + cold outreach. Invoice from India under LUT — no Dubai entity needed yet.</p>',
    '<div class="wk">अंतरराष्ट्रीय प्रीमियम · $2–6 हज़ार</div><p><b>डॉलर अर्थशास्त्र को 3–5 गुना बदल देता है।</b> अमेरिका/यूके/यूएई — लिंक्डइन व कोल्ड आउटरीच से। भारत से LUT के अंतर्गत बिल — दुबई इकाई की अभी आवश्यकता नहीं।</p>')
rep('<span class="txt">Execution Phases</span>', '<span class="txt">क्रियान्वयन चरण</span>')
rep('<div class="wk">Phase I · Now → Feb 2027 · Rahu–Moon</div><p><b>Stabilise &amp; be seen.</b> Productise the offers, ship one sellable digital product (this dossier as a service), build 3 spec redesigns of famous brands, run 30 outbound conversations weekly. This daśā favours visibility — sell hard.</p>',
    '<div class="wk">चरण 1 · अभी → फ़र॰ 2027 · राहु–चंद्र</div><p><b>स्थिर होइए, दिखिए।</b> ऑफ़र को उत्पाद बनाइए, एक बिकाऊ डिजिटल उत्पाद प्रस्तुत कीजिए (यही दस्तावेज़ एक सेवा के रूप में), प्रसिद्ध ब्रांडों के 3 नमूना-पुनर्रचना बनाइए, साप्ताहिक 30 संवाद कीजिए। यह दशा दृश्यता की पक्षधर है — डटकर बेचिए।</p>')
rep('<div class="wk">Phase II · Feb 2027 → Mar 2028 · Rahu–Mars</div><p><b>Execution sprint.</b> 25–30 retainers live, 50% of revenue in USD, contract talent only, AI-accelerated delivery. Close aggressively before the daśā turns.</p>',
    '<div class="wk">चरण 2 · फ़र॰ 2027 → मार्च 2028 · राहु–मंगल</div><p><b>निष्पादन की दौड़।</b> 25–30 रिटेनर सक्रिय, आय का 50% डॉलर में, केवल अनुबंधित प्रतिभा, AI-त्वरित डिलीवरी। दशा बदलने से पहले आक्रामक समापन।</p>')
rep('<div class="wk">Phase III · Mar 2028+ · Jupiter Mahādaśā</div><p><b>Structural ascent.</b> Agency brand + productised IP (templates, SaaS). Open the Dubai entity only after ₹1 Cr international profit. ₹15–20 Cr becomes the Year-4 target, funded by this base.</p>',
    '<div class="wk">चरण 3 · मार्च 2028+ · बृहस्पति महादशा</div><p><b>संरचनात्मक आरोहण।</b> एजेंसी ब्रांड + उत्पादित बौद्धिक संपदा (टेम्पलेट, SaaS)। दुबई इकाई केवल ₹1 करोड़ अंतरराष्ट्रीय लाभ के बाद। ₹15–20 करोड़ इसी आधार पर वर्ष-4 का लक्ष्य बनता है।</p>')
rep('<span class="txt">Expansion &amp; The Dubai Question</span>', '<span class="txt">विस्तार व दुबई-प्रश्न</span>')
rep('<div class="wk">Nashik → Pune → Mumbai</div><p><b>No offices — beachheads.</b> Win 5 anchor clients per city through niche portfolios and referral partners (CAs, architects, brokers). Travel for closings only; deliver remotely.</p>',
    '<div class="wk">नासिक → पुणे → मुंबई</div><p><b>दफ़्तर नहीं — मोर्चे।</b> हर शहर में 5 आधार-ग्राहक जीतिए — विशिष्ट पोर्टफोलियो व रेफ़रल साझेदारों (सीए, वास्तुकार, ब्रोकर) से। यात्रा केवल सौदे के समापन हेतु; डिलीवरी दूरस्थ।</p>')
rep('<div class="wk">The International Engine</div><p><b>Before any entity, build the pipeline.</b> 15 USD conversations weekly on LinkedIn/Upwork; UAE agencies also subcontract Indian studios at $30–60/hr — a direct door into that market.</p>',
    '<div class="wk">अंतरराष्ट्रीय इंजन</div><p><b>किसी भी इकाई से पहले पाइपलाइन बनाइए।</b> लिंक्डइन/अपवर्क पर साप्ताहिक 15 डॉलर-संवाद; यूएई एजेंसियाँ भारतीय स्टूडियो को $30–60/घंटा पर उप-अनुबंध भी देती हैं — उस बाज़ार का सीधा द्वार।</p>')
rep('<div class="wk">Dubai Entity — When &amp; How</div><p><b>Trigger: ₹1 Cr international profit.</b> Freezone (IFZA/Meydan) ≈ ₹1.5–3L/yr, 9% corporate tax above AED 375K, banking takes 4–8 weeks. Until then, LUT export invoicing does the job at 0% GST.</p>',
    '<div class="wk">दुबई इकाई — कब व कैसे</div><p><b>शर्त: ₹1 करोड़ अंतरराष्ट्रीय लाभ।</b> फ़्रीज़ोन (IFZA/Meydan) ≈ ₹1.5–3 लाख/वर्ष, AED 3.75 लाख से ऊपर 9% कॉर्पोरेट कर, बैंकिंग में 4–8 सप्ताह। तब तक LUT निर्यात-बिलिंग 0% GST पर काम करती है।</p>')
rep('<b>Operating rules.</b> Deploy the ₹1–5L war chest as income engines only — ≈₹50K positioning assets, ≈₹1L niche pages &amp; outbound, balance held until the first international close · Attach hosting to every local build: Hosting.com pays ≈$80 and Bluehost ≈$65 per referred sale — ten sales is ₹60–66K of found money · No office or salaried hires until ₹3L/mo profit holds 3 straight months · Export invoices under LUT (0% GST) · 10% referral programme on every delivered project · Weekly pipeline metric: 30 conversations, tracked · Dubai is a tax decision, not a growth decision.',
    '<b>कार्य-नियम।</b> ₹1–5 लाख का कोष केवल आय-इंजनों में — ≈₹50 हज़ार पोज़िशनिंग, ≈₹1 लाख विशिष्ट पेज व आउटरीच, शेष पहले अंतरराष्ट्रीय सौदे तक सुरक्षित · हर स्थानीय प्रोजेक्ट में होस्टिंग जोड़िए: Hosting.com ≈$80 व Bluehost ≈$65 प्रति बिक्री — दस बिक्री यानी ₹60–66 हज़ार अतिरिक्त · ₹3 लाख/माह लाभ 3 माह टिकने तक न दफ़्तर, न वेतनभोगी · निर्यात-बिल LUT से (0% GST) · हर प्रोजेक्ट पर 10% रेफ़रल · साप्ताहिक मापदंड: 30 संवाद · दुबई कर-निर्णय है, विकास-निर्णय नहीं।')
rep('<span>ReadyUP est. 3 Nov 2023 → founding number 3, creative expression · Rahu–Moon favours visibility; Jupiter (1st &amp; 10th lord) opens the ascent Mar 2028.</span>',
    '<span>ReadyUP स्थापना 3 नव॰ 2023 → स्थापना-अंक 3, सृजनात्मक अभिव्यक्ति · राहु–चंद्र दृश्यता का पक्षधर; गुरु (लग्नेश-दशमेश) मार्च 2028 से आरोहण खोलता है।</span>')
rep('<span style="white-space:nowrap">Page 6 · Strategic Roadmap</span>', '<span style="white-space:nowrap">पृष्ठ 6 · रणनीतिक रोडमैप</span>')

# ---------- page 7: muhurta ----------
rep('<span class="txt">Muhūrta Calendar · Electional Windows</span>', '<span class="txt">मुहूर्त पंचांग · शुभ अवसर</span>')
rep('<div class="ck">Current Daśā</div><div class="cv">Rahu–Moon → <b>Feb 2027</b></div>', '<div class="ck">वर्तमान दशा</div><div class="cv">राहु–चंद्र → <b>फ़र॰ 2027</b></div>')
rep('<div class="ck">Then</div><div class="cv">Rahu–Mars → <b>Mar 2028</b></div>', '<div class="ck">तत्पश्चात</div><div class="cv">राहु–मंगल → <b>मार्च 2028</b></div>')
rep('<div class="ck">The Ascent</div><div class="cv">Jupiter MD · <b>Mar 2028</b></div>', '<div class="ck">आरोहण</div><div class="cv">गुरु महादशा · <b>मार्च 2028</b></div>')
rep('<div class="ck">Favoured Days</div><div class="cv"><b>Mon · Wed · Thu</b></div>', '<div class="ck">शुभ वार</div><div class="cv"><b>सोम · बुध · गुरु</b></div>')
rep('<div class="ck">Tārā Anchor</div><div class="cv">Janma nakṣatra <b>Hasta</b></div>', '<div class="ck">तारा-आधार</div><div class="cv">जन्म नक्षत्र <b>हस्त</b></div>')
rep('<span class="txt">Golden Days — Guru-Puṣya Thursdays</span>', '<span class="txt">स्वर्ण दिवस — गुरु-पुष्य गुरुवार</span>')
rep('<div class="md">18 Mar 2027 <span>Thu</span></div><div class="mn">Puṣya · Śukla Ekādaśī</div><p><b>The crown date.</b> Guru-Puṣya on a bright Ekādaśī — sign the biggest contract, open the account, raise the first international invoice.</p>',
    '<div class="md">18 मार्च 2027 <span>गुरु</span></div><div class="mn">पुष्य · शुक्ल एकादशी</div><p><b>मुकुट-तिथि।</b> शुक्ल एकादशी पर गुरु-पुष्य — सबसे बड़ा अनुबंध कीजिए, खाता खोलिए, पहला अंतरराष्ट्रीय बिल जारी कीजिए।</p>')
rep('<div class="md">15 Apr 2027 <span>Thu</span></div><div class="mn">Puṣya · Navamī</div><p>Second Guru-Puṣya of the season — launch offers, begin retainers, start anything meant to compound.</p>',
    '<div class="md">15 अप्रैल 2027 <span>गुरु</span></div><div class="mn">पुष्य · नवमी</div><p>ऋतु का दूसरा गुरु-पुष्य — ऑफ़र लॉन्च कीजिए, रिटेनर आरंभ कीजिए, जो भी चक्रवृद्धि के लिए बना है वह शुरू कीजिए।</p>')
rep('<div class="md">13 Jan 2028 <span>Thu</span></div><div class="mn">Puṣya · Kṛṣṇa Dvitīyā</div><p>Final Guru-Puṣya before the Jupiter mahādaśā — set the structures the 2028 ascent will run on.</p>',
    '<div class="md">13 जन॰ 2028 <span>गुरु</span></div><div class="mn">पुष्य · कृष्ण द्वितीया</div><p>बृहस्पति महादशा से पूर्व अंतिम गुरु-पुष्य — वे ढाँचे स्थापित कीजिए जिन पर 2028 का आरोहण चलेगा।</p>')
rep('<span class="txt">Launch Windows — Go-Lives, Offers, Campaigns</span>', '<span class="txt">लॉन्च अवसर — गो-लाइव, ऑफ़र, अभियान</span>')
rep('<div class="md">24 Sep 2026 <span>Thu</span></div><div class="mn">Dhaniṣṭhā · Trayodaśī</div><p>First clean window — launch the productised offer menu and the niche landing pages.</p>',
    '<div class="md">24 सित॰ 2026 <span>गुरु</span></div><div class="mn">धनिष्ठा · त्रयोदशी</div><p>पहला निर्मल अवसर — उत्पादित ऑफ़र-सूची और विशिष्ट लैंडिंग पेज लॉन्च कीजिए।</p>')
rep('<div class="md">11 Jan 2027 <span>Mon</span></div><div class="mn">Dhaniṣṭhā · Tṛtīyā</div><p>New-year go-live; a Moon-day inside the Rahu–Moon daśā doubles the visibility current.</p>',
    '<div class="md">11 जन॰ 2027 <span>सोम</span></div><div class="mn">धनिष्ठा · तृतीया</div><p>नववर्ष गो-लाइव; राहु–चंद्र दशा में सोमवार दृश्यता की धारा दोगुनी करता है।</p>')
rep('<div class="md">11 Mar 2027 <span>Thu</span></div><div class="mn">Revatī · Tṛtīyā</div><p>Post-retrograde reset — ship the international portfolio and outreach engine.</p>',
    '<div class="md">11 मार्च 2027 <span>गुरु</span></div><div class="mn">रेवती · तृतीया</div><p>वक्री-पश्चात पुनरारंभ — अंतरराष्ट्रीय पोर्टफोलियो व आउटरीच इंजन प्रस्तुत कीजिए।</p>')
rep('<div class="md">13 Sep 2027 <span>Mon</span></div><div class="mn">Dhaniṣṭhā · Trayodaśī</div><p>Mid Rahu–Mars sprint — campaign pushes, product drops, aggressive closings.</p>',
    '<div class="md">13 सित॰ 2027 <span>सोम</span></div><div class="mn">धनिष्ठा · त्रयोदशी</div><p>राहु–मंगल दौड़ के मध्य — अभियान, उत्पाद-विमोचन, आक्रामक समापन।</p>')
rep('<div class="md">9 Dec 2027 <span>Thu</span></div><div class="mn">Revatī · Ekādaśī</div><p>Year-end release window on a bright Ekādaśī — end 2027 loud.</p>',
    '<div class="md">9 दिस॰ 2027 <span>गुरु</span></div><div class="mn">रेवती · एकादशी</div><p>शुक्ल एकादशी पर वर्षांत विमोचन — 2027 का समापन गूँज के साथ।</p>')
rep('<div class="md">10 Jan 2028 <span>Mon</span></div><div class="mn">Mṛgaśira · Trayodaśī</div><p>Pre-retrograde slot — ship before the 25 Jan Mercury stall.</p>',
    '<div class="md">10 जन॰ 2028 <span>सोम</span></div><div class="mn">मृगशिरा · त्रयोदशी</div><p>वक्री-पूर्व अवसर — 25 जनवरी के बुध-अवरोध से पहले प्रस्तुत कीजिए।</p>')
rep('<span class="txt">Signing &amp; Contracts — Fixed-Star Days</span>', '<span class="txt">हस्ताक्षर व अनुबंध — स्थिर-नक्षत्र दिवस</span>')
rep('<div class="md">2 Sep 2027 <span>Thu</span></div><div class="mn">Uttara Phalgunī · Dvitīyā</div><p><b>Moon rides natal Virgo</b> — decisions made here align with the core. Anchor partnership agreements.</p>',
    '<div class="md">2 सित॰ 2027 <span>गुरु</span></div><div class="mn">उत्तरा फाल्गुनी · द्वितीया</div><p><b>चंद्र जन्म-कन्या पर</b> — यहाँ लिए निर्णय मूल से संरेखित होते हैं। साझेदारी-अनुबंध यहीं बाँधिए।</p>')
rep('<div class="md">30 Dec 2027 <span>Thu</span></div><div class="mn">Uttara Āṣāḍhā · Tṛtīyā</div><p>Fixed-star Thursday — close the year\'s largest retainer or the international MoU.</p>',
    '<div class="md">30 दिस॰ 2027 <span>गुरु</span></div><div class="mn">उत्तराषाढ़ा · तृतीया</div><p>स्थिर-नक्षत्र गुरुवार — वर्ष का सबसे बड़ा रिटेनर या अंतरराष्ट्रीय समझौता यहीं संपन्न कीजिए।</p>')
rep('<div class="md">— <span>Note</span></div><div class="mn">Sparse by design</div><p>Fixed nakṣatras rarely clear every filter. When a signing can\'t wait, borrow a Golden Day or any launch window outside Mercury retrograde.</p>',
    '<div class="md">— <span>टिप्पणी</span></div><div class="mn">जानबूझकर विरल</div><p>स्थिर नक्षत्र हर कसौटी विरले ही पार करते हैं। हस्ताक्षर रुक न सकें तो स्वर्ण दिवस या बुध-वक्री से बाहर का कोई लॉन्च-अवसर लीजिए।</p>')
rep('<b>Cautions.</b> Mercury retrograde — sign nothing new: 25 Oct–13 Nov 2026 · 10 Feb–3 Mar 2027 · 11 Jun–4 Jul 2027 · 8–28 Oct 2027 · 25 Jan–14 Feb 2028 · Skip days when the Moon transits Sagittarius, Aries or Leo (4th/8th/12th from natal Moon) · Daily Rahu Kālam — keep launches &amp; signings outside it: Sun 16:30–18:00 · Mon 7:30–9:00 · Tue 15:00–16:30 · Wed 12:00–13:30 · Thu 13:30–15:00 · Fri 10:30–12:00 · Sat 9:00–10:30.',
    '<b>सावधानियाँ।</b> बुध वक्री — कोई नया हस्ताक्षर नहीं: 25 अक्टू॰–13 नव॰ 2026 · 10 फ़र॰–3 मार्च 2027 · 11 जून–4 जुल॰ 2027 · 8–28 अक्टू॰ 2027 · 25 जन॰–14 फ़र॰ 2028 · जिन दिनों चंद्र धनु, मेष या सिंह में हो (जन्म-चंद्र से 4/8/12) वे दिन छोड़िए · दैनिक राहु काल — लॉन्च व हस्ताक्षर इससे बाहर रखिए: रवि 16:30–18:00 · सोम 7:30–9:00 · मंगल 15:00–16:30 · बुध 12:00–13:30 · गुरु 13:30–15:00 · शुक्र 10:30–12:00 · शनि 9:00–10:30।')
rep('Electional scan Sep 2026 → Mar 2028 at 09:00 IST · favoured weekdays only (Moon, Mercury, Jupiter — the chart\'s allies) · benefic Tārābala from Hasta · Chandra-bala enforced (no 4th/8th/12th Moon) · bright-fortnight tithis preferred. Verify the final hour with a pañchāṅga on the day itself — a muhūrta sharpens intent; it never replaces it.',
    'मुहूर्त-अन्वेषण सित॰ 2026 → मार्च 2028, प्रातः 9:00 IST · केवल शुभ वार (चंद्र, बुध, गुरु — कुंडली के मित्र) · हस्त से शुभ ताराबल · चंद्रबल अनिवार्य (4/8/12 का चंद्र वर्जित) · शुक्ल पक्ष की तिथियाँ वरीय। अंतिम घड़ी उसी दिन पंचांग से जाँचिए — मुहूर्त संकल्प को धार देता है; उसका स्थान नहीं लेता।')
rep('<span>Vedic electional timing (muhūrta) · Swiss Ephemeris, Lahiri ayanāṁśa · window aligned to the Rahu → Jupiter daśā handover.</span>',
    '<span>वैदिक मुहूर्त-गणना · स्विस एफ़ेमेरिस, लाहिड़ी अयनांश · राहु → गुरु दशा-संधि से संरेखित।</span>')
rep('<span style="white-space:nowrap">Page 7 · Muhūrta Calendar</span>', '<span style="white-space:nowrap">पृष्ठ 7 · मुहूर्त पंचांग</span>')

# ---------- page 8: bridge ----------
rep('<span class="txt">The Bridge · Today → The Jupiter Ascent</span>', '<span class="txt">सेतु · आज → गुरु-आरोहण</span>')
rep('<div class="ck">Now</div><div class="cv">Rahu–Moon → <b>Feb 2027</b></div>', '<div class="ck">अभी</div><div class="cv">राहु–चंद्र → <b>फ़र॰ 2027</b></div>')
rep('<div class="ck">Transit Gift</div><div class="cv">Jupiter <b>exalted in 5H</b> → Nov 2026</div>', '<div class="ck">गोचर-वरदान</div><div class="cv">गुरु <b>पंचम में उच्च</b> → नव॰ 2026</div>')
rep('<div class="ck">Transit Test</div><div class="cv">Saturn on <b>Lagna</b> → mid-2027</div>', '<div class="ck">गोचर-परीक्षा</div><div class="cv">शनि <b>लग्न</b> पर → मध्य-2027</div>')
rep('<div class="ck">Destination</div><div class="cv">Jupiter MD · <b>Mar 2028</b></div>', '<div class="ck">गंतव्य</div><div class="cv">गुरु महादशा · <b>मार्च 2028</b></div>')
rep('<span class="txt">Phase I · Now → Feb 2027 · Rahu–Moon — Be Seen</span>', '<span class="txt">चरण 1 · अभी → फ़र॰ 2027 · राहु–चंद्र — दिखिए</span>')
rep('<div class="wk">Do</div><p><b>Publish weekly</b> — spec redesigns, before/afters, case notes. Launch the productised menu on 24 Sep 2026. Stack alliances: CAs, architects, brokers, and a hosting bundle on every build. Let the relationship breathe — Jupiter is carrying it.</p>',
    '<div class="wk">कीजिए</div><p><b>साप्ताहिक प्रकाशित कीजिए</b> — नमूना-पुनर्रचना, पहले/बाद, केस-नोट। 24 सित॰ 2026 को उत्पादित मेनू लॉन्च कीजिए। गठजोड़ जोड़िए: सीए, वास्तुकार, ब्रोकर, और हर प्रोजेक्ट में होस्टिंग। संबंध को साँस लेने दीजिए — गुरु उसे स्वयं वहन कर रहा है।</p>')
rep('<div class="wk">Don\'t</div><p><b>No image spending</b> — no office lease, no loan for optics. No project below ₹25K. Sign nothing 25 Oct – 13 Nov (Mercury retrograde). Don\'t read her silences as verdicts — Moon periods amplify moods, in you and around you.</p>',
    '<div class="wk">मत कीजिए</div><p><b>दिखावे पर व्यय नहीं</b> — न दफ़्तर का पट्टा, न छवि के लिए ऋण। ₹25 हज़ार से नीचे कोई प्रोजेक्ट नहीं। 25 अक्टू॰–13 नव॰ (बुध वक्री) में कोई हस्ताक्षर नहीं। उनकी चुप्पियों को फ़ैसला मत समझिए — चंद्र-काल भावनाएँ बढ़ाता है, आपमें भी, आस-पास भी।</p>')
rep('<div class="wk">Transit Note</div><p><b>Exalted Jupiter crossed your Sun on 29 Aug 2026</b> — the single loudest recognition window of the bridge: show the best work publicly. Saturn on the Lagna asks one fee in return — sleep, routine, and a body kept strong.</p>',
    '<div class="wk">गोचर-टिप्पणी</div><p><b>उच्च का गुरु 29 अग॰ 2026 को आपके सूर्य से गुज़रा</b> — सेतु की सबसे मुखर मान्यता-खिड़की: श्रेष्ठ कार्य सार्वजनिक कीजिए। लग्न पर बैठा शनि बदले में एक ही शुल्क माँगता है — नींद, दिनचर्या और सशक्त शरीर।</p>')
rep('<span class="txt">Phase II · Feb 2027 → Mar 2028 · Rahu–Mars — Execute</span>', '<span class="txt">चरण 2 · फ़र॰ 2027 → मार्च 2028 · राहु–मंगल — निष्पादन</span>')
rep('<div class="wk">Do</div><p><b>Close aggressively.</b> Raise the local floor to ₹45K; push international to half of revenue. Contract help, ship fast, bank cash — build a 6-month runway before the mahādaśā turns. Fire the first big shots on Guru-Puṣya: 18 Mar &amp; 15 Apr 2027.</p>',
    '<div class="wk">कीजिए</div><p><b>आक्रामक समापन।</b> स्थानीय न्यूनतम ₹45 हज़ार कीजिए; अंतरराष्ट्रीय को आय का आधा बनाइए। अनुबंधित सहायता लीजिए, तेज़ प्रस्तुत कीजिए, नकद बचाइए — महादशा बदलने से पहले 6-माह की पूँजी। पहले बड़े प्रहार गुरु-पुष्य पर: 18 मार्च व 15 अप्रैल 2027।</p>')
rep('<div class="wk">Don\'t</div><p><b>No speculation.</b> No trading, no crypto punts, no "win the ₹40L back fast" bets — Mars-Rahu burns gamblers. No disputes: settle and move. Anger drafts messages; never send them. Contracts on everything, every time.</p>',
    '<div class="wk">मत कीजिए</div><p><b>कोई सट्टा नहीं।</b> न ट्रेडिंग, न क्रिप्टो-दाँव, न "₹40 लाख झट से वापस जीतने" की बाज़ी — मंगल-राहु जुआरियों को जलाता है। कोई विवाद नहीं: निपटाइए, आगे बढ़िए। क्रोध संदेश लिखता है; उन्हें कभी भेजिए मत। हर काम पर, हर बार अनुबंध।</p>')
rep('<div class="wk">Transit Note</div><p>Saturn tests the Lagna till mid-2027 — pace the body, don\'t sprint it. From <b>27 Nov 2027 Jupiter enters your 7th house</b>: partnerships, business and personal, turn formal. That is the bridge\'s final arch into Mar 2028.</p>',
    '<div class="wk">गोचर-टिप्पणी</div><p>शनि मध्य-2027 तक लग्न को परखता है — शरीर को गति दीजिए, दौड़ाइए मत। <b>27 नव॰ 2027 से गुरु आपके सप्तम में</b>: साझेदारियाँ — व्यावसायिक और व्यक्तिगत — औपचारिक होती हैं। यही सेतु की अंतिम चाप है, मार्च 2028 में।</p>')
rep('<span class="txt">Weekly Rhythm — The Planets as a Timetable</span>', '<span class="txt">साप्ताहिक लय — ग्रह ही समय-सारणी</span>')
rep('<div class="ck">Monday · Moon</div><div class="cv">Plan &amp; <b>outreach</b></div>', '<div class="ck">सोमवार · चंद्र</div><div class="cv">योजना व <b>आउटरीच</b></div>')
rep('<div class="ck">Wednesday · Mercury</div><div class="cv">Invoices &amp; <b>follow-ups</b></div>', '<div class="ck">बुधवार · बुध</div><div class="cv">बिल व <b>फ़ॉलो-अप</b></div>')
rep('<div class="ck">Thursday · Jupiter</div><div class="cv">Proposals &amp; <b>closings</b></div>', '<div class="ck">गुरुवार · गुरु</div><div class="cv">प्रस्ताव व <b>समापन</b></div>')
rep('<div class="ck">Saturday · Saturn</div><div class="cv">Systems &amp; <b>learning</b></div>', '<div class="ck">शनिवार · शनि</div><div class="cv">प्रणालियाँ व <b>अध्ययन</b></div>')
rep('<div class="ck">Daily</div><div class="cv"><b>30</b> conversations</div>', '<div class="ck">प्रतिदिन</div><div class="cv"><b>30</b> संवाद</div>')
rep('<b>How to wait well.</b> The bridge is crossed by boring repetition — same offers, same weekdays, same outreach count — until Mar 2028 finds the machine already running · Rebuild the personal runway before any reinvestment · The ₹35–40L loss is tuition already paid; it buys judgement, not shame · Protect the four anchors: sleep before midnight, water, one rest day, and the Wednesday–Thursday work rhythm · Guard the phone after 10pm — night decisions belong to the Moon, not to you.',
    '<b>प्रतीक्षा का शास्त्र।</b> सेतु उबाऊ पुनरावृत्ति से पार होता है — वही ऑफ़र, वही वार, वही संवाद-संख्या — जब तक मार्च 2028 चलती हुई मशीन न पा ले · किसी भी पुनर्निवेश से पहले व्यक्तिगत पूँजी पुनर्निर्मित कीजिए · ₹35–40 लाख की हानि चुकाई जा चुकी फ़ीस है; वह विवेक ख़रीदती है, लज्जा नहीं · चार आधार सुरक्षित रखिए: मध्यरात्रि से पहले नींद, जल, एक विश्राम-दिवस, और बुध–गुरु की कार्य-लय · रात 10 बजे बाद फ़ोन से दूरी — रात के निर्णय चंद्रमा के हैं, आपके नहीं।')
rep('<span>Daśā strategy bridged with live transits (Swiss Ephemeris) — Jupiter exalted in Cancer 2 Jun 2026 → Nov 2026, return Jan–Jun 2027; Saturn in Pisces on the Lagna.</span>',
    '<span>दशा-रणनीति सजीव गोचरों से जुड़ी (स्विस एफ़ेमेरिस) — गुरु कर्क में उच्च 2 जून 2026 → नव॰ 2026, वापसी जन॰–जून 2027; शनि मीन में लग्न पर।</span>')
rep('<span style="white-space:nowrap">Page 8 · The Bridge</span>', '<span style="white-space:nowrap">पृष्ठ 8 · सेतु</span>')

# ---------- toolbar + countdown ----------
old_tb = '''<div class="toolbar">
  <a class="tb-btn primary" href="/SAURABH-Master-Chart-Dark.pdf" download data-testid="download-pdf-btn">'''
new_tb = '''<div class="toolbar">
  <a class="tb-btn primary" href="/SAURABH-Master-Chart-Hindi.pdf" download data-testid="download-pdf-btn">'''
rep(old_tb, new_tb)
rep('''    A4 PDF
  </a>
  <a class="tb-btn secondary" href="/SAURABH-Master-Chart-Dark-Letter.pdf" download data-testid="download-letter-btn">Letter PDF</a>
  <button class="tb-btn secondary" onclick="window.print()" data-testid="print-pdf-btn">Print</button>
  <a class="tb-btn ghost" href="/master-chart-sakura.html" data-testid="sakura-edition-link">Sakura Edition</a>
  <a class="tb-btn ghost" href="/pitch-deck.html" data-testid="pitch-deck-link">ReadyUP Deck</a>''',
'''    A4 PDF
  </a>
  <button class="tb-btn secondary" onclick="window.print()" data-testid="print-pdf-btn">प्रिंट</button>
  <a class="tb-btn ghost" href="/master-chart.html" data-testid="dark-edition-link">English · Dark</a>
  <a class="tb-btn ghost" href="/master-chart-sakura.html" data-testid="sakura-edition-link">Sakura</a>''')
rep('"Dhaniṣṭhā launch window"', '"धनिष्ठा लॉन्च अवसर"')
rep('"Revatī launch window"', '"रेवती लॉन्च अवसर"')
rep('"Guru-Puṣya · golden day"', '"गुरु-पुष्य · स्वर्ण दिवस"')
rep('"Signing day · U. Phalgunī"', '"हस्ताक्षर दिवस · उ. फाल्गुनी"')
rep('"Signing day · U. Āṣāḍhā"', '"हस्ताक्षर दिवस · उ. आषाढ़ा"')
rep('"Mṛgaśira launch window"', '"मृगशिरा लॉन्च अवसर"')
rep("el.innerHTML='Next window: <b>'+t.toLocaleDateString('en-IN',{day:'numeric',month:'short',year:'numeric'})+'</b> · '+M[i][1]+' · in <b>'+days+' day'+(days>1?'s':'')+'</b>';",
    "el.innerHTML='अगला अवसर: <b>'+t.toLocaleDateString('hi-IN',{day:'numeric',month:'short',year:'numeric'})+'</b> · '+M[i][1]+' · <b>'+days+' दिन</b> शेष';")
rep("el.textContent='Electional list complete — request a fresh scan.';", "el.textContent='मुहूर्त-सूची पूर्ण — नया अन्वेषण माँगिए।';")
rep('Muhūrta calendar loading…', 'मुहूर्त पंचांग लोड हो रहा है…')

open(P, "w").write(h)
print("PART 3 done. Missing:", len(miss))
for m in miss: print("  MISS:", m)
