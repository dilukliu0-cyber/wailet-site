# Генератор статических страниц сайта Wailet (политика, условия, поддержка). Запуск: python build.py
import html

EMAIL = 'dilukliu0@gmail.com'
OWNER = 'Zakhar Maziak'
UPDATED_RU = '9 октября 2026'
UPDATED_EN = 'October 9, 2026'

CSS = """
:root{--bg:#f6f3ec;--card:#fffdf8;--text:#23201a;--muted:#7a746a;--line:#e3ddd0;--ink:#2b2822}
@media(prefers-color-scheme:dark){:root{--bg:#1d1c1a;--card:#262624;--text:#efebe3;--muted:#a09a8f;--line:#37352f;--ink:#efebe3}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:720px;margin:0 auto;padding:28px 20px 80px}
header{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.brand{font-weight:800;font-size:20px;letter-spacing:-.3px;color:var(--ink);text-decoration:none}
nav a{color:var(--muted);text-decoration:none;margin-left:14px;font-size:14px}nav a:hover{color:var(--text)}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:26px 24px;margin-top:18px}
h1{font-size:30px;letter-spacing:-.5px;margin:18px 0 4px}h2{font-size:18px;margin:26px 0 6px}
p,li{color:var(--text)}.muted{color:var(--muted);font-size:14px}ul{padding-left:20px}
a{color:var(--ink)}.lang{margin:10px 0 0;font-size:14px}.lang a{margin-right:12px}
hr{border:0;border-top:1px solid var(--line);margin:34px 0}
"""

def page(slug, title_ru, title_en, body_ru, body_en):
    nav = ('<a href="privacy.html">Политика / Privacy</a><a href="terms.html">Условия / Terms</a>'
           '<a href="support.html">Поддержка / Support</a>')
    doc = f"""<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title_en)} | Wailet</title>
<meta name="description" content="Wailet: {html.escape(title_en)}"><style>{CSS}</style></head><body><main>
<header><a class="brand" href="index.html">Wailet</a><nav>{nav}</nav></header>
<p class="lang"><a href="#ru">Русский</a><a href="#en">English</a></p>
<section id="ru" class="card"><h1>{title_ru}</h1><p class="muted">Обновлено: {UPDATED_RU}</p>{body_ru}</section>
<section id="en" class="card"><h1>{title_en}</h1><p class="muted">Last updated: {UPDATED_EN}</p>{body_en}</section>
<p class="muted" style="margin-top:22px">© 2026 {OWNER}. Wailet</p></main></body></html>"""
    open(slug, 'w', encoding='utf-8').write(doc)


