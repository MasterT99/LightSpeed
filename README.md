# LightSpeed
 Car Damage Detection System using AI

## Project Details

| Team ID        | 86513 |
|:---:|:---|
| **Project Title**  | Car Damage Detection System |
| **College Name**   | L. D. COLLEGE OF ENGINEERING, AHMEDABAD |
| **Department**     | BE - Computer Engineering |
| **Year**           | 2020 |
| **Keyword**        | Artificial Intelligence, Machine Learning, Deep Learning, Image Processing, Damaged Car Detection, Insurance Claiming |
| **Internal Guide** | Prof. Pragnesh Patel |

### Team Details

- Mehta Bhavy
- Shah Keval
- Shah Het
- Shah Nigam
- Tamboli Rushabh

### Project Demo Video

https://youtu.be/B4H_FjYRPqg



## How to run?
1. Clone this repository.
2. Create conda/pip vitrual environment with requirements.txt file.
	- Required module versions are listed in that same file of you want to install manually. Earlier or later versions may not work.
3. Unzip model.zip in the directory `LightSpeed\CDD\static\model`.
	- Your directory should look like this:
		```
		LightSpeed\CDD\static\model
		│   car.h5
		│   door.h5
		│   front.h5
		│   hood.h5
		│   rear.h5
		│   side.h5
		│   window.h5
		│   winshield.h5
		│
		└───bumper
			│   saved_model.pb
			│
			├───assets
			└───variables
				│   variables.data-00000-of-00002
				│   variables.data-00001-of-00002
				│   variables.index
				│
				└───variables_temp_ea0f68758ae940398f50e26c2f256b68
		```
		- Delete model.zip.001-015 files after successfully extracting model files.
4. Create empty folders as shown below
   ```
   LightSpeed\CDD\static\upload
			├───coldstorage
			│   ├───front
			│   ├───left
			│   ├───rear
			│   └───right
			└───predict
				├───front
				│   └───a
				├───left
				│   └───a
				├───rear
				│   └───a
				└───right
				    └───a
   ```
	- **Make sure to create folders, otherwise program will throw errors.**
	
5. Now change directory to root folder `LightSpeed` and execute `python manage.py runserver`
6. Open http://127.0.0.1:8000 in your browser.
7. Login or signup and upload your own car images or upload from given test image set from `LightSpeed\CDD\static\upload\test` folder.

