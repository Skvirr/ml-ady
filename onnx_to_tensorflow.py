# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import onnx
from onnx_tf.backend import prepare


# %%
onnx_model = onnx.load("MoveToGoal.onnx")  # load onnx model


# %%
tf_rep = prepare(onnx_model)  # prepare tf representation


# %%
tf_rep.inputs
# %%
tf_rep.outputs


#%%
import numpy as np
array = np.array([2.0,4.0,5.0,5.0,5.0,5.0], dtype=np.float32)
pred_tf = tf_rep.run({'vector_observation': [array]})
pred_tf.version_number
pred_tf.action
tf_rep.export_graph("tensorflow_model")


# %%
