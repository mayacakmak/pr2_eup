import tf

tf_listener = None


def init():
    global tf_listener
    tf_listener = tf.TransformListener()
