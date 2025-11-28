import httpx

print("Minecraft version:")
MinecraftVersion = input()
print("Fabric version:")
FabricVersion = input()

JarUrl = "https://meta.fabricmc.net/v2/versions/loader/" + MinecraftVersion + "/" + FabricVersion + "/1.1.0/server/jar"

print("Downloading Jar file...")
JarContents = httpx.get(JarUrl).text
ServerJar = open("fabric.jar", "w")
ServerJar.write(JarContents)
ServerJar.close()
print("Jar file downloaded.")
Eula = open("eula.txt", "w")
Eula.write("eula=true")
Eula.close()
Run = open("run", "w")
Run.write("java -jar fabric.jar nogui")
Run.close()