from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import gc
import tensorflow.keras.backend as bk

basedir = 'CDD/static'


def data_generator(damage):
    test_data_gen = ImageDataGenerator(rescale=1. / 255)
    validation_generator = test_data_gen.flow_from_directory(
        os.path.join(basedir, damage),
        target_size=(224, 224),
        shuffle=False,
        class_mode='binary',
    )
    return validation_generator


def is_car():
    model = load_model(os.path.join(basedir, "model/car.h5"))
    generator = data_generator("upload/predict")
    prediction = model.predict(generator)
    a = (prediction <= 0.55)  # 0.5)
    generator = None
    gc.collect()
    bk.clear_session()
    if a.all():
        return True
    else:
        return False


def is_bumper():
    model = load_model(os.path.join(basedir, "model/bumper"))
    generator = data_generator("upload/predict/front")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_front():
    model = load_model(os.path.join(basedir, "model/front.h5"))
    generator = data_generator("upload/predict/front")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_hood():
    model = load_model(os.path.join(basedir, 'model/hood.h5'))
    generator = data_generator("upload/predict/front")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_windshield():
    model = load_model(os.path.join(basedir, 'model/winshield.h5'))
    generator = data_generator("upload/predict/front")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.4:
        return True
    else:
        return False


def is_window(folder='left'):
    model = load_model(os.path.join(basedir, 'model/window.h5'))
    generator = data_generator("upload/predict/" + folder)
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_side(folder='left'):
    model = load_model(os.path.join(basedir, 'model/side.h5'))
    generator = data_generator("upload/predict/" + folder)
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_door(folder='left'):
    model = load_model(os.path.join(basedir, 'model/door.h5'))
    generator = data_generator("upload/predict/" + folder)
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_boot():
    model = load_model(os.path.join(basedir, 'model/hood.h5'))
    generator = data_generator("upload/predict/rear")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_rear():
    model = load_model(os.path.join(basedir, 'model/rear.h5'))
    generator = data_generator("upload/predict/rear")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.5:
        return True
    else:
        return False


def is_windshield_rear():
    model = load_model(os.path.join(basedir, 'model/winshield.h5'))
    generator = data_generator("upload/predict/rear")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False


def is_bumper_rear():
    model = load_model(os.path.join(basedir, "model/bumper"))
    generator = data_generator("upload/predict/rear")
    prediction = model.predict(generator)
    generator = None
    gc.collect()
    bk.clear_session()
    if prediction <= 0.55:  # 0.5:
        return True
    else:
        return False
