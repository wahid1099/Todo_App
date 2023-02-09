echo " BUILD START"
Python3.10.7 -m pip install -r requirements.txt
Python3.10.7 manage.py collectstatic --noinput --clear
echo " BUILD END" 
