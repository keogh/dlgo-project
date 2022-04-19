# Vamos a partir de la imagen oficial de python 3
FROM python:3

# Upgrade pip
RUN pip install --upgrade pip

# Upgrade seteuptools for tensorflow
RUN pip install --upgrade setuptools


# Instalamos jupyterlab y herramientas extras para las libretas
RUN pip install notebook jupyterlab

# Exponemos el puerto 8888
EXPOSE 8888

# El directorio inicial será /root/
WORKDIR /root/

# Este comando se va a ejecutar al levantar el contenedor
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

# Instalamos bibliotecas de python para tener una libreta chila
RUN pip install \
    numpy \
    ipywidgets \
    pandas \
    matplotlib \
    scipy \
    scikit-learn \
    scikit-image \
    tensorflow \
    tensorflowjs \
    keras \
    h5py \
    flask \
    flask-cors \
    future \
    six \
    gomill

# Descomentar si se quiere soporte de face-recognition con dlib
# Instalamos requisitos para Dlib
# https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
# RUN apt-get install -y build-essential cmake
# RUN apt-get install -y libopenblas-dev liblapack-dev
# RUN apt-get install -y python3-dev

# Descomentar si se quiere soporte de face-recognition con dlib
# Instalamos python dlib module (dura muchos minutos)
# RUN pip install dlib

# Activamos las extensiones para widgets en libretas
# RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

# Activamos las extensiones para widgets en jupuyterlab (requiere nodejs)
# RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
# RUN apt-get install -y nodejs
# RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager
