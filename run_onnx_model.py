# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import onnxruntime
import numpy as np


# %%
sess = onnxruntime.InferenceSession("MoveToGoal.onnx", None)


# %%
input_ = sess.get_inputs()
for i in input_:
    print(i)
print("-------")
output_ = sess.get_outputs()
for i in output_:
    print(i)


# %%
input_name = sess.get_inputs()[0].name


# %%

array = np.array([2.0,4.0,5.0,5.0,5.0,5.0], dtype=np.float32)
pred_onx = sess.run(["continuous_actions"], {input_name: [array]})
print(pred_onx)


# %%



# %%



