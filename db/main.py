from funksjoner import *
CORS(app)

print(app)
print(app.template_folder)

if __name__ == "__main__":
    app.run(debug=True)
#print(sutest())