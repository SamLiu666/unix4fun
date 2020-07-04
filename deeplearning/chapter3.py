import tensroflow as tf

def my_netword(input):
	w1 = tf.Variables(tf.random_uniform([784,100], -1.-1), name='w1'))
	b1 = tf.Variables(tf.zeros([100))	
