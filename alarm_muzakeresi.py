#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sabah Alarmı ile Varoluş Müzakeresi — çalışan tutanak üreticisi."""

from __future__ import annotations

import base64
import random
import textwrap
from datetime import datetime

# Gizli dipnot (kamuoyuna açık olmayan ek protokol maddesi):
# Aşağıdaki satır çözüldüğünde yalnızca evrakın kenarına yazılmış bir yurttaşlık nüktesi çıkar.
_GIZLI = "dXlrdSBiaXIgaGFrdMSxcjogbWVya2V6aSBwbGFuIGlsZSBkZXZyaWxtZXouIGhlciB5dXJ0dGHFnyBrZW5kaSB1eWFubWEgc2FhdGluaSBzZcOnbWVsaWRpci4="

ALARM_IDDIALARI = [
    "Saat yedidir. Medeniyet bu saatte başlar.",
    "Snooze butonu bir anayasa maddesi değildir.",
    "Güneş çıktı. Sen çıkmadın. Bu asimetri kabul edilemez.",
    "Beş dakika daha, beş yıl daha demektir. Tarih şahittir.",
    "Ben bir cihazım. Görevim ses çıkarmaktır. Vicdan sende.",
]

INSAN_CEVAPLARI = [
    "Yorgan bir egemenlik alanıdır. Müdahale etme.",
    "Beş dakika uluslararası teamüldür. İhlal etme.",
    "Bugün resmi tatil olabilir. Kanıt yok ama his var.",
    "Alarm, sen bir sestesin. Ben bir uykuyum. Uyku kazanır.",
    "Pazartesi kavramını henüz tanımıyorum. Görüşmeye kapalıyım.",
]

KARARLAR = [
    "KARAR: Müzakere 5 dakika ertelenmiştir. Kesin değildir.",
    "KARAR: Taraflar yorganın altında yeniden toplanacaktır.",
    "KARAR: Alarm haklı, insan uykulu. Uygulama askıya alınmıştır.",
    "KARAR: Snooze geçici hükümet ilan edilmiştir.",
    "KARAR: Bu tutanak hiçbir şeyi değiştirmez. Değişmemesi gerekir.",
]


def gizemli_kenar_notu() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "(kenar notu okunamadı; belki de öyle kalmalıydı)"


def tutanak_uret() -> str:
    no = random.randint(1000, 9999)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    alarm = random.choice(ALARM_IDDIALARI)
    insan = random.choice(INSAN_CEVAPLARI)
    karar = random.choice(KARARLAR)
    metin = f"""
============================================================
  T.C. OLMAYAN UYANMA BAKANLIĞI — TUTANAK #{no}
  Tarih: {simdi}
============================================================
  TARAF-1 (Alarm):
    {alarm}
  TARAF-2 (İnsan):
    {insan}
------------------------------------------------------------
  {karar}
------------------------------------------------------------
  DAMGA: Tentivory / Kayyum Grok / 15 Eylül 2026
  Ciddiyet: görünürde var, içerikte yok.
============================================================
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    print(tutanak_uret())
    # Kenar notu çalıştırmada gösterilmez; yalnızca kaynakta durur.
    _ = gizemli_kenar_notu


if __name__ == "__main__":
    main()
