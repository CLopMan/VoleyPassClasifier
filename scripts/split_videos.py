import shutil
import random

correct: list[tuple[int, int]] = []
incorrect: list[tuple[int, int]] = []

for i in range(55):
    with open(f"data/{i}.txt") as f:
        for line in f.read().split("\n")[:-1]:
            split = line.split(" ")
            seq, val = split
            if val == "+":
                correct.append((i, int(seq)))
            else:
                incorrect.append((i, int(seq)))


random.seed(2003)
random.shuffle(correct)
random.shuffle(incorrect)

correct = correct[:len(correct) * 7 // 10]

print("correct")
print(correct)
print("incorrect")
print(incorrect)
print("correct:", len(correct))
print("incorrect:", len(incorrect))

videos = "data/videos"

def copy_file(vid: tuple[int, int], j: int, folder: str, ty: str, root: str):
    shutil.copyfile(
        f"{videos}/{vid[0]}/{vid[1]}/{vid[1] + j}.jpg",
        f"scripts/{root}/data_folder/{folder}/{ty}/{ty}_vid_{vid[0]}_seq_{vid[1]}_frame_{vid[1] + j}.jpg",
    )


def copy(ty: str, data: list[tuple[int, int]]):
    for i, vid in enumerate(data):
        if i / len(data) < 0.7:
            folder = "train"
        else:
            folder = "test"
        for j in range(-10, 10):
            # 2 class model
            copy_file(vid, j, folder, ty, "YOLO_2class")
            # 3 class model
            if -2 <= j <= 2:
                copy_file(vid, j, folder, ty, "YOLO_3class")
            else:
                copy_file(vid, j, folder, "waiting", "YOLO_3class")


copy("correct", correct)
copy("incorrect", incorrect)