privacy_ru = f"""
<p>Wailet (далее «приложение») помогает учитывать расходы по фото чеков. Разработчик: {OWNER} (далее «мы»). Эта политика объясняет, какие данные мы собираем, зачем и как ими управлять.</p>
<h2>1. Какие данные мы собираем</h2>
<ul>
<li><b>Аккаунт.</b> При входе через Apple или Google мы получаем идентификатор аккаунта, имя и адрес электронной почты (Apple может предоставить скрытый адрес).</li>
<li><b>Чеки и расходы.</b> Фото чеков, которые вы снимаете или выбираете, и данные, извлечённые из них: магазин, дата, товары, цены, категории, валюта. Также ручные расходы, пополнения кошелька и свои категории.</li>
<li><b>Настройки.</b> Язык, валюта, тема, стиль виджетов.</li>
<li><b>Токен уведомлений.</b> Технический токен устройства, чтобы отправить вам уведомление, когда чек распознан.</li>
<li><b>Данные подписки.</b> Статус и срок подписки Wailet Pro. Платёж проводит Apple, номер карты мы не получаем.</li>
</ul>
<h2>2. Зачем мы это используем</h2>
<ul>
<li>чтобы распознать чек и показать расходы, статистику и виджеты;</li>
<li>чтобы синхронизировать данные между сессиями и устройствами;</li>
<li>чтобы отправлять уведомления о результате распознавания;</li>
<li>чтобы проверять доступ к подписке Pro и лимиты бесплатного тарифа.</li>
</ul>
<p>Мы не продаём ваши данные, не показываем рекламу и не отслеживаем вас между приложениями.</p>
<h2>3. Кто обрабатывает данные</h2>
<ul>
<li><b>Supabase</b>: хранение аккаунта, чеков и фото, серверная часть приложения.</li>
<li><b>Google (Gemini API)</b>: фото чека передаётся на распознавание. Мы отправляем изображение чека и параметры (язык, валюта, названия ранее распознанных вами товаров для точности), без вашего имени и почты.</li>
<li><b>Apple</b>: вход, push-уведомления, покупки и подписки.</li>
<li><b>RevenueCat</b>: учёт подписок. Туда передаётся технический идентификатор вашего аккаунта и сведения о покупке.</li>
<li><b>Google</b>: вход через Google (по вашему выбору).</li>
</ul>
<h2>4. Хранение и удаление</h2>
<p>Данные хранятся, пока у вас есть аккаунт. Удалённые чеки лежат в корзине 30 дней, затем стираются навсегда. Вы можете удалить аккаунт в приложении: Настройки → Аккаунт → Удалить аккаунт. Тогда мы удаляем аккаунт, чеки, фото и связанные данные. Если нужна помощь, напишите на {EMAIL}.</p>
<h2>5. Безопасность</h2>
<p>Данные передаются по защищённому соединению (HTTPS). Доступ к вашим чекам ограничен вашим аккаунтом. Но ни одна система не защищена полностью, поэтому не фотографируйте документы, которые не должны попадать в приложение.</p>
<h2>6. Ваши права</h2>
<p>Вы можете запросить доступ к своим данным, их исправление или удаление, написав на {EMAIL}. Если вы находитесь в ЕС, у вас есть права по GDPR, включая жалобу в надзорный орган (в Чехии это Úřad pro ochranu osobních údajů).</p>
<h2>7. Дети</h2>
<p>Приложение не предназначено для детей младше 13 лет, и мы сознательно не собираем их данные.</p>
<h2>8. Изменения</h2>
<p>Мы можем обновлять политику. Дата последнего обновления указана вверху страницы.</p>
<h2>9. Контакты</h2>
<p>{OWNER}, <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""

privacy_en = f"""
<p>Wailet (the "app") helps you track expenses from photos of receipts. The developer is {OWNER} ("we"). This policy explains what data we collect, why, and how you can control it.</p>
<h2>1. Data we collect</h2>
<ul>
<li><b>Account.</b> When you sign in with Apple or Google we receive an account identifier, your name and email address (Apple may provide a private relay address).</li>
<li><b>Receipts and expenses.</b> Photos of receipts you take or choose, and the data extracted from them: store, date, items, prices, categories, currency. Also manual expenses, wallet top-ups and your custom categories.</li>
<li><b>Settings.</b> Language, currency, theme, widget style.</li>
<li><b>Notification token.</b> A technical device token so we can notify you when a receipt has been recognized.</li>
<li><b>Subscription data.</b> The status and period of your Wailet Pro subscription. Apple processes the payment; we never receive your card number.</li>
</ul>
<h2>2. Why we use it</h2>
<ul>
<li>to recognize receipts and show expenses, statistics and widgets;</li>
<li>to keep your data in sync between sessions and devices;</li>
<li>to send notifications about recognition results;</li>
<li>to check Pro access and free plan limits.</li>
</ul>
<p>We do not sell your data, show ads, or track you across other apps.</p>
<h2>3. Who processes the data</h2>
<ul>
<li><b>Supabase</b>: storage for your account, receipts and photos, and the app backend.</li>
<li><b>Google (Gemini API)</b>: the receipt photo is sent for recognition. We send the receipt image and parameters (language, currency, names of products you recognized earlier, for accuracy), without your name or email.</li>
<li><b>Apple</b>: sign in, push notifications, purchases and subscriptions.</li>
<li><b>RevenueCat</b>: subscription management. It receives a technical identifier of your account and purchase information.</li>
<li><b>Google</b>: sign in with Google (if you choose it).</li>
</ul>
<h2>4. Retention and deletion</h2>
<p>We keep your data while your account exists. Deleted receipts stay in the trash for 30 days and are then erased permanently. You can delete your account in the app: Settings → Account → Delete account. We then delete your account, receipts, photos and related data. For help write to {EMAIL}.</p>
<h2>5. Security</h2>
<p>Data is transmitted over secure connections (HTTPS). Access to your receipts is limited to your account. No system is completely secure, so please do not photograph documents that should not be stored in the app.</p>
<h2>6. Your rights</h2>
<p>You can ask for access to, correction of or deletion of your data by writing to {EMAIL}. If you are in the EU you have GDPR rights, including the right to lodge a complaint with a supervisory authority (in the Czech Republic: Úřad pro ochranu osobních údajů).</p>
<h2>7. Children</h2>
<p>The app is not intended for children under 13 and we do not knowingly collect their data.</p>
<h2>8. Changes</h2>
<p>We may update this policy. The date of the last update is shown at the top of the page.</p>
<h2>9. Contact</h2>
<p>{OWNER}, <a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""

