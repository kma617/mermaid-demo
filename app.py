from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

valid_instancies = [ f"Item {n}" for n in range(1, 1000)]

def render_image(item):
    # make mermaid diagram
    mermaid = f"graph LR;"
    mermaid += f"A({item}) --> B --> C --> D --> E --> F --> G"
    return mermaid

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Create route to show html page with combobox and button
@app.route("/")
def selection():
    return render_template("index.html", instancies=valid_instancies)

# Create route to show selected item where item is passed as get parameter with name item
@app.route("/show")
def selected():
    instance = request.args.get("instance")
    
    if not instance or instance not in valid_instancies:
        return "Item not found", 404
    
    mermaid_diagram = render_image(instance)
    return render_template("show.html", item=instance, mermaid_diagram=mermaid_diagram)
