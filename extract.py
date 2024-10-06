import cv2
import os

def extract_frames(video_path, output_folder, interval=60):
    # Ouvrir la vidéo
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la vidéo.")
        return
    
    # Récupérer le nombre de frames par seconde (fps) de la vidéo
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Calculer l'intervalle en termes de nombre de frames
    frame_interval = int(fps * interval)
    
    current_frame = 0
    img_count = 0
    
    # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Si le frame actuel est à l'intervalle souhaité, on sauvegarde l'image
        if current_frame % frame_interval == 0:
            img_count += 1
            img_name = f"frame_{img_count}.jpg"
            img_path = os.path.join(output_folder, img_name)
            cv2.imwrite(img_path, frame)
            print(f"Image {img_name} extraite à la frame {current_frame}")
        
        current_frame += 1
    
    cap.release()
    print(f"Extraction terminée. {img_count} images ont été extraites.")

# Utilisation de la fonction
video_path = "Driving.mp4"
output_folder = "images"
extract_frames(video_path, output_folder, interval=60)
