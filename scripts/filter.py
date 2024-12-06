from pathlib import Path
import shutil

results = []
for video in range(55):
    with open(f"{video}/annotations.txt", "r", encoding="utf-8") as f:
        for seq in f.read().splitlines():
            seq = seq.split()
            res = {
                "video": video,
                "sequence": seq[0],
                "type": seq[1],
                "annotations": [],
            }
            for i in range(2, len(seq), 5):
                ann = seq[i:i+5]
                res["annotations"].append({
                    "X": ann[0],
                    "Y": ann[1],
                    "W": ann[2],
                    "H": ann[3],
                    "type": ann[4],
                })
            results.append(res)

results = list(filter(lambda x: x["type"] in ["r_set", "l_set"], results))
n = len(results)
print(n)

output_dir = Path("res")
for i, res in enumerate(results):
    video = Path(str(res["video"]))
    seq = video/Path(res["sequence"].split(".")[0])
    dst = output_dir/seq
    dst.mkdir(exist_ok=True, parents=True)
    shutil.copytree(seq, dst, dirs_exist_ok=True)
    shutil.copyfile(video/Path("annotations.txt"), output_dir/video/Path("annotations.txt"))
