#!/usr/bin/env python3
"""Çay molası olmadan silkeleme insanlık dışıdır."""

import time


def cay_demle(saniye: int = 5) -> str:
    print("Demlik ısınıyor...")
    time.sleep(min(saniye, 2))
    return "Çay hazır. Şimdi halıya dönebilirsiniz."


if __name__ == "__main__":
    print(cay_demle())
    print("\nDAMGA / İMZA — Kayyum Grok — Tentivory — 10 Eylül 2026")
