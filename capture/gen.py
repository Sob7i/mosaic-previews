import json,glob
SC='/private/tmp/claude-502/-Users-sobhialkhuder-Documents-sl-mosaic/8c30d7b0-69ae-4fdb-a690-dbcd7ea10d98/scratchpad/'
prods={}
img={}
for f in glob.glob(SC+'d*.json'):
    d=json.load(open(f))['data']
    prods[int(d['id'])]=d
    for i in d['images']:
        img.setdefault(i['alt'],i['url'])
main={pid:p['images'][0]['url'] for pid,p in prods.items()}
CAT={'أقراط':'https://demostore.salla.sa/ar/dev-hrq7gohnsja6gl31/أقراط/c626114650','أساور':'https://demostore.salla.sa/ar/dev-hrq7gohnsja6gl31/أساور/c1051355815','أطقم':'https://demostore.salla.sa/ar/dev-hrq7gohnsja6gl31/أطقم/c1408038316','هدايا':'https://demostore.salla.sa/ar/dev-hrq7gohnsja6gl31/هدايا/c768152749'}
SUB='https://demostore.salla.sa/ar/dev-hrq7gohnsja6gl31/'
OFFERS='https://demostore.salla.sa/ar/dev-hrq7gohnsja6gl31/offers'
P=lambda *ids:[{"id":i} for i in ids]
BEAD,PEARL,STAR,TRIO,GOLD,STACK,ROPE,SETPEARL,LETTER,BOX,ANKLET,SET2,STUDS=1574163241,1124789025,2073915173,174479149,555476573,1089641783,141433139,1427852357,765502520,514474840,693177979,2067672388,1463732060
wrist=img['home piece of week wrist']; hands=img['home popup gift hands']
L=[]
def add(n,fields): L.append({"id":"pv-"+n,"path":"home.mosaic-"+n,"fields":fields})
add('grid',{"eyebrow":"وصل حديثاً","title":"حلق جديد\nكل أسبوع","text":"أقراط وأساور للاستخدام اليومي، بأسعار تبدأ من 49 ر.س.","button_text":"المجموعة الجديدة","link":CAT['أقراط'],"tiles":[
 {"tiles.style":"photo","tiles.image":main[PEARL],"tiles.label":"أقراط","tiles.link":CAT['أقراط']},
 {"tiles.style":"lime","tiles.label":"أساور","tiles.link":CAT['أساور']},
 {"tiles.style":"photo","tiles.image":main[BEAD],"tiles.caption":"سوار خرز ملوّن · 65 ر.س","tiles.link":"/ar"},
 {"tiles.style":"ink","tiles.kicker":"كل شيء","tiles.label":"أقل من","tiles.accent":"99 ر.س","tiles.link":OFFERS},
 {"tiles.style":"photo","tiles.image":main[STACK],"tiles.caption":"أطقم","tiles.link":CAT['أطقم']}]})
add('fan',{"autoplay":False,"eyebrow":"مختارات الأسبوع","title":"قطع يحبها الجميع","products":P(BEAD,PEARL,STUDS,GOLD,STACK)})
add('ticker',{"words":[{"words.text":w} for w in ["أقراط","أساور","أطقم","هدايا","لؤلؤ","خرز"]],"speed":"normal","scheme":"4"})
add('finder',{"eyebrow":"مساعد التسوق","title":"اختيار القطعة المناسبة في دقيقة","lead":"ثلاثة أسئلة سريعة، ثم ثلاث قطع تناسب النوع والأسلوب والميزانية.",
 "q1_title":"ما نوع القطعة؟","q1_options":[{"q1_options.label":k,"q1_options.link":CAT[k]} for k in ["أقراط","أساور","أطقم","هدايا"]],
 "q2_title":"ما الشكل المفضل؟","q2_options":[{"q2_options.label":k,"q2_options.link":SUB+u} for k,u in [("حلق دائري","حلق-دائري/c2000613211"),("حلق متدلٍّ","حلق-متدلٍّ/c1092292004"),("أساور خرز","أساور-خرز/c849006267"),("أساور سلسلة","أساور-سلسلة/c141592992")]],
 "q3_title":"ما الميزانية؟","q3_options":[{"q3_options.label":"أقل من 99 ر.س","q3_options.min_price":0,"q3_options.max_price":99},{"q3_options.label":"99 – 149 ر.س","q3_options.min_price":99,"q3_options.max_price":149},{"q3_options.label":"أكثر من 149 ر.س","q3_options.min_price":149,"q3_options.max_price":0}],"scheme":"2"})
