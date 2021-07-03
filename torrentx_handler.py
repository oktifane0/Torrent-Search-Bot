# (c) @AbirHasan2005 & Hemanta Pokharel & The Anon Cat

import py1337x

torrent = py1337x.py1337x()


def queryMessageContent(torrentId):
    response = torrent.info(torrentId=torrentId)
    genre = '\n\n'+', '.join(response['genre']) if response['genre'] else None
    description = '\n'+response['description'] if genre and response['description'] else '\n\n'+response['description'] if response['description'] else None
    msg = f"<b>🧣 {response['name']}</b>\n\n<b>النوع:</b> <code>{response['category']}</code>\n<b>اللغة:</b> <code>{response['language']}</code>\n<b>Seeders❤:</b> <code>{response['seeders']}</code>\n<b>Leechers😑:</b> <code>{response['leechers']}</code>\n<b>الحجم:</b> <code>{response['size']}</code>\n<b>عدد مرات التحميل:</b> <code>{response['downloads']}</code>\n<i>تم الرفع: {response['uploadDate']}</i>\n<i>Last Checked {response['lastChecked']}</i>\nتم الرفع بواسطة  <b>{response['uploader']}</b>{'<b>'+genre+'</b>' if genre else ''}{'<code>'+description+'</code>' if description else ''}\n\n<b>الرابط :</b>\n<code>{response['magnetLink']}</code>"

    return msg
