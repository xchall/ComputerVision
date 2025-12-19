# -*- coding: utf-8 -*-
from pathlib import Path
from paddleocr import TextRecognition
import paddle

print("GPU available:", paddle.device.is_compiled_with_cuda())
print("Device count:", paddle.device.cuda.device_count())


ROOT = Path(r"C:\Users\Asus\Desktop\Sturdy\4_curs_1_sem\CV\dataset\test\begickaya")
IMAGES_SUBDIR = "number"
LABELS_FILE = "number.txt"

#  "ch_RepSVTR_rec"
MODEL_NAME = "ch_SVTRv2_rec"

CASE_INSENSITIVE = True  # сравнивать без учета регистра


def read_labels(txt_path: Path):
    gt = {}
    for line in txt_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        name, text = line.split(" ", 1)   # делим только по первому пробелу
        gt[name] = text
    return gt

def main():
    img_dir = ROOT / IMAGES_SUBDIR
    labels_path = ROOT / LABELS_FILE

    gt = read_labels(labels_path)

    # Модель распознавания (без детекции)
    model = TextRecognition(
        model_name=MODEL_NAME,
        #use_gpu=True в новой версии paddleOCR, если доступно gpu, выбирает автоматически
    )

    total = 0
    correct = 0
    missing = 0
    #stem - имя файла без расширения
    for stem, gt_text in gt.items():
        total += 1

        # ищем файл по имени с расширением
        candidate = list(img_dir.glob(stem + ".jpg"))
        if not candidate:
            missing += 1
            print(f"[MISS] {stem}: no image")
            continue

        img_path = str(candidate[0])
        out = model.predict(input=img_path, batch_size=1)
        pred_text = out[0]["rec_text"]


        ok = (pred_text == gt_text)
        if ok:
            correct += 1

        status = "OK" if ok else "ERR"
        print(f"[{status}] {stem}: GT='{gt_text}' | PRED='{pred_text}'")

    acc = correct / total
    err_pct = 100.0 * (1.0 - acc)

    print("\n===== RESULTS =====")
    print(f"Model: {MODEL_NAME}")
    print(f"Samples: {total}, missing_images: {missing}")
    print(f"Exact-match accuracy: {acc*100:.2f}%")
    print(f"Exact-match error:    {err_pct:.2f}%")
    print("===================\n")


if __name__ == "__main__":
    main()
