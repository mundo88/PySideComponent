from enum import Enum
from .convert import convert,TAILWIND_COLORS,Image


class FilledIcon(Enum):
    ACCESSIBLE = 'accessible.svg'
    AD_CIRCLE = 'ad-circle.svg'
    AD = 'ad.svg'
    ADJUSTMENTS = 'adjustments.svg'
    AFFILIATE = 'affiliate.svg'
    ALARM_MINUS = 'alarm-minus.svg'
    ALARM_PLUS = 'alarm-plus.svg'
    ALARM_SNOOZE = 'alarm-snooze.svg'
    ALARM = 'alarm.svg'
    ALERT_CIRCLE = 'alert-circle.svg'
    ALERT_HEXAGON = 'alert-hexagon.svg'
    ALERT_OCTAGON = 'alert-octagon.svg'
    ALERT_SQUARE_ROUNDED = 'alert-square-rounded.svg'
    ALERT_SQUARE = 'alert-square.svg'
    ALERT_TRIANGLE = 'alert-triangle.svg'
    ALIEN = 'alien.svg'
    ALIGN_BOX_BOTTOM_CENTER = 'align-box-bottom-center.svg'
    ALIGN_BOX_BOTTOM_LEFT = 'align-box-bottom-left.svg'
    ALIGN_BOX_BOTTOM_RIGHT = 'align-box-bottom-right.svg'
    ALIGN_BOX_CENTER_MIDDLE = 'align-box-center-middle.svg'
    ALIGN_BOX_LEFT_BOTTOM = 'align-box-left-bottom.svg'
    ALIGN_BOX_LEFT_MIDDLE = 'align-box-left-middle.svg'
    ALIGN_BOX_LEFT_TOP = 'align-box-left-top.svg'
    ALIGN_BOX_RIGHT_BOTTOM = 'align-box-right-bottom.svg'
    ALIGN_BOX_RIGHT_MIDDLE = 'align-box-right-middle.svg'
    ALIGN_BOX_RIGHT_TOP = 'align-box-right-top.svg'
    ALIGN_BOX_TOP_CENTER = 'align-box-top-center.svg'
    ALIGN_BOX_TOP_LEFT = 'align-box-top-left.svg'
    ALIGN_BOX_TOP_RIGHT = 'align-box-top-right.svg'
    ANALYZE = 'analyze.svg'
    APP_WINDOW = 'app-window.svg'
    APPS = 'apps.svg'
    ARCHIVE = 'archive.svg'
    ARROW_AUTOFIT_CONTENT = 'arrow-autofit-content.svg'
    ARROW_BADGE_DOWN = 'arrow-badge-down.svg'
    ARROW_BADGE_LEFT = 'arrow-badge-left.svg'
    ARROW_BADGE_RIGHT = 'arrow-badge-right.svg'
    ARROW_BADGE_UP = 'arrow-badge-up.svg'
    ARROW_BIG_DOWN_LINE = 'arrow-big-down-line.svg'
    ARROW_BIG_DOWN_LINES = 'arrow-big-down-lines.svg'
    ARROW_BIG_DOWN = 'arrow-big-down.svg'
    ARROW_BIG_LEFT_LINE = 'arrow-big-left-line.svg'
    ARROW_BIG_LEFT_LINES = 'arrow-big-left-lines.svg'
    ARROW_BIG_LEFT = 'arrow-big-left.svg'
    ARROW_BIG_RIGHT_LINE = 'arrow-big-right-line.svg'
    ARROW_BIG_RIGHT_LINES = 'arrow-big-right-lines.svg'
    ARROW_BIG_RIGHT = 'arrow-big-right.svg'
    ARROW_BIG_UP_LINE = 'arrow-big-up-line.svg'
    ARROW_BIG_UP_LINES = 'arrow-big-up-lines.svg'
    ARROW_BIG_UP = 'arrow-big-up.svg'
    ARTBOARD = 'artboard.svg'
    ARTICLE = 'article.svg'
    ASPECT_RATIO = 'aspect-ratio.svg'
    ASSEMBLY = 'assembly.svg'
    ASSET = 'asset.svg'
    ATOM_2 = 'atom-2.svg'
    AWARD = 'award.svg'
    BABY_CARRIAGE = 'baby-carriage.svg'
    BACKSPACE = 'backspace.svg'
    BADGE_3D = 'badge-3d.svg'
    BADGE_4K = 'badge-4k.svg'
    BADGE_8K = 'badge-8k.svg'
    BADGE_AD = 'badge-ad.svg'
    BADGE_AR = 'badge-ar.svg'
    BADGE_CC = 'badge-cc.svg'
    BADGE_HD = 'badge-hd.svg'
    BADGE_SD = 'badge-sd.svg'
    BADGE_TM = 'badge-tm.svg'
    BADGE_VO = 'badge-vo.svg'
    BADGE_VR = 'badge-vr.svg'
    BADGE_WC = 'badge-wc.svg'
    BADGE = 'badge.svg'
    BADGES = 'badges.svg'
    BALLOON = 'balloon.svg'
    BALLPEN = 'ballpen.svg'
    BANDAGE = 'bandage.svg'
    BARBELL = 'barbell.svg'
    BARRIER_BLOCK = 'barrier-block.svg'
    BASKET = 'basket.svg'
    BATH = 'bath.svg'
    BATTERY_1 = 'battery-1.svg'
    BATTERY_2 = 'battery-2.svg'
    BATTERY_3 = 'battery-3.svg'
    BATTERY_4 = 'battery-4.svg'
    BATTERY = 'battery.svg'
    BED_FLAT = 'bed-flat.svg'
    BED = 'bed.svg'
    BEER = 'beer.svg'
    BELL_MINUS = 'bell-minus.svg'
    BELL_PLUS = 'bell-plus.svg'
    BELL_RINGING_2 = 'bell-ringing-2.svg'
    BELL_RINGING = 'bell-ringing.svg'
    BELL_X = 'bell-x.svg'
    BELL_Z = 'bell-z.svg'
    BELL = 'bell.svg'
    BIOHAZARD = 'biohazard.svg'
    BLADE = 'blade.svg'
    BLOB = 'blob.svg'
    BOMB = 'bomb.svg'
    BONE = 'bone.svg'
    BOOK = 'book.svg'
    BOOKMARK = 'bookmark.svg'
    BOOKMARKS = 'bookmarks.svg'
    BOOM = 'boom.svg'
    BOTTLE = 'bottle.svg'
    BOUNCE_LEFT = 'bounce-left.svg'
    BOUNCE_RIGHT = 'bounce-right.svg'
    BOW = 'bow.svg'
    BOWL_CHOPSTICKS = 'bowl-chopsticks.svg'
    BOWL_SPOON = 'bowl-spoon.svg'
    BOWL = 'bowl.svg'
    BOX_ALIGN_BOTTOM_LEFT = 'box-align-bottom-left.svg'
    BOX_ALIGN_BOTTOM_RIGHT = 'box-align-bottom-right.svg'
    BOX_ALIGN_BOTTOM = 'box-align-bottom.svg'
    BOX_ALIGN_LEFT = 'box-align-left.svg'
    BOX_ALIGN_RIGHT = 'box-align-right.svg'
    BOX_ALIGN_TOP_LEFT = 'box-align-top-left.svg'
    BOX_ALIGN_TOP_RIGHT = 'box-align-top-right.svg'
    BOX_ALIGN_TOP = 'box-align-top.svg'
    BRAND_APPLE = 'brand-apple.svg'
    BRAND_DISCORD = 'brand-discord.svg'
    BRAND_DRIBBBLE = 'brand-dribbble.svg'
    BRAND_FACEBOOK = 'brand-facebook.svg'
    BRAND_GITHUB = 'brand-github.svg'
    BRAND_GOOGLE = 'brand-google.svg'
    BRAND_PATREON = 'brand-patreon.svg'
    BRAND_PAYPAL = 'brand-paypal.svg'
    BRAND_SPOTIFY = 'brand-spotify.svg'
    BRAND_TIKTOK = 'brand-tiktok.svg'
    BRAND_TWITTER = 'brand-twitter.svg'
    BRAND_X = 'brand-x.svg'
    BRAND_YOUTUBE = 'brand-youtube.svg'
    BREAD = 'bread.svg'
    BRIEFCASE_2 = 'briefcase-2.svg'
    BRIEFCASE = 'briefcase.svg'
    BRIGHTNESS_AUTO = 'brightness-auto.svg'
    BRIGHTNESS_DOWN = 'brightness-down.svg'
    BRIGHTNESS_UP = 'brightness-up.svg'
    BRIGHTNESS = 'brightness.svg'
    BUBBLE = 'bubble.svg'
    BUG = 'bug.svg'
    BUILDING_BROADCAST_TOWER = 'building-broadcast-tower.svg'
    BULB = 'bulb.svg'
    CACTUS = 'cactus.svg'
    CALCULATOR = 'calculator.svg'
    CALENDAR = 'calendar.svg'
    CAMERA = 'camera.svg'
    CAMPFIRE = 'campfire.svg'
    CANDLE = 'candle.svg'
    CAPSULE_HORIZONTAL = 'capsule-horizontal.svg'
    CAPSULE = 'capsule.svg'
    CAPTURE = 'capture.svg'
    CARDS = 'cards.svg'
    CARET_DOWN = 'caret-down.svg'
    CARET_LEFT_RIGHT = 'caret-left-right.svg'
    CARET_LEFT = 'caret-left.svg'
    CARET_RIGHT = 'caret-right.svg'
    CARET_UP_DOWN = 'caret-up-down.svg'
    CARET_UP = 'caret-up.svg'
    CAROUSEL_HORIZONTAL = 'carousel-horizontal.svg'
    CAROUSEL_VERTICAL = 'carousel-vertical.svg'
    CASH_BANKNOTE = 'cash-banknote.svg'
    CATEGORY = 'category.svg'
    CHART_AREA_LINE = 'chart-area-line.svg'
    CHART_AREA = 'chart-area.svg'
    CHART_BUBBLE = 'chart-bubble.svg'
    CHART_CANDLE = 'chart-candle.svg'
    CHART_DONUT = 'chart-donut.svg'
    CHART_DOTS = 'chart-dots.svg'
    CHART_GRID_DOTS = 'chart-grid-dots.svg'
    CHART_PIE = 'chart-pie.svg'
    CHERRY = 'cherry.svg'
    CHESS_BISHOP = 'chess-bishop.svg'
    CHESS_KING = 'chess-king.svg'
    CHESS_KNIGHT = 'chess-knight.svg'
    CHESS_QUEEN = 'chess-queen.svg'
    CHESS_ROOK = 'chess-rook.svg'
    CHESS = 'chess.svg'
    CIRCLE_ARROW_DOWN_LEFT = 'circle-arrow-down-left.svg'
    CIRCLE_ARROW_DOWN_RIGHT = 'circle-arrow-down-right.svg'
    CIRCLE_ARROW_DOWN = 'circle-arrow-down.svg'
    CIRCLE_ARROW_LEFT = 'circle-arrow-left.svg'
    CIRCLE_ARROW_RIGHT = 'circle-arrow-right.svg'
    CIRCLE_ARROW_UP_LEFT = 'circle-arrow-up-left.svg'
    CIRCLE_ARROW_UP_RIGHT = 'circle-arrow-up-right.svg'
    CIRCLE_ARROW_UP = 'circle-arrow-up.svg'
    CIRCLE_CHECK = 'circle-check.svg'
    CIRCLE_DOT = 'circle-dot.svg'
    CIRCLE_KEY = 'circle-key.svg'
    CIRCLE_LETTER_A = 'circle-letter-a.svg'
    CIRCLE_LETTER_B = 'circle-letter-b.svg'
    CIRCLE_LETTER_C = 'circle-letter-c.svg'
    CIRCLE_LETTER_D = 'circle-letter-d.svg'
    CIRCLE_LETTER_E = 'circle-letter-e.svg'
    CIRCLE_LETTER_F = 'circle-letter-f.svg'
    CIRCLE_LETTER_G = 'circle-letter-g.svg'
    CIRCLE_LETTER_H = 'circle-letter-h.svg'
    CIRCLE_LETTER_I = 'circle-letter-i.svg'
    CIRCLE_LETTER_J = 'circle-letter-j.svg'
    CIRCLE_LETTER_K = 'circle-letter-k.svg'
    CIRCLE_LETTER_L = 'circle-letter-l.svg'
    CIRCLE_LETTER_M = 'circle-letter-m.svg'
    CIRCLE_LETTER_N = 'circle-letter-n.svg'
    CIRCLE_LETTER_O = 'circle-letter-o.svg'
    CIRCLE_LETTER_P = 'circle-letter-p.svg'
    CIRCLE_LETTER_Q = 'circle-letter-q.svg'
    CIRCLE_LETTER_R = 'circle-letter-r.svg'
    CIRCLE_LETTER_S = 'circle-letter-s.svg'
    CIRCLE_LETTER_T = 'circle-letter-t.svg'
    CIRCLE_LETTER_U = 'circle-letter-u.svg'
    CIRCLE_LETTER_V = 'circle-letter-v.svg'
    CIRCLE_LETTER_W = 'circle-letter-w.svg'
    CIRCLE_LETTER_X = 'circle-letter-x.svg'
    CIRCLE_LETTER_Y = 'circle-letter-y.svg'
    CIRCLE_LETTER_Z = 'circle-letter-z.svg'
    CIRCLE_NUMBER_0 = 'circle-number-0.svg'
    CIRCLE_NUMBER_1 = 'circle-number-1.svg'
    CIRCLE_NUMBER_2 = 'circle-number-2.svg'
    CIRCLE_NUMBER_3 = 'circle-number-3.svg'
    CIRCLE_NUMBER_4 = 'circle-number-4.svg'
    CIRCLE_NUMBER_5 = 'circle-number-5.svg'
    CIRCLE_NUMBER_6 = 'circle-number-6.svg'
    CIRCLE_NUMBER_7 = 'circle-number-7.svg'
    CIRCLE_NUMBER_8 = 'circle-number-8.svg'
    CIRCLE_NUMBER_9 = 'circle-number-9.svg'
    CIRCLE_X = 'circle-x.svg'
    CIRCLE = 'circle.svg'
    CIRCLES = 'circles.svg'
    CLOCK_HOUR_1 = 'clock-hour-1.svg'
    CLOCK_HOUR_10 = 'clock-hour-10.svg'
    CLOCK_HOUR_11 = 'clock-hour-11.svg'
    CLOCK_HOUR_12 = 'clock-hour-12.svg'
    CLOCK_HOUR_2 = 'clock-hour-2.svg'
    CLOCK_HOUR_3 = 'clock-hour-3.svg'
    CLOCK_HOUR_4 = 'clock-hour-4.svg'
    CLOCK_HOUR_5 = 'clock-hour-5.svg'
    CLOCK_HOUR_6 = 'clock-hour-6.svg'
    CLOCK_HOUR_7 = 'clock-hour-7.svg'
    CLOCK_HOUR_8 = 'clock-hour-8.svg'
    CLOCK_HOUR_9 = 'clock-hour-9.svg'
    CLOCK = 'clock.svg'
    CLOUD = 'cloud.svg'
    CLUBS = 'clubs.svg'
    COIN_BITCOIN = 'coin-bitcoin.svg'
    COIN_EURO = 'coin-euro.svg'
    COIN_MONERO = 'coin-monero.svg'
    COIN_POUND = 'coin-pound.svg'
    COIN_RUPEE = 'coin-rupee.svg'
    COIN_TAKA = 'coin-taka.svg'
    COIN_YEN = 'coin-yen.svg'
    COIN_YUAN = 'coin-yuan.svg'
    COIN = 'coin.svg'
    COMPASS = 'compass.svg'
    CONE_2 = 'cone-2.svg'
    CONE = 'cone.svg'
    CONTRAST_2 = 'contrast-2.svg'
    CONTRAST = 'contrast.svg'
    COOKIE_MAN = 'cookie-man.svg'
    COOKIE = 'cookie.svg'
    COPY_CHECK = 'copy-check.svg'
    COPY_MINUS = 'copy-minus.svg'
    COPY_PLUS = 'copy-plus.svg'
    COPY_X = 'copy-x.svg'
    COPYLEFT = 'copyleft.svg'
    COPYRIGHT = 'copyright.svg'
    CREDIT_CARD = 'credit-card.svg'
    CROP_1_1 = 'crop-1-1.svg'
    CROP_16_9 = 'crop-16-9.svg'
    CROP_3_2 = 'crop-3-2.svg'
    CROP_5_4 = 'crop-5-4.svg'
    CROP_7_5 = 'crop-7-5.svg'
    CROP_LANDSCAPE = 'crop-landscape.svg'
    CROP_PORTRAIT = 'crop-portrait.svg'
    CROSS = 'cross.svg'
    DEVICE_HEART_MONITOR = 'device-heart-monitor.svg'
    DEVICE_MOBILE = 'device-mobile.svg'
    DEVICE_TABLET = 'device-tablet.svg'
    DIALPAD = 'dialpad.svg'
    DIAMOND = 'diamond.svg'
    DIAMONDS = 'diamonds.svg'
    DICE_1 = 'dice-1.svg'
    DICE_2 = 'dice-2.svg'
    DICE_3 = 'dice-3.svg'
    DICE_4 = 'dice-4.svg'
    DICE_5 = 'dice-5.svg'
    DICE_6 = 'dice-6.svg'
    DICE = 'dice.svg'
    DIRECTION_SIGN = 'direction-sign.svg'
    DROPLET_HALF_2 = 'droplet-half-2.svg'
    DROPLET_HALF = 'droplet-half.svg'
    DROPLET = 'droplet.svg'
    EGG = 'egg.svg'
    EYE = 'eye.svg'
    FILE_X = 'file-x.svg'
    FILE = 'file.svg'
    FILTER = 'filter.svg'
    FLAG_2 = 'flag-2.svg'
    FLAG_3 = 'flag-3.svg'
    FLAG = 'flag.svg'
    FLASK_2 = 'flask-2.svg'
    FLASK = 'flask.svg'
    FOLDER = 'folder.svg'
    FORBID_2 = 'forbid-2.svg'
    FORBID = 'forbid.svg'
    FOUNTAIN = 'fountain.svg'
    FUNCTION = 'function.svg'
    GAUGE = 'gauge.svg'
    GHOST_2 = 'ghost-2.svg'
    GHOST = 'ghost.svg'
    GIFT_CARD = 'gift-card.svg'
    GIFT = 'gift.svg'
    GLASS_FULL = 'glass-full.svg'
    GLOBE = 'globe.svg'
    GPS = 'gps.svg'
    GRAPH = 'graph.svg'
    GUITAR_PICK = 'guitar-pick.svg'
    HEADPHONES = 'headphones.svg'
    HEART = 'heart.svg'
    HELP_CIRCLE = 'help-circle.svg'
    HELP_HEXAGON = 'help-hexagon.svg'
    HELP_OCTAGON = 'help-octagon.svg'
    HELP_SQUARE_ROUNDED = 'help-square-rounded.svg'
    HELP_SQUARE = 'help-square.svg'
    HELP_TRIANGLE = 'help-triangle.svg'
    HEXAGON_LETTER_A = 'hexagon-letter-a.svg'
    HEXAGON_LETTER_B = 'hexagon-letter-b.svg'
    HEXAGON_LETTER_C = 'hexagon-letter-c.svg'
    HEXAGON_LETTER_D = 'hexagon-letter-d.svg'
    HEXAGON_LETTER_E = 'hexagon-letter-e.svg'
    HEXAGON_LETTER_F = 'hexagon-letter-f.svg'
    HEXAGON_LETTER_G = 'hexagon-letter-g.svg'
    HEXAGON_LETTER_H = 'hexagon-letter-h.svg'
    HEXAGON_LETTER_I = 'hexagon-letter-i.svg'
    HEXAGON_LETTER_J = 'hexagon-letter-j.svg'
    HEXAGON_LETTER_K = 'hexagon-letter-k.svg'
    HEXAGON_LETTER_L = 'hexagon-letter-l.svg'
    HEXAGON_LETTER_M = 'hexagon-letter-m.svg'
    HEXAGON_LETTER_N = 'hexagon-letter-n.svg'
    HEXAGON_LETTER_O = 'hexagon-letter-o.svg'
    HEXAGON_LETTER_P = 'hexagon-letter-p.svg'
    HEXAGON_LETTER_Q = 'hexagon-letter-q.svg'
    HEXAGON_LETTER_R = 'hexagon-letter-r.svg'
    HEXAGON_LETTER_S = 'hexagon-letter-s.svg'
    HEXAGON_LETTER_T = 'hexagon-letter-t.svg'
    HEXAGON_LETTER_U = 'hexagon-letter-u.svg'
    HEXAGON_LETTER_V = 'hexagon-letter-v.svg'
    HEXAGON_LETTER_W = 'hexagon-letter-w.svg'
    HEXAGON_LETTER_X = 'hexagon-letter-x.svg'
    HEXAGON_LETTER_Y = 'hexagon-letter-y.svg'
    HEXAGON_LETTER_Z = 'hexagon-letter-z.svg'
    HEXAGON_MINUS = 'hexagon-minus.svg'
    HEXAGON_NUMBER_0 = 'hexagon-number-0.svg'
    HEXAGON_NUMBER_1 = 'hexagon-number-1.svg'
    HEXAGON_NUMBER_2 = 'hexagon-number-2.svg'
    HEXAGON_NUMBER_3 = 'hexagon-number-3.svg'
    HEXAGON_NUMBER_4 = 'hexagon-number-4.svg'
    HEXAGON_NUMBER_5 = 'hexagon-number-5.svg'
    HEXAGON_NUMBER_6 = 'hexagon-number-6.svg'
    HEXAGON_NUMBER_7 = 'hexagon-number-7.svg'
    HEXAGON_NUMBER_8 = 'hexagon-number-8.svg'
    HEXAGON_NUMBER_9 = 'hexagon-number-9.svg'
    HEXAGON_PLUS = 'hexagon-plus.svg'
    HEXAGON = 'hexagon.svg'
    HOME = 'home.svg'
    HOURGLASS = 'hourglass.svg'
    INFO_CIRCLE = 'info-circle.svg'
    INFO_HEXAGON = 'info-hexagon.svg'
    INFO_OCTAGON = 'info-octagon.svg'
    INFO_SQUARE_ROUNDED = 'info-square-rounded.svg'
    INFO_SQUARE = 'info-square.svg'
    INFO_TRIANGLE = 'info-triangle.svg'
    INNER_SHADOW_BOTTOM_LEFT = 'inner-shadow-bottom-left.svg'
    INNER_SHADOW_BOTTOM_RIGHT = 'inner-shadow-bottom-right.svg'
    INNER_SHADOW_BOTTOM = 'inner-shadow-bottom.svg'
    INNER_SHADOW_LEFT = 'inner-shadow-left.svg'
    INNER_SHADOW_RIGHT = 'inner-shadow-right.svg'
    INNER_SHADOW_TOP_LEFT = 'inner-shadow-top-left.svg'
    INNER_SHADOW_TOP_RIGHT = 'inner-shadow-top-right.svg'
    INNER_SHADOW_TOP = 'inner-shadow-top.svg'
    IRONING = 'ironing.svg'
    JETPACK = 'jetpack.svg'
    JEWISH_STAR = 'jewish-star.svg'
    KEY = 'key.svg'
    KEYFRAME_ALIGN_CENTER = 'keyframe-align-center.svg'
    KEYFRAME_ALIGN_HORIZONTAL = 'keyframe-align-horizontal.svg'
    KEYFRAME_ALIGN_VERTICAL = 'keyframe-align-vertical.svg'
    KEYFRAME = 'keyframe.svg'
    KEYFRAMES = 'keyframes.svg'
    LAYOUT_2 = 'layout-2.svg'
    LAYOUT_ALIGN_BOTTOM = 'layout-align-bottom.svg'
    LAYOUT_ALIGN_CENTER = 'layout-align-center.svg'
    LAYOUT_ALIGN_LEFT = 'layout-align-left.svg'
    LAYOUT_ALIGN_MIDDLE = 'layout-align-middle.svg'
    LAYOUT_ALIGN_RIGHT = 'layout-align-right.svg'
    LAYOUT_ALIGN_TOP = 'layout-align-top.svg'
    LAYOUT_BOTTOMBAR_COLLAPSE = 'layout-bottombar-collapse.svg'
    LAYOUT_BOTTOMBAR_EXPAND = 'layout-bottombar-expand.svg'
    LAYOUT_BOTTOMBAR = 'layout-bottombar.svg'
    LAYOUT_CARDS = 'layout-cards.svg'
    LAYOUT_DASHBOARD = 'layout-dashboard.svg'
    LAYOUT_DISTRIBUTE_HORIZONTAL = 'layout-distribute-horizontal.svg'
    LAYOUT_DISTRIBUTE_VERTICAL = 'layout-distribute-vertical.svg'
    LAYOUT_GRID = 'layout-grid.svg'
    LAYOUT_KANBAN = 'layout-kanban.svg'
    LAYOUT_LIST = 'layout-list.svg'
    LAYOUT_NAVBAR_COLLAPSE = 'layout-navbar-collapse.svg'
    LAYOUT_NAVBAR_EXPAND = 'layout-navbar-expand.svg'
    LAYOUT_NAVBAR = 'layout-navbar.svg'
    LAYOUT_SIDEBAR_LEFT_COLLAPSE = 'layout-sidebar-left-collapse.svg'
    LAYOUT_SIDEBAR_LEFT_EXPAND = 'layout-sidebar-left-expand.svg'
    LAYOUT_SIDEBAR_RIGHT_COLLAPSE = 'layout-sidebar-right-collapse.svg'
    LAYOUT_SIDEBAR_RIGHT_EXPAND = 'layout-sidebar-right-expand.svg'
    LAYOUT_SIDEBAR_RIGHT = 'layout-sidebar-right.svg'
    LAYOUT_SIDEBAR = 'layout-sidebar.svg'
    LAYOUT = 'layout.svg'
    LEGO = 'lego.svg'
    LOCATION = 'location.svg'
    LOCK_SQUARE_ROUNDED = 'lock-square-rounded.svg'
    LOCK = 'lock.svg'
    LUNGS = 'lungs.svg'
    MACRO = 'macro.svg'
    MAGNET = 'magnet.svg'
    MAIL_OPENED = 'mail-opened.svg'
    MAIL = 'mail.svg'
    MAN = 'man.svg'
    MANUAL_GEARBOX = 'manual-gearbox.svg'
    MAP_PIN = 'map-pin.svg'
    MEDICAL_CROSS = 'medical-cross.svg'
    MESSAGE_CIRCLE_2 = 'message-circle-2.svg'
    MICKEY = 'mickey.svg'
    MICROPHONE = 'microphone.svg'
    MICROWAVE = 'microwave.svg'
    MOOD_CONFUZED = 'mood-confuzed.svg'
    MOOD_EMPTY = 'mood-empty.svg'
    MOOD_HAPPY = 'mood-happy.svg'
    MOOD_KID = 'mood-kid.svg'
    MOOD_NEUTRAL = 'mood-neutral.svg'
    MOOD_SAD = 'mood-sad.svg'
    MOOD_SMILE = 'mood-smile.svg'
    MOON = 'moon.svg'
    MOUSE = 'mouse.svg'
    MUSHROOM = 'mushroom.svg'
    NAVIGATION = 'navigation.svg'
    OCTAGON = 'octagon.svg'
    OVAL_VERTICAL = 'oval-vertical.svg'
    OVAL = 'oval.svg'
    PAINT = 'paint.svg'
    PAW = 'paw.svg'
    PENNANT_2 = 'pennant-2.svg'
    PENNANT = 'pennant.svg'
    PENTAGON = 'pentagon.svg'
    PHONE = 'phone.svg'
    PHOTO = 'photo.svg'
    PICTURE_IN_PICTURE_TOP = 'picture-in-picture-top.svg'
    PICTURE_IN_PICTURE = 'picture-in-picture.svg'
    PIN = 'pin.svg'
    PINNED = 'pinned.svg'
    PLAYER_EJECT = 'player-eject.svg'
    PLAYER_PAUSE = 'player-pause.svg'
    PLAYER_PLAY = 'player-play.svg'
    PLAYER_RECORD = 'player-record.svg'
    PLAYER_SKIP_BACK = 'player-skip-back.svg'
    PLAYER_SKIP_FORWARD = 'player-skip-forward.svg'
    PLAYER_STOP = 'player-stop.svg'
    PLAYER_TRACK_NEXT = 'player-track-next.svg'
    PLAYER_TRACK_PREV = 'player-track-prev.svg'
    POINT = 'point.svg'
    POINTER = 'pointer.svg'
    POLAROID = 'polaroid.svg'
    PUZZLE = 'puzzle.svg'
    RADAR = 'radar.svg'
    RADIOACTIVE = 'radioactive.svg'
    RECTANGLE_VERTICAL = 'rectangle-vertical.svg'
    RECTANGLE = 'rectangle.svg'
    RELATION_MANY_TO_MANY = 'relation-many-to-many.svg'
    RELATION_ONE_TO_MANY = 'relation-one-to-many.svg'
    RELATION_ONE_TO_ONE = 'relation-one-to-one.svg'
    REPLACE = 'replace.svg'
    ROSETTE_DISCOUNT_CHECK = 'rosette-discount-check.svg'
    ROSETTE = 'rosette.svg'
    SECTION = 'section.svg'
    SETTINGS = 'settings.svg'
    SHIELD_CHECK = 'shield-check.svg'
    SHIELD_CHECKERED = 'shield-checkered.svg'
    SHIELD_HALF = 'shield-half.svg'
    SHIELD_LOCK = 'shield-lock.svg'
    SHIELD = 'shield.svg'
    SHIRT = 'shirt.svg'
    SHOPPING_CART = 'shopping-cart.svg'
    SIGN_LEFT = 'sign-left.svg'
    SIGN_RIGHT = 'sign-right.svg'
    SOUP = 'soup.svg'
    SPADE = 'spade.svg'
    SQUARE_ARROW_DOWN = 'square-arrow-down.svg'
    SQUARE_ARROW_LEFT = 'square-arrow-left.svg'
    SQUARE_ARROW_RIGHT = 'square-arrow-right.svg'
    SQUARE_ARROW_UP = 'square-arrow-up.svg'
    SQUARE_ASTERISK = 'square-asterisk.svg'
    SQUARE_CHECK = 'square-check.svg'
    SQUARE_CHEVRON_DOWN = 'square-chevron-down.svg'
    SQUARE_CHEVRON_LEFT = 'square-chevron-left.svg'
    SQUARE_CHEVRON_RIGHT = 'square-chevron-right.svg'
    SQUARE_CHEVRON_UP = 'square-chevron-up.svg'
    SQUARE_CHEVRONS_DOWN = 'square-chevrons-down.svg'
    SQUARE_CHEVRONS_LEFT = 'square-chevrons-left.svg'
    SQUARE_CHEVRONS_RIGHT = 'square-chevrons-right.svg'
    SQUARE_CHEVRONS_UP = 'square-chevrons-up.svg'
    SQUARE_DOT = 'square-dot.svg'
    SQUARE_F0 = 'square-f0.svg'
    SQUARE_F1 = 'square-f1.svg'
    SQUARE_F2 = 'square-f2.svg'
    SQUARE_F3 = 'square-f3.svg'
    SQUARE_F4 = 'square-f4.svg'
    SQUARE_F5 = 'square-f5.svg'
    SQUARE_F6 = 'square-f6.svg'
    SQUARE_F7 = 'square-f7.svg'
    SQUARE_F8 = 'square-f8.svg'
    SQUARE_F9 = 'square-f9.svg'
    SQUARE_LETTER_A = 'square-letter-a.svg'
    SQUARE_LETTER_B = 'square-letter-b.svg'
    SQUARE_LETTER_C = 'square-letter-c.svg'
    SQUARE_LETTER_D = 'square-letter-d.svg'
    SQUARE_LETTER_E = 'square-letter-e.svg'
    SQUARE_LETTER_F = 'square-letter-f.svg'
    SQUARE_LETTER_G = 'square-letter-g.svg'
    SQUARE_LETTER_H = 'square-letter-h.svg'
    SQUARE_LETTER_I = 'square-letter-i.svg'
    SQUARE_LETTER_J = 'square-letter-j.svg'
    SQUARE_LETTER_K = 'square-letter-k.svg'
    SQUARE_LETTER_L = 'square-letter-l.svg'
    SQUARE_LETTER_M = 'square-letter-m.svg'
    SQUARE_LETTER_N = 'square-letter-n.svg'
    SQUARE_LETTER_O = 'square-letter-o.svg'
    SQUARE_LETTER_P = 'square-letter-p.svg'
    SQUARE_LETTER_Q = 'square-letter-q.svg'
    SQUARE_LETTER_R = 'square-letter-r.svg'
    SQUARE_LETTER_S = 'square-letter-s.svg'
    SQUARE_LETTER_T = 'square-letter-t.svg'
    SQUARE_LETTER_U = 'square-letter-u.svg'
    SQUARE_LETTER_V = 'square-letter-v.svg'
    SQUARE_LETTER_W = 'square-letter-w.svg'
    SQUARE_LETTER_X = 'square-letter-x.svg'
    SQUARE_LETTER_Y = 'square-letter-y.svg'
    SQUARE_LETTER_Z = 'square-letter-z.svg'
    SQUARE_MINUS = 'square-minus.svg'
    SQUARE_NUMBER_0 = 'square-number-0.svg'
    SQUARE_NUMBER_1 = 'square-number-1.svg'
    SQUARE_NUMBER_2 = 'square-number-2.svg'
    SQUARE_NUMBER_3 = 'square-number-3.svg'
    SQUARE_NUMBER_4 = 'square-number-4.svg'
    SQUARE_NUMBER_5 = 'square-number-5.svg'
    SQUARE_NUMBER_6 = 'square-number-6.svg'
    SQUARE_NUMBER_7 = 'square-number-7.svg'
    SQUARE_NUMBER_8 = 'square-number-8.svg'
    SQUARE_NUMBER_9 = 'square-number-9.svg'
    SQUARE_ROTATED = 'square-rotated.svg'
    SQUARE_ROUNDED_ARROW_DOWN = 'square-rounded-arrow-down.svg'
    SQUARE_ROUNDED_ARROW_LEFT = 'square-rounded-arrow-left.svg'
    SQUARE_ROUNDED_ARROW_RIGHT = 'square-rounded-arrow-right.svg'
    SQUARE_ROUNDED_ARROW_UP = 'square-rounded-arrow-up.svg'
    SQUARE_ROUNDED_CHECK = 'square-rounded-check.svg'
    SQUARE_ROUNDED_CHEVRON_DOWN = 'square-rounded-chevron-down.svg'
    SQUARE_ROUNDED_CHEVRON_LEFT = 'square-rounded-chevron-left.svg'
    SQUARE_ROUNDED_CHEVRON_RIGHT = 'square-rounded-chevron-right.svg'
    SQUARE_ROUNDED_CHEVRON_UP = 'square-rounded-chevron-up.svg'
    SQUARE_ROUNDED_CHEVRONS_DOWN = 'square-rounded-chevrons-down.svg'
    SQUARE_ROUNDED_CHEVRONS_LEFT = 'square-rounded-chevrons-left.svg'
    SQUARE_ROUNDED_CHEVRONS_RIGHT = 'square-rounded-chevrons-right.svg'
    SQUARE_ROUNDED_CHEVRONS_UP = 'square-rounded-chevrons-up.svg'
    SQUARE_ROUNDED_LETTER_A = 'square-rounded-letter-a.svg'
    SQUARE_ROUNDED_LETTER_B = 'square-rounded-letter-b.svg'
    SQUARE_ROUNDED_LETTER_C = 'square-rounded-letter-c.svg'
    SQUARE_ROUNDED_LETTER_D = 'square-rounded-letter-d.svg'
    SQUARE_ROUNDED_LETTER_E = 'square-rounded-letter-e.svg'
    SQUARE_ROUNDED_LETTER_F = 'square-rounded-letter-f.svg'
    SQUARE_ROUNDED_LETTER_G = 'square-rounded-letter-g.svg'
    SQUARE_ROUNDED_LETTER_H = 'square-rounded-letter-h.svg'
    SQUARE_ROUNDED_LETTER_I = 'square-rounded-letter-i.svg'
    SQUARE_ROUNDED_LETTER_J = 'square-rounded-letter-j.svg'
    SQUARE_ROUNDED_LETTER_K = 'square-rounded-letter-k.svg'
    SQUARE_ROUNDED_LETTER_L = 'square-rounded-letter-l.svg'
    SQUARE_ROUNDED_LETTER_M = 'square-rounded-letter-m.svg'
    SQUARE_ROUNDED_LETTER_N = 'square-rounded-letter-n.svg'
    SQUARE_ROUNDED_LETTER_O = 'square-rounded-letter-o.svg'
    SQUARE_ROUNDED_LETTER_P = 'square-rounded-letter-p.svg'
    SQUARE_ROUNDED_LETTER_Q = 'square-rounded-letter-q.svg'
    SQUARE_ROUNDED_LETTER_R = 'square-rounded-letter-r.svg'
    SQUARE_ROUNDED_LETTER_S = 'square-rounded-letter-s.svg'
    SQUARE_ROUNDED_LETTER_T = 'square-rounded-letter-t.svg'
    SQUARE_ROUNDED_LETTER_U = 'square-rounded-letter-u.svg'
    SQUARE_ROUNDED_LETTER_V = 'square-rounded-letter-v.svg'
    SQUARE_ROUNDED_LETTER_W = 'square-rounded-letter-w.svg'
    SQUARE_ROUNDED_LETTER_X = 'square-rounded-letter-x.svg'
    SQUARE_ROUNDED_LETTER_Y = 'square-rounded-letter-y.svg'
    SQUARE_ROUNDED_LETTER_Z = 'square-rounded-letter-z.svg'
    SQUARE_ROUNDED_MINUS = 'square-rounded-minus.svg'
    SQUARE_ROUNDED_NUMBER_0 = 'square-rounded-number-0.svg'
    SQUARE_ROUNDED_NUMBER_1 = 'square-rounded-number-1.svg'
    SQUARE_ROUNDED_NUMBER_2 = 'square-rounded-number-2.svg'
    SQUARE_ROUNDED_NUMBER_3 = 'square-rounded-number-3.svg'
    SQUARE_ROUNDED_NUMBER_4 = 'square-rounded-number-4.svg'
    SQUARE_ROUNDED_NUMBER_5 = 'square-rounded-number-5.svg'
    SQUARE_ROUNDED_NUMBER_6 = 'square-rounded-number-6.svg'
    SQUARE_ROUNDED_NUMBER_7 = 'square-rounded-number-7.svg'
    SQUARE_ROUNDED_NUMBER_8 = 'square-rounded-number-8.svg'
    SQUARE_ROUNDED_NUMBER_9 = 'square-rounded-number-9.svg'
    SQUARE_ROUNDED_PLUS = 'square-rounded-plus.svg'
    SQUARE_ROUNDED_X = 'square-rounded-x.svg'
    SQUARE_ROUNDED = 'square-rounded.svg'
    SQUARE_X = 'square-x.svg'
    SQUARE = 'square.svg'
    SQUARES = 'squares.svg'
    STACK_2 = 'stack-2.svg'
    STACK_3 = 'stack-3.svg'
    STACK = 'stack.svg'
    STAR_HALF = 'star-half.svg'
    STAR = 'star.svg'
    STARS = 'stars.svg'
    SUN = 'sun.svg'
    TABLE = 'table.svg'
    THUMB_DOWN = 'thumb-down.svg'
    THUMB_UP = 'thumb-up.svg'
    TIMELINE_EVENT = 'timeline-event.svg'
    TOGGLE_LEFT = 'toggle-left.svg'
    TOGGLE_RIGHT = 'toggle-right.svg'
    TRANSFORM = 'transform.svg'
    TRANSITION_BOTTOM = 'transition-bottom.svg'
    TRANSITION_LEFT = 'transition-left.svg'
    TRANSITION_RIGHT = 'transition-right.svg'
    TRANSITION_TOP = 'transition-top.svg'
    TRASH_X = 'trash-x.svg'
    TRASH = 'trash.svg'
    TRIANGLE_INVERTED = 'triangle-inverted.svg'
    TRIANGLE_SQUARE_CIRCLE = 'triangle-square-circle.svg'
    TRIANGLE = 'triangle.svg'
    TROPHY = 'trophy.svg'
    UMBRELLA = 'umbrella.svg'
    USER = 'user.svg'
    VERSIONS = 'versions.svg'
    WINDMILL = 'windmill.svg'
    WOMAN = 'woman.svg'
    XBOX_A = 'xbox-a.svg'
    XBOX_B = 'xbox-b.svg'
    XBOX_X = 'xbox-x.svg'
    XBOX_Y = 'xbox-y.svg'
    YIN_YANG = 'yin-yang.svg'
    ZEPPELIN = 'zeppelin.svg'
    ZOOM_CANCEL = 'zoom-cancel.svg'
    ZOOM_CHECK = 'zoom-check.svg'
    ZOOM_CODE = 'zoom-code.svg'
    ZOOM_EXCLAMATION = 'zoom-exclamation.svg'
    ZOOM_IN_AREA = 'zoom-in-area.svg'
    ZOOM_IN = 'zoom-in.svg'
    ZOOM_MONEY = 'zoom-money.svg'
    ZOOM_OUT_AREA = 'zoom-out-area.svg'
    ZOOM_OUT = 'zoom-out.svg'
    ZOOM_PAN = 'zoom-pan.svg'
    ZOOM_QUESTION = 'zoom-question.svg'
    ZOOM_SCAN = 'zoom-scan.svg'
    ZOOM = 'zoom.svg'
    
    
    def pixmap(self,size: int = 24,color :str = TAILWIND_COLORS.ZINC_900,stroke_width: float = 2.0) -> Image:
        return convert(icon_path=self.value,icon_type="fill",size=size,color=color,stroke_width=stroke_width).toqpixmap()