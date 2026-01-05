## //////////////////////////////////////////
##          Host Main program.
## //////////////////////////////////////////

# import only opencv and requests
import cv2
import requests 

# El puerto que mapeas en Docker.
url = "http://localhost:8000/predict"

# capture frame from webcam using 0
cap = cv2.VideoCapture(0)

# Opcional : Ajustar la resolucion de la cámara.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# reading video stream with loop.
while True:
    # capturing frame from buffer
    ret, frame = cap.read()
    if not ret:
        break

    # encode img(frame) to send 
    _, img_encoded = cv2.imencode(".jpg", frame)

    # Send image to docker container POST
    file = {'file': ('image.jpg', img_encoded.tobytes(), 'image/jpeg')}

    try:
        # Envair al contenedor (docker)
        response = requests.post(url, files = file )
        
        # OK, dibujar en el frame.
        if response.status_code == 200:
            # Get Json Data fro docker
            data = response.json()
            # turn to list
            detections = data.get("detections",[])

            # Draw the boxes in the Host's frame
            for det in detections:
                x1, y1, x2, y2 = map(int, det["box"])
                label = f"{det['label']} {det['confidence']:.2f}"

                # Dibujar rectángulos y etiquetas.
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label , (x1, y1 - 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    except Exception as e:
        print(f"Error de Conexion con docker: {e}")

    # print(response.json()) # <<-- here reciebe YOLO coords.

    cv2.imshow('Webcam Host', frame ) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release opencv resources.
cap.release()
cv2.destroyAllWindows()
