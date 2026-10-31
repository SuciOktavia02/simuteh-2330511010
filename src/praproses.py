"""praproses.py: rangkaian praproses SIMUTEH (dipakai ulang mulai P5)."""
import json
import cv2
import numpy as np

PARAM_BAWAAN = {
    "lebar": 640,           # sampling: lebar citra kerja (piksel)
    "gamma": 1.0,           # < 1 mencerahkan, > 1 menggelapkan
    "clahe_clip": 2.0,      # 0 berarti CLAHE tidak dipakai
    "clahe_tile": 8,
    "penapis": "median",    # "none", "rerata", "gaussian", "median"
    "kernel": 3,
    "sigma": 1.0,
    "tajam_k": 0.0,         # 0 berarti tanpa penajaman
}


def _gamma_lut(g):
    """Tabel pencarian gamma: s = 255 * (r / 255) ** g (sama seperti Kode 3.2)."""
    lut = np.array([255 * (i / 255) ** g for i in range(256)])
    return lut.clip(0, 255).astype(np.uint8)


def praproses(img_bgr, p=None):
    """Urutan: ubah ukuran -> gamma -> CLAHE kanal V -> redam derau -> tajamkan."""
    p = {**PARAM_BAWAAN, **(p or {})}

    # TODO 1: ubah ukuran agar lebar = p["lebar"], rasio aspek tetap, INTER_AREA
    h, w = img_bgr.shape[:2]
    if w != p["lebar"]:
        tinggi = int(round(h * p["lebar"] / w))
        img = cv2.resize(img_bgr, (int(p["lebar"]), tinggi), interpolation=cv2.INTER_AREA)
    else:
        img = img_bgr.copy()

    # TODO 2: koreksi gamma dengan cv2.LUT bila gamma != 1
    if p["gamma"] != 1:
        img = cv2.LUT(img, _gamma_lut(p["gamma"]))

    # TODO 3: CLAHE pada kanal V saja (HSV), lalu kembali ke BGR
    if p["clahe_clip"] > 0:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        clahe = cv2.createCLAHE(clipLimit=float(p["clahe_clip"]),
                                tileGridSize=(int(p["clahe_tile"]), int(p["clahe_tile"])))
        hsv[:, :, 2] = clahe.apply(hsv[:, :, 2])
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # TODO 4: redam derau sesuai penapis, kernel, sigma
    k = int(p["kernel"])
    if p["penapis"] == "rerata":
        img = cv2.blur(img, (k, k))
    elif p["penapis"] == "gaussian":
        img = cv2.GaussianBlur(img, (k, k), float(p["sigma"]))
    elif p["penapis"] == "median":
        img = cv2.medianBlur(img, k)
    elif p["penapis"] != "none":
        raise ValueError(f"penapis tidak dikenal: {p['penapis']}")

    # TODO 5: unsharp masking bila tajam_k > 0
    if p["tajam_k"] > 0:
        blur = cv2.GaussianBlur(img, (5, 5), float(p["sigma"]))
        img = cv2.addWeighted(img, 1 + p["tajam_k"], blur, -p["tajam_k"], 0)

    return img


def simpan_param(p, path="../hasil/param_praproses.json"):
    with open(path, "w") as f:
        json.dump({**PARAM_BAWAAN, **p}, f, indent=2)
