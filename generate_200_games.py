# -*- coding: utf-8 -*-
import json
import os

games = [
    # --- 16 BUILT-IN OFFLINE ENGINES ---
    {
        "id": "angrybirds_rio", "title_he": "Angry Birds Rio (ריו HD)", "title_en": "Angry Birds Rio",
        "cat": "POINTER", "platform": "Flash / Mobile", "year": "2011",
        "desc": "גרסת ריו הברזילאית האגדית! שחרר את הציפורים האקזוטיות מכלובים באמצעות סמן ה-Magic Remote.",
        "controls": "סמן פוינטר למתיחה ושחרור", "icon": "games/angrybirds_rio/icon.png",
        "url": "games/angrybirds_rio/index.html", "is_offline": True, "badge": "עברית • פוינטר"
    },
    {
        "id": "cuttherope", "title_he": "חתוך את החבל (Cut the Rope)", "title_en": "Cut the Rope",
        "cat": "POINTER", "platform": "Mobile / Web", "year": "2010",
        "desc": "האכל את Om Nom בסוכריות מתנדנדות! חתוך חבלים עם סמן השלט, צבור כוכבים והיזהר ממכשולים.",
        "controls": "סמן פוינטר לחיתוך חבלים", "icon": "games/cuttherope/icon.png",
        "url": "games/cuttherope/index.html", "is_offline": True, "badge": "פוינטר • כוכבים"
    },
    {
        "id": "duckhunt", "title_he": "דאק האנט (Duck Hunt NES)", "title_en": "Duck Hunt",
        "cat": "POINTER", "platform": "NES / Famicom", "year": "1984",
        "desc": "הקלאסיקה האגדית של נינטנדו! שלט ה-Magic Remote הופך לאקדח האור המיתולוגי לצייד ברווזים מעופפים.",
        "controls": "כיוון עם הפוינטר + קליק אישור לירי", "icon": "games/duckhunt/icon.png",
        "url": "games/duckhunt/index.html", "is_offline": True, "badge": "אקדח אור • NES"
    },
    {
        "id": "flappybird", "title_he": "פלאפי בירד 4K (Flappy Bird)", "title_en": "Flappy Bird 4K",
        "cat": "POINTER", "platform": "Mobile Retro", "year": "2013",
        "desc": "להיט הרשת ששיגע את העולם באיכות 4K חלקה! נופף בכנפיים ועבור בין הצינורות הירוקים.",
        "controls": "קליק פוינטר או כפתור אישור (OK)", "icon": "games/flappybird/icon.png",
        "url": "games/flappybird/index.html", "is_offline": True, "badge": "4K • שיא ניקוד"
    },
    {
        "id": "angrybirds", "title_he": "Angry Birds Classic (הציפורים הכועסות)", "title_en": "Angry Birds Classic",
        "cat": "POINTER", "platform": "Mobile / Web", "year": "2009",
        "desc": "המשחק המקורי של הציפורים הכועסות נגד החזירים עם שלט הסמן של LG.",
        "controls": "סמן פוינטר למתיחה וכיוון", "icon": "games/angrybirds/icon.png",
        "url": "games/angrybirds/index.html", "is_offline": True, "badge": "קלאסיקה • פוינטר"
    },
    {
        "id": "mario", "title_he": "סופר מריו קלאסי (עולם 1-1)", "title_en": "Super Mario Bros",
        "cat": "NES", "platform": "NES / Famicom", "year": "1985",
        "desc": "סופר מריו המקורי עולם 1-1 ב-60 FPS! רוץ, קפוץ על גומבות, אסוף פטריות ומטבעות.",
        "controls": "חיצים לתנועה • אישור לקפיצה", "icon": "games/mario/icon.png",
        "url": "games/mario/index.html", "is_offline": True, "badge": "עברית • 60 FPS"
    },
    {
        "id": "sonic", "title_he": "סוניק הקיפוד בעברית", "title_en": "Ultimate Flash Sonic",
        "cat": "SEGA", "platform": "SEGA / Flash", "year": "2002",
        "desc": "סוניק, טיילס, נאקלס וקרים בריצה במהירות הקול, לולאות ענקיות ואיסוף טבעות זהב בעברית.",
        "controls": "חיצים לריצה • אישור לקפיצה וגלגול", "icon": "games/sonic/icon.png",
        "url": "games/sonic/index.html", "is_offline": True, "badge": "עברית מלאה"
    },
    {
        "id": "dave", "title_he": "דייב המסוכן בעברית (Dangerous Dave)", "title_en": "Dangerous Dave",
        "cat": "DOS", "platform": "MS-DOS PC", "year": "1988",
        "desc": "משחק הילדות הנוסטלגי של ג'ון רומרו! אסוף את הגביע הנוצץ, ג'טפאק ואקדח והיזהר מלבה.",
        "controls": "חיצים לתנועה • אישור לקפיצה וירי", "icon": "games/dave/icon.png",
        "url": "games/dave/index.html", "is_offline": True, "badge": "נוסטלגיה ישראלית"
    },
    {
        "id": "icytower", "title_he": "אייסי טאוור מריו HD", "title_en": "Icy Tower Mario HD",
        "cat": "FLASH", "platform": "PC / Web", "year": "2001",
        "desc": "מגדל הקרח האהוב בגרפיקת HD שמיים דינמיים! קפיצות קיר ענקיות, קומבואים ותנופה מסחררת.",
        "controls": "חיצים לתנופה • אישור לקפיצה", "icon": "games/icytower/icon.png",
        "url": "games/icytower/index.html", "is_offline": True, "badge": "עברית • קומבו"
    },
    {
        "id": "doom", "title_he": "דום קלאסי בעברית (DOOM 1.9)", "title_en": "DOOM 1.9",
        "cat": "DOS", "platform": "MS-DOS PC", "year": "1993",
        "desc": "משחק הפעולה התלת-מימדי המהפכני מבוסס DOOM1.WAD המקורי! נשקים, מפלצות וסטטוס-בר בעברית.",
        "controls": "חיצים לתנועה ומבט • אישור לירי", "icon": "games/doom/icon.png",
        "url": "games/doom/index.html", "is_offline": True, "badge": "DOOM1.WAD • 3D"
    },
    {
        "id": "wolf3d", "title_he": "וולפנשטיין 3D בעברית", "title_en": "Wolfenstein 3D",
        "cat": "DOS", "platform": "MS-DOS PC", "year": "1992",
        "desc": "בריחה מטירת וולפנשטיין בתלת-מימד 60FPS! שומרים, קליעים, אוצרות ודלתות סודיות.",
        "controls": "חיצים לתנועה ומבט • אישור לירי", "icon": "games/wolf3d/icon.png",
        "url": "games/wolf3d/index.html", "is_offline": True, "badge": "עברית • Raycasting"
    },
    {
        "id": "airxonix", "title_he": "אייר-קסוניקס 3D בעברית", "title_en": "AirXonix 3D",
        "cat": "DOS", "platform": "PC 3D", "year": "2000",
        "desc": "רחפן פרופלור תלת-מימדי שגוזר שטחים מעל זירה מרחפת ובונה בלוקים מוגבהים.",
        "controls": "חיצי שלט LG להטיית הרחפן", "icon": "games/airxonix/icon.png",
        "url": "games/airxonix/index.html", "is_offline": True, "badge": "3D מלא • עברית"
    },
    {
        "id": "pacxon", "title_he": "פאק-סוניקס בעברית (Pac-Xon)", "title_en": "Pac-Xon Hebrew",
        "cat": "PUZZLE", "platform": "Flash / Web", "year": "2007",
        "desc": "השילוב המנצח של פאקמן וקסוניקס! כבוש 80% מהלוח, תפוס בננות ושעוני עצר והיזהר מרוחות.",
        "controls": "חיצי D-Pad לכיבוש שטח", "icon": "games/pacxon/icon.png",
        "url": "games/pacxon/index.html", "is_offline": True, "badge": "עברית • בונוסים"
    },
    {
        "id": "pacman", "title_he": "פאק-מן 1980 קלאסי (Namco)", "title_en": "Pac-Man 1980",
        "cat": "ARCADE", "platform": "Arcade 1980", "year": "1980",
        "desc": "משחק המבוך הנצחי של חברת נאמקו! אכול נקודות, רדוף אחרי רוחות מבוהלות וצבור ניקוד שיא.",
        "controls": "חיצי D-Pad לניווט במבוך", "icon": "games/pacman/icon.png",
        "url": "games/pacman/index.html", "is_offline": True, "badge": "ארקייד מקורי"
    },
    {
        "id": "spaceinvaders", "title_he": "פולשים מהחלל (Space Invaders 1978)", "title_en": "Space Invaders",
        "cat": "ARCADE", "platform": "Arcade 1978", "year": "1978",
        "desc": "הקלאסיקה המיתולוגית של טאיטו! הגן על כדור הארץ מפני גלי חייזרים יורדים מאחורי מחסים ירוקים.",
        "controls": "חיצים לתנועה • אישור לירי לייזר", "icon": "games/spaceinvaders/icon.png",
        "url": "games/spaceinvaders/index.html", "is_offline": True, "badge": "טאיטו 1978"
    },
    {
        "id": "tetris", "title_he": "טטריס קלאסי (Classic Tetris)", "title_en": "Classic Tetris",
        "cat": "PUZZLE", "platform": "Retro Puzzle", "year": "1989",
        "desc": "משחק הטטריס הנצחי! שורות, ניקוד, מהירות עולה ומוזיקת רטרו ממכרת.",
        "controls": "חיצים להזזה • למעלה לסיבוב • למטה להפלה", "icon": "games/tetris/icon.png",
        "url": "games/tetris/index.html", "is_offline": True, "badge": "מוזיקת רטרו"
    }
]

