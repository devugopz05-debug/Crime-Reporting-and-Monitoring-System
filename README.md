# Crime Reporting and Monitoring System 🚔

A comprehensive web-based application designed to bridge the gap between citizens and law enforcement. This system streamlines the incident reporting process and ensures secure management of digital evidence.

## 📝 Project Objective
The goal of this project is to digitize manual crime records, providing a transparent platform for citizens to report grievances and for investigators to track case progress efficiently. Developed as part of the third-year Computer Science curriculum at BCM College, Kottayam.

## ✨ Key Features
* **Citizen Portal:** Secure interface for reporting various incident types (Cybercrime, Theft, etc.).
* **Evidence Management:** Support for high-quality digital evidence (Images, Videos, Documents) handled via **Git LFS**.
* **Officer Dashboard:** Real-time tracking of assigned cases, investigator notes, and status updates.
* **Search & Filter:** Advanced querying to locate reports by category, location, or urgency.
* **Automated Reporting:** Generation of monthly and category-wise crime statistics.

## 🛠️ Tech Stack
* **Backend:** Python & Django 
* **Frontend:** Bootstrap 5, JavaScript, HTML5, CSS3
* **Database:** MySQL (Relational Database Management)
* **Version Control:** Git & GitHub (with Git LFS for media assets)

## 🔄 System Workflow
1. Submission: Citizen submits a report with description, location, and media evidence.
2. Processing: Django handles the business logic, storing metadata in MySQL and media pointers via Git LFS.
3. Admin: Authorized officers review the report, assign investigators, and update the case lifecycle.

## ⚙️ Installation & Setup

1. Clone the repository:
   git clone https://github.com/devugopz05-debug/crime-reporting-system.git

2. Navigate to the project folder:
   cd crime-reporting-system

3. Create a virtual environment:
   python -m venv venv

4. Activate the environment:
   venv\Scripts\activate   (Windows)
   source venv/bin/activate (Mac/Linux)

5. Install dependencies:
   pip install -r requirements.txt

6. Apply migrations:
   python manage.py migrate

7. Run the server:
   python manage.py runserver

## 🔐 Admin Access

To access admin panel:
http://127.0.0.1:8000/admin/

Create superuser using:
python manage.py createsuperuser

## 📸 Screenshots
<img width="1920" height="1020" alt="Screenshot 2026-03-15 000543" src="https://github.com/user-attachments/assets/163e0890-3657-4d02-b9f2-6b5c322d7203" />

<img width="1898" height="903" alt="Screenshot 2026-03-15 000914" src="https://github.com/user-attachments/assets/9dee9f22-43ba-4624-9484-069b31d22511" />
<img width="1919" height="912" alt="Screenshot 2026-03-15 001108" src="https://github.com/user-attachments/assets/4b6d5dff-8f13-47c1-9e6b-ccab46ab0fae" />
<img width="1919" height="909" alt="Screenshot 2026-03-15 001416" src="https://github.com/user-attachments/assets/d8bda98c-025f-4fd1-ae54-a5ffefa827d1" />
<img width="1898" height="906" alt="Screenshot 2026-03-15 001458" src="https://github.com/user-attachments/assets/4c28ad5d-4c0a-4452-9ecd-74538ecb2528" />
<img width="1920" height="1080" alt="Screenshot 2026-03-15 001531" src="https://github.com/user-attachments/assets/b1e007e0-ba4f-4e17-942f-b57831a50e99" />
<img width="1920" height="1080" alt="Screenshot 2026-03-15 001544" src="https://github.com/user-attachments/assets/be6b70dc-a0a6-46a0-b67b-937e4a15090d" />
<img width="1898" height="913" alt="Screenshot 2026-03-15 002011" src="https://github.com/user-attachments/assets/63b93e3b-f377-4e3e-8032-ab10eede3b69" />
<img width="1896" height="909" alt="Screenshot 2026-03-15 002240" src="https://github.com/user-attachments/assets/4927fdd2-b0a5-4b21-8b65-961a3e1d76e5" />
<img width="1896" height="909" alt="Screenshot 2026-03-15 002333" src="https://github.com/user-attachments/assets/df83c6a4-f546-4b0b-8953-38fb9cada6a6" />
<img width="1886" height="913" alt="Screenshot 2026-03-15 002457" src="https://github.com/user-attachments/assets/edaf0f27-54b6-4ce0-bfa0-210717d9ccff" />
<img width="1905" height="910" alt="Screenshot 2026-03-15 002753" src="https://github.com/user-attachments/assets/e03569f0-f8ef-4a28-867e-05717d449958" />
<img width="1892" height="913" alt="Screenshot 2026-03-15 002938" src="https://github.com/user-attachments/assets/b17edd69-f2ca-4b27-9a81-8b5e36b5ca3b" />
<img width="1920" height="1080" alt="Screenshot 2026-03-12 233936" src="https://github.com/user-attachments/assets/bc7a14a1-14ed-4cd0-a2bb-10a5d7de193b" />

## 🗄️ Database Setup

1. Create a new MySQL database (e.g., crime_db)
2. Open phpMyAdmin or MySQL Workbench
3. Import the file: final_crime_report.sql
4. Update database credentials in settings.py
5. Run the project

The database was exported using phpMyAdmin.

## 👨‍💻 Developed By
Devika Mohan  
B.Sc Computer Science  
BCM College, Kottayam

## 🎓 Project Guidance
Project Guide:Ms. Vyshnavi Shaji  
Institution: BCM College, Kottayam

## 🤝 Acknowledgement
Special thanks to Faith Infosys, Changanacherry, for technical guidance and support.
