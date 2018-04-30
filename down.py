import os
import re
import sys
import string
import tensorflow as tf
from tensorflow.python.framework import ops
ops.reset_default_graph()

local_repository = 'temp'


if tf.__version__[0]<'1':
    from tensorflow.models.rnn.translate import seq2seq_model
else:
    if not os.path.exists(local_repository):
        from git import Repo
        tf_model_repository = 'https://github.com/tensorflow/models'
        Repo.clone_from(tf_model_repository,local_repository)
        sys.path.insert(0,'temp/tutorials/rnn/translate/')
        import seq2seq_model as seq2seq_model
        import data_utils as data_utils



exit()
def translation_model(sess, input_vocab_size, output_vocab_size,
                      buckets, rnn_size, num_layers, max_gradient,
                      learning_rate, lr_decay_rate, forward_only):
    model = seq2seq_model.Seq2SeqModel(
        input_vocab_size,
        output_vocab_size,
        buckets,
        rnn_size,
        num_layers,
        max_gradient,
        batch_size,
        learning_rate,
        lr_decay_rate,
        forward_only=forward_only,
        dtype=float32)

    return (model)


print('Creating Translation Model')
input_vocab_size = vocab_size
output_vocab_size = vocab_size

translate_model = translation_model(sess=sess,
                                    input_vocab_size=vocab_size,
                                    output_vocab_size=vocab_size,
                                    buckets=buckets,
                                    rnn_size=rnn_size,
                                    num_layers=num_layers,
                                    max_gradient=max_gradient,
                                    learning_rate=learning_rate,
                                    lr_decay_rate=lr_decay_rate,
                                    forward_only=False)

with tf.variable_scope(tf.get_variable_scope(), reuse=True):
    test_model = translation_model(sess=sess,
                                   input_vocab_size=vocab_size,
                                   output_vocab_size=vocab_size,
                                   buckets=buckets,
                                   rnn_size=rnn_size,
                                   num_layers=num_layers,
                                   max_gradient=max_gradient,
                                   learning_rate=learning_rate,
                                   lr_decay_rate=lr_decay_rate,
                                   forward_only=True)

    test_model.batch_size = 1

init = tf.global_variables_initializer()
sess.run(init)

# start training

train_loss = []

for i in range(generations):
    rand_bucket_ix = np.random.choice(len(bucketed_data))
    model_outputs = translate_model.get_batch()





