# Auto deploy services

# Start jupyter notebook
# jupyter notebook --generate-config /root/.ipython/profile_default/ipython_kernel_config.py 
mv jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
nohup jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --notebook-dir=/home/notebook &
