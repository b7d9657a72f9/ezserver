import httpx

print("Minecraft version:")
Version = input()

Manifest = httpx.get("https://piston-meta.mojang.com/mc/game/version_manifest.json").json()

for VersionInfo in Manifest["versions"]:

    if VersionInfo["id"] == Version:
        print(Version + " found in manifest.")
        LauncherInfo = httpx.get(VersionInfo["url"]).json()
        JarUrl = LauncherInfo["downloads"]["server"]["url"]
        print("Downloading Jar file...")
        JarContents = httpx.get(JarUrl).text
        ServerJar = open("server.jar", "w")
        ServerJar.write(JarContents)
        ServerJar.close()
        print("Jar file downloaded.")