terms_ru = f"""
<p>Используя Wailet, вы соглашаетесь с этими условиями. Разработчик: {OWNER}.</p>
<h2>1. Что делает приложение</h2>
<p>Wailet помогает учитывать расходы: распознаёт чеки с фото, считает суммы и показывает статистику. Приложение не даёт финансовых, налоговых или юридических советов. Распознавание выполняет ИИ и может ошибаться, проверяйте суммы и данные.</p>
<h2>2. Аккаунт</h2>
<p>Вход выполняется через Apple или Google. Вы отвечаете за безопасность своего аккаунта и за то, чтобы фото и данные, которые вы загружаете, не нарушали чужие права.</p>
<h2>3. Бесплатный тариф и Wailet Pro</h2>
<ul>
<li>Бесплатно: 15 добавлений расходов в месяц (сканы и ручные вместе), стиль виджетов Notion.</li>
<li><b>Wailet Pro</b>: добавления без лимита, свои категории, все стили виджетов.</li>
<li>Pro доступен по подписке: месяц или год. Актуальная цена показана на экране подписки в вашей валюте. Для годовой подписки может действовать бесплатный пробный период (неделя), условия показываются перед покупкой.</li>
<li>Оплата списывается с вашего Apple ID при подтверждении покупки. Подписка продлевается автоматически, если вы не отключите продление минимум за 24 часа до окончания периода. Управлять подпиской и отключать продление можно в настройках Apple ID (Настройки iPhone → ваше имя → Подписки).</li>
<li>Возвраты обрабатывает Apple по своим правилам.</li>
</ul>
<h2>4. Допустимое использование</h2>
<p>Нельзя использовать приложение для незаконных целей, пытаться взломать сервис, перегрузить его или обойти ограничения тарифа.</p>
<h2>5. Ответственность</h2>
<p>Приложение предоставляется «как есть». Мы не гарантируем отсутствие ошибок и перебоев. В пределах, допустимых законом, мы не отвечаем за косвенные убытки и за решения, которые вы приняли на основе данных приложения.</p>
<h2>6. Изменения и прекращение</h2>
<p>Мы можем изменять приложение и эти условия. Вы можете в любой момент удалить аккаунт в приложении (Настройки → Аккаунт → Удалить аккаунт).</p>
<h2>7. Право и контакты</h2>
<p>Применяется право Чешской Республики, если иное не требуется по закону о защите потребителей вашей страны. Вопросы: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""

terms_en = f"""
<p>By using Wailet you agree to these terms. The developer is {OWNER}.</p>
<h2>1. What the app does</h2>
<p>Wailet helps you track expenses: it recognizes receipts from photos, adds up totals and shows statistics. The app does not provide financial, tax or legal advice. Recognition is performed by AI and may be wrong, so please check amounts and data.</p>
<h2>2. Account</h2>
<p>You sign in with Apple or Google. You are responsible for the security of your account and for making sure the photos and data you upload do not infringe anyone's rights.</p>
<h2>3. Free plan and Wailet Pro</h2>
<ul>
<li>Free: 15 expense additions per month (scans and manual together), the Notion widget style.</li>
<li><b>Wailet Pro</b>: unlimited additions, custom categories, all widget styles.</li>
<li>Pro is available as a subscription: monthly or yearly. The current price is shown on the subscription screen in your currency. A free trial (one week) may apply to the yearly plan; its terms are shown before you buy.</li>
<li>Payment is charged to your Apple ID when you confirm the purchase. The subscription renews automatically unless you turn off auto-renewal at least 24 hours before the end of the current period. You can manage or cancel subscriptions in your Apple ID settings (iPhone Settings → your name → Subscriptions).</li>
<li>Refunds are handled by Apple under its own rules.</li>
</ul>
<h2>4. Acceptable use</h2>
<p>You may not use the app for unlawful purposes, attempt to hack or overload the service, or bypass plan limits.</p>
<h2>5. Liability</h2>
<p>The app is provided "as is". We do not guarantee that it is error-free or uninterrupted. To the extent permitted by law we are not liable for indirect losses or for decisions you make based on data in the app.</p>
<h2>6. Changes and termination</h2>
<p>We may change the app and these terms. You can delete your account at any time in the app (Settings → Account → Delete account).</p>
<h2>7. Governing law and contact</h2>
<p>The laws of the Czech Republic apply, unless the consumer protection law of your country requires otherwise. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
"""

support_ru = f"""
<p>Нужна помощь с Wailet? Напишите нам: <a href="mailto:{EMAIL}">{EMAIL}</a>. Обычно отвечаем в течение 1–2 рабочих дней.</p>
<h2>Частые вопросы</h2>
<p><b>Как отсканировать чек?</b> На главном экране нажмите «Добавить» и сфотографируйте чек. Распознавание идёт на сервере, можно закрыть приложение: когда чек будет готов, придёт уведомление.</p>
<p><b>Чек распознан неверно.</b> Откройте чек, нажмите карандаш и исправьте позиции, категорию или общую сумму. Изменения сохраняются сами.</p>
<p><b>Как удалить чек?</b> Откройте чек и нажмите значок корзины, либо смахните строку влево. Удалённые чеки хранятся 30 дней в корзине (Настройки → Корзина).</p>
<p><b>Как управлять подпиской или отменить её?</b> Настройки iPhone → ваше имя → Подписки → Wailet Pro. Там же отключается автопродление.</p>
<p><b>Как восстановить покупку?</b> На экране Wailet Pro нажмите «Восстановить».</p>
<p><b>Как удалить аккаунт и все данные?</b> В приложении: Настройки → Аккаунт → Удалить аккаунт. Или напишите нам.</p>
<p><b>Как добавить виджет?</b> Долгое нажатие на экран «Домой» → «+» → Wailet. Стиль выбирается в Настройки → Стиль виджетов.</p>
"""

support_en = f"""
<p>Need help with Wailet? Write to us: <a href="mailto:{EMAIL}">{EMAIL}</a>. We usually reply within 1–2 business days.</p>
<h2>FAQ</h2>
<p><b>How do I scan a receipt?</b> On the main screen tap "Add" and take a photo of the receipt. Recognition runs on the server, so you can close the app: you will get a notification when the receipt is ready.</p>
<p><b>The receipt was recognized wrongly.</b> Open the receipt, tap the pencil and fix items, category or the total. Changes save automatically.</p>
<p><b>How do I delete a receipt?</b> Open it and tap the trash icon, or swipe the row left. Deleted receipts stay in the trash for 30 days (Settings → Trash).</p>
<p><b>How do I manage or cancel my subscription?</b> iPhone Settings → your name → Subscriptions → Wailet Pro. You can turn off auto-renewal there.</p>
<p><b>How do I restore a purchase?</b> On the Wailet Pro screen tap "Restore".</p>
<p><b>How do I delete my account and all data?</b> In the app: Settings → Account → Delete account. Or write to us.</p>
<p><b>How do I add a widget?</b> Long-press the Home Screen → "+" → Wailet. Choose the style in Settings → Widget style.</p>
"""

page('privacy.html', 'Политика конфиденциальности', 'Privacy Policy', privacy_ru, privacy_en)
page('terms.html', 'Условия использования', 'Terms of Use', terms_ru, terms_en)
page('support.html', 'Поддержка', 'Support', support_ru, support_en)

index_body_ru = '<p>Wailet учитывает расходы по фото чеков: сфотографируйте чек, а категории, суммы и статистику приложение посчитает само.</p><p><a href="privacy.html">Политика конфиденциальности</a> · <a href="terms.html">Условия использования</a> · <a href="support.html">Поддержка</a></p>'
index_body_en = '<p>Wailet tracks your expenses from photos of receipts: take a photo and the app sorts categories, totals and statistics for you.</p><p><a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms of Use</a> · <a href="support.html">Support</a></p>'
page('index.html', 'Wailet', 'Wailet', index_body_ru, index_body_en)
print('ok')
