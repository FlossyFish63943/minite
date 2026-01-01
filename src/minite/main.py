from collections import Counter
from resolver import fetchFabricMCVersions as ffmcv

def verKey(ver: str):
    return tuple(map(int, ver.split(".")))

allMCVer = []

mods = int(input("Number of mods: "))

# Edge case: zero mods
if mods <= 0:
    print("[ERR] You must specify at least one mod.")
    exit(1)

for i in range(mods):
    mod = input(f"[{i + 1}/{mods}] Fabric Mod: ")
    print(f"[INFO] Fetching Minecraft versions for mod '{mod}'...\n\n")

    try:
        versions = ffmcv(mod)
    except Exception as e:
        print(f"[ERR] Error with mod '{mod}': {e}")
        exit(1)

    allMCVer.extend(versions)

# Count occurrences of each MC version
verMap = Counter(allMCVer)

# Versions supported by ALL mods
compatibleVer = [
    ver for ver, cnt in verMap.items()
    if cnt == mods
]

# Clean output
if not compatibleVer:
    print("\n[ERR] No compatible Minecraft version found.")
    exit(0)

sortedVer = sorted(compatibleVer, key=verKey)
highestVer = sortedVer[-1]

print("\n[OUT] Compatible Minecraft Versions:")
for ver in sortedVer:
    if ver == highestVer:
        print(f"  → {ver}  (HIGHEST)")
    else:
        print(f"    {ver}")

print(f"\n[OUT] Highest compatible Minecraft version: {highestVer}")
