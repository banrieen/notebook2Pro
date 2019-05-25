# Auto deploy services

# Start jupyter notebook
# jupyter notebook --generate-config /root/.juyper/jupyter_notebook_config.py 
# nohup jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --notebook-dir=/home/notebook &
nohup jupyter notebook --config  jupyter_notebook_config.py &
