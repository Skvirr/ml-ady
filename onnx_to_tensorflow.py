# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import onnx
from onnx_tf.backend import prepare
import numpy as np

# %%
onnx_model = onnx.load("MoveToGoal.onnx")  # load onnx model


# %%
tf_rep = prepare(onnx_model)  # prepare tf representation


# %%
tf_rep.inputs
# %%
tf_rep.outputs


#%%
model_name = "saved_model"
array = np.array([0,0,0,-50,0,100], dtype=np.float32)
pred_tf = tf_rep.run({'vector_observation': [array]})
print(pred_tf.version_number)
print(pred_tf.action)
tf_rep.export_graph(model_name)


# %%
import tensorflow as tf
imported = tf.saved_model.load("tensorflow_model")
f = imported.signatures["serving_default"]
# %%
