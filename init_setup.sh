echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.9"
conda create --prefix ./env python=3.9 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "install requirements_dev.txt"
pip install -r requirements_dev.txt
echo [$(date)]: "END"