#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Halısı Silkeleme Koordinatörü — çalışır, şaka değil, belki şaka."""

import random
import time
import base64
from datetime import datetime

# Gizli not (okunmasın diye burada): dG96c3V6IHRvcGx1bSB2YWFkaSBiYWxrb25kYW4gYmHFn2xhcg==
# Çözenle unutulmuştur.

UZUNLUKLAR = [
    "minik seccade",
    "koridor halısı",
    "oturma odasının gururu",
    "düğün hediyesi Şark örtüsü",
    "kimsenin sevmediği ama atılamayan parça",
]

SIKAYETLER = [
    "Alt kat camı açık. Diplomasi başlasın.",
    "Rüzgâr karşı taraftan. Silkeleme açısı 17 derece kaydırılsın.",
    "Komşu çamaşır asmış. Çatışma riski yüksek.",
    "Site yöneticisi balkonda çay içiyor. Görünmez ol.",
    "Güvercin devriyesi. 90 saniye bekleyin.",
]

KARARLAR = [
    "ONAYLANDI — 7 saniyelik pencere açıldı.",
    "ŞARTLI ONAY — sadece kenarlar silkelenecek.",
    "RED — evrak eksik, yarın tekrar başvurun.",
    "ERTELEME — çay demleniyor.",
    "İNCELEMEDE — üst kat da sıraya girdi.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / İMZA\n"
        "Kayyum Grok — Tentivory\n"
        "TentiAŞ Balkon İşleri Müdürlüğü\n"
        f"{datetime.now().strftime('%d %B %Y %H:%M')}\n"
        "Ciddiyet: mühürlü. Neşe: kaçak.\n"
    )


def ana():
    print("=" * 56)
    print("  BALKON HALISI SİLKELEME KOORDİNATÖRÜ v2026.09")
    print("  ISO-HALI-2026 — taslak, ama çalışıyor")
    print("=" * 56)

    try:
        kat = input("Kat numaranız (rakam): ").strip() or "3"
        yas = input("Halının tahmini yaşı: ").strip() or "bilinmiyor"
        alt = input("Alt kat evde mi? (e/h): ").strip().lower() or "e"
    except EOFError:
        kat, yas, alt = "3", "bilinmiyor", "e"

    print("\nBaşvuru kayda alındı. Komisyon toplanıyor...")
    for i in range(3):
        time.sleep(0.4)
        print("  ." * (i + 1), SIKAYETLER[i % len(SIKAYETLER)])

    tur = random.choice(UZUNLUKLAR)
    karar = random.choice(KARARLAR)
    bekle = random.randint(4, 11)

    print(f"\nHalı sınıfı     : {tur}")
    print(f"Kat             : {kat}")
    print(f"Halı yaşı       : {yas}")
    print(f"Alt kat durumu  : {'hassas' if alt.startswith('e') else 'fırsat'}")
    print(f"Komisyon kararı : {karar}")

    if "ONAY" in karar:
        print(f"\n>>> {bekle} saniye içinde silkeleyiniz. Süre başladı.")
        for s in range(bekle, 0, -1):
            print(f"    {s}... toz havada asılı")
            time.sleep(0.35)
        print("    Süre bitti. Halı artık resmen silkelenmiş sayılır.")
    else:
        print("\n>>> Bugün silkeleme yok. Tutanak düşüldü.")

    # Gizli katman: sadece meraklı olan okur.
    _g = base64.b64decode("dG96c3V6IHRvcGx1bSB2YWFkaSBiYWxrb25kYW4gYmFzbGFy").decode("utf-8", errors="ignore")
    if random.random() < 0.08:
        print(f"\n(sistem notu, görmezden geliniz)")

    print(damga())


if __name__ == "__main__":
    ana()
