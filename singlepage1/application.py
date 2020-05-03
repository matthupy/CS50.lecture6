from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Maecenas ultricies mi eget mauris pharetra. Eget nunc scelerisque viverra mauris in aliquam sem fringilla. Massa ultricies mi quis hendrerit dolor magna eget est. Consequat ac felis donec et odio pellentesque diam. Sodales ut eu sem integer vitae justo. Lectus quam id leo in vitae turpis massa. Ligula ullamcorper malesuada proin libero. Nibh praesent tristique magna sit amet purus. Sed nisi lacus sed viverra tellus in hac. At tempor commodo ullamcorper a lacus. Egestas egestas fringilla phasellus faucibus scelerisque eleifend. Pulvinar sapien et ligula ullamcorper malesuada proin.",
        "At consectetur lorem donec massa sapien faucibus et molestie ac. Amet mauris commodo quis imperdiet massa tincidunt nunc. Lectus urna duis convallis convallis tellus id. Diam maecenas ultricies mi eget. Tristique senectus et netus et malesuada fames ac turpis. In metus vulputate eu scelerisque felis imperdiet proin fermentum leo. Porta non pulvinar neque laoreet suspendisse interdum consectetur. Faucibus turpis in eu mi bibendum neque egestas. Amet purus gravida quis blandit. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper.",
        "Consectetur libero id faucibus nisl tincidunt eget nullam non. Dignissim suspendisse in est ante in nibh mauris. At elementum eu facilisis sed odio. Accumsan sit amet nulla facilisi morbi tempus. Dui accumsan sit amet nulla facilisi. Ut enim blandit volutpat maecenas volutpat blandit. Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Ultrices vitae auctor eu augue ut lectus arcu bibendum at. Neque viverra justo nec ultrices. Pellentesque elit eget gravida cum."]

@app.route("/first")
def first():
    return texts[0]

@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]

if __name__ == "__main__":
    app.run()