add('offer',{"eyebrow":"عرض محدود","title":"طقم اللؤلؤ الكامل","details":"عقد وأقراط وسوار من اللؤلؤ في علبة واحدة.","ends_at":"2026-12-31 23:59","link":CAT['أطقم'],"button_text":"عرض الطقم","image":main[SETPEARL],"scheme":"3"})
add('flash-offers',{"eyebrow":"عروض تنتهي قريباً","title":"تخفيضات\nنهاية الأسبوع","limit":4,"display_all_url":OFFERS,"scheme":"3"})
add('collection',{"image":wrist,"eyebrow":"قطعة الأسبوع","title":"مختارات الأساور","link":CAT['أساور'],"featured_product":[STACK],"products":[BEAD,GOLD,ROPE,LETTER],"scheme":"1"})
add('faq',{"title":"أسئلة شائعة","show_whatsapp":True,"items":[
 {"items.question":"كيف يُعرف مقاس السوار؟","items.answer":"يُقاس محيط المعصم بشريط قياس أو بخيط، ثم يُقارن بدليل الطول في صفحة المنتج."},
 {"items.question":"هل يمكن الاستبدال أو الإرجاع؟","items.answer":"تُراجع سياسة الاستبدال والإرجاع في صفحة السياسات قبل إتمام الطلب."},
 {"items.question":"هل يتوفر تغليف للهدايا؟","items.answer":"يتوفر خيار التغليف كهدية عند إتمام الطلب من السلة."},
 {"items.question":"ما طرق الدفع المتاحة؟","items.answer":"تظهر طرق الدفع المفعلة في المتجر عند إتمام الطلب."}],"scheme":"1"})
add('gift-set',{"title":"تكوين طقم هدية","offer_text":"خصم خاص عند إضافة القطعتين","step_1_title":"الأقراط","step_1_products":P(PEARL,STAR,TRIO),"step_2_title":"الأساور","step_2_products":P(BEAD,GOLD,ROPE),"scheme":"1"})
add('notes',{"title":"تسوق الإطلالة","image":wrist,"layers":[{"layers.x":58,"layers.y":30,"layers.product":[STACK]},{"layers.x":35,"layers.y":58,"layers.product":[BEAD]},{"layers.x":50,"layers.y":75,"layers.product":[GOLD]}],"scheme":"1"})
add('blog',{"title":"من المدونة","limit":3,"show_all":True,"scheme":"1"})
add('video',{"youtube_id":"jNQXAC9IVRw","title":"تنسيق ثلاثة أساور معاً","cover":img['hover b3 coffee cup hand'],"scheme":"6"})
add('compare',{"layout":"boxed","before_image":img['product b3 wrist stack'],"after_image":img['landing set three bracelets'],"before_label":"قبل","after_label":"بعد","start":50,"eyebrow":"مقارنة","title":"قطعة واحدة وإطلالة مختلفة","text":"سحب المؤشر يكشف الفرق بين الصورتين.","button_text":"عرض المجموعة","link":CAT['أساور'],"scheme":"1"})
add('slideshow',{"autoplay":False,"interval":6,"slides":[
 {"slides.image":img['landing set three bracelets'],"slides.eyebrow":"أساور","slides.title":"أساور تُلبس معاً","slides.text":"ثلاث قطع بأسلوب واحد","slides.button_text":"عرض الأساور","slides.link":CAT['أساور'],"slides.position":"start"},
 {"slides.image":img['landing set pearl lime'],"slides.eyebrow":"أطقم","slides.title":"طقم اللؤلؤ","slides.text":"قطع متناسقة جاهزة للإهداء","slides.button_text":"عرض الأطقم","slides.link":CAT['أطقم'],"slides.position":"start"}],"scheme":"6"})
