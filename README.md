**PROJET 2:     Identification Automatique des Maladies du Maïs**

**Badara Diop**<br>
**Fatimata Ka**<br>
**Limamoulaye Dia**<br>
**Elise Faye**<br>

**Précisin**
Seul les code source de l'interface utilisateur et la conception du modèle sont televersés dans ce repository. le dossier contenant le projet complet incluant tous les fichiers vous est partagé par ce lien-drive: https://drive.google.com/file/d/1mzFzNlfkVoXuVxQae977JHIvLL-sF-NV/view?usp=drive_link

Ci-desous, un guide complet pour visualiser et tester l'interface utilisateur après avoir avoir telechargé le dossier complet.
# Instructions d'installation et d'exécution

## Installation

Assurez-vous d'avoir Python installé sur votre système.

1. Installez FastAPI en utilisant la commande pip :
    * sur  linux/macos/windows
    ```bash
    pip install fastapi
    ```

2. Installez Uvicorn avec le support complet (y compris les fonctionnalités de rechargement automatique) :
    * sur  linux/macos/windows
    ```bash
    pip install "uvicorn[standard]"
    ```

3. Installez Streamlit avec la commande pip :
    * sur  linux/macos/windows
    ```bash
    pip install streamlit
    ```

## Exécution

### API FastAPI

4. Lancez l'API FastAPI en utilisant Uvicorn avec l'option --reload :
    * sur  linux/macos/windows
    ```bash
    uvicorn api1:app --reload
    ```

Cela démarrera l'API FastAPI et la rendra accessible à l'adresse http://127.0.0.1:8000.

### Interface utilisateur Streamlit

5. Lancez l'interface utilisateur Streamlit en exécutant le script frontend.py :
    * sur  linux/macos/windows
    ```bash
    streamlit run frontend.py
    ```

Cela lancera l'interface utilisateur Streamlit et l'ouvrira dans votre navigateur par défaut.


---