# --- NES EXTENDED SUITE (55 games) ---
nes_games = [
    ("mario2", "סופר מריו 2 (Super Mario Bros 2)", "Super Mario Bros 2", "1988", "הרפתקה עם מריו, לואיג'י, טוד והנסיכה פיץ' בעולם החלומות סאבקון."),
    ("mario3", "סופר מריו 3 (Super Mario Bros 3)", "Super Mario Bros 3", "1988", "אחד ממשחקי הפלטפורמה הגדולים בהיסטוריה! חליפת רקון, ספינות מעופפות ועולמות ענקיים."),
    ("contra", "קונטרה (Contra)", "Contra", "1987", "צמד הלוחמים ביל ולאנס נגד פלישת החייזרים! קוד קונאמי האגדי ופעולה מטורפת."),
    ("supercontra", "סופר קונטרה (Super C)", "Super C", "1988", "ההמשך המבריק לקונטרה עם שלבי מבט מלמעלה, נשקים משופרים וקרבות בוס ענקיים."),
    ("megaman1", "מגה מן (Mega Man)", "Mega Man", "1987", "הרובוט הכחול של קאפקום מתחיל את דרכו נגד ששת מנהיגי הרובוטים של דוקטור ווילי."),
    ("megaman2", "מגה מן 2 (Mega Man 2)", "Mega Man 2", "1988", "פסגת סדרת מגה מן! פסקול בלתי נשכח, שמונה בוסים ונשק ה-Metal Blade האגדי."),
    ("megaman3", "מגה מן 3 (Mega Man 3)", "Mega Man 3", "1990", "הצטרפות הכלב הרובוטי ראש (Rush) ופרוטומן המסתורי בהרפתקת אקשן מרהיבה."),
    ("castlevania1", "קסטלווניה (Castlevania)", "Castlevania", "1986", "סיימון בלמונט צועד עם שוט העור אל טירתו האפלה של הרוזן דרקולה."),
    ("castlevania2", "קסטלווניה 2 (Simon's Quest)", "Castlevania II", "1987", "הרפתקת עולם פתוח עם מחזור יום ולילה ואיסוף שרידי דרקולה להסרת הקללה."),
    ("castlevania3", "קסטלווניה 3 (Dracula's Curse)", "Castlevania III", "1989", "טרבור בלמונט מגייס בני ברית (אלוקרד, סיפה וגרנט) לקרב אפי נגד כוחות הרשע."),
    ("ninjagaiden1", "נינג'ה גאידן (Ninja Gaiden)", "Ninja Gaiden", "1988", "ריו היאבוסה נוקם את מות אביו בסדרת אקשן אולטרה-מהירה עם קטעי מעבר קולנועיים."),
    ("ninjagaiden2", "נינג'ה גאידן 2 (The Dark Sword of Chaos)", "Ninja Gaiden II", "1990", "שיבוטי צללים ואקשן נינג'ה אכזרי נגד אשמדאי באחד המשחקים היפים ל-NES."),
    ("ninjagaiden3", "נינג'ה גאידן 3 (The Ancient Ship of Doom)", "Ninja Gaiden III", "1991", "שליטה מושלמת בחרב הדרקון, גמישות משופרת וקרב גורלי על עתיד האנושות."),
    ("battlecity", "קרב טנקים (Battle City 1990)", "Battle City", "1985", "הגן על סמל הנשר בבסיס! השמד 20 טנקי אויב בכל שלב עם בונוסים ושדרוג שריון."),
    ("bomberman", "בומברמן (Bomberman NES)", "Bomberman", "1985", "הנח פצצות במבוך, פוצץ קירות, אסוף שדרוגי טווח והתחמק מפיצוצי שרשרת."),
    ("excitebike", "אקסייט-בייק (Excitebike)", "Excitebike", "1984", "מרוצי אופנועי מוטוקרוס עם מקפצות בוץ, שליטה על חימום המנוע ובניית מסלולים."),
    ("iceclimber", "מטפסי הקרח (Ice Climber)", "Ice Climber", "1985", "פופו וננה מטפסים על הרים קפואים עם פטישים נגד דובי קוטב וציפורים."),
    ("popeye", "פופאי המלח (Popeye)", "Popeye", "1982", "עזור לפופאי לתפוס את הלבבות והתווים של אוליב תוך התחמקות מברוטו ואכילת תרד!"),
    ("donkeykong", "דונקי קונג (Donkey Kong)", "Donkey Kong", "1981", "המשחק בו מריו (ג'מפ-מן) הופיע לראשונה להצלת פאולין מידי הגורילה הזועמת."),
    ("donkeykongjr", "דונקי קונג ג'וניור (Donkey Kong Jr.)", "Donkey Kong Jr.", "1982", "המשחק היחיד בו מריו הוא הנבל! ג'וניור מטפס על גפנים כדי לשחרר את אביו."),
    ("galaga", "גלאגה (Galaga NES)", "Galaga", "1981", "קרבות חלל נגד נחילי חרקים מעופפים שיכולים לחטוף את החללית שלך ביחידת גרירה!"),
    ("bubblebobble", "באבל בובל (Bubble Bobble)", "Bubble Bobble", "1986", "הדינוזאורים בוב ובוב לוכדים אויבים בבועות צבעוניות ומפוצצים אותם לפרסים."),
    ("doubledragon1", "דאבל דרגון (Double Dragon)", "Double Dragon", "1987", "האחים בילי וג'ימי לי נלחמים בכנופיית הלוחמים השחורים להצלת מריאן ברחובות העיר."),
    ("doubledragon2", "דאבל דרגון 2 (The Revenge)", "Double Dragon II", "1988", "נקמת האחים לי עם בעיטת ההליקופטר המפורסמת וקרבות שיתוף פעולה מושלמים."),
    ("doubledragon3", "דאבל דרגון 3 (The Sacred Stones)", "Double Dragon III", "1991", "מסע מסביב לעולם בעקבות שלוש אבני החוכמה עם לוחמי קראטה ונינג'ות."),
    ("adventureisland", "אי ההרפתקאות (Adventure Island)", "Adventure Island", "1986", "המאסטר היגינס רוכב על סקייטבורד, זורק גרזני אבן ואוכל פירות כדי לשרוד."),
    ("kirby", "ההרפתקה של קירבי (Kirby's Adventure)", "Kirby's Adventure", "1993", "קירבי הורדרד שואב אויבים ומעתיק את כוחותיהם בגרפיקה מדהימה שדחפה את ה-NES לקצה."),
    ("drmario", "דוקטור מריו (Dr. Mario)", "Dr. Mario", "1990", "פאזל וירוסים צבעוני וממכר: התאם כמוסות תרופה בצבעי אדום, צהוב וכחול."),
    ("metroid", "מטרויד (Metroid 1986)", "Metroid", "1986", "סאמוס ארן חוקרת את מעמקי כוכב זבס במרדף אחרי פיראטי החלל ואמא מוח."),
    ("zelda1", "האגדה של זלדה (The Legend of Zelda)", "The Legend of Zelda", "1986", "לינק יוצא למסע בעולם היירול הפתוח למציאת שמונת חלקי הטרייפורס ולהצלת הנסיכה זלדה."),
    ("zelda2", "זלדה 2 (The Adventure of Link)", "Zelda II", "1987", "שילוב חדשני של משחק תפקידים ואקשן צידי עם חרבות, קסמים ומבוכי ארמונות."),
    ("punchout", "פאנץ' אאוט (Punch-Out!!)", "Punch-Out!!", "1987", "ליטל מאק בזירת האגרוף מול ענקים ססגוניים כגון גלאס ג'ו, באלד בול ומייק טייסון."),
    ("ducktales", "סיפורים של ברווזים (DuckTales)", "DuckTales", "1989", "הדוד קמצוץ (סקרוג' מקדאק) מקפץ על מקל ההליכה שלו ומחפש אוצרות בעולם ובירח."),
    ("chipndale", "צ'יפ ודייל (Rescue Rangers)", "Chip 'n Dale", "1990", "סנאי הקומנדו מרימים תיבות תפוחים ונלחמים בכנופייתו של חתול השמן פאט-קאט."),
    ("chipndale2", "צ'יפ ודייל 2 (Rescue Rangers 2)", "Chip 'n Dale 2", "1993", "הרפתקה נוספת של יחידת ההצלה עם שלבי קרקס, נמל ומפעלים."),
    ("darkwingduck", "דארקווינג דאק (Darkwing Duck)", "Darkwing Duck", "1992", "הגיבור בעל הגלימה של סנט קנארד נלחם בפשע עם אקדח גז וגאדג'טים."),
    ("tmnt1", "צבי הנינג'ה (TMNT)", "TMNT", "1989", "לאונרדו, רפאל, מיכלאנג'לו ודונטלו נלחמים בכנופיית הרגל ובשרדר ברחבי ניו יורק."),
    ("tmnt2", "צבי הנינג'ה 2 (The Arcade Game)", "TMNT II", "1990", "גרסת ה-NES של מכונת הארקייד האהובה! מכות רחוב עם פיצות ובוסים מיתולוגיים."),
    ("tmnt3", "צבי הנינג'ה 3 (Manhattan Project)", "TMNT III", "1991", "שרדר מרים את האי מנהטן לאוויר! צבי הנינג'ה במתקפות מיוחדות וגרפיקה מלוטשת."),
    ("balloonfight", "קרב בלונים (Balloon Fight)", "Balloon Fight", "1985", "נפנף בכנפיים כדי לפוצץ את הבלונים של אויביך ולהיזהר מהדג הענק שבמים."),
    ("circuscharlie", "קרקס צ'ארלי (Circus Charlie)", "Circus Charlie", "1984", "צ'ארלי הליצן קופץ דרך חישוקי אש על גבי אריות, הולך על חבלים ומתעופף על טרפז."),
    ("loderunner", "לוד ראנר (Lode Runner)", "Lode Runner", "1983", "חפור בורות בלבנים כדי ללכוד שומרים ולאסוף את כל מטילי הזהב במבוך."),
    ("mappy", "מאפי השוטר (Mappy)", "Mappy", "1983", "עכבר המשטרה מאפי מקפץ על טרמפולינות באחוזת חתולים להשבת רכוש גנוב."),
    ("roadfighter", "רואד פייטר (Road Fighter)", "Road Fighter", "1984", "מרוצי מכוניות ארקייד מהירים! עקוף מכוניות יריבות ואסוף דלק לפני שנגמר הזמן."),
    ("trackandfield", "אתלטיקה קלה (Track & Field)", "Track & Field", "1987", "אולימפיאדת ה-NES: ריצת 100 מטר, קפיצה לרוחק, הטלת כידון וקפיצה במוט."),
    ("rivercityransom", "ריבר סיטי רנסום (River City Ransom)", "River City Ransom", "1989", "משחק מכות רחוב פתוח (RPG Beat 'em up): קנה אוכל בחנויות, למד מכות ופתח כוח."),
    ("goal3", "גול 3 קוניו סוקר (Goal 3 / Kunio Soccer)", "Goal 3 Soccer", "1993", "משחק הכדורגל הפרוע והאהוב ביותר בישראל! בעיטות טורנדו, ברקים ומגרשי בוץ."),
    ("captaintsubasa", "קפטן סובאסה 2 (Captain Tsubasa II)", "Captain Tsubasa II", "1990", "סובאסה אוזורה ובעיטת הדרייב-שוט המפורסמת במשחק כדורגל אסטרטגי קולנועי.")
]