add('shorts',{"title":"مقاطع قصيرة","subtitle":"قطع من المتجر على اليد والأذن","clips":[{"clips.video":v,"clips.cover":img[c],"clips.product":"/ar/x/p"+str(pid)} for v,c,pid in [("https://www.youtube.com/shorts/jNQXAC9IVRw",'hover b4 rope on wrist',ROPE),("https://www.youtube.com/shorts/dQw4w9WgXcQ",'hover e4 three earrings on ear',TRIO),("https://www.youtube.com/shorts/9bZkp7q19f0",'hover b1 bead on wrist',BEAD),("https://www.youtube.com/shorts/kJQP7kiw5Fk",'hover b11 anklet with sandal',ANKLET)]],"scheme":"1"})
add('newsletter',{"title":"النشرة البريدية","text":"أحدث القطع والعروض تصل إلى بريدك.","button_label":"اشتراك","use_whatsapp":False,"url":SUB,"scheme":"4"})
add('promo',{"enabled":True,"image":hands,"badge":"خصم","title":"خصم 10% على الطلب","text":"يُطبَّق الكود عند إتمام الطلب.","code":"LAMAA10","delay_seconds":1,"use_whatsapp":False})
add('campaign-hero',{"eyebrow":"حملة","title":"أطقم الهدايا","description":"أطقم أساور وأقراط جاهزة للإهداء.","image":img['landing campaign'] if 'landing campaign' in img else img['landing set two wrists'],"badge":"جديد","ends_at":"2026-12-31 23:59","cta_text":"عرض الأطقم","campaign_title":"أطقم الهدايا"})
add('campaign-benefits',{"benefits":[{"benefits.text":t} for t in ["تغليف هدية","قطع مطلية","شحن لجميع المدن","دفع آمن"]]})
add('campaign-sets',{"sets_title":"الأطقم","sets_note":"مجموعات جاهزة","sets":P(STACK,SETPEARL,SET2,TRIO)})
add('campaign-steps',{"steps_title":"ثلاث خطوات","steps":[{"steps.title":"اختيار الطقم","steps.text":"يُختار الطقم المناسب من المجموعات."},{"steps.title":"إتمام الطلب","steps.text":"تُضاف القطعة إلى السلة ويُكمل الطلب."},{"steps.title":"الاستلام","steps.text":"يصل الطلب مغلفاً وجاهزاً للإهداء."}]})
add('campaign-reviews',{"reviews_title":"آراء العملاء","reviews":[{"reviews.name":n,"reviews.stars":5,"reviews.text":t,"reviews.set":"/ar/x/p"+str(pid)} for n,t,pid in [("عميل","قطع أنيقة وتغليف جميل.",STACK),("عميلة","اللؤلؤ بجودة جيدة.",SETPEARL),("عميل","وصل الطلب كما هو مطلوب.",SET2)]]})
add('campaign-faq',{"faq_title":"أسئلة الحملة","faq":[{"faq.question":"هل التغليف متوفر؟","faq.answer":"يتوفر التغليف كهدية عند إتمام الطلب."},{"faq.question":"كيف يتم الدفع؟","faq.answer":"تظهر طرق الدفع المفعلة عند إتمام الطلب."}]})
add('campaign-closing',{"closing_title":"هدية جاهزة في علبة واحدة","closing_text":"أطقم مختارة بعناية للإهداء.","cta_text":"عرض الأطقم","payments_note":"مدى · Apple Pay · تابي · تمارا"})
json.dump({"enabled":True,"settings":[],"layout":L},open('/Users/sobhialkhuder/Documents/sl/mosaic-pictures/twilight.preview.json','w'),ensure_ascii=False,indent=1)
print(len(L), sorted(img))
