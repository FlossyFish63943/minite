import requests

BASEURL = "https://api.modrinth.com/v2"

def fetchFabricMCVersions(modName: str) -> set[str]:
    searchURL = f"{BASEURL}/search"
    searchParams = {
        "query": modName,
        "facets": '[["categories:fabric"]]'
    }

    searchResp = requests.get(searchURL, params=searchParams)
    searchResp.raise_for_status()

    searchData = searchResp.json()
    hits = searchData.get("hits", [])

    if not hits:
        raise ValueError(f"Mod '{modName}' not found on Modrinth")

    projectID = hits[0]["project_id"]

    versionsURL = f"{BASEURL}/project/{projectID}/version"
    versionsResp = requests.get(versionsURL)
    versionsResp.raise_for_status()

    versionsData = versionsResp.json()

    mcVersions = set()
    for version in versionsData:
        if "fabric" not in version.get("loaders", []):
            continue

        for mcVer in version.get("game_versions", []):
            mcVersions.add(mcVer)

    if not mcVersions:
        raise ValueError(f"Mod '{modName}' has no Fabric-compatible versions")

    return mcVersions


if __name__ == "__main__":
    mod = input("Fabric Mod: ")
    try:
        versions = fetchFabricMCVersions(mod)
    except Exception as e:
        print(f"❌ {e}")
        exit(1)

    print(f"\nFabric-Supported Minecraft Versions for '{mod}':")
    for ver in sorted(versions):
        print(ver)