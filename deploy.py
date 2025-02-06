"""  Python script to deploy automatically  """
import os
import shutil

# Build DeliverEase3D
os.chdir("DeliverEase3D")
os.system("npm run build")
os.chdir("..")
shutil.rmtree("dist", ignore_errors=True)
shutil.move(os.path.join("DeliverEase3D", "dist"), "dist")

# Build DeliverEase
shutil.copytree("DeliverEase", "DeliverEaseTemp", dirs_exist_ok=True)
shutil.move(
    os.path.join("DeliverEaseTemp", "index.html"),
    os.path.join("DeliverEaseTemp", "home.html")
)

for filename in os.listdir("DeliverEaseTemp"):
    shutil.move(
        os.path.join("DeliverEaseTemp", filename),
        os.path.join("dist", filename)
    )

shutil.rmtree("DeliverEaseTemp")
os.system("npm run gh-pages")
