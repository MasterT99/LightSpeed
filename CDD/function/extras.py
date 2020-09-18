
# ARE YOU GONNA EDIT THIS? DO NOT.
def handle_uploaded_file(file, folder, filename):
    with open('CDD/static/upload/predict/' + folder + '/a/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)