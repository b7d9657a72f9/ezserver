import httpx

print("Minecraft version:")
Version = input()

Manifest = httpx.get("https://qing762.is-a.dev/api/papermc").json()

JarUrl = Manifest["versions"][Version]

print("Downloading Jar file...")
JarContents = httpx.get(JarUrl).text
ServerJar = open("paper.jar", "w")
ServerJar.write(JarContents)
ServerJar.close()
print("Jar file downloaded.")
