from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from Algorithm.Kruskal import Kruskal
from Algorithm.Prim import Prim
from Helper.Parser import Parser
from Helper.GraphVisualizer import *

# Root Window
root = Tk()
root.title("Minimum Spanning Tree Solution Using Kruskal and Prim Algorithm")
root.resizable(0,0)

# Center the Window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1080
window_height = 608
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y - 30}")

# Canvas
# # background = PhotoImage(file="../assets/background.png")
canvas = Canvas(root, width = 1080, height = 608, bg = '#f3d8bb')
canvas.pack(fill="both", expand=True)
# # canvas.create_image(0, 0, image = background, anchor = "nw")

# # Basic UI Label and Shape
canvas.create_text(300, 20, anchor="nw", text= "\u26A1 Minimum Spanning Tree Finder \u26A1", font=("Georgia", 19, 'bold'), fill="#e18b71")
canvas.create_text(70, 160, anchor="nw", text= "Choose the graph file!", font=("Georgia", 16, 'bold'), fill="#e18b71")
canvas.create_text(70, 270, anchor="nw", text= "Choose the algorithm:", font=("Georgia", 16, 'bold'), fill="#e18b71")

# Algorithm Option
var = StringVar(value="Prim")
radio1 = Radiobutton(root, text="Prim", variable=var, value="Prim", font=("Georgia", 12, 'bold'), bg = "#f3d8bb", fg="#da7d65")
radio2 = Radiobutton(root, text="Kruskal", variable=var, value="Kruskal", font=("Georgia", 12, 'bold'), bg = "#f3d8bb", fg="#da7d65")
canvas.create_window(70, 300, anchor="nw", window=radio1)
canvas.create_window(70, 330, anchor="nw", window=radio2)

def solveButtonClicked():
    if var.get() == "Prim":
        findPrim()
    elif var.get() == "Kruskal":
        findKruskal()

# Solve Button
solve_button = Button(root, text="Solve", font=("Times New Roman", 14, 'bold'), command=solveButtonClicked, height=1, width=20, bg="#a7a374", fg="#FFFFFF")
canvas.create_window(80, 420, anchor="nw", window=solve_button) # 475

canvas.create_rectangle(0, 70, 1440, 75, fill="#e6a087", outline="")
canvas.create_rectangle(0, 80, 1440, 85, fill="#e6a087", outline="")
canvas.create_rectangle(400, 85, 405, 1080, fill="#e6a087", outline="")


# # Global Variables needed
parser = Parser("")
drawer = GraphVisualizer([])
valid = False

# File Name Label
fileName = StringVar()
fileName.set("")
fileNameLabel = Label(canvas, textvariable=fileName, fg="#000000", bg="#f3d9c0", font=("Times New Roman", 16), borderwidth=2, anchor="w", height= 1, width=20, relief="ridge")
fileNameWindow = canvas.create_window(70, 195, anchor="nw", window=fileNameLabel)

# # Parsing Exception Label
parseExceptionLabel = canvas.create_text(70, 240, text = "", font=("Times New Roman", 11), fill="#FFFFFF", anchor="w")

# # Procedure when the choose file button is clicked
def askFileName():
    global valid, parser, drawer, fileName, canvas, parseExceptionLabel
    valid = False
    graphFile = askopenfilename()
    temp = graphFile.split("/")[len(graphFile.split("/")) - 1]
    if (len(temp) > 19):
        fileName.set(temp[:19] + "...")
    else:
        fileName.set(temp)
    if (graphFile != ""):
        try:
            parser = Parser(graphFile)
            parser.parseFile()
            drawer = GraphVisualizer(parser.getGraph())
            updateResult([], 0, 0)
            canvas.itemconfigure(parseExceptionLabel, text="")
            valid = True
        except ValueError:
            canvas.itemconfigure(parseExceptionLabel, text="Unknown symbol in the map/graph file")
        except Exception as error:
            canvas.itemconfigure(parseExceptionLabel, text=error)

# # File Chooser Button
fileChooserButton = Button(canvas, text="\u2b60", font=("Times New Roman", 11), command=askFileName, height= 1, width=4, bg="#e6b6b4")
fileChooserWindow = canvas.create_window(275, 195, anchor="nw", window=fileChooserButton)

# # Running Algorithm Exception Label
algorithmExceptionLabel = canvas.create_text(70, 500, text = "", font=("Times New Roman", 12), fill="#FFFFFF", anchor="w")

# Start the Prim Algorithm
def findPrim():
    global parser, canvas, algorithmExceptionLabel
    try:
        prim = Prim(parser)
        prim.mst_prim()
        updateResult(prim.getPath(), prim.getDistance(), 0)
    except Exception as error:
        canvas.itemconfigure(algorithmExceptionLabel, text=error)

# Start the Kruskal Algorithm
def findKruskal():
    global parser, canvas, algorithmExceptionLabel
    try:
        kruskal = Kruskal(parser)
        kruskal.graph = Kruskal.parse_adj_matrix(parser.getGraph())
        kruskal.mst_kruskal()
        updateResult(kruskal.getPath(), kruskal.getDistance(), 1)
    except Exception as error:
        canvas.itemconfigure(algorithmExceptionLabel, text=error)

# Graph Image
graphImage = PhotoImage(file="")
background_rect = canvas.create_rectangle(500, 125, 978, 482, fill="white")
graphWindow = canvas.create_image(500, 125, anchor="nw", image=graphImage)

# Algorithm Used Label
algorithmUsedLabel = canvas.create_text(500, 510, text = "", font=("Georgia", 12), fill="#FFFFFF", anchor="w")

# Result Path Label
resultPathLabel = canvas.create_text(500, 540, text = "", font=("Georgia", 12), fill="#FFFFFF", anchor="w")

# Distance Label
distanceLabel = canvas.create_text(500, 570, text = "", font=("Georgia", 12), fill="#FFFFFF", anchor="w")

# Update result according to parameter
def updateResult(resultPath, distance, flag):
    global drawer, canvas, graphImage, graphWindow, resultPathLabel, distanceLabel
    if (resultPath != []):
        drawer.drawGraphResult(resultPath)
        if (flag == 0):
            canvas.itemconfigure(algorithmUsedLabel, text="Using Prim Algorithm")
        else:
            canvas.itemconfigure(algorithmUsedLabel, text="Using Kruskal Algorithm")
        
        pathResult = ""
        comma = 0
        for path in resultPath:
            comma += 1
            if (comma == len(resultPath)):
                pathResult += str(path[0] + 1) + "-" + str(path[1] + 1)
            else:
                pathResult += str(path[0] + 1) + "-" + str(path[1] + 1) + ", "
            
        canvas.itemconfigure(resultPathLabel, text=f"Result Path: {pathResult}")
        canvas.itemconfigure(distanceLabel, text=f"Distance      : {distance}")
    else:
        drawer.drawGraph()
        canvas.itemconfigure(algorithmUsedLabel, text="")
        canvas.itemconfigure(resultPathLabel, text="")
        canvas.itemconfigure(distanceLabel, text="")
        
    # Open the image file
    image = Image.open("Assets/graph.png")

    # Calculate the new size
    new_width = int(image.width * 0.75)
    new_height = int(image.height * 0.75)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    graphImage = ImageTk.PhotoImage(resized_image)
    canvas.itemconfigure(graphWindow, image=graphImage)


root.mainloop()