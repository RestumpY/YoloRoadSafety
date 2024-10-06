from flask import Flask, render_template, request, url_for
import os
from ultralytics import YOLO

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

# Charger le modèle YOLO
model = YOLO("yolov8n_trained.pt")

# Assurez-vous que les dossiers nécessaires existent
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    result_image_path = None
    if request.method == 'POST':
        # Vérifier si un fichier a été téléchargé
        if 'file' not in request.files:
            return render_template('index.html', error='Aucun fichier téléchargé')

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='Aucun fichier sélectionné')

        # Sauvegarder l'image téléchargée
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Effectuer une prédiction avec YOLO
        results = model.predict(source=file_path, save=True, project=app.config['RESULT_FOLDER'], name='', exist_ok=True)

        # Créer le chemin d'accès à l'image prédite dans le dossier 'static'
        result_image_path = f"results/predict/{file.filename}".replace("\\", "/")
        full_image_path = os.path.join('static', result_image_path)

        # Déboguer le chemin d'accès
        print("Chemin relatif pour le HTML:", result_image_path)
        print("Chemin absolu complet:", full_image_path)

        # Vérification : le fichier existe-t-il vraiment là où nous le pensons ?
        if not os.path.exists(full_image_path):
            print("Erreur: Le fichier n'a pas été sauvegardé là où attendu:", full_image_path)
        else:
            print("Fichier trouvé:", full_image_path)

    # Rendre le template avec potentiellement l'image prédite
    return render_template('index.html', result_image=result_image_path)

if __name__ == '__main__':
    app.run(debug=True)