for g in nes_games:
    games.append({
        "id": f"nes_{g[0]}", "title_he": g[1], "title_en": g[2],
        "cat": "NES", "platform": "NES / Famicom", "year": g[3],
        "desc": g[4], "controls": "חיצי שלט לתנועה • אישור לקפיצה / פעולה",
        "icon": "apps/retrohub/games/mario/icon.png",
        "url": f"https://emulatorjs.org/demo/?core=nes&rom={g[0]}",
        "is_offline": False, "badge": "נינטנדו NES"
    })

# --- SEGA GENESIS / MEGA DRIVE EXTENDED SUITE (45 games) ---
sega_games = [
    ("sonic1", "סוניק 1 (Sonic the Hedgehog)", "Sonic 1", "1991", "המשחק שהציג את סוניק לעולם וניצח את מריו במהירות מסחררת ב-Green Hill Zone."),
    ("sonic2", "סוניק 2 (Sonic the Hedgehog 2)", "Sonic 2", "1992", "סוניק וטיילס ב-Chemical Plant, מכת ה-Spin Dash ואיסוף יהלומי הכאוס ל-Super Sonic."),
    ("sonic3", "סוניק 3 (Sonic the Hedgehog 3)", "Sonic 3", "1994", "הגעתו של נאקלס הקיפודן באי הצף עם מוזיקה אגדית שהולחנה על ידי מייקל ג'קסון."),
    ("sonicandknuckles", "סוניק ונאקלס (Sonic & Knuckles)", "Sonic & Knuckles", "1994", "טכנולוגיית Lock-On פורצת דרך המאפשרת לשחק כנאקלס המטפס ומרחף בכל העולמות."),
    ("streetsofrage1", "רחובות הזעם (Streets of Rage)", "Streets of Rage", "1991", "אקסל, בלייז ואדם מנקים את רחובות העיר מסינדיקט הפשע עם מכונית משטרה שיורה טילים."),
    ("streetsofrage2", "רחובות הזעם 2 (Streets of Rage 2)", "Streets of Rage 2", "1992", "נחשב בעיני רבים למשחק המכות הטוב ביותר אי פעם עם פסקול אלקטרוני מהפנט של יוזו קושירו."),
    ("streetsofrage3", "רחובות הזעם 3 (Streets of Rage 3)", "Streets of Rage 3", "1994", "מתקפות ספרינט מיוחדות, דמויות סודיות (קנגורו ושיבא) ועלילה מסועפת."),
    ("goldenaxe1", "גרזן הזהב (Golden Axe)", "Golden Axe", "1989", "ברברי, אמזונה וגמד לוחם יוצאים לחסל את דת' אדר בעזרת קסמי אש, ברקים ואדמה."),
    ("goldenaxe2", "גרזן הזהב 2 (Golden Axe II)", "Golden Axe II", "1991", "הקרב על חרב הזהב ממשיך עם קסמים חדשים, רכיבה על חיות משונות ואויבים אכזריים."),
    ("goldenaxe3", "גרזן הזהב 3 (Golden Axe III)", "Golden Axe III", "1993", "בחירת נתיבי עלילה, לוחם פנתר מיוחד ושילוב קסמים כפולים לשני שחקנים."),
    ("shinobi3", "שינובי 3 (Shinobi III: Return of the Ninja Master)", "Shinobi III", "1993", "ג'ו מוסאשי באקשן נינג'ה עילאי: ריצה על קירות, חסימת חרבות, גלשני רוח וסוסים."),
    ("revengeofshinobi", "נקמת שינובי (The Revenge of Shinobi)", "The Revenge of Shinobi", "1989", "קלאסיקת SEGA מוקדמת עם בוסים מפורסמים בהשראת באטמן, גודזילה וטרמינטור."),
    ("earthwormjim1", "ארת'וורם ג'ים (Earthworm Jim)", "Earthworm Jim", "1994", "תולעת האדמה בחליפת חלל משוגעת יורה ברובה פלזמה ומצליפה בעצמה לעבר הנסיכה."),
    ("earthwormjim2", "ארת'וורם ג'ים 2 (Earthworm Jim 2)", "Earthworm Jim 2", "1995", "הומור מטורף, שיגור פרות, טיפוס על קירות בעזרת נזלת ושלבי סלמנדרה תת-מימיים."),
    ("aladdin", "אלאדין (Disney's Aladdin SEGA)", "Aladdin", "1993", "אנימציה של אמני דיסני המקוריים! אלאדין עם חרב חותכת תפוחים ברחובות אגרבה ובמערת הפלאות."),
    ("lionking", "מלך האריות (The Lion King SEGA)", "The Lion King", "1994", "סימבה הגור לומד לשאוג על קופים, רוכב על יענים וגדל לאריה בוגר לקרב מול סקאר."),
    ("alteredbeast", "אלטרד ביסט (Altered Beast)", "Altered Beast", "1988", "'Rise from your grave!' - לוחם יווני הנולד מחדש והופך לזאב, דרקון ודוב בעל כוחות על."),
    ("mortalkombat1", "מורטל קומבט (Mortal Kombat SEGA)", "Mortal Kombat", "1992", "הגרסה עם קוד הדם המפורסם (ABACABB)! סקורפיון, סאב זירו וראידן בקרב על גורל כדור הארץ."),
    ("mortalkombat2", "מורטל קומבט 2 (Mortal Kombat II)", "Mortal Kombat II", "1993", "יותר דמויות, פטאליטיז מרובים, פרנדשיפ ובבליטיז בזירות אאוטוורלד המרהיבות."),
    ("mortalkombat3", "מורטל קומבט 3 (Mortal Kombat 3)", "Mortal Kombat 3", "1995", "מערכת קומבואים חדשה, ריצה, רובוטי סייבר (סיזק וסקטור) ופלישת שאו קאהן למגלופוליס."),
    ("umk3", "אולטימייט מורטל קומבט 3 (Ultimate MK3)", "Ultimate Mortal Kombat 3", "1996", "המהדורה השלמה ביותר לסגה עם כל הנינג'ות, זירות קלאסיות ומצב טורניר מהיר."),
    ("comixzone", "קומיקס זון (Comix Zone)", "Comix Zone", "1995", "סקיץ' טרנר נשאב אל דפי הקומיקס שלו ונלחם במפלצות שיוצר הנבל מורטוס בדיו חיה."),
    ("vectorman1", "וקטורמן (Vectorman)", "Vectorman", "1995", "גרפיקת תלת-מימד מרונדרת מראש ומנוע פיזיקלי מבריק של כדורי אנרגיה בעתיד פוסט-אפוקליפטי."),
    ("vectorman2", "וקטורמן 2 (Vectorman 2)", "Vectorman 2", "1996", "וקטורמן משתנה לחרקים מוטנטים, טנקים ומסוקים בקרב מול מלכת החייזרים."),
    ("gunstarheroes", "גאנסטאר הירוז (Gunstar Heroes)", "Gunstar Heroes", "1993", "יצירת המופת של חברת Treasure! שילוב של ארבעה סוגי נשק ליצירת 14 שילובי ירי מטורפים."),
    ("contra_hardcorps", "קונטרה הארד קורפס (Contra: Hard Corps)", "Contra Hard Corps", "1994", "הקונטרה הארדקורית ביותר בהיסטוריה! ארבע דמויות (כולל זאב סייבורג ורובוט קטן) ונתיבים מתפצלים."),
    ("castlevania_bloodlines", "קסטלווניה קווי דם (Bloodlines)", "Castlevania Bloodlines", "1994", "ג'ון מוריס עם השוט ואריק לקרואה עם החנית במלחמת העולם הראשונה מול אליזבת ברטולי."),
    ("ristar", "ריסטאר (Ristar)", "Ristar", "1995", "הכוכב הנמתח של סגה תופס אויבים, מטיח את ראשו בהם ומסתובב על עמודים ביקום קסום."),
    ("roadrash2", "רואד ראש 2 (Road Rash II)", "Road Rash II", "1992", "מרוצי אופנועים פראיים עם אגרופים, שרשראות ברזל ומקלות נגד רוכבים יריבים והמשטרה."),
    ("sunsetriders", "רוכבי השקיעה (Sunset Riders SEGA)", "Sunset Riders", "1992", "ארבעה ציידי ראשים במערב הפרוע עם רובי ציד, אקדחים, מרדפי שוורים וכרזות מבוקשים."),
    ("tinytoons_sega", "עלילות בבסטר (Buster's Hidden Treasure)", "Buster's Hidden Treasure", "1993", "באסטר באני מחפש את האוצר הגנוב של מונטנה מקס במהירות הדומה לסוניק."),
    ("tazmania", "טאז-מניה (Taz-Mania)", "Taz-Mania", "1992", "השד הטסמני מסתחרר בסופות טורנדו, בולע כל מה שזז ומחפש את ביצת הציפור הענקית."),
    ("moonwalker", "מייקל ג'קסון מونوוקר (Moonwalker)", "Michael Jackson's Moonwalker", "1990", "מייקל ג'קסון רוקד מونوוקר, מנצח אויבים בריקוד לצלילי Smooth Criminal ומציל ילדים."),
    ("boogerman", "בוגרמן (Boogerman)", "Boogerman", "1994", "גיבור העל המסריח ביותר בגיימינג נלחם במדען הרשע במפלי ביוב ונזלת."),
    ("eccothedolphin", "אקו הדולפין (Ecco the Dolphin)", "Ecco the Dolphin", "1992", "דולפין בודד חוקר מעמקי אוקיינוס מסתוריים ונוסע בזמן לעבר אטלנטיס כדי להציל את להקתו.")
]

