import pickle
import os

model_config = {
    'model_path': 'c:/Users/dilla/Downloads/temp-local-text-miner/temp-local-text-miner/temp-local-text-miner/text-miner/MatEntityRecognition/materials_entity_recognition/models/matRecognition',
    'bert_path': r"C:\Users\dilla\Downloads\temp-local-text-miner\temp-local-text-miner\temp-local-text-miner\text-miner\MatBERT-master\matbert-base-cased",  # Update with the correct path
    'bert_first_trainable_layer': 0,
    'word_dim': 100,
    'word_lstm_dim': 100,
    'word_bidirect': True,
    'word_unroll': False,
    'word_rnn_wrapper': False,
    'char_dim': 25,
    'char_lstm_dim': 25,
    'char_bidirect': True,
    'char_combine_method': 'concat',
    'char_unroll': False,
    'char_rnn_wrapper': False,
    'ele_num': True,
    'only_CHO': True,
    'tar_tag': False,
    'pre_tag': False,
    'rnn_type': 'gru',
    'lower': False,
    'zeros': False,
    'use_ori_text_char': False,
    'crf': True,
    'crf_begin_end': True,
    'dropout': 0.5,
    'pre_embedding': None,
    'lr_method': 'sgd_lr_.005',  # Corrected learning method string
    'loss_per_token': False,
    'batch_size': 1,
    'num_epochs': 100,
    'steps_per_epoch': 3500,
    'weight_decay': 0.01,
    'id_to_word': {1: 'example_word'},  # Update with actual id-to-word mapping
    'id_to_char': {1: 'example_char'},  # Update with actual id-to-char mapping
    'id_to_tag': {1: 'example_tag'},    # Update with actual id-to-tag mapping
}

config_path = 'c:/Users/dilla/Downloads/temp-local-text-miner/temp-local-text-miner/temp-local-text-miner/text-miner/MatEntityRecognition/materials_entity_recognition/models/matRecognition/model_config.pkl'
with open(config_path, 'wb') as f:
    pickle.dump(model_config, f)

# Verify the contents of the configuration file
with open(config_path, 'rb') as f:
    loaded_config = pickle.load(f)
    print(f"Loaded model configuration: {loaded_config}")

print(f"Model configuration saved to {config_path}")
