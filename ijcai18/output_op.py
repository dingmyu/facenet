#-*-coding:utf-8-*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
config = tf.ConfigProto(allow_soft_placement=True) 
config.gpu_options.allow_growth = True 
tf.logging.set_verbosity(tf.logging.INFO)

saver = tf.train.import_meta_graph('model-20180109-153439.meta') 
#print (saver.saver_def.filename_tensor_name)
#print (saver.saver_def.restore_op_name)
#print (saver.saver_def)
#all_vars = tf.all_variables()
#for item in all_vars:
#    print (item)
graph = tf.get_default_graph()
for op in graph.get_operations():
     print (op.name, op.values())
'''
with tf.Session() as sess:
     saver.restore(sess, "model-20180109-153439.ckpt-0")
     # 输出op.names
     graph = tf.get_default_graph()
     for op in graph.get_operations():
         print (op.name)
'''