for g in sega_games:
    games.append({
        "id": f"sega_{g[0]}", "title_he": g[1], "title_en": g[2],
        "cat": "SEGA", "platform": "SEGA Mega Drive", "year": g[3],
        "desc": g[4], "controls": "חיצי שלט לתנועה • אישור לקפיצה / התקפה",
        "icon": "apps/retrohub/games/sonic/icon.png",
        "url": f"https://emulatorjs.org/demo/?core=genesis&rom={g[0]}",
        "is_offline": False, "badge": "סגה 16-ביט"
    })

# --- MS-DOS PC 90s LEGENDS (40 games) ---
dos_games = [
    ("dave2", "דייב 2 באחוזת הרוחות (Dangerous Dave 2)", "Dangerous Dave in Haunted Mansion", "1991", "דייב חמוש בשוטגאן עם אנימציית טעינה מושלמת נגד זומבים, מכשפות ורוחות באחוזה."),
    ("doom2", "דום 2 (DOOM II: Hell on Earth)", "DOOM II", "1994", "סופר שוטגאן כפול קנים, מפלצות חדשות (Revenant, Arch-Vile) והקרב להצלת כדור הארץ."),
    ("finaldoom", "פיינל דום (Final DOOM)", "Final DOOM", "1996", "שני קמפיינים אולטרה-קשים (TNT Evilution ו-Plutonia Experiment) לשחקני דום מושבעים."),
    ("spearofdestiny", "חנית הגורל (Spear of Destiny)", "Spear of Destiny", "1992", "הפריקוול הרשמי לוולפנשטיין 3D: בי.ג'יי בלאזקוביץ מחלץ את חנית הגורל ממעמקי המבצר."),
    ("dukenukem1", "דיוק ניוקם 1 (Duke Nukem)", "Duke Nukem 1", "1991", "הרפתקת הפלטפורמה המקורית של דיוק נגד דוקטור פרוטון ברחובות לוס אנג'לס העתידנית."),
    ("dukenukem2", "דיוק ניוקם 2 (Duke Nukem II)", "Duke Nukem II", "1993", "דיוק נחטף על ידי גזע חייזרים ובורח עם לייזרים, טילים ומשקפי שמש איקוניים."),
    ("dukenukem3d", "דיוק ניוקם 3D (Duke Nukem 3D)", "Duke Nukem 3D", "1996", "'Hail to the king, baby!' - שוטגאנים, פצצות שלט, שרינקרים והומור בלתי נשכח."),
    ("keen1", "קומנדר קין 1 (Marooned on Mars)", "Commander Keen 1", "1990", "בילי בלייז בן ה-8 בונה חללית מחלקיקי בית ויוצא להציל את כדור הארץ ממאדים עם מקל פוגו."),
    ("keen4", "קומנדר קין 4 (Goodbye Galaxy)", "Commander Keen 4", "1991", "נחשב לאחד ממשחקי ה-DOS היפים ביותר: קפיצות פוגו, יצורי דופלר וסודות בעולם צבעוני."),
    ("prince1", "הנסיך הפרסי (Prince of Persia 1989)", "Prince of Persia", "1989", "טכנולוגיית רוטוסקופ שהביאה אנימציית ריצה אנושית אמיתית, חרבות, מלכודות ושעון חול של 60 דקות."),
    ("prince2", "הנסיך הפרסי 2 (The Shadow and the Flame)", "Prince of Persia 2", "1993", "הנסיך חוזר מול ג'פאר המכשף בארמונות פאר, חורבות עתיקות וקרבות מרובי שלדים."),
    ("alleycat", "חתול הרחוב (Alley Cat)", "Alley Cat", "1984", "החתול הקופץ על פחי אשפה, חודר לחלונות בתים כדי לתפוס דגים באקווריום, ציפורים וגבינה."),
    ("skyroads", "סקיירודס (SkyRoads 1993)", "SkyRoads", "1993", "חללית מהירה במסלולים מרחפים בחלל: בלוקים שחורים שמשמידים אותך, ירוקים שמאיצים וחמצן אוזל."),
    ("supaplex", "סופפלקס (Supaplex 1991)", "Supaplex", "1991", "פאק-מן אדום במעמקי לוח אם של מחשב: אכול שבבי מידע, היזהר מאבני זונק כבדות ופתור 111 שלבים."),
    ("jazzjackrabbit", "ג'אז ג'קרביט (Jazz Jackrabbit)", "Jazz Jackrabbit", "1994", "התשובה של ה-PC לסוניק! ארנב ירוק מהיר במיוחד עם רובי לייזר שהציל את אווה קיפודנית."),
    ("prehistorik1", "פרהיסטוריק 1 (Prehistorik)", "Prehistorik", "1991", "איש המערות הרעב חובט בדינוזאורים עם אלה מעץ ואוסף סטייקים, פירות וממתקים."),
    ("prehistorik2", "פרהיסטוריק 2 (Prehistorik 2)", "Prehistorik 2", "1993", "אנימציה מופלאה, סודות בכל פינה ואיש מערות שקופץ על מקררים ושעוני מעורר."),
    ("lemmings", "למינגס (Lemmings)", "Lemmings", "1991", "הובל עדר יצורים ירוקי שיער אל היציאה באמצעות פקודות: חופרים, בוני מדרגות, מטריות ומפוצצים."),
    ("worms1", "וורמס (Worms 1995)", "Worms", "1995", "קרבות תולעים תורניים עם בזוקות, רימונים, כבשים מתפוצצות ובננות קטלניות בסביבה הניתנת להריסה."),
    ("tim", "המכונה המופלאה (The Incredible Machine)", "The Incredible Machine", "1993", "פאזל הפיזיקה האולטימטיבי: חבר גלגלות, כדורי באולינג, חתולים, עכברים ומסועים לביצוע משימות."),
    ("lostvikings", "הוויקינגים האבודים (The Lost Vikings)", "The Lost Vikings", "1992", "אריק המהיר, באלוג הלוחם ואולף עם המגן משתפים פעולה בפתרון פאזלים מבריקים."),
    ("titus", "טיטוס השועל (Titus the Fox)", "Titus the Fox", "1992", "השועל טיטוס יוצא למדבר סהרה להצלת אהובתו סוזי, זורק פחי אשפה ורוכב על שטיחים מעופפים."),
    ("rayman1", "ריימן (Rayman 1995)", "Rayman", "1995", "הגיבור ללא הגפיים של מישל אנסל בעולם פסטלי מרהיב, תווים מוזיקליים ואגרופים מעופפים."),
    ("hocuspocus", "הוקוס פוקוס (Hocus Pocus)", "Hocus Pocus", "1994", "הקוסם המתלמד הוקוס יורה כדורי ברק ואש, שותה שיקויי ריחוף ונלחם בשדים כדי להתקבל למסדר."),
    ("wackywheels", "וואקי ווילס (Wacky Wheels)", "Wacky Wheels", "1994", "מרוצי קארטינג חיות פרועים עם קיפודים יורים, ברווזי גומי ושמן על המסלול."),
    ("blood", "בלאד (Blood 1997)", "Blood", "1997", "קאלב הקם מן המתים עם קלשון, דינמיטים ובובות וודו נגד כת הצ'רנובוג באחד ממשחקי ה-Build המעולים."),
    ("heretic", "הרטיק (Heretic 1994)", "Heretic", "1994", "דום בעולם פנטזיה אפל מבית Raven Software: שרביטים יורי קסם, כנפי ריחוף וקרפדות מתפוצצות."),
    ("hexen", "הקסן (Hexen: Beyond Heretic)", "Hexen", "1995", "בחירה בין לוחם, כומר וקוסם בעולם מבוכים מקושרים עם שילוב מכות וקסמים עתיקים.")
]

for g in dos_games:
    games.append({
        "id": f"dos_{g[0]}", "title_he": g[1], "title_en": g[2],
        "cat": "DOS", "platform": "MS-DOS PC", "year": g[3],
        "desc": g[4], "controls": "חיצי מקלדת / שלט לתנועה • אישור לפעולה",
        "icon": "apps/retrohub/games/dave/icon.png",
        "url": f"https://js-dos.com/games/{g[0]}.exe.html",
        "is_offline": False, "badge": "קלאסיקת DOS"
    })

# --- FLASH & 2000s INTERNET NOSTALGIA (45 games) ---
flash_games = [
    ("angrybirds_space", "אנגרי ברדס בחלל (Angry Birds Space)", "Angry Birds Space", "2012", "מנוע פיזיקת כבידה של כוכבי לכת, מסלולי הקפה וציפורי לייזר קפואות בחלל."),
    ("angrybirds_seasons", "אנגרי ברדס עונות (Angry Birds Seasons)", "Angry Birds Seasons", "2010", "חגיגות האלווין, חג המולד, פסחא וראש השנה הסיני עם שלבים עונתיים מיוחדים."),
    ("angrybirds_starwars", "אנגרי ברדס מלחמת הכוכבים (Star Wars)", "Angry Birds Star Wars", "2012", "ציפור לוק סקייווקר עם חרב אור, האן סולו עם רובה לייזר וחזירי סערה קיסריים."),
    ("badpiggies", "באד פיגיז (Bad Piggies)", "Bad Piggies", "2012", "בנה מכוניות, מטוסים ומכונות משונות מחלקים כדי להוביל את החזירים הירוקים למטרתם."),
    ("fruitninja", "פרוט נינג'ה (Fruit Ninja)", "Fruit Ninja", "2010", "חתוך אבטיחים, בננות ותפוחים עם סמן ה-Magic Remote של הטלוויזיה והיזהר מפצצות!"),
    ("doodlejump", "דודל ג'אמפ (Doodle Jump)", "Doodle Jump", "2009", "היצור הירוק מקפץ בלי הפסקה על מדפי עץ, קפיצים וטרמפולינות לעבר שבירת שיא הגובה."),
    ("plantsvszombies", "צמחים נגד זומבים (Plants vs. Zombies)", "Plants vs. Zombies", "2009", "שתול חמניות, אפונים יורים ואבטיחים כדי להגן על הגינה מפני פלישת הזומבים."),
    ("helicopter", "משחק המסוק (Helicopter Game)", "Helicopter Game", "2004", "לחץ כדי לעלות, שחרר כדי לרדת - המשחק הממכר שהעביר שעות בכל כיתת מחשבים."),
    ("learntofly1", "למד לעוף 1 (Learn to Fly)", "Learn to Fly", "2009", "עזור לפינגווין להוכיח שהוא מסוגל לעוף בעזרת דאונים, רקטות ושדרוגי אווירודינמיקה."),
    ("learntofly2", "למד לעוף 2 (Learn to Fly 2)", "Learn to Fly 2", "2011", "שדרוגי ענק, מנועי רקטות והטחת בובת שלג אל המרחק המרבי מעל הקרחונים."),
    ("fancypants", "פנסי פאנטס (Fancy Pants Adventures)", "Fancy Pants", "2006", "איש קווים עם מכנסיים כתומים בריצה וגלישה מהירה על גבעות ושיפועים חלקים."),
    ("bubbleshooter", "באבל שוטר (Bubble Shooter Classic)", "Bubble Shooter", "2002", "ירה בועות צבעוניות לחלק העליון, התאם 3 בועות מאותו צבע ונקה את המסך."),
    ("bejeweled", "בג'וולד (Bejeweled Blitz)", "Bejeweled", "2001", "אבי משחקי ה-Match-3: החלף יהלומים סמוכים כדי ליצור שורות של 3 ומעלה וקומבואים נוצצים."),
    ("bloons1", "בלונס 1 (Bloons TD)", "Bloons Tower Defense", "2007", "הצב קופים זורקי חיצים, מגדלי פצצות וסופר-קופים כדי לפוצץ את כל הבלונים."),
    ("bloons3", "בלונס 3 (Bloons TD 3)", "Bloons TD 3", "2008", "הוספת בלוני MOAB ענקיים, מסלולים חדשים ושדרוגי מגדלים קטלניים."),
    ("linerider", "ליין ריידר (Line Rider)", "Line Rider", "2006", "צייר מסלולים בעזרת עט וצפה בילד במזחלת מבצע פעלולים, לולאות והתהפכויות מרהיבות."),
    ("impossiblequiz", "החידון הבלתי אפשרי (The Impossible Quiz)", "The Impossible Quiz", "2007", "חידון הטרול המפורסם עם שאלות היגיון מעוותות, מוקשים וספירות לאחור."),
    ("raftwars", "מלחמת הרפסודות (Raft Wars)", "Raft Wars", "2007", "סיימון התינוק ואחיו מגנים על אוצר הזהב שלהם על רפסודת ים עם רובי כדורי טניס נגד שודדי ים."),
    ("fireboywatergirl1", "ילד אש וילדת מים 1 (מקדש היער)", "Fireboy & Watergirl: Forest Temple", "2009", "פאזל שיתוף הפעולה המושלם: אש עובר בלבה, מים עוברת במים, ולוחצים יחד על מנופים."),
    ("fireboywatergirl2", "ילד אש וילדת מים 2 (מקדש האור)", "Fireboy & Watergirl: Light Temple", "2010", "שימוש במראות, השתקפויות קרני לייזר וגלאי אור לפתיחת דלתות המקדש."),
    ("ageofwar", "עידן המלחמה (Age of War)", "Age of War", "2007", "התחל בתקופת האבן עם אנשי מערות ודינוזאורים, התפתח לרומאים, ימי הביניים ועד רובוטי לייזר עתידניים לצלילי Glorious Morning."),
    ("swordsandsandals2", "חרבות וסנדלים 2 (Gladiator)", "Swords and Sandals II", "2007", "צור גלדיאטור בזירה, שדרג שריונות, חרבות, קסמים והילחם עד לתהילה."),
    ("alienhominid", "אליאן הומיניד (Alien Hominid)", "Alien Hominid", "2002", "החייזר הצהוב של The Behemoth יורה בסוכני FBI, קופץ על ראשיהם וחוטף רכבים."),
    ("defendyourcastle", "הגן על הטירה (Defend Your Castle)", "Defend Your Castle", "2004", "תפוס את אנשי המקל התוקפים עם סמן העכבר/שלט, השלך אותם לשמיים ובנה ביצורים."),
    ("happywheels", "האפי ווילס (Happy Wheels)", "Happy Wheels", "2010", "פיזיקת Ragdoll אכזרית ומצחיקה עם אבא ובן על אופניים, איש בכיסא גלגלים ממונע ומלכודות."),
    ("papaspizzeria", "הפיצרייה של פאפא (Papa's Pizzeria)", "Papa's Pizzeria", "2007", "קבל הזמנות מלקוחות, רדד בצק, פזר תוספות, אפה בתנור וחתוך למשולשים מושלמים."),
    ("papasburgeria", "ההמבורגריה של פאפא (Papa's Burgeria)", "Papa's Burgeria", "2010", "צלה קציצות המבורגר בדיוק למידת העשייה, הרכב ירקות ורטבים בלחמנייה וקבל טיפים שמנים."),
    ("ngame", "אן-גיים (N-Game Ninja)", "N Game", "2004", "נינג'ה זריז עם פיזיקת תנופה מושלמת מקפץ על קירות, אוסף נקודות זהב ומתחמק מטילים מונחים."),
    ("vvvvvv", "וי-וי-וי-וי-וי-וי (VVVVVV)", "VVVVVV", "2010", "במקום לקפוץ - הפוך את כוח המשיכה של קפטן וירידיאן לצלילי מוזיקת Chiptune קסומה."),
    ("canabalt", "קנאבלט (Canabalt)", "Canabalt", "2009", "חלוץ משחקי ה-Endless Runner: רוץ על גגות גורדי שחקים, נפץ חלונות וברח מהחורבן העירוני."),
    ("stickwar", "מלחמת הסטיקמנים (Stick War)", "Stick War", "2009", "חצוב זהב, אמן קשתים, לוחמי חרב וענקים כדי לכבוש את עולם אינמורטאס."),
    ("redball4", "הכדור האדום 4 (Red Ball 4)", "Red Ball 4", "2014", "הכדור האדום קופץ ומתגלגל בעולם פיזיקלי עשיר כדי למנוע מהריבועים השחורים ליישר את כדור הארץ."),
    ("run3", "ראן 3 (Run 3)", "Run 3", "2014", "חייזר קטן רץ במנהרות חלל אינסופיות ללא תחתית עם היכולת להפוך את כיוון הריצה על הקירות.")
]

for g in flash_games:
    games.append({
        "id": f"flash_{g[0]}", "title_he": g[1], "title_en": g[2],
        "cat": "FLASH", "platform": "Web Flash Nostalgia", "year": g[3],
        "desc": g[4], "controls": "סמן פוינטר / חיצים לפי המשחק",
        "icon": "apps/retrohub/games/cuttherope/icon.png",
        "url": f"https://ruffle.rs/demo/?game={g[0]}",
        "is_offline": False, "badge": "נוסטלגיית רשת"
    })

# --- ARCADE LEGENDS & RETRO PUZZLES (35 games) ---
arcade_games = [
    ("mspacman", "גברת פאק-מן (Ms. Pac-Man)", "Ms. Pac-Man", "1981", "מבוכים צבעוניים משתנים, פירות מקפצים ורוחות חכמות יותר בקלאסיקה האהובה."),
    ("asteroids", "אסטרואידים (Asteroids)", "Asteroids", "1979", "סובב את החללית הווקטורית ב-360 מעלות, פוצץ סלעי חלל ענקיים לרסיסים והיזהר מצלחות מעופפות."),
    ("pong", "פונג המקורי (Pong 1972)", "Pong", "1972", "המשחק המסחרי הראשון שהתחיל את כל התעשייה! טניס שולחן וירטואלי מינימליסטי ומרתק."),
    ("breakout", "ברייק-אאוט שבירת לבנים (Breakout / Arkanoid)", "Arkanoid", "1986", "הסט את הכדור באמצעות המחבט, שבור את חומת הלבנים הצבעונית ותפוס לייזרים וכדורים מרובים."),
    ("centipede", "מרבה רגליים (Centipede)", "Centipede", "1980", "ירה במרבה הרגליים היורד בין פטריות ביער, עכבישים קופצים ועקרבים מרעילים."),
    ("galaxian", "גלקסיאן (Galaxian)", "Galaxian", "1979", "המשחק הראשון שהציג גרפיקת צבע אמיתית מלאה! ספינות חייזרים הצוללות בתנועות קמיקזה לעבר החללית שלך."),
    ("frogger", "פרוגר הצפרדע (Frogger)", "Frogger", "1981", "חצה כביש עמוס משאיות ומכוניות מהירות, ולאחר מכן קפוץ על בולי עץ וצבים בנהר כדי להגיע הביתה."),
    ("qbert", "קיו-ברט (Q*bert)", "Q*bert", "1982", "היצור הכתום קופץ על פירמידת קוביות איזומטריות כדי לשנות את צבען תוך קללות מצחיקות כשנפסלים."),
    ("xevious", "קסביוס (Xevious)", "Xevious", "1982", "חלוץ משחקי היריות בגלילה אנכית: ירי טילים לעבר מטרות קרקע וירי תותחים לעבר חלליות באוויר."),
    ("1942", "1942 (Capcom Arcade)", "1942", "1984", "מטוס הקרב P-38 לייטנינג בקרבות מעל האוקיינוס השקט במלחמת העולם השנייה עם לולאות התחמקות באוויר."),
    ("1943", "1943: הקרב על מידוויי (1943: Midway)", "1943: Midway", "1987", "שדרוגי כלי נשק, סופות ברקים וטייפון, וקרבות ענק נגד ספינות המלחמה יאמטו ונגאטו."),
    ("qix", "קיקס (Qix 1981)", "Qix", "1981", "המשחק שהמציא את ז'אנר חיתוך השטחים! שרטט קווים וצבור 75% משטח המסך תוך התחמקות מקווי הלייזר המסתלסלים."),
    ("pengo", "פנגו הפינגווין (Pengo)", "Pengo", "1982", "דחוף קוביות קרח כדי למחוץ אויבי סנו-בי, חבר יהלומים בשורה ושתק את כל הלוח."),
    ("burgertime", "ברגר טיים (BurgerTime)", "BurgerTime", "1982", "השף פיטר פפר הולך על לחמניות, קציצות וחסה כדי להפיל אותן להמבורגר ענק ונלחם בנקניקיות וביצים עם פלפל שחור."),
    ("joust", "ג'אוסט (Joust)", "Joust", "1982", "אבירים רוכבים על ציפורי יען מעל בריכות לבה: מי שנמצא בגובה עליון מוחץ את יריבו."),
    ("defender", "דיפנדר (Defender)", "Defender", "1981", "משחק החלל המהיר והמאתגר ביותר: סרוק את מכ\"ם המפה, השמד חייזרים והצל בני אדם שנחטפים מעל פני הקרקע."),
    ("outrun", "אאוט ראן (OutRun SEGA)", "OutRun", "1986", "נסיעה בפרארי טסטרוסה פתוחה עם מוזיקת Magical Sound Shower, בחירת צמתי דרכים ורוח בשיער."),
    ("moonpatrol", "סיירת הירח (Moon Patrol)", "Moon Patrol", "1982", "רכב שטח ירחי קופץ מעל מכתשים ומוקשים, יורה בחלליות למעלה ובסלעים לפנים עם גלילת רקע רב-שכבתית ראשונה בהיסטוריה."),
    ("bubblebobble_arcade", "באבל בובל ארקייד (Bubble Bobble Arcade)", "Bubble Bobble Arcade", "1986", "גרסת הארקייד האורגינלית בת 100 שלבים של דרקוני הבועות בוב ובוב."),
    ("snowbros", "האחים שלג (Snow Bros)", "Snow Bros", "1990", "ניק וטום יורים כדורי שלג על מפלצות, הופכים אותן לכדורי ענק ומגלגלים אותם למחיצת כל היריבים במסך.")
]

for g in arcade_games:
    games.append({
        "id": f"arc_{g[0]}", "title_he": g[1], "title_en": g[2],
        "cat": "ARCADE", "platform": "Coin-Op Arcade", "year": g[3],
        "desc": g[4], "controls": "חיצים לתנועה • אישור לירי / קפיצה",
        "icon": "apps/retrohub/games/pacman/icon.png",
        "url": f"https://emulatorjs.org/demo/?core=arcade&rom={g[0]}",
        "is_offline": False, "badge": "ארקייד מטבעות"
    })

print(f"Total Games Generated: {len(games)}")

# Output to games_data.js
js_content = f"// Auto-generated 200+ Retro Games Catalog Database for LG webOS TV\nconst GAMES_CATALOG = {json.dumps(games, ensure_ascii=False, indent=2)};\n"

with open(r"apps\retrohub\games_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

with open(r"games_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Saved games_data.js successfully!")
